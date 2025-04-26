## Datenanalyse und Erkenntnisse
Hinweis: folgende Unterkapitel beziehen sich grundsätzlich auf einen Zeitraum von den letzten 10 Jahren (01.01.2015 - 31.12.2024).

### Wetterentwicklung in der Schweiz
Die in diesem Kapitel präsentierten Daten stammen von MeteoSwiss, der offiziellen Wetter- und Klimainstitution der Schweiz. Die Messwerte werden von verschiedenen meteorologischen Stationen erfasst, die strategisch über das gesamte Land verteilt sind. Diese breite Streuung der Messpunkte stellt sicher, dass die erfassten Wetter- und Klimadaten eine repräsentative Abdeckung für die gesamte Schweiz bieten.

#### Verteilung der Wettermessstationen in der Schweiz

Die nachfolgende Karte gibt einen Überblick über die Standorte der jeweiligen Messstationen und verdeutlicht die flächendeckende Erfassung der Daten. 

<iframe src="assets/diagramme/swiss_stations_map.html"></iframe> 

Zur besseren Einordnung der Wetterstationen, folgend eine Tabelle zur Höhenverteilung. Daraus kann man ableiten, dass ein Grossteil der Wetterstationen unter 500 Höhenmeter liegen und der andere Grossteil zwischen 500 und 1'500 Meter.

{% include_relative assets/md/hoehenverteilung_stationen.md %}

#### Monatliche Sonnenstunden in der Schweiz: Trends, Verteilung und saisonale Muster

Die folgenden zwei interaktiven Grafiken veranschaulichen die Anzahl der Sonnenstunden pro Monat in der Schweiz über die vergangenen zehn Jahre.

Das Liniendiagramm stellt die Entwicklung der monatlichen Sonnenstunden im Verlauf der Jahre dar und bietet zudem eine Übersicht über den Durchschnitt und den Median. So lassen sich langfristige Trends und saisonale Schwankungen auf einen Blick erkennen.

<iframe src="assets/diagramme/sunhours_per_month.html"></iframe>


Die folgende Grafik stellt die Verteilung der Sonnenstunden in einer alternativen Darstellungsform als Boxplot dar. Diese Visualisierung ermöglicht eine präzisere Analyse der Spannweite, Medianwerte und möglicher Ausreisser innerhalb der Daten.

<iframe src="assets/diagramme/sunhours_distribution_per_month.html"></iframe>

Und hier noch als Violinplot:

<iframe src="assets/diagramme/sunhours_violinplot_per_month.html"></iframe>

Aus diesen Diagrammen kann man folgende Feststellungen ableiten:
* **Hohe Sonnenstunden im Sommer, niedrige im Winter:** Die Sonnenstunden pro Monat erreichen ihren Höhepunkt in den Sommermonaten (Mai bis August), mit einem deutlichen Rückgang in den Wintermonaten (November bis Februar).
* **Eindeutiger Trend zu mehr Sonnenstunden im Frühling und Herbst:** Frühling und Herbst weisen eine moderate Anzahl an Sonnenstunden auf, was für die Solarproduktion außerhalb der Sommermonate von Bedeutung ist.
* **Schwankende Jahreswerte:** In den dargestellten Jahren gibt es Schwankungen bei der Gesamtzahl der Sonnenstunden, was auf jahreszeitlich bedingte Variationen hinweist, aber auch auf mögliche langfristige klimatische Veränderungen.

<br>

#### Regionale Analyse der Sonnenstunden: Kantonale Unterschiede und Einflussfaktoren

Für die Auswertungen der Sonnenstunden pro Kanton und der Darstellung auf einer Karte mussten die Wetterdaten (Sonnenstunden) mit den  Wettermessstationen-Daten kombiniert werden. Ausserdem mussten die Daten angereichert werden, z.B. mit den Kantonen anhand der Orte der Messstationen.

<iframe src="assets/diagramme/swiss_sunhours_map.html"></iframe>

Aus diesem Diagramm kann man folgende Feststellungen ableiten:

