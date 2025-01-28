# Exercise 3.4
"""Write a function that finds the Fibonacci sequence up to an integer N > 0 in the notebook. 
Now call this function for N = 10 and N=100.
Zenzi Pahla
UN-OG Core training
25 January 2025
"""

# Writing a Fibonacci sequence without using modules
def fibonacci(N):
    fibonacci_sequence = [0, 1]
    while True:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_value > N:
            break
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence    

# Call the function for N = 10 and N = 100
fibonacci_10 = fibonacci(10)
fibonacci_100 = fibonacci(100)
print("Fibonacci sequence up to 10:", fibonacci_10)      #Output: Fibonacci sequence up to 10: [0, 1, 1, 2, 3, 5, 8]
print("Fibonacci sequence up to 100:", fibonacci_100)    #Output: Fibonacci sequence up to 100: [0, 1, 1, 2, 3, 8, 13, 21, 34, 55, 89]

# Writing a Fibonacci sequence using modules
import itertools

def fib(N):
    a, b = 0, 1
    for x in itertools.count():
        if a > N:
            break
        yield a
        a, b = b, a + b

# Call the function for N = 10 and N = 100
fib_10 = list(fib(10))
fib_100 = list(fib(100))
print("Fibonacci sequence up to 10:", fib_10)      #Output: Fibonacci sequence up to 10: [0, 1, 1, 2, 3, 5, 8]
print("Fibonacci sequence up to 100:", fib_100)    #Output: Fibonacci sequence up to 100: [0, 1, 1, 2, 3, 8, 13, 21, 34, 55, 89]