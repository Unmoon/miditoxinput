import json
import logging
import time

import pygame.midi
from pyxinput import vController

from .handlers.button import ButtonHandler
from .handlers.slider import SliderHandler

log = logging.getLogger("miditoxinput")

handler_types = dict(ButtonHandler=ButtonHandler, SliderHandler=SliderHandler)


def main():
    controller = vController()
    handlers = dict()

    for handler in json.load(open("controller.json", "r"))["handlers"]:
        handler_command = handler["command"]
        handler_class = handler_types.get(handler["type"])
        handler_args = handler.get("args", [])
        handlers[handler_command] = handler_class(controller=controller, **handler_args)

    pygame.midi.init()
    if pygame.midi.get_default_input_id() == -1:
        log.error("No MIDI input found (device ID is -1)!")
        exit(-1)

    log.info("Initializing MIDI input '%i'.", pygame.midi.get_default_input_id())
    midi = pygame.midi.Input(pygame.midi.get_default_input_id())
    log.info("Ready!")

    while True:
        try:
            if midi.poll():
                command = midi.read(1)[0][0]
                log.debug("Command is: '%s'", command)
                handler = handlers.get(command[1], None)
                if handler is not None:
                    handler.handle(command)
            time.sleep(0.001)
        except KeyboardInterrupt:
            exit(1)


if __name__ == "__main__":
    main()
