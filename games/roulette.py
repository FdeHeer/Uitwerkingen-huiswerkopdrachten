from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

from random import randint

console = Console()

def show_roulette_options():
    """Toont de verschillende opties van roulette."""

    table = Table(
        box=box.SQUARE,
        show_lines=False,
        header_style="Bold",
        padding=(0, 2),
    )

    table.add_column("Optie", justify="center")
    table.add_column("Actie", justify="right")

    table.add_row("1", "Rood")
    table.add_row("2", "Zwart")
    table.add_row("3", "Even")
    table.add_row("4", "Oneven")
    table.add_row("0", "Stop")

    console.print(
        Panel.fit(
            table,
            title="[bold #FFFFFF]Roulette[/bold #FFFFFF]",
            border_style="#FFFFFF",
            padding=(0, 1),
        )
    )


def determine_win(choice, color, odd_even):
    """Bepaalt aan de hand van de gekozen gok of de speler heeft gewonnen."""

    if choice == 1 and color == "[red]rood[/red]":
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
            console.print("[bold red]Dit is niet mogelijk[/bold red]")
            continue

        elif stake > balance:
            console.print("[bold red]Dit is niet mogelijk[/bold red]")
            continue

        else:
            return stake


def play_roulette(balance):
    """In deze functie wordt roulette gespeeld en het saldo bijgewerkt."""

    while True:
        show_roulette_options()

        choice = int(input("Kies je gok (0 om te stoppen): "))

        if choice == 0:
            break
        stake = ask_for_bet(balance)
        balance -= stake

        spin = randint(0, 36)

        if spin == 0:
            color = "[green]groen[/green]"
            odd_even = "geen"

        else:
            if spin % 2 == 0:
                color = "zwart"
                odd_even = "even"
            else:
                color = "[red]rood[/red]"
                odd_even = "oneven"

        win = determine_win(choice, color, odd_even)

        if win:
            balance += 2 * stake
            result = "Gefeliciteerd, je hebt gewonnen!"
        else:
            result = (
                f"Helaas, je hebt verloren!\n"
                f"Je verliest: €{stake:.2f}"
            )

        message = (
            f"De bal valt op: {spin}\n"
            f"De kleur is: {color}\n"
            f"Het getal is: {odd_even}\n\n"
            f"{result}\n"
            f"Je nieuwe saldo is: €{balance:.2f}"
        )

        console.print(
            Panel.fit(
                message,
                title="Output",
                border_style="#FFFFFF"
            )
        )

    return balance
