## Daten sammeln
Für die Analyse des Solarpotenzials in der Schweiz wurden umfassende Datensätze aus offiziellen Quellen zusammengetragen und aufbereitet. Die wichtigsten Daten stammen vom Bundesamt für Energie (BFE) und MeteoSwiss. Das BFE liefert detaillierte Informationen zur installierten Solarleistung, der Anzahl an Photovoltaikanlagen, den Einspeisevergütungen sowie zu Subventionen und Förderprogrammen. Diese Daten ermöglichen eine genaue Untersuchung der Entwicklung der Solarenergie in der Schweiz über die letzten zehn Jahre und helfen dabei, wirtschaftliche und politische Einflussfaktoren zu bewerten.

Neben den wirtschaftlichen und technischen Aspekten ist die Sonneneinstrahlung der entscheidende Faktor für die Effizienz und Leistungsfähigkeit von Solaranlagen. Um diesen Einfluss zu quantifizieren, wurden die Daten von MeteoSwiss herangezogen. Sie enthalten Messwerte zur Globalstrahlung, den täglichen Sonnenstunden und den Temperaturen an verschiedenen Wetterstationen in der Schweiz. Diese Parameter sind essenziell, um den Zusammenhang zwischen Sonnenenergie und Stromproduktion zu analysieren. Darüber hinaus erlauben sie eine saisonale Betrachtung, da die Solarleistung im Sommer deutlich höher ist als in den Wintermonaten.

Die gesammelten Daten wurden nach ihrer Bereinigung in ein einheitliches Format überführt. Um eine präzisere Analyse zu ermöglichen, erfolgte die Aggregation auf Stundenbasis. Dies erlaubt eine genauere Untersuchung von Trends und Schwankungen im Tagesverlauf sowie eine präzisere Modellierung der Solarstromproduktion. Die Kombination dieser umfangreichen Datensätze bildet die Grundlage für die Untersuchung der Vergangenheit und ermöglicht es, Prognosen für die zukünftige Entwicklung der Solarenergie in der Schweiz abzuleiten.

### MeteoSchweiz - Sonnenstunden je Wetterstation
#### Datenquelle
Die meteorologischen Daten stammen von MeteoSchweiz und wurden über die Plattform IDAWeb bezogen. Die Datengrundlage basiert auf einem Netz von 132 automatisierten Wetterstationen, die flächendeckend in der ganzen Schweiz verteilt sind. Eine Ausnahme bildet der Kanton Appenzell Ausserrhoden (AR), in dem derzeit keine Wetterstation betrieben wird, siehe Kapitel "Wetterentwicklung in der Schweiz".

Für die vorliegende Analyse wurde der Zeitraum vom 01.01.2015 bis zum 31.12.2024 ausgewertet. In IDAWeb wurde gezielt nach dem Parameter «Sonnenstunden» gefiltert. Zusätzlich wurde ein Stationsfilter angewendet, um ausschliesslich Wetterstationen innerhalb der Schweiz auszuwählen. Die so extrahierten Daten bilden die Grundlage für die Analyse der saisonalen und regionalen Unterschiede in der Sonneneinstrahlung.

Der Zugriff auf die Daten erforderte eine offizielle Registrierung bei MeteoSchweiz. Zu diesem Zweck wurde ein entsprechendes Formular unterzeichnet und eingereicht. Die Daten dürfen ausschliesslich für Lehre und Forschung verwendet werden.

<div class="float-right-image" style="width: 250px">
    <img src="assets/images/meteoschweiz_logo.png">
    <div class="image-label">https://x.com/meteoschweiz</div>
</div>

#### Datenqualität und Bereinigung
Die Messdaten von MeteoSchweiz gelten als sehr zuverlässig, da sie vom nationalen Wetterdienst kontinuierlich erhoben, validiert und überwacht werden. Gemäss Rückmeldung von MeteoSchweiz wurden zwischen 2020 und 2023 sämtliche relevanten Wetterstationen auf direkte Messung der Sonnenscheindauer umgerüstet. Seit dem 4. August 2023 liegen daher ausschliesslich gemessene Daten vor. Frühere Werte basieren teilweise auf berechneten Modellen.

In der Datenaufbereitung zeigte sich, dass nicht für alle Stationen in allen Jahren vollständige Werte vorlagen – sei es, weil eine Station noch nicht in Betrieb war, oder weil sie temporär ausser Betrieb war (z. B. durch Wartungen oder technische Störungen). Für diese Fälle wurden jährliche Durchschnittswerte anderer Stationen desselben Kantons als Näherung verwendet. Insgesamt waren davon 2'561 von 15'960 Datensätzen betroffen, was einem Anteil von 16.05 % entspricht. Diese Verrechnungen wurden bei der Interpretation entsprechend berücksichtigt.

