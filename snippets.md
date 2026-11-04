Nov 3, Tuesday, 2026:
Today i learned some file handling! i learned that we use the `with()` block with `open()` to append a file like this:
    
    with open("journal.txt", "a") as f:
        f.write(f"{now} --- {statement}\n") 

I also attemped a CSES practice question called "Weird Algorithm" and got stuck for some reason, oh well, bbetter luck next time i guess. I'm kind of said and guilt-ridden though. Anyways, i'll try some gaming to cool my mind off today, bye now! And oh, forgot the bug, here's the code i used Haim (i'm writing to myself):

n = int(input("Enter any number (1 - 1 million): ")) 
while n != 1:
    if n % 2 == 0:
        n = (n / 2) 
        print(n)
    elif n % 2 != 0:
        n = (n * 3) 
        print(n) 

check the bug tomorrow, bye now!, for real. 

Nov 4, Wednesday, 2026
Today i replaced the "statement" input variable with a parameter. The value in that parameter comes from the CLI now! Here's how:
    -  we define a variable where CLI arguments go, commonly parser. Then we do this:
        `parser = argparse.ArgumentParser()"`

    -  this is used to get the basic stuff like descriptions
    - next we do this:

        `parser.add_argument()`

    -  This adds any arguments we want to add, all of which have to be inside Quotes. 

## Argparse Optional Flags & Optional Args
parser.add_argument("text", nargs="?") # Optional positional
parser.add_argument("-r", "--read", action="store_true") # Flag (-r or --read)
# Access via args.text and args.read (True/False)