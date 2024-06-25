import re

def numerical_sort(value):
    numbers = re.findall(r'\d+', value)
    return int(numbers[0]) if numbers else 0

# using regex matching
# Sort lists like ["1ab","10gs","2qs"] based oncounting at start.
# use spListSort1([list to be sorted]) after import.

def spListSort1(filenames):
    return(sorted(filenames, key=numerical_sort))

