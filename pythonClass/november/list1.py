scores = [60, 80, 70, 90, 40, 34, 20, 88, 100, 75, 95, 45, 55, 65, 85, 95]

def addFive(score):
    return score + 5

def greaterThanFifty(score):
    return score > 50

greaterScores = filter(greaterThanFifty, scores)
newScores = map(addFive, scores)

print(list(newScores))
print(list(greaterScores))

