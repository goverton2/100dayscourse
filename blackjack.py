#imports
import random
import art

bj = False

#unlimited deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()

if play == "y":
  bj = True
  
while bj == True:
  print(art.logo)

  my_hand = [random.choice(cards), random.choice(cards)]
  sum_mh = sum(my_hand)
  comp_hand = [random.choice(cards), random.choice(cards)]
  sum_ch = sum(comp_hand)

  print(f"Your cards: {my_hand}, current score: {sum_mh}")
  print(f"Computer's first card: {comp_hand[0]}")

  #final score
  def score_print(myhand, summh, comphand, sumch):
    print(f"Your final hand: {myhand}, with final score {summh}.")
    print(f"The computer's final hand: {comphand}, with a final score {sumch}.")

  #evaluate final scores
  def eval(myhand, summh, comphand, sumch):
    sumch = sum(comphand)
    summh = sum(myhand)
    
    if summh > 21:
      print(f"You busted with {myhand} and a score of {summh}. Sorry, bro.")
    elif sumch > 21:
      print(f"The computer busted with {comphand} and a score of {sumch}. Your {myhand} wins!")
    elif summh > sumch:
      score_print(myhand, summh, comphand, sumch)
      print("You win!")
    elif summh < sumch:
      score_print(myhand, summh, comphand, sumch)
      print("You lose!")
    else:
      score_print(myhand, summh, comphand, sumch)
      print("Draw!")
  
  #computer hand simulation
  def comp_hand_sim(sumch, comphand):
    while sumch < 17:
      comphand.append(random.choice(cards))
      sumch = sum(comphand)
      if 11 in comphand and sumch > 21:
        comphand.remove(11)
        comphand.append(1)
        sumch = sum(comphand)

  #special case when you start with bj
  if sum_mh == 21:
    comp_hand_sim(sum_ch, comp_hand)
    eval(my_hand, sum_mh, comp_hand, sum_ch)
    bj = False

  else:
    cont = input("Type 'y' to get another card, type 'n' to pass: ")

    if cont == "n":
      comp_hand_sim(sum_ch, comp_hand)
      eval(my_hand, sum_mh, comp_hand, sum_ch)

    else:
      while cont == "y" and sum_mh < 22:
        my_hand.append(random.choice(cards))
        sum_mh = sum(my_hand)
        if 11 in my_hand and sum_mh > 21:
          my_hand.remove(11)
          my_hand.append(1)
          sum_mh = sum(my_hand)
        if sum_mh > 21:
          eval(my_hand, sum_mh, comp_hand, sum_ch)
        else:
          print(f"Your cards: {my_hand}, current score: {sum_mh}")
          cont = input("Type 'y' to get another card, type 'n' to pass: ")
        
      else:
        if sum_mh < 22:
          comp_hand_sim(sum_ch, comp_hand)
          eval(my_hand, sum_mh, comp_hand, sum_ch)
          cont = "n"

  #once we stop
  bj = False
