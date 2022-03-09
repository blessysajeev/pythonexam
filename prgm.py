import csv
with open("des.csv", newline='') as csvfile:
    a = DictReader(csvfile)
    print(a)
    print("name","age")
    print("---------")
    for i in a:
        print(name[i],age[i])