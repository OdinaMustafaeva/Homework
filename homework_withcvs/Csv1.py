# bu bir shahar yoki mamlakatdagi mahallalar va mahalladagi odamlarni ro‘yxatga olish vazifasini bajaradi
# work wth csv


import csv

fieldnames = ['location', 'name', 'age', 'phone_number', 'work']


def add_new_data(name_file, f, num):
    global fieldnames
    if num == 1:
        with open(name_file, "w") as my_new:
            new_d = csv.DictWriter(my_new, fieldnames, delimiter=',')
            new_d.writeheader()
            new_d.writerow(f)
    else:
        with open(name_file, "a") as my_new2:
            my_new2.write(f)


for i in range(3):
    big_q = input("""
     #1 = add new district
     #2 = add new data 
     #3 = know someone's location
     #4 = see all data
     >:""")
    if big_q == '1':
        with open("distructsname.txt", "a") as distructs:
            new_district = input("enter new district name")
            new_district1 = open(new_district, "a+")
            distructs.write(f"\n{new_district}")
            print('you must to add one person your new distruct director')
            dict1 = {
                'name': input("enter name"),
                'age': input("enter age"),
                'location': input("enter location"),
                'phone_number': input("enter phone number"),
                'work': input("enter work")
            }
            add_new_data(new_district, dict1, 1)
    elif big_q == '2':
        with open('distructsname.txt', 'r') as distructs:
            a = distructs.read()
            ch_dis = input(f"{a} which distruct  :")
            try:
                ch_dis1 = open(ch_dis, "a")
            except FileNotFoundError:
                print('This file not found')
            else:
                location = input("enter location")
                name = input("enter name")
                age = input("enter age")
                phone_number = input("enter phone number")
                work = input("enter work")
                dict1 = f"\n{location}, {name}, {age}, {phone_number}, {work}"
                add_new_data(ch_dis, dict1, 2)

    elif big_q == '3':
        with open("distructsname.txt", "r+") as distructs:
            a = distructs.read()
            ch_dis = input(f"{a} which distruct  :")
            try:
                ch_dis1 = open(ch_dis, "r+")
            except FileNotFoundError:
                print('This data not found')
            else:
                redo = csv.DictReader(ch_dis1)
                print('name and location')
                for j in redo:
                    print(f"{j['name']} = {j['location']}")
    elif big_q == '4':
        with open('distructsname.txt', 'r+') as distructs:
            a = distructs.read()
            ch_dis = input(f"{a} which distruct  :")
            try:
                ch_dis1 = open(ch_dis, "r+")
            except FileNotFoundError:
                print('This data not found')
            else:
                redo1 = csv.DictReader(ch_dis1)
                for v in redo1:
                    print(v)
