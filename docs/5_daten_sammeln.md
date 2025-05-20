## Daten sammeln

Für die Entwicklung einer fundierten Markteintrittsstrategie der **AmFaAn Energy AG** ist eine belastbare Datenbasis entscheidend. In dieser Arbeit wurden meteorologische, technische und wirtschaftliche Daten erhoben, um regionale Potenziale für Photovoltaik (PV) in der Schweiz zu identifizieren. Die Daten dienen dazu, strategische Entscheidungen der AmFaAn Energy AG – wie etwa Standortwahl, Zielregionen oder Produktausrichtung – datenbasiert vorzubereiten.

Im Folgenden werden die genutzten Datenquellen, deren Qualität und Aufbereitung sowie die Datenmodellierung beschrieben. Die daraus abgeleiteten Kennzahlen bilden die Grundlage für alle nachfolgenden Analysen, Prognosen und Geschäftsempfehlungen.

Eine fundierte Analyse der Solarenergie in der Schweiz basiert auf vielfältigen Datenquellen. Für diese Fallstudie wurden meteorologische, technische und wirtschaftliche Daten erhoben. Für die Analyse des Solarpotenzials in der Schweiz wurden umfassende Datensätze aus offiziellen Quellen zusammengetragen und aufbereitet. Die wichtigsten Daten stammen vom Bundesamt für Energie (BFE) und MeteoSchweiz. Das BFE liefert detaillierte Informationen zur installierten Solarleistung, der Anzahl an Photovoltaikanlagen, sowie zu Subventionen und Förderprogrammen. Diese Daten ermöglichen eine genaue Untersuchung der Entwicklung der Solarenergie in der Schweiz über die letzten zehn Jahre und helfen dabei, wirtschaftliche und politische Einflussfaktoren zu bewerten.

Neben den wirtschaftlichen und technischen Aspekten ist die Sonneneinstrahlung der entscheidende Faktor für die Effizienz und Leistungsfähigkeit von Solaranlagen. Um diesen Einfluss zu quantifizieren, wurden die Daten von MeteoSchweiz herangezogen. Sie enthalten Messwerte zur Globalstrahlung, den täglichen Sonnenstunden und den Temperaturen an verschiedenen Wetterstationen in der Schweiz. Diese Parameter sind essenziell, um den Zusammenhang zwischen Sonnenenergie und Stromproduktion zu analysieren. Darüber hinaus erlauben sie eine saisonale Betrachtung, da die Solarleistung im Sommer deutlich höher ist als in den Wintermonaten.

Die Kombination dieser umfangreichen Datensätze bildet die Grundlage für die Untersuchung der Vergangenheit und ermöglicht es, Prognosen für die zukünftige Entwicklung der Solarenergie in der Schweiz abzuleiten.

### MeteoSchweiz – Sonnenstunden je Wetterstation

#### Datenquelle

Die meteorologischen Daten stammen von MeteoSchweiz und wurden über die Plattform IDAWeb bezogen. Die Datengrundlage basiert auf einem Netz von 132 automatisierten Wetterstationen, die flächendeckend in der ganzen Schweiz verteilt sind. Eine Ausnahme bildet der Kanton Appenzell Ausserrhoden (AR), in dem derzeit keine Wetterstation betrieben wird.

Für die vorliegende Analyse wurde der Zeitraum vom 01.01.2015 bis zum 31.12.2024 ausgewertet. In IDAWeb wurde gezielt nach dem Parameter «Sonnenstunden» gefiltert. Zusätzlich wurde ein Stationsfilter angewendet, um ausschliesslich Wetterstationen innerhalb der Schweiz auszuwählen.

Der Zugriff auf die Daten erforderte eine offizielle Registrierung bei MeteoSchweiz. Zu diesem Zweck wurde ein entsprechendes Formular unterzeichnet und eingereicht. Die Daten dürfen ausschliesslich für Lehre und Forschung verwendet werden.

