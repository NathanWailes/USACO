/*
ID: pablomo1
PROG: milk2
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int
main(void)
{

  // INPUT FORMAT
  // Line 1: The single integer N
  // Lines 2..N+1: Two non-negative integers less than 1,000,000, the starting
  // and ending time in seconds after 0500
  // SAMPLE INPUT (file milk2.in)
  // 3
  // 300 1000
  // 700 1200
  // 1500 2100
  ifstream fin ("milk2.in");
  int number_of_cows;
	fin >> number_of_cows;

  // this big for-loop creates the master schedule I'll be using to answer
  // the questions I'm being asked.
  string master_schedule = "";
  for (int c = 0; c < number_of_cows; ++c) {
    int c_start;
    int c_end;
    fin >> c_start >> c_end;
    
    //if the cow's milking extends beyond the current max value of the
    //master schedule, extend the master schedule to that value, making
    //the values zero for now.
    while (c_end > master_schedule.length()){
      master_schedule.append("0");
    }
    
    //this sets the range of the master_schedule to 1 that takes place during
    //this guy's milking
    for (int i = 0; i < master_schedule.length(); ++i){
      if (i < c_end && i >= c_start){
        master_schedule.replace(i, 1, "1");
      }
    }
  }
  
  //initializing variables I'll be using in the next part
  int milk_type = 1;
  int max_milk_start = 0;
  int max_milk_end = 0;
  int max_milk_time = 0;
  int idle_type = 0;
  int max_idle_start = 0;
  int max_idle_end = 0;
  int max_idle_time = 0;
  
  //i want to be able to keep track of a current run and compare it against
  //the max run i've found so far
  int current_run_length = 0;
  int current_run_type = 3; //just setting this to anything other than 1 or 0
  int current_run_start = 0;
  
  //I'm only supposed to count idle time AFTER MILKING STARTS, so I need to
  //keep track of whether milking has started or not.
  int milking_started = 0;

  //at this point I already have a completed schedule, so now I just need to
  //figure out what the longest stretches of milking/idleness are. I'm going to
  //walk this loop through every minute in the schedule and figure out, minute-
  //-by-minute, how this minute affects my max idleness/milking.
  for (int i = 0; i < master_schedule.length(); ++i){
    int i_busy_or_idle = atoi(master_schedule.substr(i,1).c_str());
    
    //cout << master_schedule.at(i);
    //cout << i_busy_or_idle;
    //the code below handles what happens if the current minute is a
    //continuation of the previous minute's activity or not (eg the previous
    //minute was spent milking and the current minute is also spent milking)
    if (i_busy_or_idle == current_run_type){
      ++current_run_length;
    }
    else {
      current_run_type = i_busy_or_idle;
      current_run_start = i;
      current_run_length = 1;
    }
    
    //the code below checks if the just-ended run is longer than the max run I
    //have recorded so far, and if so sets the max to the just-completed run
    if ((current_run_type == milk_type) &&
        (current_run_length > max_milk_time)){
      max_milk_start = current_run_start;
      max_milk_end = i;
      max_milk_time = current_run_length;
      milking_started = 1;
    }
    if ((current_run_type == idle_type) &&
        (current_run_length > max_idle_time) && milking_started == 1){
      max_idle_start = current_run_start;
      max_idle_end = i;
      max_idle_time = current_run_length;
    }
  }

  // OUTPUT FORMAT:
  // A single line with two integers that represent the longest continuous time
  // of milking and the longest idle time.
  // SAMPLE OUTPUT (file milk2.out):
  // 900 300
  ofstream fout ("milk2.out");
	fout << max_milk_time << " " << max_idle_time << endl;
  return (0);
}