* **Regionale Unterschiede:** In den südlichen Teilen der Schweiz (z. B. Tessin) gibt es mehr Sonnenstunden als in nördlicheren Regionen wie Zürich oder Basel.
* **Sonnenreiche Kantone:** Kantone wie **Genf**, **Wallis**, **Thurgau** und **Graubünden** weisen besonders hohe Werte auf – meist über **1700 Sonnenstunden pro Jahr**.
* **Weniger Sonnenstunden in Zentralschweiz und Alpenraum:** Kantone wie **Uri**, **Glarus**, **Schwyz** und **Obwalden** erreichen teils weniger als **1300 Sonnenstunden jährlich**.
* **Einfluss geografischer Faktoren:** Die Unterschiede lassen sich durch eine Kombination aus **Südlage, Höhenlage und geringerer Nebelhäufigkeit** erklären.
* **Benachteiligung durch Topografie:** Regionen in **Tälern oder mit häufigem Winternebel** (z. B. Mittelland, Zentralschweiz) haben tendenziell tiefere Werte.


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

#### Photovoltaik-Leistung in der Schweiz: Zoom auf regionale Unterschiede

Die folgende Visualisierung zeigt die Verteilung der Photovoltaikanlagen (PV-Anlagen) in der Schweiz ab 2015 bis 2024. Die Kreise stehen für die kumulierte Leistung in Kilowatt (kW) pro Region. Je grösser der Kreis, desto höher die installierte Gesamtleistung in diesem Gebiet.

<iframe src="assets/diagramme/elcoms_map.html"></iframe>

Zentrale Erkenntnisse:
* Starke Konzentration in Städten: In urbanen Zentren wie Zürich, Lausanne, Bern und Basel sind besonders viele und leistungsstarke PV-Anlagen installiert. Dies lässt sich durch eine hohe Gebäudedichte und ein gesteigertes Interesse an nachhaltiger Energie erklären.

* Auffällige regionale Unterschiede: Während im Mittelland und in der Nordwestschweiz viele leistungsstarke Anlagen installiert wurden, ist die Dichte in alpinen Regionen geringer. Dennoch sind auch dort einzelne Standorte mit hoher Gesamtleistung sichtbar.

* Details bei genauerem Hinsehen: Beim Hineinzoomen in die Karte werden feinere regionale Unterschiede sichtbar. So lassen sich einzelne Gemeinden mit besonders hoher oder niedriger Leistung identifizieren.

Die Visualisierung gibt somit einen klaren Überblick über den Stand der Solarenergie in der Schweiz. Sie macht regionale Unterschiede sichtbar und zeigt, wo bereits viel in Photovoltaik investiert wurde – und wo noch Potenzial besteht.

#### Entwicklung der installierten PV-Leistung pro Kanton (2015–2024)

<iframe src="assets/diagramme/elcom_entwicklung_total_power.html"></iframe>

Die Grafik zeigt die kumulative Entwicklung der installierten Gesamtleistung von Photovoltaikanlagen pro Kanton in der Schweiz im Zeitraum von 2015 bis 2024. Deutlich wird, dass alle Kantone einen kontinuierlichen Zubau verzeichnen – allerdings mit grossen Unterschieden beim Wachstumstempo.

Besonders auffällig ist der starke Anstieg in einzelnen Kantonen, die bereits früh in den Ausbau der Solarenergie investiert haben oder in denen grössere Anlagen realisiert wurden. Der Vergleich zeigt zudem, dass wirtschaftlich starke oder bevölkerungsreiche Kantone tendenziell eine höhere installierte Gesamtleistung aufweisen.

Der stetige Zuwachs über alle Jahre hinweg verdeutlicht die zunehmende Bedeutung der Solarenergie in der Schweiz. Die unterschiedlichen Ausgangsniveaus und Wachstumsraten liefern zudem wichtige Hinweise auf das regionale Potenzial, aber auch auf bestehende Unterschiede bei Fördermassnahmen, Flächenverfügbarkeit oder politischem Engagement.


<iframe src="assets/diagramme/elcom_total_power_2024.html"></iframe>

Die Balkengrafik zeigt die kumulierte Gesamtkapazität der installierten Photovoltaikanlagen pro Kanton in der Schweiz im Zeitraum von 2015 bis 2024. An der Spitze liegen die Kantone Bern und Zürich mit jeweils rund 150 MW installierter Leistung, gefolgt von Aargau, St. Gallen und Waadt. Diese Kantone verfügen über günstige Rahmenbedingungen, eine hohe Gebäudedichte und engagierte Förderprogramme, was den Ausbau begünstigt hat.

