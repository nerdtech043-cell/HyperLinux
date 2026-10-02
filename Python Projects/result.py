name = input("What is your name? ")
age = input("What is your age? ")
subjects = int(input("How many subjects did you take? "))
total = 0 
average = 0

for i in range(subjects):
    subject = input(f"What is the name of subject {i+1}? ")
    score = int(input(f"What is the score of {subject}? "))
    total += score 
    print(f"{subject}: {score}")

average = total / subjects 
percentage = (total / (subjects * 100)) * 100  

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")