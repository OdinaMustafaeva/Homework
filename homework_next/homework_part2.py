# homework4
def only_even_numbers(func):
    def even(a, b):
        if (a + b) % 2 != 0:
            return 'please enter only even numbers'
        else:
            func(a, b)

    return even


@only_even_numbers
def pluser(a, b):
    return a + b


print(pluser(10, 4))
print(pluser(10, 5))


# homework 5
def sum_list(func):
    def listr(ls):
        try:
            type(ls) == list
        except Exception:
            print("Please enter list!")

    return listr


@sum_list
def divider(ls):
    return ls


print(divider([2, 3]))
print(divider(10))
