# Analyzing CS:GO Skin-Prices
Ziel: Sammeln eines großen Datensatzes von Skin-Preisen mittels automatisiertem Crawler. Anschließende Analyse der Daten und Signifikanzbewertung der Features, welche in ein Machine-Learning-Modell zur Preisvorhersage übergeben werden.


### Übersicht der Files im Projekt
| File | Beschreibung |
| --- | --- |
| [CSGO_Crawler.py](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/Scraping%20Code/CSGO_Colorfulness.py) | Dieser Code wurd genutzt, um die Daten aus [Skinport](https://skinport.com) zu extrahieren - der Output des Codes ist in der Datei [allitems.csv](https://drive.google.com/file/d/12HyWiR1LFt9Jpp1zG0RlbUeI-FhVsT4F/view?usp=sharing) einsehbar; Achtung: für [allitems.csv](https://drive.google.com/file/d/12HyWiR1LFt9Jpp1zG0RlbUeI-FhVsT4F/view?usp=sharing) wurden nur die richtigen Skins gecrawled. In der py-Datei befindet sich allerdings auch der Code, um alle anderen Items zu crawlen (ist in der Datei selbest beschrieben) - Ausführung des Codes: Beginn am 26.03.2022 um 11:58 Uhr, Ende am 27.03.2022 um 15:01 Uhr |
| [CSGO_Colorfulness.py](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/Scraping%20Code/CSGO_Crawler.py) | Dieser Code wurde genutzt, um die gesammelten Daten mit dem Feature 'colorfulness' anzureichern - der Output des Codes ist in der Datei [allitems_w_colors.csv](https://drive.google.com/file/d/1-FDwI__Ci8fGxpFblqMqJw8hknOLNInT/view?usp=sharing) einsehbar - Ausführung des Codes: Beginn am 13.04.2022 um 9:29 Uhr, Ende am 14.04.2022 um 13:21 Uhr |
| [CSGO_Analytics.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Analytics.ipynb) | Säuberung der Daten und EDA |
| [CSGO_Significance_Testing.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Significance_Testing.ipynb) | Testen der Features auf Signifikanz, inklusive Ergebnistabelle |
| [CSGO_ML_Model.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_ML_Model.ipynb) | XGBoost-Modell zur Vorhersage der Skin-Preise, inklusive Ergebnistabelle |
    


### Benötigte Daten aus GoogleDrive
[Dieser Link](https://drive.google.com/drive/folders/1jo_B2uZqdP_QrxFDANSfYoqUNVIo9V4e?usp=sharing) führt zum GoogleDrive-Ordner, in welchem die benötigten Daten gespeichert sind.  
Darin befinden sich folgenden Dateien:


| File | Beschreibung |
| --- | --- |
| [allitems.csv](https://drive.google.com/file/d/12HyWiR1LFt9Jpp1zG0RlbUeI-FhVsT4F/view?usp=sharing) | Originaldaten aus dem Scraping-Prozess (nachdem [CSGO_Crawler.py](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/Scraping%20Code/CSGO_Colorfulness.py) durchgelaufen ist) |
| [allitems_w_colors.csv](https://drive.google.com/file/d/1-FDwI__Ci8fGxpFblqMqJw8hknOLNInT/view?usp=sharing) | Originaldaten [allitems.csv](https://drive.google.com/file/d/12HyWiR1LFt9Jpp1zG0RlbUeI-FhVsT4F/view?usp=sharing) mit Colorfulness-Feature angereichert (nachdem [CSGO_Colorfulness.py](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/Scraping%20Code/CSGO_Crawler.py) durchgelaufen ist) |
| [allitems_cleaned_1.csv](https://drive.google.com/file/d/1-FK57NE42ojNiG0hu5YXMC9iK-KmmZ0n/view?usp=sharing) | Speicherpunkt in [CSGO_Analytics.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Analytics.ipynb) |
| [allitems_cleaned_2.csv](https://drive.google.com/file/d/1-vpY-5cmxMPvWPRxAltUTCsEc6Fx4xk4/view?usp=sharing) | Speicherpunkt in [CSGO_Analytics.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Analytics.ipynb) |
| [allitems_cleaned_3.csv](https://drive.google.com/file/d/1-SWB6TU-BrlI_0QcO8L7OOzGEdgc962F/view?usp=sharing) | Speicherpunkt in [CSGO_Analytics.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Analytics.ipynb) |
| [allitems_ready_for_model.csv](https://drive.google.com/file/d/1-nygFv0YkZV9kbxF1PI2rjEMykERkI2z/view?usp=sharing) | Entstanden aus [CSGO_Significance_Testing.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Significance_Testing.ipynb) und verwendet in [CSGO_ML_Model.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_ML_Model.ipynb) |

