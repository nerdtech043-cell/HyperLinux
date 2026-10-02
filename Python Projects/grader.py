def main(name):
    marks = 0 
    
    def grader():
        
        nonlocal marks 
        
        marks = int(input("Enter Your Marks: ")) 
        A = marks >= 80 or marks <= 100
        B = marks >= 70 or marks < 80 
        C = marks >= 60 or marks < 70
        D = marks >= 50 or marks < 60
        F = marks < 50

        if A:
            print(f"Congrats {name}! you got a distinction.") 
        elif B:
            print(f"Good work {name}! you got an excellent grade.") 
        elif C: 
            print(f"Nice work {name}, though you could've gotten a better grade.")
        elif D:
            print(f"This is disappointing {name}. Work Harder next time. Very disappointing!!!") 
        elif F:
            print(f"You failed {name}!!! You're a disgrace!") 

    return grader 

if __name__ == "__main__":
    import argparse 
    
    parser = argparse.ArgumentParser(
        description="Allows a student to enter their name for a more personalized experience."
    )
    
    parser.add_argument(
        "-n", "--name", required=True, help="Enter the student's name." 
    )

    args = parser.parse_args()

system = main(args.name) 
system()