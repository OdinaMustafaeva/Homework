# A
list_20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10]
iter_ = iter(list_20)
for i in list_20:
    if i % 2 == 0:
        print(f"-{next(iter_)}")
    else:
        print(next(iter_))


# B

def get_20():
    for i in range(1, 20):
        if i % 2 == 0:
            yield f"-{i}"
        else:
            yield f"{i}"


run_it = get_20()
for i in run_it:
    print(i)