Am unteren Ende der Rangliste befinden sich kleinere oder topografisch anspruchsvollere Kantone wie Appenzell Innerrhoden, Uri und Obwalden. Dort sind die Ausbaupotenziale begrenzter, was sich in der niedrigeren kumulierten Leistung widerspiegelt. Die Grafik verdeutlicht die regionalen Unterschiede beim PV-Ausbau und zeigt gleichzeitig, wo noch ungenutztes Potenzial vorhanden ist.

#### Choroplethenkarte des Photovoltaik-Ausbaus auf Gemeindeebene

Die untenstehende Choroplethenkarte zeigt die aggregierte installierte Leistung von Photovoltaikanlagen (PV) in der Schweiz pro Gemeinde im Zeitraum von 2015 bis 2024. Die Karte basiert auf offiziellen Gemeindedaten und bildet die kumulierte Solarleistung (in Megawatt, MW) farblich abgestuft ab. Je dunkler eine Gemeinde eingefärbt ist, desto höher ist die installierte Gesamtleistung in diesem Zeitraum.

Die Daten wurden zusammengeführt und georeferenziert, um einen räumlichen Überblick über den Ausbau der Solarenergie auf lokaler Ebene zu ermöglichen.

<iframe src="assets/diagramme/map_cumulative_pv_power.html"></iframe>

Die Karte zeigt deutliche regionale Unterschiede beim Ausbau der Photovoltaik in der Schweiz. Besonders Gemeinden im Mittelland, nördlich des Genfersees und im Raum Zürich weisen hohe installierte Leistungen auf. Diese Ballungsräume verfügen über eine hohe Gebäudedichte, gute wirtschaftliche Voraussetzungen und teilweise gezielte Fördermassnahmen. In ländlicheren oder gebirgigen Regionen, insbesondere im Südosten und in Teilen des Wallis und Graubündens, fällt die installierte Leistung pro Gemeinde hingegen deutlich geringer aus. Dies deutet auf ungenutztes Potenzial für den weiteren PV-Ausbau in diesen Gebieten hin.

### Solarpotenzial der Gebäude in der Schweiz: Dächer und Fassaden nach Kanton

Die Gebäude der Schweiz – insbesondere ihre Dach- und Fassadenflächen – bergen ein erhebliches ungenutztes Potenzial für die Solarstromproduktion. In diesem Abschnitt analysieren wir, wie viel Energie theoretisch durch Photovoltaik auf bestehenden Gebäudeflächen in den einzelnen Kantonen erzeugt werden könnte.

