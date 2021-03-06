toyrobot
========

Toy Robot Code Challenge given by iress.

- Created:  2022-May-13
- Creator:  [Darwin Molero](mailto:darwin.molero@coderax.com)


Overview
--------

The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no
other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented
from falling to destruction. Any movement that would result in the robot falling from the table must be prevented,
however further valid movement commands must still be allowed.


Specification
-------------

This is a console application that can read in commands of the following form:

* PLACE X,Y,F
* MOVE
* LEFT
* RIGHT
* REPORT

> Input can be from a file, or from standard input, as the developer chooses.


#### PLACE

* will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. 
* The origin (0,0)
can be considered to be the SOUTH WEST most corner. 
* It is required that the first command to the robot is a PLACE
command, after that, any sequence of commands may be issued, in any order, including another PLACE command. 
* The
application should discard all commands in the sequence until a valid PLACE command has been executed.


#### MOVE

* will move the toy robot one unit forward in the direction it is currently facing.


#### LEFT and RIGHT 
* will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

#### REPORT

* will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.


Rules
-----

* A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.
* The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. 
* Any
move that would cause the robot to fall must be ignored.


Usage
-----

First create a virtual environment for this project.

    $ conda create --name toyrobot python=3.9.12

Activate the virtual environment

    $ conda activate toyrobot

Install requirements

    $ pip install -r requirements.txt

Run tests

    $ pytest -s tests

To run in interactive mode:

    $ python main.py

To run with a script:

    $ python main.py <path/to/script-file>

where path/to/script-file contains the toy robot commands.

example:

    $ python main.py bot-script.trs

will run the sample bot-script.trs file provided. 
