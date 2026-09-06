import random

print("\n\n ------WELCOME TO THE GAME------")

player_score = 0
ai_score = 0

try :
    while True :

        choices = ['rock' , 'paper' , 'sieser']
        player = input("\nWhat would you want to choose ; 'rock' , 'paper' , 'sieser' : ")

        ai_player = random.choice(choices)

        wins = [ (0,1) , (1,0) , (2,1) ]

        player_index = choices.index(player.lower())
        ai_index = choices.index(ai_player)

        print(f"\nYou choose {player.lower()} and the opponent choose {ai_player} ")

        if player_index == ai_index :
            print("it's draw ! ")

        elif (player_index,ai_index) in wins :
            print("You win !")
            player_score += 1

        else :
            print("You lose ! ")
            ai_score += 1

        print(f"\nThe score now is ;  {player_score} : {ai_score} ")

        if player_score == 3 or ai_score == 3 :
            if player_score == 3 :
                print("\nYou win the game gungratulation ! ")

            else : 
                print("\nYou lose the game.Good luck next time ")

            break

except Exception as e :
    print(e) 
