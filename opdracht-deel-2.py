# Importeer de benodigde modules


# Constante waarden in hoofdletters
BASE_URL = ""
SCORE_FILE = ""  # Bestand voor het opslaan van scores

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

    Returns:
        int: De eindscore van de speler.
    """
    # TODO: Implementeer het spelmechanisme voor het raden van regio's


def save_score(username, score):
    """
    Sla de score van de speler op in een bestand.

    Stappen:
    1. Open het scorebestand in append-modus.
    2. Schrijf de gebruikersnaam en score gescheiden door een komma naar het bestand.
    3. Sluit het bestand.

    Args:
        username (str): De naam van de speler.
        score (int): De score van de speler.
    """
    # TODO: Implementeer het opslaan van de score in het bestand


def display_scores():
    """
    Lees en toon de opgeslagen scores.

    Stappen:
    1. Controleer of het scorebestand bestaat.
    2. Lees de scores uit het bestand, splits elke regel op de komma.
    3. Bewaar de scores in een lijst en toon deze aan de speler.
    4. Toon een melding als er geen scores zijn opgeslagen.

    Returns:
        None
    """
    # TODO: Implementeer het lezen en tonen van scores


def main():
    """
    Voer het spel uit en beheer scores.

    Stappen:
    1. Vraag de speler om zijn gebruikersnaam in te voeren.
    2. Haal de landeninformatie op via de API.
    3. Controleer of de gegevens succesvol zijn opgehaald.
    4. Start het spel en verkrijg de score van de speler.
    5. Sla de score van de speler op in het scorebestand.
    6. Toon alle opgeslagen scores aan het einde van het spel.
    """
    # TODO: Implementeer de hoofdlogica om het spel uit te voeren en scores te beheren


# Start het spel als dit script direct wordt uitgevoerd
if __name__ == "__main__":
    main()
