# homework1

def get_next_multiple(num, s):
    real_num = num
    for i in range(s):
        yield num + real_num
        real_num = real_num + num


number = int(input('enter number'))
number_of_plus = int(input('enter number plus'))
get_funk = get_next_multiple(number, number_of_plus)
for _ in range(number_of_plus):
    print(next(get_funk))


# homework2

def get_next_prime():
    s = False
    for num in range(100):
        flag = False
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break
            if flag == False:
                yield num


sd = get_next_prime()
for i in sd:
    print(i)


# homework3

def deco(one):
    def silco(two):
        return one * two

    return silco


f_num = int(input("enter one number:"))
s_num = int(input("enter two number:"))
my_prog = deco(f_num)
print(my_prog(s_num))
