import pandas as pd
import requests
from pathlib import Path
from PIL import Image
import requests
import cv2
import numpy as np


data = pd.read_csv("allitems.csv")

data['colorfulness'] = ''

# Quelle für Algorithmus nach Hasler & Süsstrunk 2003: https://pyimagesearch.com/2017/06/05/computing-image-colorfulness-with-opencv-and-python/

def image_colorfulness(image):
	# das Bild in seine jeweiligen RGB-Komponenten aufteilen
	(B, G, R) = cv2.split(image.astype("float"))
	# berechnen rg = R - G
	rg = np.absolute(R - G)
	# berechnen yb = 0.5 * (R + G) - B
	yb = np.absolute(0.5 * (R + G) - B)
	# den Mittelwert und die Standardabweichung von "rg" und "yb" berechnen
	(rbMean, rbStd) = (np.mean(rg), np.std(rg))
	(ybMean, ybStd) = (np.mean(yb), np.std(yb))
	# den Mittelwert und die Standardabweichungen kombinieren
	stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
	meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))
	# die "Colorfulness"-Metrik ableiten und zurückgeben
	return stdRoot + (0.3 * meanRoot)


# Loop für alle Einträge im Datensatz, um Colorfulness zu berechnen
# wichtig hierbei: benötigtes Bild ist nicht Standardbild, welches unter "image" im Datensatz vorkommt. Hierfür wird customized Bild des Skins benötigt (zB auf welchem Sticker, Abnutzung etc. erkennbar ist).
# dies wird über die assetId erreicht, mit welcher ein Link aufgebaut wird, um mit diesen dann mittels Requests das Bild abzufragen.
for x in range(len(data)):
  url = "https://cdn.skinport.com/images/screenshots/" + str(data.assetId[x]) + "/playside_256x128.png"
  im = Image.open(requests.get(url, stream=True).raw)
  rgb_image = im.convert('RGB')
  pix = np.array(rgb_image)
  result = image_colorfulness(pix)
  data.colorfulness[x] = result
  print(x)
  print(result)

