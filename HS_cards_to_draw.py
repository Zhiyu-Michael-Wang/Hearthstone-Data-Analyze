from random import randint
TOTAL_CARDS_NUM = 30
RANDOM_CARD = "Random Card"
TEST_TIME = 10000


def get_key_cards():
    key_cards = []
    print("What cards do you want to draw? [Enter their names one by one. Enter 'FINISH' to end this process.]")
    done = False
    count = 0
    while not done:
        count += 1
        card = input("card" + str(count) + ": ")
        if card == "FINISH" or count > 30:
            break
        duplicate = input("Duplicate? [Enter 'Y' for yes. All other input will be count as no.] \n").capitalize()
        duplicate = True if duplicate == "Y" else False
        if duplicate:
            draw_both = input("Do you need to draw both of them? [Enter 'Y' for yes. All other input will be count as no.] \n").capitalize()
            draw_both = True if draw_both == "Y" else False
            if draw_both:
                key_cards.append(card + "2")
            else:
                key_cards.append(card)
        key_cards.append(card)
    return key_cards
        

def generate_deck(key_cards):
    deck = [RANDOM_CARD] * TOTAL_CARDS_NUM
    position = 0
    for key_card in key_cards:
        deck[position] = key_card
        position += 1
    return deck


def draw_cards(deck, key_cards, hold_keys_begin):
    DREW = 'Drew'
    holds = []
    count = 1

    # initial draw
    for ii in range(3):

        # draw a card here
        draw_position = randint(0, 29)
        while deck[draw_position] == DREW:
            draw_position = randint(0, 29)
        # draw another card if it's not one of the key cards
        if hold_keys_begin and deck[draw_position] == RANDOM_CARD:
            chosen_position = draw_position
            draw_position = randint(0, 29)
            while deck[draw_position] == DREW or draw_position == chosen_position:
                draw_position = randint(0, 29)
        # draw another card if it is one of the key cards
        elif not hold_keys_begin and deck[draw_position] != RANDOM_CARD:
            chosen_position = draw_position
            draw_position = randint(0, 29)
            while deck[draw_position] == DREW or draw_position == chosen_position:
                draw_position = randint(0, 29)
        
        # append the card into 'holds' if it's not a random card
        if deck[draw_position] != RANDOM_CARD:
            holds.append(deck[draw_position])            
        deck[draw_position] = DREW

    # print('//Initial draw ' + str(holds))

    # later draws
    while set(key_cards) & set(holds) != set(key_cards):
        count += 1
        draw_position = randint(0, 29)
        while deck[draw_position] == DREW:
            draw_position = randint(0, 29)
        if deck[draw_position] != RANDOM_CARD:
            holds.append(deck[draw_position])
            # print('//Draw '+ str(count) + ' ' + deck[draw_position])
        deck[draw_position] = DREW
        

    return count 
    

def main():
    key_cards = get_key_cards()
    print(key_cards)

    total_count = 0
    for ii in range(TEST_TIME):
        deck = generate_deck(key_cards)
        count = draw_cards(deck, key_cards, True)
        total_count += count
    average = total_count/TEST_TIME
    print('You\'ll need about ' + str(average) + ' draws to get all your key cards')


if __name__ == "__main__":
    main()