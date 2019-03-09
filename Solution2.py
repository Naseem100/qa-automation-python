IS_TRUE = True
IS_FALSE = False


def num_add(a, b):
    return a + b


def num_sub(a, b):
    return a - b


def num_mul(a, b):
    return a * b


def num_div(a, b):
    return a / b


def num_floor(a, b):
    return a // b


def num_rem(a, b):
    return a % b


PANCAKE_INGREDIENTS = {
    "flour": 2,
    "eggs": 4,
    "milk": 200,
    "butter": False,
    "salt": .001
}

FIBONACCI_NUMBERS = [
    1,1,2,3,5,8,13,21,34,55,89,144
]


def ingredient_exists(ingr, dict):
    if ingr in dict:
        return True
    else:
        return False


def fatten_pancakes(dict):
    fatPancakes = dict.copy()
    fatPancakes["eggs"] = 6
    fatPancakes["butter"] = True
    return fatPancakes


def add_sugar(dict):
    newRecipe = dict.copy()
    newRecipe["sugar"] = 0
    return newRecipe


def remove_salt(dict):
    dict.pop("salt")
    return dict


def add_fibonacci(lst):
    lst.append(lst[len(lst) - 1] + lst[len(lst) - 2])
    return lst


def fib_exists(lst, n):
    if n in lst:
        return True
    else:
        return False


def which_fib(lst, n):
    return lst.index(n) + 1


def main():
    print(num_add(1, 2))
    print(num_sub(1, 2))
    print(num_mul(1, 2))
    print(num_div(1, 2))
    print(num_floor(1, 2))

    print(ingredient_exists("cream", PANCAKE_INGREDIENTS))
    print(fatten_pancakes(PANCAKE_INGREDIENTS))
    print(add_sugar(PANCAKE_INGREDIENTS))
    print(remove_salt(PANCAKE_INGREDIENTS))
    print(add_fibonacci(FIBONACCI_NUMBERS))
    print(fib_exists(FIBONACCI_NUMBERS, 144))
    print(which_fib(FIBONACCI_NUMBERS, 55))


if __name__ == "__main__":
    main()
