# A program to calculate Fibonacci
# Modify by: Kaden
# Input: N
# Process:
#   Define Fib(1) = 1, Fib(2) =1
#   Define function Fib(N) = Fib(N-1) + Fib(N-2)
# Output: Fib(N)


def Fib(N):
    if(N == 1):
        return 1
    if(N == 2):
        return 1
    return Fib(N - 1) + Fib(N - 2)


def C3_Q16():
    # Print instruction
    print("Welcome to Fibonacci tool.")
    print("This tool will help you to calculate Fibonacci at position N")
    print("Please input a number, this tool will show you the value of Fibonacci.")

    # ------
    N = eval(input("What is the position?:  "))
    value = Fib(N)
    print("The value is", value)


C3_Q16()
