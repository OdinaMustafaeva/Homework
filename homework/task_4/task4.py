import csv
with open("new_country_of_the_world.csv", "a+") as new_world:
    with open("country_of_the_world.csv", "r+") as old_world:
        red = csv.DictReader(old_world)
        for i in red:
            new_b = new_world.write(i[''])