# Copyright (c) 2012 Nathan Wailes

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author(s): Nathan Wailes

#ID: pablomo1
#PROG: milk2
#LANG: Python

# TASK
# Three farmers rise at 5 am each morning and head for the barn to milk three
# cows. The first farmer begins milking his cow at time 300 (measured in seconds
# after 5 am) and ends at time 1000. The second farmer begins at time 700 and
# ends at time 1200. The third farmer begins at time 1500 and ends at time 2100.
# The longest continuous time during which at least one farmer was milking a cow
# was 900 seconds (from 300 to 1200). The longest time no milking was done,
# between the beginning and the ending of all milking, was 300 seconds (1500
# minus 1200).

# Your job is to write a program that will examine a list of beginning and
# ending times for N (1 <= N <= 5000) farmers milking N cows and compute (in
# seconds):

# 1) The longest time interval at least one cow was milked.
# 2) The longest time interval (after milking starts) during which no cows were
#    being milked.


def main():

    import re

    # INPUT FORMAT
    # Line 1: The single integer N
    # Lines 2..N+1: Two non-negative integers less than 1,000,000, the starting
    # and ending time in seconds after 0500
    # SAMPLE INPUT (file milk2.in)
    # 3
    # 300 1000
    # 700 1200
    # 1500 2100
    input_file = open('milk2.in', 'r')
    number_of_cows = int(input_file.readline())

    #this big for-loop creates the master schedule I'll be using to answer
    #the questions I'm being asked.
    master_schedule = []
    for c in range(number_of_cows):
        c_schedule = input_file.readline()

        #get the start and end of this cow's milking
        c_start = re.findall("^[0-9]*", c_schedule)
        c_start = int(c_start[0]) #turns c_start from a list into an int
        c_end = re.findall("[0-9]*$", c_schedule)
        c_end = int(c_end[0])

        #if the cow's milking extends beyond the current max value of the
        #master schedule, extend the master schedule to that value, making
        #the values zero for now.
        while c_end > len(master_schedule):
            master_schedule.append(0)

        #this sets the range of the master_schedule to 1 that takes place during
        #this guy's milking
        for i in range(len(master_schedule)):
            if i <= c_end and i >= c_start:
                master_schedule[i] = 1


    #initializing variables i'll be using in the next part
    milk_type = 1 #the type variable is used when comparing 
    max_milk_start = 0
    max_milk_end = 0
    max_milk_time = 0
    idle_type = 0
    max_idle_start = 0
    max_idle_end = 0
    max_idle_time = 0

    #i want to be able to keep track of a current run and compare it against
    #the max run i've found so far
    current_run_length = 0
    current_run_type = 3 #just setting this to anything other than 1 or 0
    current_run_start = 0 

    #at this point I already have a completed schedule, so now I just need to
    #figure out what the longest stretches of milking/idleness are. I'm going to
    #walk this loop through every minute in the schedule and figure out, minute-
    #-by-minute, how this minute affects my max idleness/milking.
    for i in range(len(master_schedule)):
        i_busy_or_idle = master_schedule[i]

        #the code below handles what happens if the current minute is a
        #continuation of
        #the previous minute's activity (eg the previous minute was spent
        #milking and the current minute is also spent milking)
        if i_busy_or_idle == current_run_type:
            current_run_length += 1
        else:
            current_run_type = i_busy_or_idle
            current_run_start = i
            current_run_length = 1

        #the code below checks if the just-ended run is longer than the max
        #run i have recorded so far, and if so sets the max to the
        #just-completed run
        if current_run_type == milk_type and \
                              current_run_length > max_milk_time:
            max_milk_start = current_run_start
            max_milk_end = i
            max_milk_time = current_run_length

        if current_run_type == idle_type and \
                              current_run_length > max_idle_time:
            max_idle_start = current_run_start
            max_idle_end = i
            max_idle_time = current_run_length

    print "Longest milking time: " + str(max_milk_time)

    print "Max idle time: " + str(max_idle_time)

    # OUTPUT FORMAT:
    # A single line with two integers that represent the longest continuous time
    # of milking and the longest idle time.
    # SAMPLE OUTPUT (file milk2.out):
    # 900 300
    output_file = open('milk2.out', 'w')
    output_file.write("%d %d\n" % (max_milk_time, max_idle_time))


if __name__ == '__main__':
    main()
