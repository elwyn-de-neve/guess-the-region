# Importeer de benodigde modules

# Constante waarden in hoofdletters
BASE_URL = ""

# Parameters voor de API request om alleen de benodigde velden op te halen
PARAMS = {
    "": ""
}

# Mogelijke regio's met bijbehorende cijfers
REGION_OPTIONS = {
    1: "Africa",
    2: "Americas",
    3: "Asia",
    4: "Europe",
    5: "Oceania",
    6: "Antarctic"
}


def get_countries_data():
    """
    Haalt landeninformatie op van de API.

    Stappen:
    1. Verstuur een GET-verzoek naar de API met de juiste parameters.
    2. Controleer of het verzoek succesvol was.
    3. Verwerk de JSON-respons om een lijst van landen terug te geven.
    4. Geef een foutmelding weer als het ophalen niet lukt.

    Returns:
        list: Lijst van landen met naam en regio of None bij een fout.
    """
    # TODO: Implementeer het ophalen van gegevens van de API


def play_guess_the_region_game(countries):
    """
    Spel waarbij je moet raden in welke regio een land ligt.

    Stappen:
    1. Filter de landenlijst om alleen landen met geldige regio's en namen te behouden.
    2. Start een scoreteller op 0.
    3. Selecteer willekeurig een land uit de lijst.
    4. Vraag de speler om de regio te raden door een cijfer in te voeren.
    5. Vergelijk de keuze van de speler met de juiste regio.
    6. Verhoog de score bij een correct antwoord, laat doorgaan.
    7. Stop het spel en toon de eindscore als het antwoord fout is.

    Args:
        countries (list): Lijst met landeninformatie.
    """
    # TODO: Implementeer het spelmechanisme voor het raden van regio's


def main():
    """
    Voer het spel uit.

    Stappen:
    1. Haal de landeninformatie op via de API.
    2. Controleer of de gegevens succesvol zijn opgehaald.
    3. Start het spel als de gegevens beschikbaar zijn.
    4. Toon een foutmelding als het ophalen van gegevens mislukt.
    """
    # TODO: Haal landeninformatie op en start het spel


# Start het spel als dit script direct wordt uitgevoerd
if __name__ == "__main__":
    main()
