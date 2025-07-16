# Fibonacci numbers are defined as follows:
# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2) for n > 1

# Fibonacci formula: 
# F(n) = F(n-1) + F(n-2)

# fibonacci algorithm: 
# get the first two fibonacci numbers
# then use a loop to calculate the next numbers up to n by adding the last two numbers
# update the value of the last two numbers in each iteration
# # return the nth fibonacci number

# Loops vs Recursion:
# 1. For loop to calculate Fibonacci numbers iteratively

# implementation of Fibonacci numbers using a loop
# two variables to store the last two Fibonacci numbers 
# a loop that runs from 2 to n (n is 18 in this case)
# Print the new Fibonacci number in each iteration
# Update the last two Fibonacci numbers in each iteration

# varibles to store the last two Fibonacci numbers
prev1 = 0
prev2 = 1

# loop to calculate Fibonacci numbers iteratively
for fibo in range(2, 19):
    # calculate the next Fibonacci number by adding the last two numbers
    new_fibo = prev1 + prev2
    print(new_fibo)
    # update the last two Fibonacci numbers
    prev1 = prev2
    prev2 = new_fibo
    
# 2. implementation of Fibonacci numbers using recursion
last1 = 0
last2 = 1
count = 2 # begin counting from the third Fibonacci number

def fibonacci_recursive(last1, last2):
    global count
    if count <= 19:
        new_fibo = last1 + last2
        print(new_fibo)
        count += 1
        fibonacci_recursive(last2, new_fibo) # recursive call to continue the sequence
    else: 
        return
    
fibonacci_recursive(last1, last2) # call the recursive function to start the sequence
    