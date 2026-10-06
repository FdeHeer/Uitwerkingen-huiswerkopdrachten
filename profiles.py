MIN_AGE = 18

players = {}
current_player = None


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


def create_account(total_cost, name=None):
    """Zorgt dat er een nieuw spelersaccount kan worden aangemaakt."""

    global current_player

    if name is None:
        name = input("Naam voor het nieuwe account: ").capitalize()
        if name in players:
            print("Dit account bestaat al. Gebruik wissel account om het te openen.")
            return

    birthdate = (input("Voer je geboortedatum in (dd-mm-yyyy): "))
    access_casino(birthdate)

    gender = (input("Wat is je geslacht? (M/V/A): "))
    starting_budget = float(input("Wat is je startbudget in euro?: "))
    balance = starting_budget - total_cost

    players[name] = create_profile(name, birthdate, gender, balance)
    current_player = name


def create_profile(name, birthdate, gender, balance):
    """Zorgt dat spelersprofiel zichtbaar wordt a.d.h.v. ingevoerde gegevens."""

    profile = {
        "naam": name,
        "geboortedatum": birthdate,
        "gender": gender,
        "saldo": balance,
        "gespeelde_spellen": {},
    }
    return profile


def show_account():
    """Toont de gegevens van het account dat op dit moment actief is."""

    profile = players[current_player]
    balance = profile["saldo"]
    played_games = profile["gespeelde_spellen"]

    print(f"Naam: {current_player}")
    print(f"Saldo: {balance:.2f}")
    print(f"Gespeelde spellen: {played_games}")
    print(f"Beschikbare spelers: {list(players.keys())}")


def show_all_players():
    """Toont alle spelers en hun huidige saldo."""

    for name, profile in players.items():
        print(f"{name}: saldo €{profile['saldo']}")


def switch_account():
    """Wisselt naar een ander bestaand spelersaccount en sluit accouts aan die niet bestaan."""

    global current_player

    name = input("Naar welk account wil je wisselen?: ").capitalize()

    if name in players:
        current_player = name
    else:
        print("Dit account bestaat niet.")
        return


def remove_account():
    """Hiermee kan een bestaand spelersaccount worden verwijderd en uitgesloten dat het laatste account wordt verwijderd."""

    global current_player

    name = input("Welk account wil je verwijderen?: ").capitalize()

    if name not in players:
        print("Dit account bestaat niet.")
        return

    elif len(players) == 1:
        print("Het laatste account mag niet worden verwijderd.")
        return

    del players[name]

    if name == current_player:
        current_player = list(players.keys())[0]


def get_current_balance():
    """Geeft het huidige saldo van de actieve speler terug."""

    return players[current_player]["saldo"]


def update_current_balance(balance):
    """Werkt het saldo van de huidige speler bij."""

    players[current_player]["saldo"] = balance


def register_played_game(game_name):
    """Registreert hoe vaak de huidige speler een spel heeft gspeeld."""

    played_games = players[current_player]["gespeelde_spellen"]

    if game_name in played_games:
        played_games[game_name] += 1

    else:
        played_games[game_name] = 1


def initialize_player(total_cost):
    """Weergeeft het overzicht van de spelers en bepaalt welke speler actief is."""

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

        print("----------------------------")
        print("Casino de Gouden Driehoek")
        print("----------------------------")
        print()
        determine_salutation(profile["gender"], current_player)
        print()
        print("Budgetchecker")
        print("---------------")
        print(f"Saldo: €{balance:.2f}")
        print("----------------------------")

    else:
        create_account(total_cost, name)

        profile = players[current_player]
        balance = profile["saldo"]
        starting_budget = balance + total_cost

        print("----------------------------")
        print("Casino de Gouden Driehoek")
        print("----------------------------")
        print()
        determine_salutation(profile["gender"], name)
        print()
        print("Budgetchecker")
        print("---------------")
        print(f"Startbudget: €{starting_budget:.2f}")
        print(f"Vaste kosten: €{total_cost:.2f}")
        print(f"Saldo: €{balance:.2f}")
        print("----------------------------")