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
Die Grafik zeigt, dass der Strombedarf in der Schweiz von 2015 bis 2024 insgesamt angestiegen ist – besonders ab 2022. Den zusätzlichen Bedarf deckten vor allem die Wasserkraft, die deutlich zulegte, und die Photovoltaik, die stetig ausgebaut wurde. Kernkraft und thermische Energie blieben weitgehend konstant, während andere erneuerbare Quellen nur einen kleinen Anteil beitrugen. Damit wird klar: Der Mehrbedarf wurde primär durch erneuerbare Energien gedeckt.

<iframe src="assets/diagramme/stromproduktion_kuchendiagramm_slider.html"></iframe>

Aus der Grafik kann eine deutliche Zunahme der Solarenergie (Photovoltaik) herausgelesen werden. Von 2015 bis 2024 war das eine Zunahme von fast dem 5-fachen. Im Vergleich zu den zwei Hauptenergiequellen Wasserkraft und Kernkraft ist es immer noch ein sehr kleiner Anteil.

Insgesamt zeigt die Analyse, wie Solarenergie in der Schweiz als zunehmend wichtige Energiequelle mit bedeutendem Wachstumspotenzial wahrgenommen wird, besonders im Kontext von Subventionen und staatlichen Fördermassnahmen.

### Effizienz der PV-Anlagen in der Schweiz
In der Schweiz werden hauptsächlich kristalline Silizium-Module verwendet. Der durchschnittliche Wirkungsgrad dieser Module hat sich in den letzten zehn Jahren wie folgt entwickelt.

<iframe src="assets/diagramme/Wirkungsgrad_PV_Anlagen.html"></iframe>

Die Daten wurden mittels ChatGPT erstellt und dies von verschiedenen Quellen wie zum Beispiel von Swissolar und BFE.
Folgend die Erkenntniss aus dem Diagramm:
In der Schweiz hat sich der durchschnittliche Wirkungsgrad von Photovoltaik-Modulen in den letzten zehn Jahren kontinuierlich verbessert. Während der Wert im Jahr 2015 noch zwischen 15 % und 16 % lag, erreichte er 2024 bereits 22 % bis 24 %. Besonders zwischen 2015 und 2020 ist ein gleichmässiger Anstieg um jeweils rund 1 Prozentpunkt pro Jahr zu erkennen. Seit 2021 stagniert die Entwicklung leicht, zeigt aber weiterhin eine positive Tendenz.

Diese Verbesserung ist auf technologische Fortschritte in der Zellproduktion zurückzuführen, insbesondere bei kristallinen Siliziummodulen, die in der Schweiz am häufigsten verbaut werden. Der höhere Wirkungsgrad bedeutet, dass bei gleicher Fläche heute deutlich mehr Solarstrom produziert werden kann als noch vor wenigen Jahren.

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

### Solaranlagen in der Schweiz

Dieses Kapitel zeigt auf, wie sich die installierte Leistung und die Verteilung der Solaranlagen im Zeitraum von 2015 bis 2024 entwickelt haben. Anhand von Visualisierungen wird ersichtlich, in welchen Regionen besonders viele Anlagen gebaut wurden und wo weiteres Potenzial besteht. Die Daten geben zudem Aufschluss darüber, wie geografische und klimatische Bedingungen den Ausbau beeinflussen und welche Unterschiede sich zwischen den einzelnen Kantonen zeigen.

Die folgende Visualisierung zeigt die Verteilung der Photovoltaikanlagen (PV-Anlagen) in der Schweiz ab 2015 bis 2024. Die Kreise stehen für die kumulierte Leistung in Kilowatt (kW) pro Region. Je grösser der Kreis, desto höher die installierte Gesamtleistung in diesem Gebiet.

<iframe src="assets/diagramme/elcoms_map.html"></iframe>

Zentrale Erkenntnisse:
* Starke Konzentration in Städten: In urbanen Zentren wie Zürich, Lausanne, Bern und Basel sind besonders viele und leistungsstarke PV-Anlagen installiert. Dies lässt sich durch eine hohe Gebäudedichte und ein gesteigertes Interesse an nachhaltiger Energie erklären.

* Auffällige regionale Unterschiede: Während im Mittelland und in der Nordwestschweiz viele leistungsstarke Anlagen installiert wurden, ist die Dichte in alpinen Regionen geringer. Dennoch sind auch dort einzelne Standorte mit hoher Gesamtleistung sichtbar.

* Details bei genauerem Hinsehen: Beim Hineinzoomen in die Karte werden feinere regionale Unterschiede sichtbar. So lassen sich einzelne Gemeinden mit besonders hoher oder niedriger Leistung identifizieren.

Die Visualisierung gibt somit einen klaren Überblick über den Stand der Solarenergie in der Schweiz. Sie macht regionale Unterschiede sichtbar und zeigt, wo bereits viel in Photovoltaik investiert wurde – und wo noch Potenzial besteht.

<iframe src="assets/diagramme/elcom_entwicklung_total_power.html"></iframe>

Die Grafik zeigt die kumulative Entwicklung der installierten Gesamtleistung von Photovoltaikanlagen pro Kanton in der Schweiz im Zeitraum von 2015 bis 2024. Deutlich wird, dass alle Kantone einen kontinuierlichen Zubau verzeichnen – allerdings mit grossen Unterschieden beim Wachstumstempo.

Besonders auffällig ist der starke Anstieg in einzelnen Kantonen, die bereits früh in den Ausbau der Solarenergie investiert haben oder in denen grössere Anlagen realisiert wurden. Der Vergleich zeigt zudem, dass wirtschaftlich starke oder bevölkerungsreiche Kantone tendenziell eine höhere installierte Gesamtleistung aufweisen.

Der stetige Zuwachs über alle Jahre hinweg verdeutlicht die zunehmende Bedeutung der Solarenergie in der Schweiz. Die unterschiedlichen Ausgangsniveaus und Wachstumsraten liefern zudem wichtige Hinweise auf das regionale Potenzial, aber auch auf bestehende Unterschiede bei Fördermassnahmen, Flächenverfügbarkeit oder politischem Engagement.


<iframe src="assets/diagramme/elcom_total_power_2024.html"></iframe>

Die Balkengrafik zeigt die kumulierte Gesamtkapazität der installierten Photovoltaikanlagen pro Kanton in der Schweiz im Zeitraum von 2015 bis 2024. An der Spitze liegen die Kantone Bern und Zürich mit jeweils rund 150 MW installierter Leistung, gefolgt von Aargau, St. Gallen und Waadt. Diese Kantone verfügen über günstige Rahmenbedingungen, eine hohe Gebäudedichte und engagierte Förderprogramme, was den Ausbau begünstigt hat.

Am unteren Ende der Rangliste befinden sich kleinere oder topografisch anspruchsvollere Kantone wie Appenzell Innerrhoden, Uri und Obwalden. Dort sind die Ausbaupotenziale begrenzter, was sich in der niedrigeren kumulierten Leistung widerspiegelt. Die Grafik verdeutlicht die regionalen Unterschiede beim PV-Ausbau und zeigt gleichzeitig, wo noch ungenutztes Potenzial vorhanden ist.


TODO @Amel

<iframe src="assets/diagramme/map_cumulative_pv_power.html"></iframe>

TODO @Amel