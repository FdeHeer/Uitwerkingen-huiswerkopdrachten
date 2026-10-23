from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

from datetime import datetime, date

console = Console()

BORDER_STYLE = "#FFFFFF"

MIN_AGE = 18

players = {}
current_player = None


def determine_salutation(gender, name):
    """Greets the player based on their entered gender and name."""

    if gender == "M":
        return f"Welkom, meneer, {name}"

    elif gender == "V":
        return f"Welkom, mevrouw, {name}"

    else:
        return f"Welkom, {name}"


def calculate_age(birthdate):
    """Checks whether the player is at least 18 years old based on their exact date of birth and is allowed to enter the casino."""

    birthdate_value = datetime.strptime(birthdate, "%d-%m-%Y").date()
    today_value = date.today()

    if birthdate_value > today_value:
        raise ValueError("""De geboortedatum mag niet in de toekomst liggen!.""")

    age = today_value.year - birthdate_value.year

    if (today_value.month, today_value.day) < (birthdate_value.month, birthdate_value.day):
        age -= 1

    if age < MIN_AGE:
        console.print("""[bold red]Je voldoet niet aan de minimale leeftijdsgrens van 18 jaar. 
            Je hebt geen toegang tot het casino.
                    [/bold red]""")
        exit(1)

    return age


def create_account(total_cost, name=None):
    """Creates a new player acoount."""

    global current_player

    if name is None:
        name = input("Naam voor het nieuwe account: ").capitalize()
        if name in players:
            console.print("[bold red]Dit account bestaat al. Gebruik wissel account om het te openen.[/bold red]")
            return

    birthdate = (input("Voer je geboortedatum in (dd-mm-yyyy): "))
    calculate_age(birthdate)

    gender = (input("Wat is je geslacht? (M/V/A): "))
    starting_budget = float(input("Wat is je startbudget in euro?: "))
    balance = starting_budget - total_cost

    players[name] = create_profile(name, birthdate, gender, balance)
    current_player = name


def create_profile(name, birthdate, gender, balance):
    """Displays the player's profile based on their given information."""

    profile = {
        "naam": name,
        "geboortedatum": birthdate,
        "gender": gender,
        "saldo": balance,
        "gespeelde_spellen": {},
    }
    return profile


def show_account():
    """Shows the details of the currently active account."""

    profile = players[current_player]
    balance = profile["saldo"]
    played_games = profile["gespeelde_spellen"]

    console.print(f"[bold]Naam[/bold]: {current_player}")
    console.print(f"[bold]Saldo[/bold]: {balance:.2f}")
    console.print(f"[bold]Gespeelde spellen[/bold]: {played_games}")
    console.print(f"[bold]Beschikbare spelers[/bold]: {list(players.keys())}")


def show_all_players():
    """Shows all players and their current balance."""

    table = Table(
        box=box.SQUARE,
        show_lines=False,
        header_style="Bold",
        padding=(0, 2),
    )

    table.add_column("Speler", justify="center")
    table.add_column("Saldo", justify="right")

    for name, profile in players.items():
        table.add_row(name, f"€{profile['saldo']:.2f}")

    console.print(
        Panel.fit(
            table,
            title="[bold #FFFFFF]Beschikbare spelers[/bold #FFFFFF]",
            border_style=BORDER_STYLE,
            padding=(0, 1),
        )
    )


def switch_account():
    """Switches to another existing player account and prevents switching to account that does not exist."""

    global current_player

    name = input("Naar welk account wil je wisselen?: ").capitalize()

    if name in players:
        current_player = name
    else:
        console.print("[red]Dit account bestaat niet.[/red]")
        return


def remove_account():
    """Removes an existing account and prevents the last remaining account from being deleted."""

    global current_player

    name = input("Welk account wil je verwijderen?: ").capitalize()

    if name not in players:
        console.print("[red]Dit account bestaat niet.[/red]")
        return

    elif len(players) == 1:
        console.print("[bold red]Het laatste account mag niet worden verwijderd.[/bold red]")
        return

    del players[name]

    if name == current_player:
        current_player = list(players.keys())[0]


def get_current_balance():
    """Returns the current balance of the active player."""

    return players[current_player]["saldo"]


def update_current_balance(balance):
    """Updates the current player's balance."""

    players[current_player]["saldo"] = balance


def register_played_game(game_name):
    """Tracks how many times the current player has played a certain game."""

    played_games = players[current_player]["gespeelde_spellen"]

    if game_name in played_games:
        played_games[game_name] += 1

    else:
        played_games[game_name] = 1


def initialize_player(total_cost):
    """Displays an overview of the players and determines which player is available."""

    global players
    global current_player

    players = {
        "Nora": {
            "naam": "Nora",
            "geboortedatum": "15-06-1995",
            "gender": "V",
            "saldo": 50,
            "gespeelde_spellen": {}
        },

        "Lizzy": {
            "naam": "Lizzy",
            "geboortedatum": "10-02-1993",
            "gender": "V",
            "saldo": 100,
            "gespeelde_spellen": {}
        },

        "Max": {
            "naam": "Max",
            "geboortedatum": "3-03-2000",
            "gender": "M",
            "saldo": 230,
            "gespeelde_spellen": {}
        },

        "Harm": {
            "naam": "Harm",
            "geboortedatum": "27-10-1978",
            "gender": "M",
            "saldo": 500,
            "gespeelde_spellen": {}
        }
    }

    name = input("Wat is je naam?: ").capitalize()
    current_player = name

    if name in players:
        profile = players[current_player]
        balance = profile["saldo"]

        salutation = determine_salutation(profile["gender"], current_player)

        table = Table(
            box=None,
            show_header=False,
            padding=(0,2)
        )

        table.add_column("Omschrijving")
        table.add_column("Bedrag", justify="right")

        table.add_row(salutation, "")
        table.add_row("","")
        table.add_row("Huidig saldo", f"€{balance:.2f}")

        console.print(
            Panel.fit(
                table,
                title="Casino de Gouden Driehoek",
                border_style=BORDER_STYLE
            )
        )

    else:
        create_account(total_cost, name)

        profile = players[current_player]
        balance = profile["saldo"]
        starting_budget = balance + total_cost

        salutation = determine_salutation(profile["gender"], current_player)

        table = Table(
            box=None,
            show_header=False,
            padding=(0, 2)
        )

        table.add_column("Omschrijving")
        table.add_column("Bedrag", justify="right")

        table.add_row(salutation, "")
        table.add_row("", "")
        table.add_row("Startbudget", f"€{starting_budget:.2f}")
        table.add_row("Vaste kosten", f"€{total_cost:.2f}")
        table.add_row("Huidig saldo", f"€{balance:.2f}")

        console.print(
            Panel.fit(
                table,
                title="Casino de Gouden Driehoek",
                border_style=BORDER_STYLE
            )
        )