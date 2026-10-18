stack = [None] * 5
top = -1
overflow = top == len(stack) - 1
underflow = top == -1

def push():
    global top 
    global stack 

    if overflow: 
        print("\n############################################")
        print("# Stack is full, try popping some item(s)! #") 
        print("############################################") 
        return 

    else:
        value = input("\nEnter an item to be pushed to stack (\"q\" to quit): ") 
        stack[top] = value 
        print(f"Item pushed: {value}") 
        top += 1 
        return 

def pop():
    global top 
    global stack 

    if underflow:
        print("\n#############################################")
        print("# Stack is empty, try pushing some item(s)! #") 
        print("#############################################") 
        return 

    else: 
        value = stack[top] 
        stack[top] = None 
        top -= 1 
        print(f"Item popped: {value}") 
        return 

def display():
    global stack 

    if top == -1:
        print("\n######################################")
        print("# Stack is empty, nothing to display #") 
        print("######################################")
        return 

    else: 
        for i in range(top, -1, -1):
            print(stack[i])  
        return 

while True:
    ask = int(input("\nChoose one of the following.....\n1. Push \n2. Pop \n3. Display \n4. Exit \n\nChoice: ")) 

    if ask == 1: 
        push() 
    elif ask == 2:
        pop() 
    elif ask == 3:
        display() 
    elif ask == 4:
        print("Bye!")
        break 
    else:
        break 
        