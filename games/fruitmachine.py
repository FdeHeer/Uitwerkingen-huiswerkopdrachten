from Uitwerkingen.games.roulette import ask_for_bet


def determine_rolls(round_number):
    """Bepaalt a.d.h.v. het rondenummer welke drie symbolen worden gedraaid."""

    result = round_number % 5

    if result == 1:
        return "kers", "citroen", "ster"
    elif result == 2:
        return "kers", "kers", "kers"
    elif result == 3:
        return "ster", "ster", "citroen"
    elif result == 4:
        return "citroen", "kers", "ster"
    else:
        return "ster", "ster", "ster"


def determine_payout(rol1, rol2, rol3, stake):
    """Berekent de uitbetaling o.b.v. de uitkomst van de drie symbolen en de inzet."""

    if rol1 == rol2 and rol2 == rol3:
        return 3 * stake
    elif rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return stake
    else:
        return 0


def play_fruitmachine(balance):
    """In deze functie wordt de fruitmachine gespeeld en het saldo bijgewerkt."""

    round_number = 1

    while True:

        print("Je hebt gekozen om de fruitmachine te spelen")
        print(f"Jouw huidig saldo is: {balance}")

        choice = input("Druk op enter om te spelen of typ 'stop' om te stoppen: ")

        if choice == "stop":
            return balance

        elif choice == "":
            stake = ask_for_bet(balance)
            balance -= stake

        else:
            print("Ongeldige keuze.")
            continue

        rol1, rol2, rol3 = determine_rolls(round_number)
        print(f"Rollen: {rol1}, {rol2}, {rol3}")

        payout = determine_payout(rol1, rol2, rol3, stake)

        if payout > 0:
            balance += payout
            print(f"Gefeliciteerd! Je wint €{payout:.2f}")

        else:
            print("Helaas, je hebt verloren.")

        print(f"Je huidige saldo is: €{balance:.2f}")

        round_number += 1