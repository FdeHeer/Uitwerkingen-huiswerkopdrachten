from Uitwerkingen.games.roulette import play_roulette
from Uitwerkingen.games.fruitmachine import play_fruitmachine
from Uitwerkingen.games.blackjack import play_blackjack
from profiles import show_account, create_account, show_all_players, switch_account, remove_account, initialize_player, \
    register_played_game
from profiles import get_current_balance, update_current_balance
from exchange import run_exchange

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

BORDER_STYLE = "#888888"

#Verplichte casinokosten
ENTRANCE_FEE = 15
CLOAKROOM_FEE = 3
MANDATORY_DRINK_COST = 5
TOTAL_FIXED_COSTS = ENTRANCE_FEE + CLOAKROOM_FEE + MANDATORY_DRINK_COST


def show_main_menu():
    """Displays the different options of the main menu."""

    table = Table(
        box=box.SQUARE,
        show_lines=False,
        header_style="Bold",
        padding=(0, 2),
    )

    table.add_column("Optie", justify="center")
    table.add_column("Actie", justify="right")

    table.add_row("1", "Spellen")
    table.add_row("2", "Saldo")
    table.add_row("3", "Account")
    table.add_row("4", "Wisselkantoor")
    table.add_row("0", "Stop")

    console.print(
        Panel.fit(
            table,
            title="[bold #FFFFFF]HOOFDMENU[/bold #FFFFFF]",
            border_style=BORDER_STYLE,
            padding=(0, 1),
        )
    )


def show_account_menu():
    """Displays the different options of the account menu."""

    show_account()

    table = Table(
        box=box.SQUARE,
        show_lines=False,
        header_style="Bold",
        padding=(0, 2),
    )

    table.add_column("Optie", justify="center")
    table.add_column("Actie", justify="center")

    table.add_row("1", "Toon alle accounts")
    table.add_row("2", "Nieuw account")
    table.add_row("3", "Wissel account")
    table.add_row("4", "Verwijder account")

    console.print(
        Panel.fit(
            table,
            title="[bold #FFFFFF]ACCOUNTMENU[/bold #FFFFFF]",
            border_style=BORDER_STYLE,
            padding=(0, 1),
        )
    )

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
        console.print("[red]Ongeldige keuze[/red]")


def main():
    """Starts the casino program and handles the player's choices."""
    initialize_player(TOTAL_FIXED_COSTS)

    while True:
        show_main_menu()

        choice = int(input("Kies een optie: "))

        if choice == 1:

            table = Table(
                box=box.SQUARE,
                show_lines=False,
                header_style="Bold",
                padding=(0, 2),
            )

            table.add_column("Optie", justify="center")
            table.add_column("Spel", justify="right")

            table.add_row("1", "Roulette")
            table.add_row("2", "Fruitmachine")
            table.add_row("3", "Blackjack")
            table.add_row("0", "Terug")

            console.print(
                Panel.fit(
                    table,
                    title="[bold #FFFFFF]SPELLEN[/bold #FFFFFF]",
                    border_style=BORDER_STYLE,
                    padding=(0, 1),
                )
            )

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
                console.print("[red]Ongeldige keuze[/red]")

        elif choice == 2:
            balance = get_current_balance()
            console.print(f"[bold blue]Je huidige saldo is: €{balance:.2f}[/bold blue]")

        elif choice == 3:
            show_account_menu()

        elif choice == 4:
            euro_amount = run_exchange()

            if euro_amount is not None:
                balance = get_current_balance() + euro_amount
                update_current_balance(balance)

        elif choice == 0:
            console.print("[bold]Bedankt voor je bezoek, tot de volgende keer![/bold]")
            break

        else:
            console.print("[red]Ongeldige keuze[/red]")

main()
