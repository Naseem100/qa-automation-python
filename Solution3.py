from math import sqrt

def sum_of_digits(n):
    sum = 0
    if n < 0:
        num = str(n - 2*n)
    else:
        num = str(n)
    for x in range(0, len(num)):
        sum += int(num[x])
    return sum

def to_digits(n):
    nstr = str(n)
    for x in range(0, len(nstr)):
        print(nstr[x])

digits = [
    2, 3, 4, 6, 9
]


def to_number(digits1):
    returned = ""
    for x in range(0, len(digits1)):
        returned += str(digits1[x])
    return returned


vowels = [
    'a', 'e', 'i', 'o', 'u', 'y'
]


def count_vowels(str):
    num_of_vowels = 0
    for x in range(0, len(str)):
        if str[x] in vowels:
            num_of_vowels += 1
    return num_of_vowels


def prime_number(number):
    if number < 2:
        return True
    for x in range(2, int(sqrt(number) + 1)):
        if number % x == 0:
            return False
    return True


def fact_digits(n):
    strn = str(n)
    sum = 0
    for x in range(0, len(strn)):
        sums = 1
        for y in range(1, int(strn[x]) + 1):
            sums *= y
        sum += sums
    return sum


def fibonacci(n):
    sum = 0
    sum2 = 1
    sum3 = 0
    fibonaccis = list()
    for x in range(0, n):
        sum += sum3
        sum3 = sum2
        sum2 = sum
        fibonaccis.append(sum)
    return fibonaccis


def fib_number(n):
    fibonaccis = fibonacci(n + 1)
    string = ""
    for x in range(0, n + 1):
        string += str(fibonaccis[x])
    return string


def palindrome(obj):
    strobj = str(obj)
    if strobj == strobj[::-1]:
        return "This is a palindrome"
    else:
        return "This is not a palindrome"


def char_histogram(s):
    charDict = dict()
    for x in s:
        if x in charDict:
            charDict[x] = charDict[x] + 1
        else:
            charDict[x] = 1
    return charDict


def main():
    print(sum_of_digits(-33))
    to_digits(323)
    print(to_number(digits))
    print(count_vowels("hhafdfdheiougfgfgf"))
    print(prime_number(25))
    print(fact_digits(145))
    print(fibonacci(10))
    print(fib_number(3))
    print(palindrome("12321"))
    print(char_histogram("This is a test"))


if __name__ == "__main__":
    main()


