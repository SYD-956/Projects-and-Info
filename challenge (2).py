def quiz_complete(score):
	print(f"Final Score: {score} out of 20")

# Introduction of the Knowledge quiz
print("Welcome to the LeBron James Quiz!")
print("You will answer each question with a, b, c, or d.\n")
# Correct answers
correct_answer1 = "d"
correct_answer2 = "b"
correct_answer3 = "b"
correct_answer4 = "c"
correct_answer5 = "a"
# Initial score
score = 0
# List of Questions
answer1 = input("When was LeBron James drafted in the NBA?\n a: 2004, b: 2006, c: 2007, or d: 2003\n")
if answer1 == correct_answer1:
	print("Correct!")
	score += 4
else:
	print("No points! Wrong answer")
answer2 = input("Which team did LeBron James win his first NBA title with?\n a: Golden State Warriors, b: Miami Heat, c: Los Angeles Lakers, or d: Cleveland Cavaliers\n")
if answer2 == correct_answer2:
	print("Correct!")
	score += 4
else:
	print("No points! Wrong answer")
answer3 = input("How many championships does LeBron James have?\n a: 2, b: 4, c: 1, or d: 5\n")
if answer3 == correct_answer3:
	print("Correct!")
	score += 4
else:
	print("No points! Wrong answer")
answer4 = input("What year did LeBron James become the all-time scoring leader?\n a: 2020, b: 2025, c: 2023, or d: 2021\n")
if answer4 == correct_answer4:
	print("Correct!")
	score += 4
else:
	print("No points! Wrong answer")
answer5 = input("In what year did LeBron James win his first NBA MVP?\n a: 2009, b: 2011, c: 2013, or d: 2015\n") 
if answer5 == correct_answer5:
	print("Correct!")
	score += 4
else:
	print("No points! Wrong answer")
if score < 0:
   score = 0

quiz_complete(score)
