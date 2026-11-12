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


inventory = ["sword", "shield", "potion", "armor", "boots", "axe"]

inventory[0:2]
inventory[:3]
inventory[0:4:2]


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
students = [["Joel", 85, 95, 70],
            ["Anne", 95, 100, 100],
            ["Mike", 77, 70, 85]]
print(students[0][3], students[2][2])



for student in students:
    for i in student:
        print(f"Data {i}")
        print()


movies = [
    ["The Holy Grail", 1975, 9.99],
    ["Life of Brian", 1979, 12.30],
    ["The Meaning of Life", 1983, 7.50]
]

for row in movies:
    print(row)

for row in movies:
    for column in row:
        print(f"{column}")


numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]

count = numlist.count(14)   
numlist.reverse()
numlist.sort()

print(numlist)

foodlist = ["orange", "apple", "Pear", "banana"]
foodlist.sort()
print(foodlist) 

foodlist.sort(key=str.lower)
print(foodlist)

print(len(foodlist))


sorted_foodlist = sorted(foodlist, key=str.lower)

print(sorted_foodlist)


score_list = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25, 5, 15, 84, 3, 14, 2, 8, 10, 14, 25, 5, 15, 84, 3, 14, 2, 8, 10, 14, 25, 5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
minimum = min(score_list)
maximum = max(score_list) 
total = sum(score_list) 
total = sum(score_list)

print(f"Minimum: {minimum}, Maximum: {maximum}, Total: {total}")


