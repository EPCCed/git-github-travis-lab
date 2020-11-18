#!/usr/bin/env python3
# --------------------------------------------------------------------------------------
# Course: Programming Skills - Online INFD11016 Sep-Dec 2020
# Course organiser: Dr Chris Wood.
#
# ID of practical: Continuous integration and Travis CI practical
# Name of student: Enrique Mendez, e.mendez@sms.ed.ac.uk
# Details about practical: Here, we will set up a  Travis CI job, based around a
# simple test program , to get you up and running with Travis CI
#
# References and and Acknowledgements
# * Jackson, Mike (24 Oct 2018).  EPCC, The University of Edi.
# --------------------------------------------------------------------------------------
#
# COMMENTS ON PROGRAM
# simple test that calls on main rot13 program and function rot13_char
#
# --------------------------------------------------------------------------------------

from msc.rot13 import rot13
from msc.rot13 import rot13_char

def test_function_name1():
    assert "raevdhr" == rot13("enrique"), "Unexpected character"

# the following functions assert for an invalid result
def test_function_name2():
    assert "pynved" != rot13("claire"), "Unexpected character"