#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Simple python script to calculate seat numbers 
# Usage: seat.py seats economy business
# Example: A KR-860 with 78% economy, 15% business and 7% first

import sys

def seat(seat, economy, business):
    print("Economy: {0}".format(seat*economy/100))
    print("Business: {0}".format(seat*business/200))
    print("First: {0}".format(seat*(100-economy-business)/400))
    
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {0} seats economy business".format(sys.argv[0]))
    else:
        seat(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