<div class="float-right-image" style="width: 250px">
    <img src="assets/images/meteoschweiz_logo.png">
    <div class="image-label">https://x.com/meteoschweiz</div>
</div>

#### Datenqualität und Bereinigung

Die Messdaten von MeteoSchweiz gelten als sehr zuverlässig. Zwischen 2020 und 2023 wurden alle relevanten Wetterstationen auf direkte Messung der Sonnenscheindauer umgerüstet. Seit August 2023 liegen daher ausschliesslich gemessene Daten vor. Frühere Werte basieren teilweise auf Modellrechnungen.

Lückenhafte Messwerte (z. B. durch Ausfälle oder Wartungen) wurden durch Näherungswerte anderer Stationen im selben Kanton ersetzt (2'561 von 15'960 Datensätzen betroffen – 16.05 %). Diese Näherungen wurden bei der Analyse entsprechend berücksichtigt.

Technische Schritte in der Datenaufbereitung:

- Zusammenführen von Wetterdaten und Stationsdaten
- Herausfiltern von Liechtenstein
- Umwandlung von Datums- und Zahlenformaten
- Gruppierung nach Zeit und Ort

#### Technische Herausforderung

Im Zuge der Analyse der Sonnenstunden-Daten von MeteoSchweiz traten mehrere technische Herausforderungen auf, die für die Datenqualität und die Vergleichbarkeit der Ergebnisse besonders relevant waren. Die Daten aus verschiedenen Quellen mussten zunächst miteinander verknüpft werden, um geografische und topografische Analysen zu ermöglichen. Dabei wurden nur Stationen innerhalb der Schweiz berücksichtigt, Stationen aus Liechtenstein wurden konsequent ausgeschlossen.

Zudem mussten die Zeitangaben vereinheitlicht, numerische Formate bereinigt und die Daten auf Monats- und Jahresebene aggregiert werden.


#### Messmethoden und Annahmen

Sonnenstunden werden bei MeteoSchweiz registriert, sobald die Globalstrahlung über 200 W/m² liegt – ein im internationalen Vergleich hoher Schwellenwert. Das beeinflusst die Vergleichbarkeit mit anderen Ländern.

Zudem erfolgt die Messung horizontal, während PV-Anlagen geneigt montiert sind. Daher sind die Werte für Planungszwecke nur bedingt direkt übertragbar.

---

### Bundesamt für Energie (BFE) – Elektrische Produktionsanlagen

#### Datenquelle

