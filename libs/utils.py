import re
import locale

# Funktion zur Umrechnung von Grad-Minuten-Sekunden (GMS) in Dezimalgrad (DG)
def gms_to_dg(gms):
    """
        Konvertiert eine GMS-Koordinate (z. B. '12°34') in Dezimalgrad.
    """
    # Überprüfen, ob die Eingabe dem erwarteten Format entspricht
    match = re.match(r"(\d+)°(\d+)", gms)
    if match:
        grad = int(match.group(1))  # Extrahiert die Grad-Komponente
        minuten = int(match.group(2))  # Extrahiert die Minuten-Komponente
        return grad + (minuten / 60)  # Umrechnung in Dezimalgrad
    # Fehler werfen, wenn das Format nicht stimmt
    raise ValueError("Ungültiges Format. Erwartet: 'XX°YY'")

# Formatieren einer Zahl in das Schweizer Format
def format_swiss(value):
    if isinstance(value, (int, float)):
        return locale.format_string('%.2f', value, grouping=True).replace(',', "'")
    return value