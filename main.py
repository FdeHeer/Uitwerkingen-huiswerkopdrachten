from Uitwerkingen.games.roulette import play_roulette
from Uitwerkingen.games.fruitmachine import play_fruitmachine
from Uitwerkingen.games.blackjack import play_blackjack


#Verplichte casinokosten
ENTRANCE_FEE = 15
CLOAKROOM_FEE = 3
MANDATORY_DRINK_COST = 5
TOTAL_FIXED_COSTS = ENTRANCE_FEE + CLOAKROOM_FEE + MANDATORY_DRINK_COST

MIN_AGE = 18


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


def ask_input():
    """Vraagt de persoonlijke gegevens en het startbudget van de speler."""

    name = (input("Voer je voor- en achternaam in: "))
    birthdate = (input("Voer je geboortedatum in (dd-mm-yyyy): "))
    gender = (input("Wat is je geslacht? (M/V/A): "))
    starting_budget = float(input("Wat is je startbudget in euro?: "))

    return name, birthdate, gender, starting_budget


def determine_salutation(gender, name):
    """Begroet de speler o.b.v. het ingevoerde geslacht en de naam."""

    if gender == "M":
        print(f"Welkom, meneer,", name)

    elif gender == "V":
        print(f"Welkom, mevrouw,", name)

    else:
        print(f"Welkom,", name)


def access_casino(birthdate):
    """Controleert a.d.h.v. het geboortejaar of de speler oud genoeg is om toegang te krijgen tot het casino."""

    birth_day, birth_month, birth_year = birthdate.split("-")
    birth_year = int(birth_year)

    if birth_year > 2008:
        print("""Je voldoet niet aan de minimale leeftijdsgrens van 18 jaar. 
Hierdoor heb je geen toegang tot het casino.
        """)
        exit(1)


def show_intro(starting_budget):
    """Berekent het startsaldo van de speler en dit voldoende is om toegang te krijgen tot het casino."""

    balance = starting_budget - TOTAL_FIXED_COSTS
    budget_check = "Je hebt genoeg budget voor toegang tot het casino." if TOTAL_FIXED_COSTS <= starting_budget else "Je hebt niet voldoende budget om toegang te krijgen tot het casino."

    return balance, budget_check


def main():
    """Start het casinoprogramma en reageert op de keuzes van de speler."""

    name, birthdate, gender, starting_budget = ask_input()
    access_casino(birthdate)
    balance, budget_check = show_intro(starting_budget)

    print("----------------------------")
    print("Casino de Gouden Driehoek")
    print("----------------------------")
    print()
    determine_salutation(gender, name)
    print()
    print("Budgetchecker")
    print("---------------")
    print(f"Startbudget: €{starting_budget:.2f}")
    print(f"Vaste kosten: €{TOTAL_FIXED_COSTS:.2f}")
    print(f"Saldo: €{balance:.2f}")
    print("----------------------------")
    print()
    print(budget_check)
    print()

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
                balance = play_roulette(balance)

            elif game_choice == 2:
                balance = play_fruitmachine(balance)

            elif game_choice == 3:
                balance = play_blackjack(balance)

            elif game_choice == 0:
                continue

            else:
                print("Ongeldige keuze.")

        elif choice == 2:
            print(f"Je huidige saldo is: €{balance:.2f}")

        elif choice == 3:
            print(f"Naam: {name}")
            print(f"Geboortedatum: {birthdate}")
            print(f"Geslacht: {gender}")

        elif choice == 0:
            print("Bedankt voor je bezoek, tot de volgende keer!")
            break

        else:
            print("Ongeldige keuze.")

main()
