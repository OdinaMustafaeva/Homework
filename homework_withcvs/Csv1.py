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
    new_district = input("enter new district name")
    new_district1 = open(new_district, "a+")
    with open("distructsname.csv", "r+") as distructs:
        distructs.write(new_district)
        print('Good')
elif big_q == '2':
    add_distructs = []
    with open("distructsname.csv", "r+") as distructs:
        a = distructs.read()
        add_distructs.append(a)
        ch_dis = input(f"{add_distructs} which distruct  :")
        try:
            ch_dis1 = open(ch_dis, "a+")
        except Exception:
            print('This data not found')
        else:
            all_d = csv.DictWriter(ch_dis1, fieldnames, delimiter=',')
            inp = int(input('how much data do you to add?'))
            for s in range(inp):
                print(f'data {s}')
                all_list = {
                    'location': input(f'data enter location'),
                    'name': input('enter name'),
                    'age': input('enter age')
                }
                all_d.writerow(all_list)





elif big_q == '3':
    add_distructs = []
    with open("distructsname.csv", "r+") as distructs:
        a = distructs.read()
        add_distructs.append(a)
        ch_dis = input(f"{add_distructs} which distruct  :")
        try:
            ch_dis1 = open(ch_dis, "r+")
        except Exception:
            print('This data not found')
        else:
            redoo = csv.reader(ch_dis1)
            print('name and location')
            for i in redoo:
                print(f"{i}")

elif big_q == '4':
    add_distructs = []
    with open("distructsname.csv", "r+") as distructs:
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
