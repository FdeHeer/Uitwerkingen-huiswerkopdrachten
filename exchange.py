from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import requests
import os
from dotenv import load_dotenv

console = Console()

load_dotenv()
api_key = os.getenv("EXCHANGE_API_KEY")
EXCHANGE_RATE_URL = "https://v6.exchangerate-api.com/v6/{}/latest/{}"


def get_exchange_request():
    """Asks the user which currency and amount they want to exchange."""

    while True:
        currency = input("Welke valuta wil je wisselen?: ").strip().upper()

        if currency == "STOP":
            return None, None

        if len(currency) == 3:
            break

        else:
            console.print("[bold red]Dit is niet mogelijk. De valuta code mag enkel drie tekens omvatten, bijvoorbeeld USD. Probeer opnieuw.[/bold red]")

    while True:
        try:
            foreign_currency_amount = float(input("Welk bedrag wil je wisselen?: "))
            break

        except ValueError:
            console.print("[bold red]Dit is niet mogelijk. Vul een numerieke waarde, bijvoorbeeld 150.[/bold red]")

    return foreign_currency_amount, currency


def get_exchange_rate_for_currency(currency):
    """Retrieves the exchange rate from the selected currency to euros."""

    if api_key is None:
        console.print("[bold red]API-sleutel niet gevonden[/bold red]")
        return None

    url = EXCHANGE_RATE_URL.format(api_key, currency)

    try:
        response = requests.get(url)

    except requests.exceptions.ConnectionError:
        console.print("[bold red]API niet bereikbaar.[/bold red]")
        return None

    if response.status_code != 200:
        console.print("[red]De wisselkoers kon niet worden opgehaald.[/red]")
        return None

    data = response.json()
    conversion_rates = data["conversion_rates"]
    exchange_rate = conversion_rates["EUR"]
    return exchange_rate


def convert_to_euro(foreign_currency_amount, exchange_rate):
    """Converts the foreign currency amount to euros."""

    euro_amount = foreign_currency_amount * exchange_rate
    return euro_amount


def print_exchange_result(foreign_currency_amount, currency, exchange_rate, euro_amount):
    """Prints the exchange result."""

    result = (
        f"[bold green]Bedrag[/bold green]: {foreign_currency_amount:.2f} ({currency})\n"
        f"[bold green]Koers naar euro:[/bold green] {exchange_rate}\n"
        f"[bold green]Euro's[/bold green]: {euro_amount:.2f}\n"
    )

    console.print(
        Panel.fit(
            result,
            title="[bold #FFFFFF]WISSELKANTOOR[/bold #FFFFFF]",
            padding=(0, 1),
        )
    )


def run_exchange():
    """Handles the functionalities of the currency exchange office."""

    foreign_currency_amount, currency = get_exchange_request()

    if foreign_currency_amount is None or currency is None:
        return None

    exchange_rate = get_exchange_rate_for_currency(currency)

    if exchange_rate is None:
        console.print("[bold red]Het ophalen van de wisselkoers is niet gelukt.[/bold red]")
        return None

    euro_amount = convert_to_euro(foreign_currency_amount, exchange_rate)

    print_exchange_result(foreign_currency_amount, currency, exchange_rate, euro_amount)

    return euro_amount

