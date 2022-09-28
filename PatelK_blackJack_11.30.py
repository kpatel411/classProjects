#Khushi Patel
#Final Project: Black Jack
#CSC-121 Dr. Tartaro
#12/14/2021

from random import randint
from collections import namedtuple

#rank
JACK = 11
QUEEN = 12
KING = 13
ACE = 11
#suit
SPADE = 1
DIAMOND = 2
HEART = 3
CLUB = 4

def main():
  playBlackJack()

def playBlackJack():
  playAgain = True
  while playAgain == True:
    userCard1 = randomCard()
    userCard2 = randomCard()
    userHand = []
    userHand.append(userCard1)
    userHand.append(userCard2)
    dealerHand = []
    #dealerCard1 = randomCard()
    #dealerHand.append(dealerCard1)
    #printCard(dealerCard1)
    dealerHand.append(randomCard())
    print("Your Cards:")
    printCard(userCard1)
    printCard(userCard2)
    print("Dealer's Cards:")
    dealerCard1 = randomCard()
    dealerHand.append(dealerCard1)
    printCard(dealerCard1)
    seeDealerHand = checkDealerHand(dealerHand)
    if seeDealerHand == True:
      requestContinue(userHand, dealerHand)
      playAgain = False
      return playAgain  
      playAgainString = requestString("Do you wish to play again? Yes or No?")
      if playAgainString == "Yes" or playAgainString == "yes":
        playAgain = True
      else:
        playAgain = False
        print("Thank you for playing!")
    #return playAgain
    print("Dealer draws:")
    dealerCard2 = randomCard() 
    dealerHand.append(dealerCard2)
    printCard(dealerCard2)
    calculateScore(userHand)
    calculateScore(dealerHand)
    requestContinue(userHand, dealerHand)
  
# create a suit and value of all cards then get the user to "Deal" 2 random cards
def randomCard():
  rank = ""
  suit = ""
  randomRank = random.randint(1,12)
  randomSuit = random.randint(1,4)
  card = createCard(randomSuit, randomRank)
  return card
  
def createCard(suit, rank):
  Card = namedtuple("Card", ['rank','suit'])
  card = Card(rank, suit)
  return card
  
def createDeck():
  finishedDeck = []
  for suit in range(1,5):
    for rank in range(2,14):
      card = createCard(suit, rank)
      finishedDeck.append(card)
  return finishedDeck
  
def printCard(Card1):
  suitprint = ""
  rankprint = ""
  if (Card1.suit == SPADE):
    suitprint = "spade"
  elif (Card1.suit == DIAMOND):
    suitprint = "diamond"
  elif (Card1.suit == HEART):
    suitprint = "heart"
  else:
    suitprint = "club"
    
  if (Card1.rank == ACE):
    rankprint = "ace"
  elif (Card1.rank == JACK):
    rankprint = "jack"
  elif (Card1.rank == QUEEN):
    rankprint = "queen"
  elif (Card1.rank == KING):
    rankprint = "king"
  else:
    rankprint = str(Card1.rank)
  print (rankprint + " of " + suitprint)
  
def printCardList(hand):
  for card in hand:
    printCard(card)

# output any two random cards to dealer(computer)
# show 1 to user by printing out the suit and value of the card

# write and if statement that when dealer's hand is 21 then game reveals both cards & tells user has lost
# else continue on with the game until reaching 21
# Note: aces are worth only 11 at this stage; consider getting input for either 1 or 11
def calculateScore(hand):
  sumVariable = 0
  countAces = 0
  for card in hand:
    if card.rank is not ACE:
      sumVariable += card.rank
    else: 
      countAces += 1
  for i in range(countAces):
    if sumVariable <= 10:
      sumVariable += 11
    else:
      sumVariable += 1
  return sumVariable

# use requestString function to ask user to hit, stand or quit; works with step 3 create a for loop steps 4-7; create a hit function 
def requestContinue(userHand, dealerHand):
  user_input = requestString("Would you like to hit, stand, or quit?")
  if "hit" == user_input: #USER DRAWS CARD
    card = randomCard()
    print("Your card:")
    printCard(card)
    userHand.append(card)
    userHitCard(userHand)
    if calculateScore(userHand) <= 17:
      requestContinue(userHand, dealerHand)
    if calculateScore(userHand) <= 21:
      requestContinue(userHand, dealerHand)
    #have hit input lead to drawing a card
  elif "stand" == user_input: #DEALER DRAWS CARD
    card = randomCard()
    if calculateScore(dealerHand) <= 17:
      card = randomCard()
      dealerHand.append(card)
      print("Dealer draws:")
      printCard(card)
    if calculateScore(dealerHand) <= 21:
      requestContinue(userHand, dealerHand)
      printCard(card)
      #have it exit when stand gets to 21 or over!!!!!!
    else:
      print("YOU WIN!")
    #dealerSum draws a randomCard
    #have stand input lead to dealer drawing a card and user stops playing
  elif "quit" == user_input:
    #have the game end and show win/loss and bet outcome
    userPoints = calculateScore(userHand)
    dealerPoints = calculateScore(dealerHand)
    if userPoints >= dealerPoints and userPoints <= 21:
      print(userPoints)
      print("YOU WIN!")
    else:
      print("user " + str(userPoints))
      print("dealer " + str(dealerPoints))
      print("YOU LOSE!")
    user_input = requestString("Would you like to play again?")
    if user_input == "yes":
      main()
    else:
      print("Goodbye!")
     
# write if statement for when user says hit, deal another random card to user by printing out suit and face value
def userHitCard(hand): #this function should be used for drawing a card when user enters hit consider a loop since amount of cards can be random
  userPoints = calculateScore(hand)
  print(userPoints)
  if userPoints == 21:
    print("You win a BlackJack!")
  elif userPoints != 21:
    print("Sorry you lose. Dealer wins BlackJack.")
  elif userPoints > 21:
    print("You lose BlackJack.")
    
def checkDealerHand(hand):
  dealerStillPlay = True
  total = calculateScore(hand)
  if total == 21:
    print("Dealer's Hand:")
    printCardList(hand)
    print("Game over. Dealer has won 21.")
    dealerStillPlay = False
    playAgain = False
  return dealerStillPlay    
