import csv

i = 1
with open('mushrooms.csv', 'r') as shrooms:
    shrooms.readline()
    posionclass = csv.reader(shrooms, delimiter =',')

    for row in posionclass:
        if(row[0] == "e"):
            print("Mushroom", i, "is edible")
            i = i + 1
        else:
            print("Mushroom", i, "is poisonous")
            i = i + 1