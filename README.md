# TwitterCLI

an attempt to replicate Gary Bernhardt's functional twitter client in python
from memory

call nosetests in the root directory to run tests

## Structure

Things are rendered by the Blessed library

Architecture is based on something of a react-style unidirectional flow - we
respond to keystrokes or events in a main loop, which modifies the state
and pushes it down into the lower-level components

Our primary components are currently (going to be):
    1. main.py
        this is the main thing that holds terminal information and handles
        overall rendering
    2. several Screens
        these correspond to presentational components from React, where each
        has some state that it is given and it returns the representation of
        that state

Some specific screens are
    1. tweet list
    2. status bar

## Design Decisions

We are caching things in files for now because it's simple and we don't want to
introduce additional dependencies like redis. If we need something more complex
we will switch ASAP
