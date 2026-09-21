#!/usr/bin/env python3

# name of student and app
print("Kevin Child's Test Scores App")

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
# initialize the variable for accumulating scores
total_score = 0  
score1 = int(input("Enter test score: ")) # get first score
total_score += score1
score2 = int(input("Enter test score: ")) # get second score
total_score += score2
score3 = int(input("Enter test score: ")) # get third score
total_score += score3

# calculate total score
total_score = score1 + score2 + score3  

# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================")

# display all three individual test scores
print("Scores:", score1, score2, score3)

# display the total score and average score
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)

print()
print("Bye")


