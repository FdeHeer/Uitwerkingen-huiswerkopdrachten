import random
from Uitwerkingen.games.roulette import ask_for_bet

from rich.console import Console
from rich.panel import Panel

console = Console()

#Constanten
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def create_deck():
    """Maakt een deck van 52 kaarten"""

    deck = []
    for suit in SUITS:
        for rank in RANKS:
            card = f"{suit}{rank}"
            deck.append(card)

    return deck


def draw_card(deck,hand):
    """Trekt een kaart uit het deck en voegt deze toe aan de hand"""

    card = deck.pop()
    hand.append(card)

    return card


def show_hand(label, hand, hide_card=False):
    """Toont de kaarten van de hand en zorgt dat de tweede kaart kan worden verborgen"""

    visible_cards = hand[:]

    if hide_card == True:
        visible_cards[1] = "??"

    message = f"{label}: {' | '.join(visible_cards)}"

    console.print(
        Panel(
            message,
            title="Output",
            border_style="#FFFFFF"
        )
    )


def calculate_hand_value(hand):
    """Berekent de totale waarde van de hand en maakt daarin onderscheid voor A, J, Q, K in waarde.
    Alle andere kaarten behouden hun integer waarde"""

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
    """Berekent de waarde van één kaart"""

    rank = card[1:]

    if rank == "J" or rank == "K" or rank == "Q":
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)


def play_blackjack(balance):
    """In deze functie wordt blackjack gespeeld en het saldo bijgewerkt"""

    while True:

        message = (
            "Je hebt gekozen om blackjack te spelen\n"
            f"Je huidige saldo is: €{balance:.2f}"
        )

        console.print(
            Panel(
                message,
                title="Blackjack",
                border_style="#FFFFFF"
            )
        )

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

            console.print(f"[#FFD700]De waarde van de hand is: {calculate_hand_value(player_hand)}[/#FFD700]")

            show_hand("Dealer hand", dealer_hand, hide_card=True)

            while calculate_hand_value(player_hand) < 21:
                choice = input("Wil je hit of stand?: ")

                if choice == "stand":
                    break

                elif choice == "hit":
                    drawn_card = draw_card(deck, player_hand)
                    console.print(f"[italic]Je hebt kaart {drawn_card} getrokken[/italic]")

                    show_hand("Jouw hand", player_hand, hide_card=False)

                    if calculate_hand_value(player_hand) > 21:
                        console.print("[bold red]Helaas, je bent bust![/bold red]")
                        return balance

                else:
                    console.print("[bold red]Ongeldige keuze[/bold red]")
                    continue

            show_hand("Dealer hand", dealer_hand, hide_card=False)

            while calculate_hand_value(dealer_hand) < 17:
                drawn_card = draw_card(deck, dealer_hand)
                console.print(f"[italic]De dealer heeft kaart {drawn_card} getrokken[/italic]")

                show_hand("Dealer hand", dealer_hand, hide_card=False)

            player_total = calculate_hand_value(player_hand)
            dealer_total = calculate_hand_value(dealer_hand)

            if dealer_total > 21:
                balance = balance + 2 * stake
                result = f"Gefeliciteerd, je hebt gewonnen. Je nieuwe saldo bedraagt: €{balance:.2f}"

            elif player_total > dealer_total:
                balance = balance + 1.5 * stake
                result = f"Gefeliciteerd, je hebt gewonnen. Je nieuwe saldo bedraagt: €{balance:.2f}"

            elif player_total == dealer_total:
                balance = balance + stake
                result = f"Het is gelijkspel. Je saldo bedraagt: €{balance:.2f}"

            else:
                result = f"Helaas, je hebt verloren. Je verliest €{stake:.2f}"

            message = (
                f"Jouw hand: {' | ' .join(player_hand)}\n"
                f"Dealer hand: {' | '.join(dealer_hand)}\n\n"
                f"Jouw totaal: {player_total}\n"
                f"Dealer totaal: {dealer_total}\n\n"
                f"{result}\n"
                f"Je uiteindelijke saldo bedraagt: €{balance:.2f}"
            )

            console.print(
                Panel(
                    message,
                    title="Output",
                    border_style="#FFFFFF"
                )
            )

            return balance

        else:
            console.print("[bold red]Ongeldige keuze[/bold red]")





