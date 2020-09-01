import logging

import pyxinput

from .base import BaseHandler

log = logging.getLogger("miditoxinput")
SLIDER_RANGE = 127


class SliderHandler(BaseHandler):
    def __init__(
        self, controller: pyxinput.vController, axis: str, inverted: bool = False
    ):
        log.info(
            "Creating SliderHandler: axis '%s' on controller '%s'%s",
            axis,
            controller.id,
            " (inverted)" if inverted else "",
        )
        self.controller = controller
        self.axis = axis
        self.inverted = -1 if inverted else 1

    def handle(self, command):
        log.debug(
            "Setting controller axis '%s' to '%f'",
            self.axis,
            ((command[2] - SLIDER_RANGE / 2) / SLIDER_RANGE * 2) * self.inverted,
        )
        self.controller.set_value(
            self.axis,
            ((command[2] - SLIDER_RANGE / 2) / SLIDER_RANGE * 2) * self.inverted,
        )
