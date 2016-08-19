# pgmatrix
pygame to rpi-rgb-led-matrix adapter for the raspberry pi

# Into
This library is an adaper for hzeller's rpi-rgb-led-matrix that allows you to write content for your led display using pygame!

# Motivation
This goal of this project is to provide a convenient and efficient way to interface with a large LED display using pygame and a raspberry pi. I found that the python bindings included in the rpi-rgb-led-matrix were a bit slow. They were also, as far as I could tell, not compatible with the Adafruit HAT, and I could not find an easy way to remap the pins. By separating the rendering layer from the driver layer, I was able to easily achieve a 60hz refresh rate while still using pygame and all of the configuration oiptions available in the C++ library.

# How it works
The library is divided into a pythonn frontend and a c++ backend. The frontend provides functions and a skeletal extendable app that takes content from a dummy pygame display and pipe it to the backend as a raw bytestring. The backend (matrix-server) reads each frame from the pipe, transforms it to match the configuration of the display, and writes the frame to the display.

# Installation
First, clone the project. rpi-rgb-led-matrix is included as a submodule.
The library uses python 2.7, which is probably already installed on your raspberry pi.
Additionally, you must install pygame. The installation process varies depending on your OS.

Once the prerequisites have been satisfied:

`make`


# Usage
You'll want to execute the program from a screen / tmux session.

In one terminal, cd into the client directory:

`$ cd client`

and run the desired script:

`$ sudo python ./demo-image.py <brightness(1..100)> <width(1..32) <height(1..32)> [program arguments]`

In a second terminal run the server:

`$ sudo ./matrix-server <brightness(1..100)> <width(1..32) <height(1..32)>`

Note: The python client is responsible for making the named pipe if it does not exist. So if the pipe has not been made, the client must be run before to sever or the server will crash silently.

TODO: Make server create pipe if it does not exist

Example:

session 1:

`$ cd client && sudo python ./demo-image.py 50 6 4 test.png`

session 2:

`$ sudo matrix-server`

# Examples

Several example scipts are included which demonstrate just a few things you can do with your cool display!
Currently included are:
- An Image Viewer
- A flying text display
- A NewRelic app performance monitor
- A mirror wall using the Raspberry Pi camera

# More Things
