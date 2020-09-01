# MIDI to XInput
Use MIDI inputs as Xbox controllers.

## Requirements

* Python 3.7

Virtual environment should be created before installing.
```shell script
python -m venv venv
venv\Scripts\activate
python -m pip install -U pip setuptools
```

## Install in editable mode

`-e` allows editing the application without having to reinstall it.
```shell script
pip install -e .
python -m miditoxinput
```

## Running

```shell script
python -m miditoxinput
```
## Configuring

### Debug logging

Debug logging will be useful for figuring out what commands your MIDI device outputs.
```shell script
python -m miditoxinput DEBUG
```

For example, the following slider's `command` is 77. 
```text
2020-09-01 10:53:47,866 DEBUG: Command is: '[184, 77, 123, 0]'
2020-09-01 10:53:47,881 DEBUG: Command is: '[184, 77, 122, 0]'
2020-09-01 10:53:47,896 DEBUG: Command is: '[184, 77, 121, 0]'
2020-09-01 10:53:47,911 DEBUG: Command is: '[184, 77, 120, 0]'
```

The following button's `command` is 59.
```text
2020-09-01 10:56:05,898 DEBUG: Command is: '[152, 59, 127, 0]'
2020-09-01 10:56:06,241 DEBUG: Command is: '[136, 59, 0, 0]'
```

## Codestyle

This project uses [Black](https://github.com/psf/black) for code formatting.

```shell script
pip install black
black miditoxinput/
black setup.py
```
