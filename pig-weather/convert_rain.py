#!/usr/bin/env python

import sys
import string

while True:
  line = sys.stdin.readline()
  if not line:
    break

  row = string.strip(line, "\n")
  year, month, max_temp, min_temp, frost_days, rainfall_mm, sunshine = string.split(row, "\t")
  rainfall_inches = float(rainfall_mm) / 25.4
  print "\t".join([year, month, max_temp, min_temp, frost_days, str(rainfall_inches), sunshine])