Für diese Auswertung haben wir auf die bereits aufbereiteten Daten von [sonnendach.ch](https://www.sonnendach.ch/) zurückgegriffen. Diese Plattform basiert auf umfassenden Berechnungen des Bundesamtes für Energie (BFE) und berücksichtigt Aspekte wie Dachneigung, Ausrichtung, Verschattung und Flächengrösse.

Wir haben uns bewusst für diese Vorgehensweise entschieden, da die Originaldaten als Geopackage-Dateien über 5 GB gross waren. Eine direkte Verarbeitung dieser Rohdaten war technisch nicht möglich, da sowohl der verfügbare Arbeitsspeicher der Webplattform als auch die Leistungsfähigkeit des verwendeten Laptops nicht ausreichten, um diese Datenmengen effizient zu laden und zu analysieren. Insbesondere der Versuch, eine vollständige Folium-Map zu generieren, führte wiederholt zu Abstürzen aufgrund von Speicherüberlastung.

<iframe src="https://map.geo.admin.ch/#/embed?lang=de&center=2669890.62,1173563.63&z=0&topic=energie&layers=ch.bfe.solarenergie-eignung-daecher;ch.bfe.solarenergie-eignung-fassaden&bgLayer=ch.swisstopo.swissimage&featureInfo=default" style="border: 0;width: 100%;height: 650px;max-width: 100%;max-height: 100%;" allow="geolocation"></iframe>

Die Auswertung zeigt, dass das Solarenergiepotenzial in der Schweiz regional sehr unterschiedlich verteilt ist. Kantone mit hoher Gebäudedichte, grosser Dachflächenverfügbarkeit und günstiger Ausrichtung – wie Zürich, Bern, Waadt und Aargau – weisen das höchste theoretische Potenzial auf. Auch das Tessin erzielt dank seiner überdurchschnittlichen Sonneneinstrahlung trotz kleinerer Fläche hohe Werte.

Auffällig ist, dass selbst in Kantonen mit bisher geringem Photovoltaik-Ausbau (z. B. Jura, Glarus oder Nidwalden) erhebliche ungenutzte Flächenreserven bestehen. Dies unterstreicht, dass der zukünftige Ausbau der Solarenergie in der Schweiz nicht nur von der Sonneneinstrahlung, sondern auch stark von politischen, wirtschaftlichen und infrastrukturellen Rahmenbedingungen abhängig sein wird.

Ein weiterer wichtiger Punkt: Neben den Dachflächen bieten insbesondere vertikale Fassaden in städtischen Gebieten zusätzliche Ausbauchancen, die bislang vergleichsweise wenig genutzt werden.

Insgesamt belegen die Ergebnisse, dass die bestehende Gebäudeinfrastruktur in der Schweiz ein zentrales Element für die Erreichung der Energiewendeziele darstellen kann – vorausgesetzt, dass das technische Potenzial konsequent erschlossen und durch geeignete Fördermassnahmen begleitet wird.

### Fazit Datenanalyse und Erkenntnisse

Die umfassende Analyse über den Zeitraum der letzten zehn Jahre liefert ein klares Bild der klimatischen, geografischen und energietechnischen Entwicklungen in der Schweiz. Im Zentrum stehen die steigende Bedeutung der Solarenergie sowie deren regional unterschiedliche Verbreitung.

Wetter und Sonnenstunden:
Die Auswertung der MeteoSchweiz-Daten zeigt eine erwartungsgemäße saisonale Verteilung der Sonnenstunden: Hohe Werte im Sommer, niedrige im Winter. Besonders auffällig ist jedoch der Trend zu mehr Sonnenstunden im Frühling und Herbst – ein positiver Faktor für die gleichmäßigere Nutzung von Solarenergie über das Jahr hinweg. Auch regional bestehen klare Unterschiede, wobei sich der Süden (z. B. Tessin) durch besonders viele Sonnenstunden auszeichnet, ebenso wie einige hochgelegene Standorte. Dies unterstreicht die Relevanz standortbezogener Analysen für zukünftige PV-Investitionen.

Solarenergie und Stromproduktion:
Der Anteil der Solarenergie an der gesamten Stromproduktion hat sich in der Dekade deutlich erhöht – fast verfünffacht – und trägt mittlerweile signifikant zur Energieversorgung bei. Dennoch bleibt ihr Anteil im Vergleich zu Wasserkraft und Kernenergie gering. Die Entwicklung des Wirkungsgrads von PV-Modulen zeigt technologische Fortschritte, die es ermöglichen, auf gleicher Fläche zunehmend mehr Energie zu erzeugen.

Stromverbrauch und Elektromobilität:
Während der Stromverbrauch in den meisten Sektoren stabil blieb oder leicht zurückging, zeigt sich ein starker Anstieg im Bereich Elektromobilität. Diese Entwicklung hebt den wachsenden Bedarf an erneuerbarem Strom hervor und betont die Notwendigkeit eines zügigen Ausbaus von Solar- und anderen erneuerbaren Energiequellen.

Regionale Unterschiede beim PV-Ausbau:
Die regionale Analyse des PV-Ausbaus zeigt klare Schwerpunkte in wirtschaftlich starken und bevölkerungsreichen Kantonen sowie in urbanen Zentren. Gleichzeitig offenbart die Choroplethenkarte ungenutztes Potenzial in alpinen und strukturschwächeren Regionen. Die Unterschiede lassen sich durch eine Kombination aus Fördermaßnahmen, wirtschaftlichen Bedingungen, technischer Umsetzbarkeit und politischem Willen erklären.

Gesamtbetrachtung:
Die Ergebnisse belegen, dass die Schweiz beim Ausbau der Solarenergie bedeutende Fortschritte gemacht hat, jedoch weiterhin regionale Disparitäten bestehen. Das Potenzial ist noch nicht ausgeschöpft – weder technologisch noch geographisch. Eine gezieltere Förderung in bisher unterrepräsentierten Regionen, gekoppelt mit weiteren Effizienzsteigerungen bei PV-Anlagen, könnte die nachhaltige Energiezukunft der Schweiz entscheidend voranbringen.

Diese Erkenntnisse bieten eine solide Grundlage für politische Entscheidungen, Investitionsstrategien und die zukünftige Ausrichtung der Schweizer Energiepolitik.

----