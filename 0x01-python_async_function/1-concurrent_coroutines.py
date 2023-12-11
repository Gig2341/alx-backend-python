#!/usr/bin/env python3

'''
this module imports wait_random from the previous python file and writes an
async routine called wait_n that takes in 2 int arguments ( n and max_delay).
You will spawn wait_random n times with the specified max_delay.
wait_n returns the list of all the delays (float values). The list of
the delays should be in ascending order without using sort() because of
concurrency.
'''


