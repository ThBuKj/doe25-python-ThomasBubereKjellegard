# Systemövervakning (System Monitor)

Ett enkelt Python-program för att övervaka systemresurser (CPU, Minne, Disk) och sätta upp larm.

## Filöversikt

* **`main.py`**: Startfilen som hanterar huvudmenyn och programflödet.
* **`menu.py`**: Innehåller funktioner för att visa menyn och hantera användarens val.
* **`monitoring.py`**: Kärnlogik för systemövervakning. Hanterar statusinsamling (`psutil`), larmhantering och live-övervakningsläget.
* **`alarms.py`**: En klass (`Alarm`) för att representera ett larmobjekt (typ och tröskelvärde).

## Funktioner

1.  **Starta övervakning**: Startar en bakgrundstråd som kontinuerligt kontrollerar om satta larm har överskridits.
2.  **Visa aktuell systemstatus**: Visar aktuell CPU-, Minnes- och Diskanvändning.
3.  **Skapa larm**: Gör det möjligt att sätta en tröskel (i procent) för CPU, Minne eller Disk.
4.  **Visa aktiva larm**: Listar alla konfigurerade larm.
5.  **Starta live-övervakning**: Visar systemstatus kontinuerligt i terminalen (uppdateras varannan sekund).

## Krav

Programmet använder biblioteket `psutil`. Det måste vara installerat för att programmet ska fungera.

```bash
pip install psutil