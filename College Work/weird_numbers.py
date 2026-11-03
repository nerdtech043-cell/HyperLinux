n = int(input("Enter any number (1 - 1 million): ")) 
while n != 1:
    if n % 2 == 0:
        n = (n / 2) 
        print(n)
    elif n % 2 != 0:
        n = (n * 3) 
        print(n)