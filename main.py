import random

def deal_card():
    cards = [ 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10 ,10 ]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.apeend(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "Lost"
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score > 21:
        return "opponent went over, You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


user_cards = []
computer_cards = []
game_over = False
computer_score = 0

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, Curent score: {user_score}")
    print(f"    Computer cards: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        user_should_deal = input("Would you like to play? type 'y' or 'n':   ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            game_over = True


while computer_score != 0 and computer_score > 17:
    computer_cards.apeend(deal_card())
    computer_score = calculate_score(computer_cards)


print(compare(computer_score, user_score))