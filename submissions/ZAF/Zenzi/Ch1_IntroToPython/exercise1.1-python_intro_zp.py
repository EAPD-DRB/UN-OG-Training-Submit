# exercise 1.1 python_intro.py
"""Python Essentials: Introduction to Python.
Zenzi Pahla
OG-ZAF Training
18 September 2024
"""


# Problem 1 (write code below)
if __name__ == "__main__":
        print("Hello, world!")    

# Problem 2
def sphere_volume(r):
        """caclulate r."""
        return r
r = 4/3 * 3.14159 * r**3
print(r)
# Answer I get = 7.647679845147599e+24
    
# Problem 3
def isolate(a, b, c, d, e):
     """Print the arguments spearated by spaces but print 5 spaces on either side of b."""
     print(a, b, c, d, e)

     isolate(1, 2, 3, 4, 5)
# Didn't know how to use the sep and end functions

# Problem 4
def first_half(my_string):
    first_half("my_string")
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    

def backward(my_string):
    step(backward)
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
#Could not do Problem 4 using these functions
#Problem 4 using the functions learned before
my_string = "Complicated"
"""Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters""" 
my_string[:5]
backward("Complicated")
# Could not use these functions

# Problem 5
def list_ops(a, b, c, d):
     return a, b, c, d
list_ops = ["bear", "ant", "cat", "dog"] 
list_ops.append("eagle")
list_ops.insert(2, "fox")
list_ops.remove("bear")
# don't know how to sort in alphabetical order
list_ops.insert(4, "hawk")
list_ops.remove("eagle")
list_ops.insert(5, "hunter")
list_ops


# Problem 6
def pig_latin(word):
    return word
word = "zenzi"
print(word)
if 'a' in word == 1:
    print(word + "hay")
elif 'e' in word == 1:
     print(word + "hay")
elif 'i' in word == 1:
     print(word + "hay")
elif 'o' in word == 1:
     print(word + "hay")
elif 'u' in word == 1:
     print(word + "hay")                       
else:
    print(word + "ay")

# Problem 7
largest_palindrome = 0
for i in range(999, 99, -1):
     for j in range(i, 99, -1):
          product = i * j
          if str(product) == str(product)[::-1]:
               if product > largest_palindrome:
                    largest_palindrome = product
print(largest_palindrome)

# Problem 8
def alt_harmonic(n):
    x = 0
    for i in range(0, n):
         x = x + 1 / (i + 1)
         return x
print(i)
