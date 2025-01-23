import matplotlib.pyplot as plt
from owslib.wms import WebMapService
from PIL import Image
from io import BytesIO

# URL за достъп до WMS услугата
wms_url = "http://mapsref.brgm.fr/wxs/1GG/CGMW_Bedrock_and_Structural_Geology"

# Свързване с WMS услугата (уточняване на версията 1.3.0)
wms = WebMapService(wms_url, version="1.3.0")

# Извеждане на наличните слоеве от услугата
print("Налични слоеве:")
for layer_name, layer_info in wms.contents.items():
    print(f"Слой: {layer_name} - Заглавие: {layer_info.title}")

# Избиране на слой за визуализация (например, "World_CGMW_50M_Geology")
selected_layer = "World_CGMW_50M_Geology"

# Определяне на рамките (bounding box) и координатната референтна система (CRS)
# Забележка: При WMS 1.3.0 редът на bbox е (MinLon, MinLat, MaxLon, MaxLat)
bbox = (-180, -90, 180, 90)  # Глобални граници на картата
crs = "EPSG:4326"  # Координатна референтна система

# Уточняване на размерите на изображението и неговия формат
width, height = 1024, 512  # Размери в пиксели
format = "image/png"  # Формат на изображението

try:
    # Изпращане на заявка за изображение към WMS услугата
    response = wms.getmap(
        layers=[selected_layer],  # Избраният слой за визуализация
        srs=crs,  # Координатна референтна система
        bbox=bbox,  # Рамки на картата
        width=width,  # Ширина на изображението
        height=height,  # Височина на изображението
        format=format,  # Формат на изображението
        transparent=True  # Прозрачност на слоя (ако е поддържано)
    )

    # Проверка дали има получени данни от услугата
    if response:
        # Зареждане на изображението с помощта на PIL
        image = Image.open(BytesIO(response.read()))

        # Визуализация на картата с matplotlib
        plt.figure(figsize=(12, 6))
        plt.imshow(image)
        plt.axis("off")  # Скриване на координатните оси
        plt.title(f"Визуализация на карта: {selected_layer}")  # Заглавие на картата
        plt.show()
    else:
        print("Не беше получен отговор от WMS услугата.")
except Exception as e:
    # Обработване на грешки при заявката
    print(f"Възникна грешка при извличане на картата: {e}")
