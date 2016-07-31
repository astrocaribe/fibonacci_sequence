#! /ust/bin/env python

#Header
"""
:Description:   Function for the Fibonacci Sequence.

:Execute:
                >>> python fibonacci_sequence

:Input(s):      User Input (integer)

:Output(s):     Calculated total from the sequence

:Author:        Tommy LeBlanc
                http://astrocaribe.com

:Revisions:
                - Written by Tommy LeBlanc, Aug 2016
"""

from __future__ import print_function
from sys import version_info


# Functions
# ------------------------------------------------------------------------------

# Check python version. Returns 'True' for python3, else returns 'False' for
# python2
def is_python3( version ):
    return version > 2


# Calculate the fibonacci number given an integer
def fNumber( inputValue ):

    if inputValue == 0:
        return 0
    elif inputValue == 1:
        return 1
    else:
        fibonacci_number = fNumber( inputValue - 1 ) + fNumber( inputValue - 2)
        return fibonacci_number
