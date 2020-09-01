import logging

import pyxinput

from .base import BaseHandler

log = logging.getLogger("miditoxinput")


class ButtonHandler(BaseHandler):
    def __init__(self, controller: pyxinput.vController, button: str):
        log.info(
            "Creating ButtonHandler: axis '%s' on controller '%s'",
            button,
            controller.id,
        )
        self.controller = controller
        self.button = button

    def handle(self, command):
        value = 0 if command[2] == 0 else 1
        log.debug("Setting controller button '%s' to '%i'", self.button, value)
        self.controller.set_value(self.button, value)
