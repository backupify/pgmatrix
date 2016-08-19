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


# Construction and Panel Layout
The rpi-rgb-led-matrix repo has some great wisdom for constructing and wiring a display. I used the suggestion of alimunum bars for distributing current to the panels. I didn't have convenient access to a shop so I picked up some Door Bottoms from Ace Hardware. They are super cheap work perfectly as pre-drilled aluminum extrusions. The holes were distanced perfectly for the panels.

To hold the panels together, we 3D printed some simple brackets and screwed them onto the panels. This was actually not enough support, so we planned to put a frame around the completed screen. However, zip-tying the aluminum extrusions across the back of the display added enough support for the display to hold together on its own. A frame would still be needed to mount the display.

The server assumes that the panels are laid out in an 'S' formation, with the first panel in the bottom left corner, like so:

![layout](https://github.com/backupify/pgmatrix/blob/master/results/panel-order.jpg?raw=true)

The exact number of panels (in the x and y direction) can be configured via command line arguments as long as the panels follow this configuation. 

# Usage
You'll want to execute the program from a screen / tmux session.

In one terminal, cd into the client directory:

`$ cd client`

and run the desired script:

`$ sudo python ./demo-image.py <brightness(1..100)> <width(1..32) <height(1..32)> [program arguments]`

In a second terminal run the server:

`$ sudo ./matrix-server <brightness(1..100)> <width(1..32) <height(1..32)>`

Brightness should be an integer from 0 to 100, and width and height are in panels, not in pixels.

Note: The python client is responsible for making the named pipe if it does not exist. So if the pipe has not been made, the client must be run before to sever or the server will crash silently.

TODO: Make server create pipe if it does not exist

Example:

session 1:

`$ cd client && sudo python ./demo-image.py 50 6 4 test.png`

session 2:

`$ sudo matrix-server 50 6 4`

# Examples

Several example scipts are included which demonstrate just a few things you can do with your cool display!
Currently included are:
- An Image Viewer
- A flying text display
- A NewRelic app performance monitor
- A mirror wall using the Raspberry Pi camera

# Results and Notes
After assembling the large (6x4x32px) display, we noticed that it is very straining to look at from a distance of less than six feet. Additionally, arranging the panels in alternation directions causes a slight contrast between rows when viewed at an angle.

As you can see, these are very simple examples, but pygame makes it very easy to combine these in interesting ways and do all sorts of cool effects. You can very easily play video, manipulate images, create moderately complex pixel animations, or anything else you can do with pygame, which is a lot!

Final display in action (please excuse the scan lines!):

A Big Mirror:
![Camera](https://github.com/backupify/pgmatrix/blob/master/results/camera.jpg?raw=true)

Pretty good color reproduction:
![Color](https://github.com/backupify/pgmatrix/blob/master/results/color.jpg?raw=true)
