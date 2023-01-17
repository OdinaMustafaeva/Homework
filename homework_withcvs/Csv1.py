# work wth csv
import csv

fieldnames = ['location', 'name', 'age']

big_q = input("""
     #1 = add new district
     #2 = add new data 
     #3 = know someone's location
     #4 = see all data
     >:""")
if big_q == '1':
    new_district = input("enter n ew district name")
    new_district1 = open(new_district, "a+")
    with open("distructsname.txt", "r+") as distructs:
        distructs.write(f"{new_district} ,")
        print('Good')
        csv.DictWriter(new_district, fieldnames, delimiter=',')
elif big_q == '2':
    add_distructs = []
    with open("distructsname.txt", "r+") as distructs:
        a = distructs.read()
        add_distructs.append(a)
        ch_dis = input(f"{add_distructs} which distruct  :")
        try:
            ch_dis1 = open(ch_dis, "a+")
        except Exception:
            print('This data not found')
        else:
            location: input("enter location")
            name: input("enter name")
            age: input("enter age")
            csv.writer(a)

elif big_q == '3':
    add_distructs = []
    with open("distructsname.txt", "r+") as distructs:
        a = distructs.read()
        add_distructs.append(a)
        ch_dis = input(f"{add_distructs} which distruct  :")
        try:
            ch_dis1 = open(ch_dis, "r+")
        except Exception:
            print('This data not found')
        else:
            redoo = csv.DictReader(ch_dis1)
            print('name and location')
            for i in redoo:
            print(f"{i['name']} = {i['location']}")
elif big_q == '4':
    add_distructs = []
    with open("distructsname.txt", "r+") as distructs:
        a = distructs.read()
        add_distructs.append(a)
        ch_dis = input(f"{add_distructs} which distruct  :")
        try:
            ch_dis1 = open(ch_dis, "r+")
        except Exception:
            print('This data not found')
        else:
            redoo = csv.DictReader(ch_dis1)
            for i in redoo:
            print(i)
