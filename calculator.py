def main():
    x = int(input("What is x? "))
    print("The square of x is", square(x))

def square(n):
    return pow(n, 2)

main()