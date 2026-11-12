names = ["Kevin", "Josh", "aaron"]

length = len(names)
names.append("tyler")
names.insert(1, "anas")
names.remove("anas")
names.pop()
names.index("Kevin")

print(length)

print(names[1])

scores = [60, 80, 70, 90, 40, 34, 20]

def sumOfScores(score):
    total = 0   
    for item in score:
        total += item
    return total

cal = sumOfScores(scores)
print(cal)


for i, item in enumerate(names, start=1):
    print(f"{i}. {item}")


inventory = ["sword", "shield", "potion", "armor", "boots"]

prices = [100, 150, 50, 200, 75]

for item, price in zip(inventory, prices):
    print(f"{item}: ${price}")
    



for item in names:
    print(item)

for score in scores:
    if score == 88:
        break
    print(score)


# 3 rows x 4 columns - student grades
students = [["John", 85, 90, 78],
            ["Jane", 92, 88, 95],
            ["Mike", 75, 80, 70]]
print(students[1][2])


