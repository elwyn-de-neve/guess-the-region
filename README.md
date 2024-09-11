# Raad de Regio Spel

Dit project bestaat uit twee delen waarin een eenvoudig Python-spel wordt gemaakt. De speler moet raden in welke regio een willekeurig geselecteerd land ligt, gebaseerd op gegevens die worden opgehaald via de REST Countries API.

## Inhoudsopgave

1. [Overzicht](#overzicht)
2. [Deel 1: Basisversie zonder scores](#deel-1-basisversie-zonder-scores)
   - Functies
   - Installatie
   - Gebruik
3. [Deel 2: Uitgebreide versie met scores en gebruikersnamen](#deel-2-uitgebreide-versie-met-scores-en-gebruikersnamen)
   - Toegevoegde Functionaliteiten
   - Installatie
   - Gebruik
   - Score Opslag en Weergave

## Overzicht

Het doel van het spel is om te raden in welke regio een land ligt, zoals Afrika of Europa. De speler krijgt de naam van een land te zien en moet het bijbehorende nummer van de regio invoeren om door te gaan. Deel 1 bevat de basisfunctionaliteit, terwijl deel 2 uitbreidingen toevoegt, zoals het bijhouden van scores en gebruikersnamen.

## Deel 1: Basisversie zonder scores

### Functies

- **API Gegevens Ophalen**: Haalt landeninformatie op van de REST Countries API met de velden `name` en `region`.
- **Regio Raden Spel**: De speler moet raden in welke regio een willekeurig geselecteerd land ligt.
- **Einde van het Spel**: Het spel eindigt wanneer de speler een fout maakt, en de eindscore wordt getoond.

### Installatie

1. Zorg dat Python is geïnstalleerd op je systeem.
2. Installeer de benodigde module (`requests`) met de volgende command:
   ```bash
   pip install requests
   ```
3. Clone of download dit project naar je lokale omgeving.

### Gebruik

1. Voer het script uit met:
   ```bash
   python main.py
   ```
2. Volg de instructies op het scherm om de regio van een willekeurig land te raden.
3. Het spel stopt wanneer je fout raadt en toont je eindscore.

---

## Deel 2: Uitgebreide versie met scores en gebruikersnamen

### Toegevoegde Functionaliteiten

- **Gebruikersnaam Invoer**: De speler voert zijn naam in bij het starten van het spel.
- **Score Opslaan**: De score van de speler wordt opgeslagen in een bestand (`score.txt`).
- **Scores Weergeven**: Aan het einde van het spel worden alle opgeslagen scores weergegeven, zodat de speler zijn prestatie kan vergelijken met eerdere pogingen.

### Installatie

1. Zorg dat Python is geïnstalleerd op je systeem.
2. Installeer de benodigde module (`requests`) met de volgende command:
   ```bash
   pip install requests
   ```
3. Clone of download dit project naar je lokale omgeving.

### Gebruik

1. Voer het script uit met:
   ```bash
   python main.py
   ```
2. Voer je gebruikersnaam in wanneer hierom gevraagd wordt.
3. Volg de instructies op het scherm om de regio van een willekeurig land te raden.
4. Het spel stopt wanneer je fout raadt en toont je eindscore.
5. Je score wordt opgeslagen, en aan het einde van het spel worden alle scores weergegeven.

### Score Opslag en Weergave

- Scores worden opgeslagen in een bestand genaamd `score.txt` in hetzelfde directory als het script.
- Elke score wordt opgeslagen in de vorm `gebruikersnaam,score`.
- Aan het einde van elk spel worden alle scores weergegeven.

