subjects = []
while True: 
    entry = input("Enter your subject name: ") 
    if entry == "None" or entry == "none":
        break  
    subjects.append(entry) 

for i in range(len(subjects)):
    subjects[i] = "A-levels " + subjects[i] 
    print(subjects[i]) 
