import random
import time
time.sleep(0.5)
print("Welcome to Blackjack21.")
time.sleep(1.6)
print("Just before we start, here are some rules you should know...")
time.sleep(1.5)
skip=input("Press enter to continue, or enter 'skip' to skip the rules.")
if skip!="skip" :
    print("-An 'Ace' can equal 1 or 11, depending on the size of your combination.If the combo is larger than 21,the ace will equal 1 .If not, it will equal 11.")
    skip=input(" ")
    print("-Cards such as J,Q,K will be counted as 10, and the rest will stay the same.")
    skip=input(" ")    
    print("-A 'hit 'means to request another card from the deck, increasing your combo.")
    skip=input(" ")
    print("A 'double stand' is to double your bet, and recieving one extra card.")
    skip=input(" ")
    print("-A 'stand' means to end your turn.")
    skip=input(" ")
    print("-A 'bust' is when the combination of cards exceeds any more than 21, losing all the points in that round.")
    skip=input(" ")
    print("-A 'Blackjack' is when you have a total of 21 points by having a combination of an Ace and any other card.")
    skip=input(" ")
    print("-All players start with 10 chips for bet,and every game must have a minimum deal of 1 chip.")
    skip=input(" ")
    print("Now that we've gone through the rules, it's time for a game of Blackjack...")
    time.sleep(2.5)