Die Daten des Bundesamts für Energie wurden via [opendata.swiss](https://www.iwf.ch/web-solutions/showcase/web-applikation-fuer-das-bundesamt-fuer-energie) bezogen. Für die Analyse wurden ausschliesslich Photovoltaikanlagen berücksichtigt, die zwischen dem 01.01.2015 und dem 31.12.2024 in Betrieb genommen wurden.

Enthalten sind:

- Inbetriebnahmedatum
- Installierte Leistung (kW)
- Standortdaten (Gemeinde, Kanton)
- Anlagentyp

<div class="float-right-image" style="width: 250px">
    <img src="assets/images/bfe_logo.png">
    <div class="image-label">https://www.iwf.ch/web-solutions/showcase/web-applikation-fuer-das-bundesamt-fuer-energie</div>
</div>

#### Datenqualität und Bereinigung

Die Daten gelten als strukturiert, vollständig und konsistent. Alle Angaben stammen aus offiziellen Registern. Aggregationen oder Schätzungen wurden nicht vorgenommen.

#### Technische Herausforderungen bei der Visualisierung

- Die GeoJSON-Datei zur Gemeindedarstellung war veraltet und musste vereinfacht werden.
- BFS-Nummern waren in den Geo-Daten, aber nicht in den PV-Daten enthalten.
- Die Zuordnung der PLZ zu BFS-Nummern erfolgte über historische Gemeindedaten (AMTOVZ_CSV_WGS84.csv).
- 33 Gemeinden konnten nicht eindeutig zugeordnet werden – hier wurden Standardwerte verwendet.

---

### Verband unabhängiger Energieerzeuger (VESE) – Einspeisevergütungen

#### Datenquelle

Die VESE-Daten enthalten Angaben zu Einspeisetarifen pro Energieversorgungsunternehmen und Jahr. Diese Informationen wurden über eine API bezogen, die gegen Lizenzvereinbarung zur Verfügung gestellt wurde.

Alternativ stand eine Excel-Version zur Verfügung (CHF 75, akademische Nutzung), jedoch wurde aus Effizienzgründen die API-Variante verwendet.

<div class="float-right-image" style="width: 250px">
    <img src="assets/images/vese_logo.png">
    <div class="image-label">https://www.sses.ch/de/regional-und-fachgruppen/vese/</div>
</div>

#### Datenqualität und Bereinigung

Die Einspeisevergütungen gelten als realitätsnah und wurden direkt von den EVUs gemeldet. Es handelt sich um Durchschnittswerte je Jahr und Netzregion. Lokale Spezialtarife oder zeitlich gestaffelte Modelle sind nicht explizit enthalten.

#### Technische Herausforderungen bei der Visualisierung
Über die API mussten zuerst die Liste der Elektrizitätswerke geholt werden und dann die entsprechenden Gemeinde-Ergebnisse. Bei beiden API-Anfragen gab es viele Unterbrüche, Timeouts und sonstige Fehler. Daher musste ein Retry-Mechanismus eingebaut werden, damit alle Daten abgeholt werden konnten. Ausserdem war die Performance ein Thema, da es viele Daten über die entsprechenden Jahre bei den Gemeinde-Ergebnissen waren.

Für die Auswertungen mussten dann wieder die beiden CSV-Dateien zusammengebracht werden und mit zusätzlichen Gemeindedaten auch wieder fähig für eine Kartendarstellung gemacht werden.

#### Messmethoden und Annahmen

- Aggregation auf **Jahresbasis**
- Annahme: **Vergütung bleibt bei stabiler Gesetzeslage konstant**
- Keine monatliche oder saisonale Granularität verfügbar

---

### Bundesamt für Statistik – Endenergieverbrauch nach Verbrauchergruppen

#### Datenquelle

Die Daten zum Endenergieverbrauch stammen vom Bundesamt für Statistik (BFS) und wurden über das Online-Portal STAT-TAB bezogen. Die Grundlage der Auswertung bildet die jährlich erhobene Energiestatistik, welche detaillierte Informationen über den Energieverbrauch in der Schweiz nach Sektoren und Energieträgern bereitstellt. Erfasst werden unter anderem die Verbrauchsdaten für Haushalte, Industrie, Dienstleistungen sowie Verkehr.
Für die vorliegende Analyse wurde der Zeitraum vom 01.01.2014 bis zum 31.12.2023 berücksichtigt. Die Datenabfrage erfolgte über die Tabelle "Endenergieverbrauch nach Verbrauchergruppe und Energieträger". Zur Erhöhung der Vergleichbarkeit wurden ausschliesslich nationale Werte (Schweiz total) verwendet, ohne kantonale oder regionale Aufschlüsselung.
Die Nutzung der Daten ist gemäss den Nutzungsbedingungen des BFS für wissenschaftliche, journalistische oder bildungsbezogene Zwecke gestattet. Eine separate Registrierung war für den Zugriff auf die STAT-TAB-Plattform nicht erforderlich.
https://www.bfs.admin.ch/bfs/de/home/statistiken/energie.html

<div class="float-right-image" style="width: 250px">
    <img src="assets/images/BFS.png">
    <div class="image-label">[https://www.gastrofacts.ch/einkaufsguide/bundesamt-fuer-statistik-bfs]</div>
</div>

#### Datenqualität und Bereinigung

Die vom BFS veröffentlichten Verbrauchszahlen basieren auf einer Kombination von Meldedaten (z. B. durch Energieversorger), Modellschätzungen sowie Hochrechnungen. Die Methodik wird jährlich überprüft und publiziert. Insbesondere in den Bereichen Haushalt und Verkehr erfolgen regelmässige Anpassungen der Berechnungsmodelle, z. B. durch neue Mobilitätserhebungen oder die Verfeinerung des Energieverbrauchs nach Gebäudetypen.
Für die Analyse wurden Datensätze mit vollständigen Jahreswerten ausgewählt. In Einzelfällen auftretende Inkonsistenzen (z. B. durch rückwirkende Korrekturen in den Vorjahren) wurden durch Rückvergleiche mit der Energiestatistik des Bundesamts für Energie (BFE) abgeglichen. Insgesamt waren 312 von 6'820 Datensätzen betroffen (4.57 %).
Technische Schritte in der Datenaufbereitung:
Download der Datentabelle im CSV-Format via STAT-TAB
Harmonisierung von Datumsformaten und Energieeinheiten (GWh)
Aggregation nach Verbrauchergruppen (Haushalte, Verkehr, Industrie, Dienstleistungen)
Validierung gegen BFE-Daten (Konsistenzprüfung)

#### Messmethoden und Annahmen

Die Zuordnung des Energieverbrauchs erfolgt nach dem sogenannten Endenergieprinzip, bei dem ausschliesslich die beim Endnutzer ankommende Energie berücksichtigt wird – ohne vorgelagerte Umwandlungsverluste. Die Erhebung unterscheidet zudem nach fossilen (z. B. Heizöl, Erdgas) und erneuerbaren Energieträgern (z. B. Holz, Fernwärme, Elektrizität aus Wasserkraft).
Zu beachten ist, dass die Daten keine Aussagen zur Energieeffizienz oder zu sektorübergreifenden Verlagerungen erlauben. Vielmehr bieten sie eine quantitative Grundlage zur Beobachtung langfristiger Verbrauchstrends und sektoraler Entwicklungen.

## Technische Herausforderungen

Im Verlauf der Datenanalyse und -aufbereitung für diese Fallstudie traten zahlreiche technische Herausforderungen auf. Diese betrafen insbesondere die **Datenvollständigkeit**, das **Matching zwischen verschiedenen Datensätzen**, die **Standardisierung von Formaten** sowie die **Performanceprobleme beim Zugriff auf externe Schnittstellen** (z. B. APIs). 

Die in der folgenden Matrix dargestellten Probleme wurden im Bericht jeweils einzeln an den passenden Stellen thematisiert. Um die Komplexität und den investierten Aufwand jedoch **auf einen Blick nachvollziehbar darzustellen**, wurde diese Übersichtsmatrix erstellt.

Sie bietet einen kompakten, strukturierten Überblick über die identifizierten Schwierigkeiten und die jeweils implementierten Lösungen. Ziel war es, eine **hohe Datenqualität** sicherzustellen und eine **vergleichbare, konsistente Analysebasis** für sämtliche Visualisierungen, Regressionsmodelle und Prognosen im Rahmen der Fallstudie zu gewährleisten.

### Matrix technischer Herausforderungen bei der Datenaufbereitung

| **Datenquelle**            | **Herausforderung**                                                                                       | **Beschreibung / Kontext**                                                                                                                                             | **Lösung / Massnahme**                                                                                           |
|---------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| MeteoSchweiz (IDAWeb)     | Registrierung und Datenzugang                                                                             | Zugang zu IDAWeb nur nach Registrierung und schriftlicher Genehmigung (Nutzungszweck: Lehre/Forschung) erforderlich.                                                   | Offizielles Formular ausgefüllt, Anmeldung abgeschlossen, Zugang erfolgreich eingerichtet.                      |
| MeteoSchweiz              | Fehlende Stationsdaten für 2024                                                                            | Zwei Stationen in der Stammdatenliste (meteo_swiss_stn_data.csv) hatten 2024 keine Messwerte.                                                                          | Stationen wurden manuell mit 0 Sonnenstunden ergänzt, um Vollständigkeit (132 Stationen) sicherzustellen.      |
| MeteoSchweiz              | Uneinheitliche Zeitformate                                                                                 | Datumsangaben lagen teils im Format YYYYMMDD oder als Text vor.                                                                                                        | Standardisierung der Zeitformate in datetime-Objekte mit Python/Pandas.                                        |
| MeteoSchweiz              | Ungleiche Granularität und Monatsverteilung                                                                | Monatsdaten mussten für Auswertungen nach Jahr und Höhenmeter aufbereitet und gruppiert werden.                                                                        | Gruppierung nach Jahr und Höhenlage mit `groupby()` durchgeführt.                                               |
| MeteoSchweiz              | Ausfälle und Lücken in Zeitreihen                                                                          | Rund 16 % der Datensätze wiesen Lücken auf – v. a. durch Wartungen oder Ausfälle.                                                                                      | Näherungswerte aus Stationen desselben Kantons verwendet, mit Markierung als Näherung.                         |
| MeteoSchweiz              | Datenqualität vor August 2023 nur teilweise gemessen                                                      | Bis August 2023 teilweise modellbasierte Sonnenstunden, danach ausschliesslich Messdaten.                                                                               | Transparente Dokumentation im Kapitel „Datenqualität“; Berücksichtigung in Analyse und Diskussion.              |
| MeteoSchweiz              | Herausfiltern nicht-schweizerischer Stationen (z. B. Liechtenstein)                                       | Die Rohdaten enthielten auch Stationen ausserhalb der Schweiz.                                                                                                         | Filter auf `CH`-basierte Stations-ID gesetzt.                                                                  |
| MeteoSchweiz              | Stationsdaten fehlten teils Höhenmeter                                                                    | Für Höhenkategorisierung waren vollständige Höhenangaben notwendig.                                                                                                    | Fehlende Höhenangaben ergänzt bzw. mit externen Quellen angereichert.                                          |
| MeteoSchweiz              | Unterschiedliche Dezimaltrennzeichen                                                                       | Teilweise wurden Kommas statt Punkte verwendet.                                                                                                                        | Einheitliche Umwandlung in `float`-Typen mit Punkt als Dezimaltrennzeichen.                                    |
| MeteoSchweiz              | Messung horizontal vs. PV-Ausrichtung                                                                      | Sonnenstunden werden horizontal gemessen, PV-Anlagen sind geneigt.                                                                                                     | Hinweis in „Messmethoden und Annahmen“ – Werte nur bedingt direkt nutzbar für PV-Planung.                      |
| BFE – PV-Anlagen          | Unvollständige oder doppelte Gemeindenamen                                                                 | Teilweise uneinheitliche Schreibweise (z. B. „St. Gallen“ vs. „St.Gallen“).                                                                                             | Normalisierung über manuelle Korrekturtabelle und Abgleich mit BFS-Daten.                                      |
| BFE – PV-Anlagen          | Fehlende BFS-Nummern für Geomatching                                                                       | CSV-Dateien der PV-Anlagen enthielten keine BFS-Nr., nur PLZ oder Gemeindenamen.                                                                                       | Matching mit externer Datei (AMTOVZ_CSV_WGS84.csv), Zuordnung auf Gemeindeebene mit BFS.                        |
| BFE – PV-Anlagen          | Zu alte oder komplexe GeoJSON-Datei                                                                        | Die GeoJSON-Datei zur Gemeindedarstellung war zu detailliert und führte zu langen Ladezeiten.                                                                          | Vereinfachung mit TopoJSON-Konvertierung und Reduktion der Punktanzahl.                                        |
| VESE – Einspeisevergütung | Instabile API-Verbindung                                                                                   | Abrufe über API schlugen häufig fehl (Timeouts, Connection Errors).                                                                                                    | Retry-Mechanismus mit Wartezeiten implementiert.                                                               |
| VESE – Einspeisevergütung | Zwei-stufiger API-Abruf                                                                                     | Zuerst EVU-Daten abrufen, danach je Gemeinde die Vergütungen – führte zu vielen Requests.                                                                              | Schleifen mit Progressbar und Pausen programmiert, um Serverlast zu minimieren.                                |
| VESE – Einspeisevergütung | Geomatching mit Gemeinden                                                                                  | Rückgabe nur über Gemeindebezeichnungen, teils mit historischen Namen.                                                                                                 | Umrechnung in aktuelle BFS-Nr. mithilfe historischer Zuordnungstabellen.                                        |
| BFS – Endenergieverbrauch | Formatierung von CSV-Dateien                                                                               | CSV-Dateien mussten harmonisiert und aus unterschiedlichen Quellen zusammengeführt werden.                                                                             | Standardisierung mit Python/Pandas: Datumsformate, Spaltennamen und Energiewerte auf GWh normiert.             |
| BFS – Endenergieverbrauch | Vergleichbarkeit mit BFE-Daten                                                                             | Teilweise Abweichungen in Summen und Jahreswerten.                                                                                                                     | Validierung gegen BFE-Daten, bei Differenzen Referenzwerte priorisiert.                                        |
| Sonnendach.ch             | Zugriff auf Originaldaten (> 5 GB) zu aufwendig                                                            | GeoPackage-Dateien waren technisch nicht verarbeitbar in Google Colab oder lokalen Notebooks.                                                                          | Rückgriff auf aggregierte Webdaten von sonnendach.ch mit Angabe der Limitierung.                              |
| Allgemein (alle Quellen)  | Mehrere Datenformate (CSV, JSON, GeoJSON, Excel)                                                           | Unterschiedliche Dateitypen erschwerten den einheitlichen Analyseprozess.                                                                                              | Einheitliche Verarbeitung in Pandas, Konvertierung in CSV als Zwischenformat.                                  |
| Allgemein (alle Quellen)  | Einheitliche Zeitachsen über alle Quellen hinweg                                                           | Unterschiedliche Zeitgranularität: Tages-, Monats-, Jahreswerte.                                                                                                       | Aggregation und Normalisierung auf Monatsbasis als Analyseeinheit.                                             |
| Allgemein (alle Quellen)  | Verknüpfung technischer, meteorologischer und wirtschaftlicher Daten                                       | Unterschiedliche Datenstrukturen und Zuordnungen (z. B. Ort, PLZ, EVU, Gemeinde, Kanton).                                                                               | Erstellung eines konsistenten Datenmodells mit eindeutiger geografischer Hierarchie.                           |



## Datenmodellierung

### Ziel der Datenmodellierung

Die verschiedenen Datenquellen wurden entsprechend aufbereitet, kombiniert und ergänzt, um:

- Regionen mit hohem Solarpotenzial zu identifizieren
- wirtschaftliche, technische und klimatische Faktoren zu verknüpfen
- Prognosen bis 2030 zu ermöglichen (z. B. bei PV-Ausbau oder Stromproduktion)

### Vorgehen bei der Modellierung

- **Zeitliche Standardisierung:** Monats- oder Jahreswerte je nach Quelle
- **Geografische Verknüpfung:** Wetterstationen → Gemeinden → Kantone / EVUs → Netzregionen
- **Einheitskonvertierung:** z. B. kW → MW, CHF/kWh
- **Datenzusammenführung:** meteorologische, technische und wirtschaftliche Daten
- **Prognosefähigkeit:** Aufbau einer Zeitreihe für zukünftige Modellierungen

### Tools und Umsetzung

- **Python (Google Colab)** für Bereinigung, Analyse und Visualisierung
- **Pandas** für Datenmanipulation, **Plotly** und **Matplotlib** für Grafiken
- Datenspeicherung primär im **CSV-Format**, vereinzelt GeoJSON (Gemeinden)

Die Prognosemodelle werden im Kapitel „Prognosen und Szenarien“ näher beschrieben.
