import itertools
import datetime
import re

# helper functions
def chech_if_hour_is_valid(numbers):
  """
  takes list of strings representing components of time, checks wether its a valid hour

  input: list[<str>,<str>,<str>,<str>]
  returns: <Boolean>
  """
  hour = int("".join(numbers[0:2]))
  minutes = int("".join(numbers[2:4]))
  if (hour < 24 and minutes < 60):
    return True
  return False

def check_HHMM_format(time):
  """
  checks if string matches "HH:MM" pattern

  input <string>
  returns <Boolean>
  """
  pattern = r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
  if re.match(pattern, time):
    return True
  return False


# main function
def next_time_(time):
  """
  takes time in HH:MM format
  returns next hour created with the same numbers and time delta upon it
  
  input:    <string>    ex. "21:01"
  returns:   <string>   ex. "21:01 => (21:10, 0:09)
  """
  if check_HHMM_format(time):
    time_numbers = list(time.replace(":", ""))   #['2','1','0','1']
    input_time = "".join(time_numbers)            #'2101'

    permutations = list(itertools.permutations(time_numbers))   #all possible permutations
    valid_hours_numbers = list(filter(chech_if_hour_is_valid, permutations))
    valid_hours_numbers_unique = list(dict.fromkeys(valid_hours_numbers))     #[('2','1','0','1'),...]

    if (len(valid_hours_numbers_unique) == 1):
      #only one possibility -> 24h till next hour
      return f"{time} => ({time}, 24:00)"

    valid_hours_unique_sorted = sorted("".join(i) for i in valid_hours_numbers_unique)  #['0112','0121',...]
    greater_hours = sorted("".join(i) for i in valid_hours_numbers_unique if "".join(i) > "".join(time_numbers))  #['2110',...]

    next_time = greater_hours[0] if len(greater_hours) > 0 else valid_hours_unique_sorted[0]
    day_delta = 0 if len(greater_hours) > 0 else 1

    time_object_input = datetime.timedelta(hours = int(input_time[0:2]), minutes = int(input_time[2:4]), seconds = 0)                #input time object
    time_object_next = datetime.timedelta(days = day_delta, hours = int(next_time[0:2]), minutes = int(next_time[2:4]), seconds = 0) #next time object

    delta_datetime_object = time_object_next - time_object_input                                                                      #timedelta object
  
    delta_time = str(delta_datetime_object).split(":")   #['00','09','00']

    input_time_format = datetime.time(int(input_time[0:2]), int(input_time[2:4])).strftime("%H:%M")          #21:10
    next_time_format = datetime.time(int(next_time[0:2]), int(next_time[2:4])).strftime("%H:%M")          #21:10
    delta_time_format = ":".join(delta_time[0:2])

    return f"{input_time_format} => ({next_time_format}, {delta_time_format})"
    
  else:
    return "Please enter time in valid format => HH:MM(24h) => ex. 22:22"





#rozwiazanie
time_input = input("Enter time in HH:MM format(24h):  ")
print(next_time_(time_input))



