# =============== #
# A stack!        #
# =============== # 
from sys import exit

def main():
    stack = [None] * 5
    Top = 0
    underflow = len(stack) <= 0
    overflow = len(stack) > 5 

    def Push():
        nonlocal stack 
        nonlocal Top 
        nonlocal underflow

        
        while Top <= 4: 
            value = input("\nEnter a value to be pushed to the stack (\"q\" for quit): ") 
            if value.lower() in ["q", "quit"] and underflow:
                print("Please enter a value before quitting!") 
                continue 

            elif value.lower() in ["q", "quit"] and not underflow:
                return 

            else:
                stack[Top] = value 
                Top += 1 
                print(stack) 


            
            

                

    while True: 
        ask = int(input("Choose any of the following.......\n(1) Push \n\nChoice: ")) 
        
        if ask == 1: 
            if not overflow: 
                Push() 
            else: 
                print("The stack is full! try popping some items.") 
                return 

        else:
            exit("Bye!")


stacking = main() 
stacking()