Technisch mussten folgende Daten-Bereinigungen und - Anpassungen vorgenommen werden (siehe ipynb\meteo_swiss_data.ipynb):
* Die Datensets der Wetterdaten und Wetterstationen zusammenführen
* Lichtenstein filtern
* Konvertieren in Datumsformat zum zusätzlichen filtern
* Konvertieren in Zahlenformate
* Gruppieren von Daten
* ...


#### Messmethoden und Annahmen
Die Bestimmung der Sonnenscheindauer erfolgt bei MeteoSchweiz auf Basis eines festgelegten Schwellenwerts für die Globalstrahlung. Überschreitet die Strahlung einen Wert von 200 W/m², gilt der entsprechende Zeitraum als sonnig. Dieser Schwellenwert ist im internationalen Vergleich relativ hoch – in vielen anderen Ländern wird ein Wert von nur 120 W/m² verwendet. Dies hat Einfluss auf die ausgewiesene Anzahl an Sonnenstunden und muss bei internationalen Vergleichen entsprechend berücksichtigt werden.

Ein weiterer relevanter Punkt betrifft die Messgeometrie: Die Globalstrahlung wird horizontal zur Erdoberfläche gemessen. Photovoltaikanlagen hingegen sind in der Regel geneigt montiert, um den Einfallswinkel des Sonnenlichts zu optimieren. Dadurch unterscheidet sich die effektive Einstrahlung auf Solarpanels von den gemessenen Werten. Eine direkte Übertragung der gemessenen Strahlung auf die reale Stromproduktion ist deshalb nur eingeschränkt möglich.

Für detaillierte Modellierungen und physikalisch fundierte Abschätzungen stehen ergänzend Messwerte zur diffusen und teilweise auch zur direkten Strahlung zur Verfügung – alle in der Einheit Watt pro Quadratmeter (W/m²). Diese ermöglichen eine differenziertere Betrachtung der lokalen Einstrahlungsverhältnisse.

### Bundesamt für Enegerie (BFE) - Elektrische Produktionsanlagen 
#### Datenquelle
Die Datengrundlage dieses Abschnitts basiert auf einem CSV-Datensatz, der über die Plattform opendata.swiss bezogen wurde. Dieser Datensatz wird vom Bundesamt für Energie (BFE) zur Verfügung gestellt und enthält Informationen zu elektrischen Produktionsanlagen in der Schweiz.

Für diese Analyse wurde die Datei gefiltert, sodass ausschliesslich Photovoltaikanlagen berücksichtigt wurden, deren Inbetriebnahmedatum zwischen dem 01.01.2015 und dem 31.12.2024 liegt. Die Datei enthält Angaben zur installierten Leistung (in kW), zum Standort (Kanton, Gemeinde), zur Kategorie der Anlage sowie zum Zeitpunkt der Inbetriebnahme.

<div class="float-right-image" style="width: 250px">
    <img src="assets/images/bfe_logo.png">
    <div class="image-label">https://www.iwf.ch/web-solutions/showcase/web-applikation-fuer-das-bundesamt-fuer-energie</div>
</div>

#### Datenqualität und Bereinigung
Die Daten basieren auf Einträgen im offiziellen Produktionsanlagenregister und gelten als konsistent sowie gut strukturiert. Da es sich um Primärdaten handelt, wurden sie nicht verändert oder ergänzt. Es fanden weder Aggregationen noch Schätzungen statt. Die Inbetriebnahmedaten erlauben zeitlich präzise Auswertungen pro Jahr, während die Standortinformationen eine regionale Analyse ermöglichen.

#### Messmethoden und Annahmen
Der Datensatz enthält Angaben zur installierten Leistung (in kW), zum Inbetriebnahmedatum sowie zu Standortangaben. Er enthält keine Informationen zur effektiven Stromproduktion, zu Einspeisewerten oder zu technischen Details wie Ausrichtung oder Verschattung. Die Analyse beschränkt sich entsprechend auf die zeitliche und geografische Verteilung der installierten PV-Leistung.

### Verband unabhängiger Energieerzeuger (VESE) - Einspeisevergütung
#### Datenquelle

<div class="float-right-image" style="width: 250px">
    <img src="assets/images/vese_logo.png">
    <div class="image-label">https://www.sses.ch/de/regional-und-fachgruppen/vese/</div>
</div>
Für die Analyse der wirtschaftlichen Rahmenbedingungen im Bereich der Solarenergie wurde ergänzend auf Daten des VESE – Verband unabhängiger Energieerzeuger zurückgegriffen. Der VESE ist eine Fachgruppe der Schweizerischen Vereinigung für Sonnenenergie (SSES) und unterstützt insbesondere Kleinproduzenten und Prosumenten bei regulatorischen, technischen und wirtschaftlichen Fragestellungen rund um die Stromproduktion aus erneuerbaren Energien.

