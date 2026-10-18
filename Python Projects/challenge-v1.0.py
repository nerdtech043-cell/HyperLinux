# =========================== #
# Problem 2271E of Codeforces # 
# =========================== # 
import random 

# populating the array 'a' 
print('') 
n = int(input("\nEnter the length of the array 'a': "))
a = [] 
for _ in range(n):
    a.append(f"{(random.randint(1, 999)):03d}") 
print(a) 
print('') 

# emptying 'a' 
k = int(input("Enter any random integer"))