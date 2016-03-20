

    master_schedule = []

    print master_schedule

    for c in range(number_of_cows):
        c_schedule = input_file.readline()
        c_start = re.findall("^[0-9]*", c_schedule)
        c_start = c_start[0] #turns c_start from a list into an int
        c_end = re.findall("[0-9]*$", c_schedule)
        c_end = c_end[0]

        #if the master schedule is empty...
        if not len(master_schedule):
            master_schedule.append("idle" + str(c_start) + "milking")
            master_schedule.append("milking" + str(c_end) + "idle")
            print master_schedule
        else:
            for i in range(len(master_schedule)):
                i_time = re.findall("[0-9]*", master_schedule[i])
                
                if i = 0:
                    if c_start < i_time:
                        master_schedule.insert(i, "idle" + str(c_start) + "milking")
                         

                    
                i_minus_one_time = re.findall("[0-9]*", master_schedule[i-1])
                i_plus_one_time = re.findall("[0-9]*", master_schedule[i+1])
                print i_minus_one_time
                print i_time
                print i_plus_one_time
                if master_schedule[i] < c_start:
                    master_schedule.insert(i+1, c_start)
                    break

    print master_schedule
