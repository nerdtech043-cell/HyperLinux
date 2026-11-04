# creating a student study log script for myself 
import argparse 
from datetime import datetime 
from pathlib import Path

FILE = Path(__file__).parent / "journal.txt"

def record(statement): 
    now = datetime.now().isoformat() 

    with open(FILE, "a") as f:
        f.write(f"{now} --- {statement}\n") 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A CLI to log my study sessions!") 
    parser.add_argument("text", nargs="?" ,help="Write what i did today.") 
    parser.add_argument("-r", "--read", action="store_true", help="Read my log")

    args = parser.parse_args()  

    if args.read:
        with open(FILE, "r") as f:
            print(f.read()) 

    elif args.text:
        record(args.text) 

    else: 
        print("Please provide a text to log or use '-r' to read.")


