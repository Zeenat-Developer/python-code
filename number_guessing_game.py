winning_number=67
game_over=False
guess=1
while True:
    number=int(input("Enter a number"))
     
    if number==winning_number:

        print("yes you are the winner")
        break

    else:

        if number<winning_number:

            print("number is too low")
        else:
            print("number is too high")
        guess=guess+1    
        continue
        
