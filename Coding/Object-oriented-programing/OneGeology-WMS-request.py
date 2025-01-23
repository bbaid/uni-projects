# Този скрипт изпраща заявка към WMS сървър за получаване на карта и я визуализира с помощта на matplotlib.
# Също така изпраща заявка за GetCapabilities и записва отговора в XML файл.

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import xml.etree.ElementTree as ET

# Дефиниране на променливите
layer = 'GEBCO_LATEST_TID'  # Уверете се, че този слой съществува в документа за възможности
bbox = (-180.0, -90.0, 180.0, 90.0)  # Глобална ограничителна кутия
crs = "EPSG:4326"  # Система за координатни референции
width, height = 2*1024, 2*512  # Размери на изображението
format = "image/png"  # Формат на изображението

onegeology_wms_url = "https://wms.gebco.net/mapserv"

# Заявка GetMap
params = {
    'service': 'WMS',
    'version': '1.3.0',
    'request': 'GetMap',
    'layers': layer,
    'crs': crs,
    'bbox': f"{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]}",
    'width': width,
    'height': height,
    'format': format,
    'transparent': True
}

response = requests.get(onegeology_wms_url, params=params)

# Проверка дали заявката е успешна
if response.status_code == 200:
    try:
        # Отваряне на изображението от съдържанието на отговора
        image = Image.open(BytesIO(response.content))
        
        # Визуализиране на изображението с помощта на matplotlib
        plt.imshow(image)
        plt.axis('off')  # Скриване на оста
        plt.show()
    except Exception as e:
        print("Неуспешно отваряне на изображението")
        print("Грешка:", e)
else:
    print("Неуспешно получаване на изображението")
    print("Код на състоянието:", response.status_code)
    print("Текст на отговора:", response.text)

# Заявка GetCapabilities
capabilities_url = "https://wms.gebco.net/mapserv"
params = {
    'service': 'WMS',
    'version': '1.3.0',
    'request': 'GetCapabilities'
}

response = requests.get(capabilities_url, params=params)

# Проверка дали заявката е успешна
if response.status_code == 200:
    # Парсиране на XML отговора
    root = ET.fromstring(response.content)
    
    # Печатане на обобщение на XML структурата
    print("XML Обобщение:")
    for child in root:
        print(f"Таг: {child.tag}, Атрибути: {child.attrib}")
    
    # Записване на текста на отговора в файл
    with open('response.xml', 'w') as file:
        file.write(response.text)
else:
    print("Неуспешно получаване на възможностите")
    print("Код на състоянието:", response.status_code)
    print("Текст на отговора:", response.text)
