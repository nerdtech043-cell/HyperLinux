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