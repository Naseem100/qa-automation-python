def main():
    print(f_c(1))
    print(f_x(3, 2, 5))
    print(sum(2))

if __name__ == "__main__":
    main()

def f_c(x):
    '''Takes any input and returns the constant 4'''
    return 4

def f_x(x, a, b):
    return a*x + b

def sum(x):
    return f_x(x, 1, 1) + f_x(x, 2, 2) + f_x(x, 3, 3))