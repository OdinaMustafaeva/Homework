# homework4
def only_even_numbers(func):
    my = []

    def even(*args):
        for i in args:
            if i % 2 == 0:
                my.append(i)
                continue
            return f"please enter only even numbers"
        return func(my)

    return even


@only_even_numbers
def pluser(my_lis):
    b = 0
    for i in my_lis:
        b += i
    return b


print(pluser(2, 4, 5))
print(pluser(6, 4, 8))


# homework 5
def sum_list(func):
    def listr(ls):
        if type(ls) != list:
            print("Please enter list!")
        else:
            return func(ls)

    return listr


@sum_list
def divider(ls):
    return len(ls)


print(divider([2, 3]))
print(divider(10))
