import random
import string

forename = input("Enter your forename: ") 
surname = input("Enter your surname: ") 
random_number = "".join(random.choice(string.digits) for _ in range(3)) 
idcode = forename[0:2].upper() + surname[0].upper() + surname[-1].upper() + random_number
print(f"Your ID is: {idcode}")