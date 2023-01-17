# work wth csv
import csv

distructs = open("distructsname.txt", 'r+')
fieldnames = ['location', 'name', 'age']
for i in range(3):
    big_q = input("""
     #1 = add new district
     #2 = add new data 
     #3 = know someone's location
     #4 = see all data
     >:""")
    if big_q == '1':
        new_district = input("enter new district name")
        new_district1 = open(new_district, "w")
        distructs.write(f"{new_district}")
        distructs.write(",")
        print('Good')
    elif big_q == '2':
        add_distructs = []
        a = distructs.read()
        add_distructs.append(a)
        ch_dis = input(f"{add_distructs} which distruct  :")
        try:
            ch_dis1 = open(ch_dis, "r+")
        except Exception:
            print('This data not found')
        else:
            list_da = {
                'name': input("enter name"),
                'age': input("enter age"),
                'location': input("enter location")
            }
            new_d = csv.DictWriter(ch_dis1, fieldnames, delimiter=',')
            new_d.writeheader()
            new_d.writerow(list_da)


    elif big_q == '3':
        add_distructs = []
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
