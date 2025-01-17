import numpy as np


def setupDeck():
    deck = []
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                for l in range(1,4):
                    deck.append([i,j,k,l])
    deck_arr = np.array(deck)
    np.random.shuffle(deck_arr)
    return deck_arr

def checkColumn(x,y,z):
    if(x==y and y==z):
        return True
    elif(x!=y and y!=z and x!=z):
        return True
    return False


def checkSet(card1, card2, card3):
    if(checkColumn(card1[0],card2[0],card3[0]) and checkColumn(card1[1],card2[1],card3[1]) and checkColumn(card1[2],card2[2],card3[2]) and checkColumn(card1[3],card2[3],card3[3])):
        return True
    return False

def displayGame(cards):
    print("_____________________________________________________________")
    print("|   "+str(cards[0])+"\t|\t"+str(cards[1])+"\t|\t"+str(cards[2])+"   |")
    print("_____________________________________________________________")
    print("|   "+str(cards[3])+"\t|\t"+str(cards[4])+"\t|\t"+str(cards[5])+"   |")
    print("_____________________________________________________________")
    print("|   "+str(cards[6])+"\t|\t"+str(cards[7])+"\t|\t"+str(cards[8])+"   |")
    print("_____________________________________________________________")
    print("|   "+str(cards[9])+"\t|\t"+str(cards[10])+"\t|\t"+str(cards[11])+"   |")
    print("_____________________________________________________________")

    if(cards.shape[0]>12):
        print("| "+str(cards[12])+"\t|\t"+str(cards[13])+"\t|\t"+str(cards[14])+"  |")
        print("_____________________________________________________________")


def isSetPossible(cards):
    for i in range(cards.shape[0]):
        for j in range(cards.shape[0]):
            for k in range(cards.shape[0]):
                if(i!=j and j!=k and i!=k):
                    if(checkSet(cards[i], cards[j], cards[k])):
                        return True
    return False   

def findSet(cards):
    for i in range(cards.shape[0]):
        for j in range(cards.shape[0]):
            for k in range(cards.shape[0]):
                if(i!=j and j!=k and i!=k):
                    if(checkSet(cards[i], cards[j], cards[k])):
                        return [str(i),str(j),str(k)]


if __name__=='__main__':
    #setup game
    deck = setupDeck()
    displayed_cards = deck[:12, :]
    for i in range(12):
        deck = np.delete(deck, 0,0)

    if(not(isSetPossible(displayed_cards))):
        for i in range(3):
            displayed_cards = np.append(displayed_cards, [deck[0,:]], axis=0)
            deck = np.delete(deck, 0, 0)

    sets_found=0
    while(isSetPossible(displayed_cards) and deck.shape[0]>=3):
        displayGame(displayed_cards)
        # choice_str = input("Please select 3 cards: ")
        # card_choices = choice_str.split(' ')
        card_choices = findSet(displayed_cards)

        #check if valid set
        valid_set = checkSet(displayed_cards[int(card_choices[0])], displayed_cards[int(card_choices[1])], displayed_cards[int(card_choices[2])])

        if(valid_set):
            print("You found a valid set!\n\n")
            sets_found+=1

            if(displayed_cards.shape[0]<=12):
                for i in range(3):
                    displayed_cards[int(card_choices[i])]=deck[0,:]
                    deck = np.delete(deck,0,0)
            else:
                card_choices_int = [int(card_choices[0]), int(card_choices[1]), int(card_choices[2])].sort()
                for j in range(3):
                    displayed_cards = np.delete(displayed_cards, 2-j, 0)
                    x=2

            if(not(isSetPossible(displayed_cards)) and deck.shape[0]>=3):
                for i in range(3):
                    displayed_cards = np.append(displayed_cards, [deck[0,:]], axis=0)
                    deck = np.delete(deck, 0, 0)

        else:
            print("That is not a valid set!\n\n")
            
    print("\n\nThere are no more possible sets! \nYou found "+str(sets_found)+" sets with "+str(deck.shape[0]+displayed_cards.shape[0])+" cards left in the deck.\n")
