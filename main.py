# Constante waarden
BASE_URL = ""
PARAMS = {
    "": ""  # Haal alleen de naam en regio op
}


def get_countries_data():
    """
    Haalt landeninformatie op van de REST Countries API.
    - Gebruik de requests library om een GET request te sturen naar de API.
    - Verwerk de JSON-response.
    - Retourneer een lijst van landen met alleen de noodzakelijke velden (naam en regio).
    """

    # Schrijf hier de code om data van de API op te halen


def play_guess_the_region_game(countries):
    """
    Start het spel waarbij de speler moet raden in welke regio een willekeurig land ligt.
    - Maak een lijst van landen met geldige namen en regio's.
    - Zet een score bijhouden mechanisme op.
    - Gebruik een loop waarin een willekeurig land wordt gekozen.
    - Vraag de gebruiker om de regio te raden.
    - Controleer het antwoord en verhoog de score als het juist is, of stop het spel als het fout is.
    - Toon de huidige score bij elke juiste gok en de eindscore als het fout is.
    """

    # Initialiseer de score en maak een lijst van landen met correcte data
    # Gebruik een loop om het spel te laten doorgaan zolang het antwoord goed is
    # Haal een willekeurig land op en vraag de gebruiker om te raden
    # Controleer of de invoer juist is en verhoog de score of beëindig het spel


def main():
    """
    De hoofdfunctie van het programma:
    - Roep de functie aan om landeninformatie op te halen.
    - Controleer of de data correct is opgehaald.
    - Start het spel met de opgehaalde landeninformatie.
    """

    # Roep hier de functie aan om de landen data op te halen
    # Controleer of er data is opgehaald en start anders een foutmelding


# Zorg ervoor dat het spel start wanneer het script direct wordt uitgevoerd
if __name__ == "__main__":
    main()
