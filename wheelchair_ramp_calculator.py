#!/usr/bin/env python

__author__ = "Sam Gordon"
__email__ = "seg@well.com"

# wheelchair ramp force-requirement calculator

import math

patient_wt = 130
wheelchair_wt = 30
rr = 1.005
ramp_incline_degrees = 4.78 # ADA incline of 1/12


radians = math.radians(ramp_incline_degrees)
wt = patient_wt + wheelchair_wt
wt_w_rr= wt*rr

total_force = wt_w_rr * math.sin(radians)
print(total_force)
