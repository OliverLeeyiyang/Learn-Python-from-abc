# Basic Input and output
def calculate(a):
    return a ** 2


# Default value for a function parameter
## Examples
## Requirements for using default value (put it at the end)

def caca(a,c,b=2):
    return a ** b + c

def main():
    b = calculate(250)
    print(f"The square of 250 is: {b}")
    c = caca(2,20)
    print(f"3 raised to the power of 2 is: {c}")
if __name__ == "__main__":
    main()
