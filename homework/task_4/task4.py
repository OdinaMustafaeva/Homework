import csv

with open("new_country_of_the_world.csv", "a+") as new_world:
    with open("country_of_the_world.csv", "r+") as old_world:
        def get_v():
            red = old_world.readlines()
            for i in red:
                i = i.replace(",", ".")
                new_world.write(i)


        get_v()
