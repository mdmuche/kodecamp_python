# the program should get a student score and display the appropriate grade for the score.

# 70 - 100 = A
# 60 - 69 = B
# 50 - 59 = C
# 45 - 49 = D
# 0 - 44 = F

# Algorithm

# get the student score
# to check the score for the appropriate grade
# display the appropriate grade for the score

score = input("please enter your score: ")
score = int(score)

if score >= 70 and score <= 100:
    print("your score is A")
elif score >= 60 and score <= 69:
    print("your score is B")
elif score >= 50 and score <= 59:
    print("your score is C")
elif score >= 45 and score <= 49:
    print("your score is D")
elif score >= 0 and score <= 44:
    print("your score is F")
else:
    print("invalid score")
