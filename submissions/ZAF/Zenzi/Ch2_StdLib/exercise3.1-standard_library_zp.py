# standard_library.py
"""Python Essentials: The Standard Library.
Zenzi Pahla
UN-OG-ZAF
4 November 2024
"""

# Problem 1
def prob1(L):
    return L
L = [5, 3, 2, 9, 8, 1, 7]
print(min(L), max(L), sum(L)/7)
  ## Output: 1 9 5.0

# Problem 2
"""Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
integer = {"first": 123, "second": 64206, "third": 115}
random_numbers = integer
for item, number in random_numbers.items():
    integer[item] = (number + 1)
print(random_numbers)    
print(integer)
  # Base integers have been lost
integer = dict(random_numbers)
for item, number in integer.items():
    integer[item] = (number + 1)  
print(random_numbers)    
print(integer)
 #integers are mutable

strings = ["Zenzi", "Sarai", "Mwansa", "Themba"]
family = strings
family.insert(4, "Pahla")
print(family)
print(strings)
family.remove("Pahla")
  # Base strings lost
strings = dict(family)
family.insert(4, "Pahla")
print(family)
print(strings)
  # Strings are immutable

lists = ["math", 65, "science", 49, "home econonomics", 98, "english", 52]
high_school_grades = lists
high_school_grades.append("geography")
high_school_grades.append(73)
print(high_school_grades)
print(lists)
  # Base list lost
lists = dict(high_school_grades)
high_school_grades.append("geography")
high_school_grades.append(73)
print(high_school_grades)
print(lists) 
  # Lists are immutable

def tuples(a, b, c, d):
    return((a + b + c + d) / 4)
monthly_salary = tuples(5000, 6000, 4500, 8600)
print(monthly_salary)
# Tuples are immutable    
    
sets = {"Vera Songwe", "Ngozi Okonjo-Iweala", "Helene Rey"}
favourite_economists = sets
favourite_economists.add("Michelle Tertilt")
print(sets)
print(favourite_economists)
favourite_economists.discard("Michelle Tertilt")
  #Base set lost
sets = dict(favourite_economists)
favourite_economists.add("Michelle Tertilt")
print(sets)
print(favourite_economists)
  #Sets are immutable

# Problem 3
def hypot(a, b):
    return a + b, a * b
calculator = hypot(9, 12)
print(calculator)
 #Answer: (21, 108)

import calculator
calculator.sqrt(hypot)
  #Recieved an error message

# Problem 4
def power_set(A):
    return 2**A
A = {'a', 'b', 'c'}

from itertools import chain
for i,number in enumerate(chain(range(3))):
    if i == 0:
        print(set(A))
    elif i > 0:
        print(power_set) 


# Problem 5: Implement shut the box.
from itertools import combinations
def isvalid(roll, remaining):
    if roll not in range(1, 13):
        return False
    for i in range(1, len(remaining)+1):
        if any([sum(combo) == roll for combo in combinations(remaining, i)]):
            return True
    return False

isvalid(20, 5)
 #returns false because 20 is outside the range
isvalid(1, 2)
# keep getting an error despite 1 being in the range
# error: oject of type 'int' has no len()

def parse_input(player_input, remaining):
    try:
        choices = [int(i) for i in player_input.split()]
        if len(set(choices)) != len(choices):
            raise ValueError
        if any([number not in remaining for number in choices]):
            raise ValueError
        return choices
    except ValueError:
        return []
parse_input(5, 7)
  # error: 'int' object has no attribute 'split'


