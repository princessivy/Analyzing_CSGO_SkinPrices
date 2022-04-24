# Analyzing CS:GO Skin-Prices
Ziel: Sammeln eines großen Datensatzes von Skin-Preisen. Anschließend sollten die Daten analysiert werden und Features gefunden werden, die die Preise der einzelnen Skins erklären.


### Übersicht der Files im Projekt
| File | Beschreibung |
| --- | --- |
| [CSGO_Crawler.py](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Crawler.py) | XX |
| [CSGO_Colorfulness.py](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Colorfulness.py) | XX |
| [CSGO_Analytics.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Analytics.ipynb) | XX |
  
    
      
        


### Benötigte Daten aus GoogleDrive
[Dieser Link](https://drive.google.com/drive/folders/1jo_B2uZqdP_QrxFDANSfYoqUNVIo9V4e?usp=sharing) führt zum GoogleDrive-Ordner, in welchem die benötigten Daten gespeichert sind.  
Darin befinden sich folgende Dateien:


| File | Beschreibung |
| --- | --- |
| [allitems.csv](https://drive.google.com/file/d/12HyWiR1LFt9Jpp1zG0RlbUeI-FhVsT4F/view?usp=sharing) | Originaldaten aus dem Scraping-Prozess (nachdem [CSGO_Crawler.py](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Crawler.py) durchgelaufen ist) |
| [allitems_w_colors.csv](https://drive.google.com/file/d/1-FDwI__Ci8fGxpFblqMqJw8hknOLNInT/view?usp=sharing) | Originaldaten [allitems.csv](https://drive.google.com/file/d/12HyWiR1LFt9Jpp1zG0RlbUeI-FhVsT4F/view?usp=sharing) mit Colorfulness-Feature angereichert (nachdem [CSGO_Colorfulness.py](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Colorfulness.py) durchgelaufen ist) |
| [allitems_cleaned_1.csvb](https://drive.google.com/file/d/1-FK57NE42ojNiG0hu5YXMC9iK-KmmZ0n/view?usp=sharing) | Daten bereinigt auf wichtige Features, NaN-Werte entfernt, Null-Werte entfernt (Speicherpunkt in [CSGO_Analytics.ipynb](https://github.com/princessivy/Analyzing_CSGO_SkinPrices/blob/main/CSGO_Analytics.ipynb) erkenntlich) |
