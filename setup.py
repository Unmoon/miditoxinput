from setuptools import find_packages
from setuptools import setup

setup(
    name="miditoxinput",
    version="1.0.0",
    url="https://github.com/Unmoon/miditoxinput",
    author="Unmoon",
    author_email="joona@unmoon.com",
    description="Use MIDI inputs as Xbox controllers.",
    packages=find_packages(),
    install_requires=["pygame", "pyxinput"],
)
