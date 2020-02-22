from random import randint

choices = ["ROCK", "PAPER", "SCISSORS"]

playAgain = "y"
pChoice = ""



def play():
    playAgain = input("Press 'y' to begin")
    while playAgain == "y":
        cpuPts = 0
        playerPts = 0
        userName = input("Enter your name")
        while cpuPts < 2 and playerPts < 2:
            pChoice = input("ROCK, PAPER, OR SCISSORS?")
            cpu = choices[randint(0,2)]
            if pChoice == cpu:
                print("Its a tie!")
            elif pChoice == "ROCK":
                if cpu == "SCISSORS":
                    print(userName + " wins! Rock beats scissors")
                    playerPts += 1
                else:
                    print("Computer wins! Paper beats rock")
                    cpuPts += 1
            elif pChoice == "PAPER":
                if cpu == "ROCK":
                    print(userName + " wins! Paper beats rock")
                    playerPts += 1
                else:
                    print("Computer wins! Scissors beats paper")
                    cpuPts += 1
            elif pChoice == "SCISSORS":
                if cpu == "PAPER":
                    print(userName + " wins! Scissors beats paper")
                    playerPts += 1
                else:
                    print("Computer wins! Rock beats scissors")
                    cpuPts += 1
            else:
                print("INVALID CHOICE TRY AGAIN")
                playAgain = "y"
        if cpuPts == 2:
            print("Computer won the game!")
            playAgain = input("Play Again? (y) or (n)")
        elif playerPts == 2:
            print(userName + " won the game!")
            playAgain = input("Play Again? (y) or (n)")
        

        
    

        
    

        
        

