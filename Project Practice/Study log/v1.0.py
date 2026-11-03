# creating a student study log script for myself 
import argparse 
from datetime import datetime 


def record(): 
    statement = input("Type: ") 
    now = datetime.now().isoformat() 

    with open("journal.txt", "a") as f:
        f.write(f"{now} --- {statement}\n") 

record() 