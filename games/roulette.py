def show_roulette_options():
    """Toont de verschillende opties van roulette."""

    print("""Kies één van de volgende opties:
          1. Rood
          2. Zwart
          3. Even
          4. Oneven
          0. Stop""")


def determine_win(choice, color, odd_even):
    """Bepaalt aan de hand van de gekozen gok of de speler heeft gewonnen."""

    if choice == 1 and color == "rood":
        return True
    elif choice == 2 and color == "zwart":
        return True
    elif choice == 3 and odd_even == "even":
        return True
    elif choice == 4 and odd_even == "oneven":
        return True
    else:
        return False


def ask_for_bet(balance):
    """Vraagt om een inzet die niet hoger mag zijn dan het huidige saldo."""

    while True:
        stake = float(input("Hoeveel geld wil je inzetten: "))

        if stake <= 0:
            print("Dit is niet mogelijk")
            continue

        elif stake > balance:
            print("Dit is niet mogelijk")
            continue

        else:
            return stake


def play_roulette(balance):
    """In deze functie wordt roulette gespeeld en het saldo bijgewerkt."""

    round_number = 1

    while True:
        show_roulette_options()

        choice = int(input("Kies je gok (0 om te stoppen): "))

        if choice == 0:
            break
        stake = ask_for_bet(balance)
        balance -= stake

        spin = (round_number * 7) % 37
        print(f"De bal valt op: {spin}")

        if spin == 0:
            color = "groen"
            odd_even = "geen"

        else:
            if spin % 2 == 0:
                color = "zwart"
                odd_even = "even"
            else:
                color = "rood"
                odd_even = "oneven"

        print(f"De kleur is {color}")
        print(f"Het getal is {odd_even}")

        win = determine_win(choice, color, odd_even)

        if win:
            balance += 2 * stake
            print("Gefeliciteerd, je hebt gewonnen")
        else:
            print("Helaas, je hebt verloren")
            print(f"Je verliest: € {stake:.2f}")

        print(f"Je nieuwe saldo is: {balance:.2f}")

        round_number += 1

    return balance
