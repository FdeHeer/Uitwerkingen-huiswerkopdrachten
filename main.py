from Uitwerkingen.games.roulette import play_roulette
from Uitwerkingen.games.fruitmachine import play_fruitmachine
from Uitwerkingen.games.blackjack import play_blackjack
from profiles import show_account, create_account, show_all_players, switch_account, remove_account, initialize_player, \
    register_played_game
from profiles import get_current_balance, update_current_balance

#Verplichte casinokosten
ENTRANCE_FEE = 15
CLOAKROOM_FEE = 3
MANDATORY_DRINK_COST = 5
TOTAL_FIXED_COSTS = ENTRANCE_FEE + CLOAKROOM_FEE + MANDATORY_DRINK_COST


def show_main_menu():
    """Toont de verschillende opties van het hoofdmenu."""

    print()
    print("-----HOOFDMENU-----")
    print()
    print("""Kies één van de volgende opties:
      1. Spellen
      2. Saldo
      3. Account
      0. Stop""")


def show_account_menu():
    show_account()

    print("""Kies één van de volgende opties:
1. Toon alle accounts
2. Nieuw account
3. Wissel account
4. Verwijder account""")

    choice = input("Welke optie kies je?: ")

    if choice == "1":
        show_all_players()

    elif choice == "2":
        create_account(TOTAL_FIXED_COSTS)

    elif choice == "3":
        switch_account()

    elif choice == "4":
        remove_account()

    else:
        print("Ongeldige keuze.")


def main():
    """Start het casinoprogramma en reageert op de keuzes van de speler."""
    initialize_player(TOTAL_FIXED_COSTS)

    while True:
        show_main_menu()

        print()
        choice = int(input("Kies een optie: "))

        if choice == 1:
            print("""
-----SPELLEN-----
    1. Roulette
    2. Fruitmachine
    3. Blackjack
    0. Terug
        """)

            game_choice = int(input("Welk spel wil je spelen?: "))

            if game_choice == 1:
                balance = get_current_balance()
                balance = play_roulette(balance)
                update_current_balance(balance)
                register_played_game("Roulette")

            elif game_choice == 2:
                balance = get_current_balance()
                balance = play_fruitmachine(balance)
                update_current_balance(balance)
                register_played_game("Fruitmachine")

            elif game_choice == 3:
                balance = get_current_balance()
                balance = play_blackjack(balance)
                update_current_balance(balance)
                register_played_game("Blackjack")

            elif game_choice == 0:
                continue

            else:
                print("Ongeldige keuze.")

        elif choice == 2:
            balance = get_current_balance()
            print(f"Je huidige saldo is: €{balance:.2f}")

        elif choice == 3:
            show_account_menu()

        elif choice == 0:
            print("Bedankt voor je bezoek, tot de volgende keer!")
            break

        else:
            print("Ongeldige keuze.")

main()
