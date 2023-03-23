print("Wlecome to blackjack! \n\n")
wins = 0
losses = 0

def game(wins,losses):

    # Blackjack
    import random
    playerhand = []
    computerhand = []

    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]

    #pick a card
    def PickACard(deck,hand):
        newcard =random.choice(deck)

        #print("dealt",newcard)
        hand.append(newcard)
        deck.remove(newcard)
        return deck,hand

    print("The cards are being dealt!")


    #call the 'pick a card' function for the player
    deck,hand = PickACard(deck,playerhand)
    #call it a second time - player needs 2 cards
    deck,hand = PickACard(deck,playerhand)

    #call the 'pick a card' function for computer
    deck,hand = PickACard(deck,computerhand)
    #call it a second time - computer needs 2 cards
    deck,hand = PickACard(deck,computerhand)

    #summary of what has happened
    print("Here is your hand: ")
    print(playerhand)

    # display the total value of the hand
    print("Youre total score is:",sum(playerhand))

    #print("Computer's hand: ")
    #print(computerhand)

    # allow player to twist or stick
    again = True
    pbust = False
    while again == True and pbust == False:
        agn = input("Would you like to draw another card? [Y/N]")
        if agn.upper() == "Y":
            PickACard(deck,playerhand)
            #summary of what has happened
            print("Here is your hand: ")
            print(playerhand)

            # display the total value of the hand
            print("Youre total score is:",sum(playerhand))
            if sum(playerhand) > 21:
                print("You are bust!")
                pbust = True
        else:
            again = False
            print("You have now chosen to stand. These are your cards: ")
            print(playerhand)

    if pbust == False:
        # allow computer to twist or stick
        again = True
        cbust = False
        while again == True and cbust == False:
            if sum(computerhand) < 15:
                again = True
                PickACard(deck,computerhand)
                #summary of what has happened
                #print("computer drew another card! hand: ")
                #print(computerhand)

                # display the total value of the hand
                #print("computer's total score is:",sum(computerhand))
                if sum(computerhand) > 21:
                    print("computer is bust!")
                    cbust = True

                
            else:
                again = False
                #print("The computer has now chosen to stand. These are the cards: ")
                #print(computerhand)
        # determine winner
        if cbust == True:
            print("Player Wins!!")
            wins = wins + 1
        elif sum(playerhand) == 21:
            print("Player has blackjack!! You win!!")
            wins = wins + 1
        elif sum(playerhand) >= sum(computerhand):
            print("Player has the better hand. Player wins!")
            wins = wins + 1
        else:
            print("Dealer wins!")
            print("LOSER!!!")
            losses = losses + 1
    else:
        print("You lose!")
        losses = losses + 1
    print("The dealer had the following cards: ")
    print(computerhand)
    print("With the value: ")
    print(sum(computerhand))

    #print("remaining cards in deck")
    #print(deck)
    return wins,losses
    print()


playing = True
while playing == True:
    score = game(wins,losses)
    print("Games won: ",score[0])
    print("Games lost: ",score[1])
    rply = input("Would you like to play again? [Y/N]")
    if rply.upper() == "N":
        playing = False
    print("OK! \n ")

input("Thanks for playing :) ")

    
