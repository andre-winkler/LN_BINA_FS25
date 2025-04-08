## Datenanalyse und Erkenntnisse
Hinweis: folgende Unterkapitel beziehen sich grundsätzlich auf einen Zeitraum von den letzten 10 Jahren (01.01.2015 - 31.12.2024).

### Wetterentwicklung in der Schweiz
Die in diesem Kapitel präsentierten Daten stammen von MeteoSwiss, der offiziellen Wetter- und Klimainstitution der Schweiz. Die Messwerte werden von verschiedenen meteorologischen Stationen erfasst, die strategisch über das gesamte Land verteilt sind. Diese breite Streuung der Messpunkte stellt sicher, dass die erfassten Wetter- und Klimadaten eine repräsentative Abdeckung für die gesamte Schweiz bieten.

Die nachfolgende Karte gibt einen Überblick über die Standorte der jeweiligen Messstationen und verdeutlicht die flächendeckende Erfassung der Daten. 

<iframe src="assets/diagramme/swiss_stations_map.html"></iframe>


Die folgenden zwei interaktiven Grafiken veranschaulichen die Anzahl der Sonnenstunden pro Monat in der Schweiz über die vergangenen zehn Jahre.

Das Liniendiagramm stellt die Entwicklung der monatlichen Sonnenstunden im Verlauf der Jahre dar und bietet zudem eine Übersicht über den Durchschnitt und den Median. So lassen sich langfristige Trends und saisonale Schwankungen auf einen Blick erkennen.

<iframe src="assets/diagramme/sunhours_per_month.html"></iframe>


Die folgende Grafik stellt die Verteilung der Sonnenstunden in einer alternativen Darstellungsform als Boxplot dar. Diese Visualisierung ermöglicht eine präzisere Analyse der Spannweite, Medianwerte und möglicher Ausreisser innerhalb der Daten.

<iframe src="assets/diagramme/sunhours_distribution_per_month.html"></iframe>

Aus diesen zwei Diagrammen kann man folgende Feststellungen ableiten:
* **Hohe Sonnenstunden im Sommer, niedrige im Winter:** Die Sonnenstunden pro Monat erreichen ihren Höhepunkt in den Sommermonaten (Mai bis August), mit einem deutlichen Rückgang in den Wintermonaten (November bis Februar).
* **Eindeutiger Trend zu mehr Sonnenstunden im Frühling und Herbst:** Frühling und Herbst weisen eine moderate Anzahl an Sonnenstunden auf, was für die Solarproduktion außerhalb der Sommermonate von Bedeutung ist.
* **Schwankende Jahreswerte:** In den dargestellten Jahren gibt es Schwankungen bei der Gesamtzahl der Sonnenstunden, was auf jahreszeitlich bedingte Variationen hinweist, aber auch auf mögliche langfristige klimatische Veränderungen.

<br>
Für die Auswertungen der Sonnenstunden pro Kanton und der Darstellung auf einer Karte mussten die Wetterdaten (Sonnenstunden) mit den  Wettermessstationen-Daten kombiniert werden. Ausserdem mussten die Daten angereichert werden, z.B. mit den Kantonen anhand der Orte der Messstationen.

<iframe src="assets/diagramme/swiss_sunhours_map.html"></iframe>

Aus diesem Diagramm kann man folgende Feststellungen ableiten:
* **Regionale Unterschiede:** In den südlichen Teilen der Schweiz (z.B. Tessin) gibt es mehr Sonnenstunden als in den nördlicheren Regionen (z.B. Zürich oder Basel).

<br>
TODO Amel - Python Code von Diagramm fehlt
<iframe src="assets/diagramme/sonnenstunden_3d_final_extrem_flach.html" width="100%" height="600px"></iframe>

TODO Amel - Feststellungen

### Solarenergie-Entwicklung in der Schweiz

Folgende zwei Grafiken präsentieren die Energie-Entwicklung in der Schweiz der letzten 10 Jahre. Einmal als Flächenchart und für detailliertere Auswertung als Pie-Chart.

<iframe src="assets/diagramme/solar_vs_other_energy_sources.html"></iframe>

<iframe src="assets/diagramme/stromproduktion_kuchendiagramm_2015_2024.html" 
        width="100%" height="600px" style="border:none;"></iframe>

TODO Feststellungen hier beschreiben