Die von VESE bereitgestellten Daten beziehen sich auf die Einspeisevergütungen für Photovoltaik-Anlagen in der Schweiz. Die Vergütungen werden dabei pro Energieversorgungsunternehmen (EVU) und pro Jahr angegeben und ermöglichen eine präzise wirtschaftliche Analyse auf regionaler Ebene.

Der Zugang zu den vollständigen historischen Rohdaten wurde über eine API-Schnittstelle realisiert, welche durch eine individuelle Lizenzvereinbarung zur Verfügung gestellt wurde. Die API enthält Daten ab dem Jahr 2015 bis mindestens Anfang 2025. Alternativ wurde vom VESE auch ein Excel-Datensatz angeboten, der jedoch mit Kosten verbunden war (CHF 75 für akademische Nutzung), weshalb die API-Variante bevorzugt wurde.

#### Datenqualität und Bereinigung
#### Messmethoden und Annahmen
Die Einspeisevergütung wird von den Energieversorgern individuell festgelegt. VESE erhebt jährlich die Tarife und aggregiert diese nach Regionen und Netzbetreibern. Die gelieferten Daten geben daher einen realitätsnahen Überblick über die wirtschaftlichen Anreize für die Einspeisung von Solarstrom ins Netz. Da es sich bei den meisten Werten um gemeldete Durchschnittswerte handelt, können lokale Sondertarife, Eigenverbrauchsmodelle oder zeitlich gestaffelte Tarife in Einzelfällen abweichen.

Die Aggregation in der Analyse erfolgte auf Jahressicht. Monatliche oder saisonale Vergütungsschwankungen sind in den VESE-Daten nicht enthalten. Für die Einbindung in die Prognosemodelle wurde angenommen, dass sich die durchschnittliche Einspeisevergütung bei gleichbleibender regulatorischer Lage stabil entwickelt.

-----Monats oder Jahressicht, bitte klären!!!!!!----- (Notiz an mich selbst - Amel)

### Datenmodellierung
#### Ziel der Datenmodellierung
Die Datenmodellierung hatte zum Ziel, die verschiedenen Datenquellen dieser Fallstudie – MeteoSchweiz, Bundesamt für Energie (BFE) und der Verband VESE – in eine einheitliche Struktur zu überführen. Nur so war es möglich, die Daten sinnvoll miteinander zu verknüpfen, zu analysieren und Prognosen zu erstellen. Ein besonderer Fokus lag auf der zeitlichen und regionalen Vergleichbarkeit der Werte.

#### Vorgehen bei der Modellierung
Die Modellierung erfolgte auf Basis der bereits bereinigten Datensätze (siehe Kapitel "Datenqualität und Bereinigung"). Dabei wurden folgende Schritte durchgeführt:

- Standardisierung der Zeitdimension:
    Alle Datensätze wurden auf Monats- oder Jahreswerte aggregiert, abhängig von der Datenverfügbarkeit (z. B. MeteoSchweiz: monatlich, VESE: jährlich).

- Geografische Zuordnung:
    Die Daten wurden soweit möglich kantonal oder kommunal aufbereitet. Wetterstationen wurden Gemeinden bzw. Kantonen zugewiesen, Einspeisevergütungen den Netzbetreibern und damit ebenfalls geografischen Regionen.

- Einheitliche Formate und Einheiten:
    Die Werte wurden vereinheitlicht (z. B. kW → MW, CHF/kWh), um eine konsistente Darstellung in den Visualisierungen zu ermöglichen.

- Verknüpfung der Datenquellen:
    Die bereinigten und standardisierten Datensätze wurden in einem gemeinsamen Datenmodell zusammengeführt. Dies ermöglichte z. B. die Kombination von meteorologischen Daten mit installierter Solarleistung oder Einspeisevergütungen auf regionaler Ebene.

- Strukturierung für Prognosen:
    Für die Erstellung der Prognose wurde eine geeignete Datenbasis mit Zeitreihe aufgebaut, um diese später modellgestützt fortzuschreiben. Dabei wurden auch externe Faktoren wie Förderung oder Stromverbrauch berücksichtigt.

#### Tools und Umsetzung
Die technische Umsetzung der Modellierung erfolgte mit Python in einem Google-Colab-Notebook. Die Daten wurden überwiegend im CSV-Format verarbeitet und mit Pandas sowie weiteren Bibliotheken transformiert. Für die Visualisierung kamen Plotly und Matplotlib zum Einsatz. Die Prognose-Modelle befinden sich derzeit in Bearbeitung und werden im Kapitel „Prognosen und Szenarien“ dokumentiert.



