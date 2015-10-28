#!/usr/bin/env python

__author__ = "Sam Gordon"
__email__ = "seg@well.com"

# wheelchair ramp force-requirement calculator

import math

rr = 1.005
ramp_incline_degrees = 4.78 # ADA incline of 1/12 is 4.78deg


radians = math.radians(ramp_incline_degrees)

# collecting data for patients up to 300 pounds,

def percentage(part, whole):
    return 100 * float(part)/float(whole)

wt = 60
for i in range(60,300):
    wt += 1
    wt_w_rr = wt * rr
    total_force = wt_w_rr * math.sin(radians)
    print(str(wt) + " lbs   " + str("%.2f" % total_force) + " " + "lbs " + "  " + str(ramp_incline_degrees) + " degree incline   " + str("%.3f" %percentage(total_force, wt)) + " percent of pt total weight")
