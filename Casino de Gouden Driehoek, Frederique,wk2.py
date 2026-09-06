#Verplichte casinokosten
ENTRANCE_FEE = 15
CLOAKROOM_FEE = 3
MANDATORY_DRINK_COST = 5
TOTAL_FIXED_COSTS = ENTRANCE_FEE + CLOAKROOM_FEE + MANDATORY_DRINK_COST

MIN_AGE = 18

name = (input("Voer je naam in: "))
birthdate = (input("Voer je geboortedatum in (dd-mm-yyyy): "))
birth_day, birth_month, birth_year = birthdate.split("-")
birth_year = int(birth_year)

if birth_year > 2008:
    print("Je voldoet niet aan de minimale leeftijdsgrens van 18 jaar")
    exit(1)

gender = (input("Wat is je geslacht? (M/V): "))
starting_budget = float (input("Wat is je startbudget in euro?: "))
salutation = f"meneer {name}" if gender == "M" else f"mevrouw {name}"
saldo = starting_budget - TOTAL_FIXED_COSTS

budget_check = "Je hebt genoeg budget voor toegang tot het casino." if TOTAL_FIXED_COSTS <= starting_budget else "Je hebt niet voldoende budget om toegang te krijgen tot het casino."

print("----------------------------")
print("Casino de Gouden Driehoek")
print("----------------------------")
print()
print(f"Welkom, {salutation}")
print()
print("Budgetchecker")
print("---------------")
print(f"Startbudget: €{starting_budget:.2f}")
print(f"Vaste kosten: €{TOTAL_FIXED_COSTS:.2f}")
print (f"Saldo: €{saldo:.2f}")
print("----------------------------")
print()
print(budget_check)
print()
print("""Kies één van de volgende opties:
      1. Rood
      2. Zwart
      3. Even
      4. Oneven
      0. Stop""")
print()

while True:
    round_number = 1
    spin = (round_number * 7) % 37
    number_of_choice = int(input("Kies je gok (0 om te stoppen): "))

    if number_of_choice == 0:
        break
    stake = float(input("Hoeveel geld wil je inzetten: "))
    if stake <= 0:
        print("Dit is niet mogelijk")
        continue
    elif stake > saldo:
        print("Dit is niet mogelijk")
        continue

    saldo -= stake

    print(f"De bal valt op: {spin}")

    if spin == 0:
        color = "groen"
        parity = "geen"
    elif spin <= 18:
        if spin % 2 == 0:
            color = "zwart"
            parity = "even"
        else:
            color = "rood"
            parity = "oneven"
    else:
        if spin % 2 == 0:
            color = "zwart"
            parity = "even"
        else:
            color = "rood"
            parity = "oneven"

    print(f"De kleur is: {color}")
    print(f"Het getal is: {parity}")

    win = False
    saldo += 2 * stake

    if number_of_choice == 1 and color == "rood":
            win = True
            print(f"Gefeliciteerd, je hebt gewonnen. Je nieuwe saldo is: €{saldo:.2f}")
    elif number_of_choice == 2 and color == "zwart":
            win = True
            print(f"Gefeliciteerd, je hebt gewonnen. Je nieuwe saldo is: €{saldo:.2f}")
    elif number_of_choice == 3 and parity == "even":
            win = True
            print(f"Gefeliciteerd, je hebt gewonnen. Je nieuwe saldo is: €{saldo:.2f}")
    elif number_of_choice == 4 and parity == "oneven":
            win = True
            print(f"Gefeliciteerd, je hebt gewonnen. Je nieuwe saldo is: €{saldo:.2f}")
    else:
        print("Helaas, je hebt verloren.")
        print(f"Je verliest: €{stake:.2f}")
        print(f"Je nieuwe saldo is: €{saldo:.2f}")

    round_number += 1

print(f"Je eindsaldo is: €{saldo:.2f}. Bedankt voor het spelen en tot de volgende keer!")

# Vraag: Er gaat iets niet helemaal goed met het saldo. Als de speler verloren heeft, verrekent hij het saldo niet goed en hij laat de hele tijd dezelfde uitkomst zien bij iedere ronde.
