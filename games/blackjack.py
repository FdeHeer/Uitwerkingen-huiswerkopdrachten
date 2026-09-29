import random
from Uitwerkingen.games.roulette import ask_for_bet

#Constanten
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def create_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            card = f"{suit}{rank}"
            deck.append(card)

    return deck


def draw_card(deck,hand):
    card = deck.pop()
    hand.append(card)

    return card


def show_hand(label, hand, hide_card=False):
    visible_cards = hand[:]

    if hide_card == True:
        visible_cards[1] = "??"

    print(f"{label}: {' | '.join(visible_cards)}")


def calculate_hand_value(hand):
    total = 0
    number_of_aces = 0

    for card in hand:
        card_value = calculate_card_value(card)
        total += card_value

        if card[1] == "A":
            number_of_aces += 1

    while total > 21 and number_of_aces > 0:
        total -= 10
        number_of_aces -= 1

    return total


def calculate_card_value(card):
    rank = card[1:]

    if rank == "J" or rank == "K" or rank == "Q":
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)


def play_blackjack(balance):


    while True:

        print("Je hebt gekozen om blackjack te spelen")
        print(f"Je huidige saldo is: €{balance:.2f}")

        choice = input("Druk op enter om te spelen of typ 'stop' om te stoppen: ")

        if choice == "stop":
            return balance

        elif choice == "":
            stake = ask_for_bet(balance)
            balance -= stake

            deck = create_deck()
            random.shuffle(deck)
            dealer_hand = []
            player_hand = []

            draw_card(deck, dealer_hand)
            draw_card(deck, dealer_hand)
            draw_card(deck, player_hand)
            draw_card(deck, player_hand)

            show_hand("Jouw hand", player_hand, hide_card=False)
            show_hand("Dealer hand", dealer_hand, hide_card=True)

            while calculate_hand_value(player_hand) < 21:
                choice = input("Wil je hit of stand?: ")

                if choice == "stand":
                    break

                elif choice == "hit":
                    drawn_card = draw_card(deck, player_hand)
                    print(f"Je hebt kaart {drawn_card} getrokken")

                    show_hand("Jouw hand", player_hand, hide_card=False)

                    print(f"De waarde van de hand is: {calculate_hand_value(player_hand)}")

                    if calculate_hand_value(player_hand) > 21:
                        print("Helaas, je bent bust")
                        return balance

                else:
                    print("Ongeldige keuze")
                    continue

            show_hand("Dealer hand", dealer_hand, hide_card=False)

            while calculate_hand_value(dealer_hand) < 17:
                drawn_card = draw_card(deck, dealer_hand)
                print(f"De dealer heeft kaart {drawn_card} getrokken")

                show_hand("Dealer hand", dealer_hand, hide_card=False)

            player_total = calculate_hand_value(player_hand)
            dealer_total = calculate_hand_value(dealer_hand)

            if dealer_total > 21:
                balance = balance + 2 * stake
                print(f"Gefeliciteerd, je hebt gewonnen. Je nieuwe saldo bedraagt: €{balance:.2f}")

            elif player_total > dealer_total:
                balance = balance + 1.5 * stake
                print(f"Gefeliciteerd, je hebt gewonnen. Je nieuwe saldo bedraagt: €{balance:.2f}")

            elif player_total == dealer_total:
                balance = balance + stake
                print(f"Het is gelijkspel. Je saldo bedraagt: €{balance:.2f}")

            else:
                print(f"Helaas, je hebt verloren. Je verliest €{stake:.2f}")

            print(f"Je uiteindelijke saldo bedraagt: €{balance:.2f}")
            return balance

        else:
            print("Ongeldige keuze")





