## Datenanalyse und Erkenntnisse
Hinweis: folgende Unterkapitel beziehen sich grundsätzlich auf einen Zeitraum von den letzten 10 Jahren (01.01.2015 - 31.12.2024).

### Wetterentwicklung in der Schweiz
Die in diesem Kapitel präsentierten Daten stammen von MeteoSwiss, der offiziellen Wetter- und Klimainstitution der Schweiz. Die Messwerte werden von verschiedenen meteorologischen Stationen erfasst, die strategisch über das gesamte Land verteilt sind. Diese breite Streuung der Messpunkte stellt sicher, dass die erfassten Wetter- und Klimadaten eine repräsentative Abdeckung für die gesamte Schweiz bieten.

Die nachfolgende Karte gibt einen Überblick über die Standorte der jeweiligen Messstationen und verdeutlicht die flächendeckende Erfassung der Daten. 

<iframe src="assets/diagramme/swiss_stations_map.html"></iframe>

Zur besseren Einordnung der Wetterstationen, folgend eine Tabelle zur Höhenverteilung. Daraus kann man ableiten, dass ein Grossteil der Wetterstationen unter 500 Höhenmeter liegen und der andere Grossteil zwischen 500 und 1'500 Meter.

{% include_relative assets/md/hoehenverteilung_stationen.md %}

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

<iframe src="assets/diagramme/sonnenstunden_3d.html" style="height: 850px !important"></iframe>

Die Auswertung der kumulierten Sonnenstunden über alle berücksichtigten Wetterstationen in der Schweiz zeigt moderate regionale Unterschiede. Stationen im südlichen Teil des Landes, insbesondere im Tessin (z. B. Lugano, Magadino, Cimetta), weisen tendenziell höhere Summen auf als viele Stationen im Mittelland oder in der Nordschweiz. Auch einzelne hochgelegene Stationen wie der Gornergrat oder Piz Corvatsch verzeichnen vergleichsweise hohe Werte über den gesamten Analysezeitraum hinweg.

Die Differenz zwischen der Wetterstation mit dem höchsten und jener mit dem niedrigsten kumulierten Wert liegt bei etwa 20 bis 25 %. Diese Unterschiede lassen sich vermutlich durch eine Kombination aus klimatischen, topografischen und meteorologischen Faktoren erklären.

Die Visualisierung der Werte – beispielsweise in Form einer Karte oder eines Balkendiagramms – ermöglicht eine erste räumliche Einordnung der Sonnenscheindauer. Eine genauere Betrachtung einzelner Stationen zeigt zudem, dass lokale Effekte (z. B. Nebelhäufigkeit, Tal- oder Höhenlage, städtische Umgebung) eine wesentliche Rolle spielen können. Für eine umfassende Bewertung der Ursachen wären jedoch weiterführende meteorologische Analysen notwendig.

### Solarenergie-Entwicklung in der Schweiz

Folgende zwei Grafiken präsentieren die Energie-Entwicklung in der Schweiz der letzten 10 Jahre. Einmal als Flächenchart und für detailliertere Auswertung als Pie-Chart.

<iframe src="assets/diagramme/solar_vs_other_energy_sources.html"></iframe>

<iframe src="assets/diagramme/stromproduktion_kuchendiagramm_slider.html"></iframe>

Aus der Grafik kann eine deutliche Zunahme der Solarenergie (Photovoltaik) herausgelesen werden. Von 2015 bis 2023 war das eine Zunahme von fast dem 5-fachen. Im Vergleich zu den zwei Hauptenergiequellen Wasserkraft und Kernkraft ist es immer noch ein sehr kleiner Anteil.

Insgesamt zeigt die Analyse, wie Solarenergie in der Schweiz als zunehmend wichtige Energiequelle mit bedeutendem Wachstumspotenzial wahrgenommen wird, besonders im Kontext von Subventionen und staatlichen Fördermassnahmen.

### Effizienz der PV-Anlagen in der Schweiz
In der Schweiz werden hauptsächlich kristalline Silizium-Module verwendet. Der durchschnittliche Wirkungsgrad dieser Module hat sich in den letzten zehn Jahren wie folgt entwickelt.

<iframe src="assets/diagramme/Wirkungsgrad_PV_Anlagen.html"></iframe>

Die Daten wurden mittels ChatGPT erstellt und dies von verschiedenen Quellen wie zum Beispiel von Swissolar und BFE.
Folgend die Erkenntniss aus dem Diagramm:
* Der durchschnittliche Modulwirkungsgrad von PV-Anlagen in der Schweiz hat sich in den letzten 10 Jahren stetig verbessert.
* Im Jahr 2015 lag der durchschnittliche Wirkungsgrad bei etwa 15,5 %, während er im Jahr 2024 auf 23 % gestiegen ist.
* Besonders zwischen den Jahren 2019 und 2021 ist ein signifikanter Anstieg des Wirkungsgrads zu beobachten.
* Nach 2021 bleibt der Wirkungsgrad relativ stabil, mit einem leichten Anstieg bis 2024.

Diese Entwicklung zeigt den Fortschritt in der Technologie und Effizienz von PV-Modulen in der Schweiz.

### Stromverbrauch in der Schweiz
Die Grafik zeigt den Strom-Endverbrauch in der Schweiz zwischen 2015 und 2023, aufgeteilt nach verschiedenen Sektoren wie Haushalt, Industrie, Dienstleistungen, Bahnen, Elektromobilität und Verkehr. Sie bietet einen Überblick über die Entwicklung des Verbrauchs in diesen Bereichen.

<iframe src="assets/diagramme/Strom_Endverbrauch_Schweiz.html"></iframe>

Erkenntnisse, welche wir gewonnen haben:
* **Haushalt**: Der Stromverbrauch der Haushalte bleibt über die Jahre relativ stabil, mit leichten Schwankungen.
* **Industrie**: Der Verbrauch in der Industrie zeigt einen leichten Rückgang, insbesondere nach 2019, was auf Effizienzsteigerungen oder wirtschaftliche Veränderungen hindeuten könnte.
* **Dienstleistungen**: Der Verbrauch im Dienstleistungssektor bleibt ebenfalls stabil, mit einem leichten Rückgang in den letzten Jahren.
* **Bahnen**: Der Stromverbrauch der Bahnen bleibt konstant, was die Bedeutung des öffentlichen Verkehrs in der Schweiz unterstreicht.
* **Elektromobilität**: Ein deutlicher Anstieg ist im Bereich Elektromobilität zu erkennen, insbesondere ab 2020, was auf die zunehmende Verbreitung von Elektrofahrzeugen hinweist.
* **Verkehr Beleuchtung und übriger Verkehr**: Diese Kategorien zeigen einen leichten Rückgang, was auf Effizienzsteigerungen oder Änderungen in der Infrastruktur hindeuten könnte.
