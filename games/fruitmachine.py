from Uitwerkingen.games.roulette import ask_for_bet

from rich.console import Console
from rich.panel import Panel

from random import choice

console = Console()

BORDER_STYLE = "#FFFFFF"

SYMBOLS = ["kers", "citroen", "ster", "bel", "diamant"]


def determine_rolls():
    """Determines which three symbols appear based on the round number."""

    rol1 = choice(SYMBOLS)
    rol2 = choice(SYMBOLS)
    rol3 = choice(SYMBOLS)

    return rol1, rol2, rol3


def determine_payout(rol1, rol2, rol3, stake):
    """Calculates the payout based on the three symbols and the bet amount."""

    if rol1 == rol2 and rol2 == rol3:
        return 3 * stake
    elif rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return stake
    else:
        return 0


def play_fruitmachine(balance):
    """Plays the slotmachine and update the player's balance."""

    while True:

        message= (
            "Je hebt gekozen om de fruitmachine te spelen!\n"
            f"Jouw huidige saldo is: {balance:.2f}"
        )

        console.print(
            Panel(
                message,
                title="Fruitmachine",
                border_style=BORDER_STYLE
            )
        )

        choice = input("Druk op enter om te spelen of typ 'stop' om te stoppen: ")

        if choice == "stop":
            return balance

        elif choice == "":
            stake = ask_for_bet(balance)
            balance -= stake

        else:
            console.print("[bold red]Ongeldige keuze.[/bold red]")
            continue

        rol1, rol2, rol3 = determine_rolls()

        payout = determine_payout(rol1, rol2, rol3, stake)

        if payout > 0:
            balance += payout
            result = f"Gefeliciteerd! Je wint €{payout:.2f}"

        else:
            result = (
                "Helaas, je hebt verloren.\n"
                f"Je verliest €{stake:.2f}"
            )

        message = (
            f"Rollen: {rol1} | {rol2} | {rol3}\n\n"
            f"{result}\n"
            f"Je huidige saldo is: €{balance:.2f}"
        )

        console.print(
            Panel(
                message,
                title="Output",
                border_style=BORDER_STYLE
            )
        )