import sys

from .handlers import *

log_levels = {
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
}

log_level = log_levels.get(sys.argv[1]) if len(sys.argv) > 1 else logging.INFO

log = logging.getLogger("miditoxinput")
log.setLevel(log_level)

log_handler = logging.StreamHandler(sys.stdout)
log_handler.setLevel(log_level)
log_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
log_handler.setFormatter(log_formatter)
log.addHandler(log_handler)
