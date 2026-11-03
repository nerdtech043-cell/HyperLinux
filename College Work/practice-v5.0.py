
while True: 
    Product_Code = input("Enter the product code: ") 

    if Product_Code[0:3].isalpha() and Product_Code[-3:].isdigit() and len(Product_Code)  <= 7 and Product_Code[0:3].isupper():
        print("\nCorrect!") 
        break 

    elif not Product_Code[0:3].isalpha() and not Product_Code[0:3].isupper():
        print("Please make sure the first four characters are all uppercase letters!")
        continue

    elif not Product_Code[-3:].isdigit():
        print("Please make sure the last three characters of the code are all digits!")
        continue 

    elif len(Product_Code) > 7:
        print("Please do not exceed the seven character limit!") 
        continue