retry="yes"
gpbet=10
while (gpbet>1):
    if retry=="yes" :
        Ace="an Ace"
        Ace1=1
        Ace2=11
        Ace3=1
        Ace4=11
        J="J"
        Q="Q"
        K="K"
        hard=[J,Q,K,J,Q,K,J,Q,K,J,Q,K]
        x=[Ace,Ace,Ace,Ace,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,J,J,J,J,Q,Q,Q,Q,K,K,K,K]
        computer1=random.choice(x)
        x.remove(computer1)
        computer2=random.choice(x)
        x.remove(computer2)
        player1=random.choice(x)
        x.remove(player1)
        player2=random.choice(x)
        x.remove(player2)
        pbet=0
        while (1>pbet):
            pbet=int(input("How many chips would you like to deal with?"))
            if gpbet>=pbet>=1:
                print("Very well.")
            else:
                print("Invalid number. Please enter integers only.")
                pbet=int(input("How many chips would you like to deal with?"))
        time.sleep(1)
        print("you got cards",player1,"and", player2,".")
        if computer1==Ace :
          print("The dealer has an Ace")
        else:
          print("The dealer has a ",computer1)
        for cards in hard:
            if player1==cards:
              player1=10
            elif player2==cards:
              player2=10
            elif computer1==cards:
              computer1=10
            elif computer2==cards:
              computer2=10
        if player1==Ace:
            if player2 != Ace:
              if (11+player2)>21:
                player1=Ace1
              else:
                player1=Ace2
            else:
                player1=Ace1
                
        if player2==Ace:
            if player1 != Ace1: 
              if(11+player1)>21:
                player2=Ace1
              else:
                player2=Ace2
            else:
                player2=Ace2
                
        if computer1==Ace:
            if computer2 != Ace:
                if (11+computer2)>21:
                    computer1=Ace3
                else:
                    computer1=Ace4
            else:
                computer1=Ace3

        if computer2==Ace:
            if computer1 != Ace1:
              if(11+computer1)>21:
                  computer2=Ace3
              else:
                  computer2=Ace4
            else:
                computer2=Ace4

        ptotal=player1+player2
        ctotal=computer1+computer2
        time.sleep(0.8)
        if pbet<=(gpbet/2):
            ds="key"
            gpbet=gpbet-pbet
            while ds=="key":
                ds=input("Would you like to double stand?")
                if ds=="yes":
                    gpbet=gpbet-pbet
                    pbet=2*pbet
                    player3=random.choice(x)
                    x.remove(player3)
                    time.sleep(0.3)
                    print("drawing...")
                    if player3==Ace:
                      print("You gained an Ace")
                      if player1==Ace1 or player2==Ace1:
                        player3=Ace1
                      elif player1==Ace2:
                        player1=Ace1
                        player3=Ace1
                      elif player2==Ace2:
                        player2=Ace1
                        player3=Ace1
                      elif (ptotal+11)>21:
                        player3=Ace1
                      else:
                        player3=Ace2
                    else:
                      print("You gained a ",player3)
                      for cards in hard:
                        if player3==cards:
                          player3=10
                      if player1==Ace2:
                        if (player2+player3+11)>21:
                          player1=Ace1
                        else:
                          player1=Ace2
                      elif player2==Ace2:
                        if (player1+player3+11)>21:
                          player2=Ace1
                        else:
                          player2=Ace2
                    ptotal=player1+player2+player3
                    if ptotal>21:
                        print("you've busted.")
                        ptotal=0
                elif ds=="no":
                    players_choice="key"
                    while players_choice=="key" :
                        players_choice=input("Would you like to hit or stand?")
                        if players_choice=="stand":
                            print("Sure.We shall continue.")
                            ptotal=player1+player2
                            time.sleep(0.8)
                            print("The dealer's turn...")
                        elif players_choice=="hit":
                            player3=random.choice(x)
                            x.remove(player3)
                            if player3==Ace:
                              print("You gained an Ace")
                              if player1==Ace1 or player2==Ace1:
                                player3=Ace1
                              elif player1==Ace2:
                                player3=Ace1  
                                if (player2+player3)>21:  
                                    player1=Ace1
                                else:
                                    player1=Ace2
                              elif player2==Ace2:
                                player3=Ace1
                                if (player1+player3)>21:
                                    player2=Ace1
                                else:
                                    player2=Ace2
                              elif (ptotal+11)>21:
                                player3=Ace1
                              else:
                                player3=Ace2
                            else:
                              print("You gained a ",player3)
                              for cards in hard:
                                if player3==cards:
                                  player3=10
                              if player1==Ace2:
                                if (player2+player3+11)>21:
                                  player1=Ace1
                                else:
                                  player1=Ace2
                              elif player2==Ace2:
                                if (player1+player3+11)>21:
                                  player2=Ace1
                                else:
                                  player2=Ace2
                            ptotal=player1+player2+player3
                            pcards=[player1,player2,player3]
                            if ptotal>21:
                              print("you've busted.")
                              ptotal=0
                            while(0<ptotal<21):
                              players_choice=input("would you like to hit or stand?")
                              time.sleep(0.8)
                              if players_choice=="stand":
                                print("Sure,We shall continue.")
                                time.sleep(0.8)
                                print("The dealer's turn...")
                                break
                              elif players_choice=="hit":
                                player4=random.choice(x)
                                x.remove(player4)
                                if player4==Ace:
                                    print("you gained an",player4)
                                    for pcard in pcards:
                                        if pcard==Ace1:
                                            player4=Ace1
                                        elif pcard==Ace2:
                                            player4=Ace1
                                            pcard=Ace1
                                        elif (11+ptotal)>21:
                                            player4=Ace1
                                        else:
                                            player4=Ace2
                                else:
                                    print("you gained a",player4)
                                    pcards.append(player4)
                                    for cards in hard:
                                        if player4==cards:
                                          player4=10
                                    for pcard in pcards:
                                        if pcard==11:
                                            pcards.remove(pcard)
                                            if (ptotal-pcard+11)>21:
                                                pcard=Ace1
                                            else:
                                                pcard=Ace2
                                            pcards.append(pcard)
                                ptotal=ptotal+player4
                                if ptotal>21:
                                  print("you've busted.")
                                  ptotal=0  
                              else :
                                  print("Sorry , I didn't get that. Please enter everything in lower case.")
                                  players_choice="key"
                        else :
                            print("Sorry, I didn't get that. Please enter everything in lower case.")
                            players_choice="key"
                    
                            
                else :
                    print("Sorry, I didn't get that. Please enter everything in lower case.")
                    ds="key"
        else :
                    gpbet=gpbet-pbet
                    players_choice="key"
                    time.sleep(0.8)
                    while players_choice=="key" :
                        players_choice=input("Would you like to hit or stand?")
                        if players_choice=="stand":
                            print("Sure.We shall continue.")
                            ptotal=player1+player2
                            time.sleep(0.8)
                            print("The dealer's turn...")
                            break
                        elif players_choice=="hit":
                            player3=random.choice(x)
                            x.remove(player3)
                            if player3==Ace:
                              print("You gained an Ace")
                              if player1==Ace1 or player2==Ace1:
                                player3=Ace1
                              elif player1==Ace2:
                                player3=Ace1  
                                if (player2+player3)>21:  
                                    player1=Ace1
                                else:
                                    player1=Ace2
                              elif player2==Ace2:
                                player3=Ace1
                                if (player1+player3)>21:
                                    player2=Ace1
                                else:
                                    player2=Ace2
                              elif (ptotal+11)>21:
                                player3=Ace1
                              else:
                                player3=Ace2
                            else:
                              print("You gained a ",player3)
                              for cards in hard:
                                if player3==cards:
                                  player3=10
                              if player1==Ace2:
                                if (player2+player3+11)>21:
                                  player1=Ace1
                                else:
                                  player1=Ace2
                              elif player2==Ace2:
                                if (player1+player3+11)>21:
                                  player2=Ace1
                                else:
                                  player2=Ace2
                            ptotal=player1+player2+player3
                            pcards=[player1,player2,player3]
                            if ptotal>21:
                              print("you've busted.")
                              ptotal=0
                            while(0<ptotal<21):
                              players_choice=input("would you like to hit or stand?")
                              time.sleep(0.8)
                              if players_choice=="stand":
                                print("Sure,We shall continue.")
                                time.sleep(0.8)
                                print("The dealer's turn...")
                                break
                              elif players_choice=="hit":
                                player4=random.choice(x)
                                x.remove(player4)
                                if player4==Ace:
                                    print("you gained an",player4)
                                    for pcard in pcards:
                                        if pcard==Ace1:
                                            player4=Ace1
                                        elif pcard==Ace2:
                                            player4=Ace1
                                            pcard=Ace1
                                        elif (11+ptotal)>21:
                                            player4=Ace1
                                        else:
                                            player4=Ace2
                                else:
                                    print("you gained a",player4)
                                    pcards.append(player4)
                                    for cards in hard:
                                        if player4==cards:
                                          player4=10
                                    for pcard in pcards:
                                        if pcard==Ace2:
                                            pcards.remove(pcard)
                                            if (ptotal-pcard+11)>21:
                                                pcard=Ace1
                                            else:
                                                pcard=Ace2
                                            pcards.append(pcard)
                                ptotal=ptotal+player4
                                if ptotal>21:
                                  print("you've busted.")
                                  ptotal=0
                                break  
                              else :
                                  print("Sorry , I didn't get that. Please enter everything in lower case.")
                                  players_choice=input("would you like to hit or stand?")
                        else :
                            print("Sorry, I didn't get that. Please enter everything in lower case.")
                            players_choice=input("would you like to hit or stand?")
        if (computer1+computer2)<16:
          print("The dealer has a ",computer1,"and a ",computer2)  
          computer3=random.choice(x)
          x.remove(computer3)
          for cards in hard:
              if computer3==cards:
                computer3=10
          if computer3==Ace:
            print("The dealer gained an Ace")
            if (computer1+computer2+11)>21:
              computer3=Ace1
            else:
                computer3=Ace2
          else:
            print("The dealer gained a ",computer3)
          ctotal=computer1+computer2+computer3
          if ctotal>21:
            print("The dealer has busted.")
            ctotal=0
        else :
          ctotal=computer1+computer2
        time.sleep(1)
        print("Your points add up to ", ptotal)
        print("The dealer's points add up to ",ctotal)
        if ctotal>ptotal:
          print("The chips go to the dealer.")
        elif ptotal>ctotal:
          print("The chips go to the player.")
          gpbet=gpbet+(2*pbet)
        else:
          print("It's a tie.The chips are returned. ")
          gpbet=gpbet+pbet
        time.sleep(1)
        print("you have ",gpbet,"chips left.")
        retry=input("Would you like to have another game?")
    elif retry=="no":
      print("Calculating total points...")
      time.sleep(1)
      if gpbet>10:
          print("You earned £",gpbet-10)
      elif gpbet<10:
          print("you lost £",10-gpbet)
      else :
          print("You have not lost or gained any points.")
      break
    else:
        print("Sorry, I didn't get that. Please enter everything in lower case.")
        retry=input("Would you like to have another game?")
else:
    print("you've ran out of chips.Please come again next time.")

