import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Define the variables
layer = 'example_layer'
longitude = 90.0
latitude = 90.0
map_scale = 90.0
img_size = 1024

gebco_wms_url = "https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv"

params = {
    'service': 'WMS', 
    'version': '1.3.0',
    'request': 'GetMap',
    'layers': layer,
    'crs': 'EPSG:4326',
    'bbox': f"{longitude - map_scale},{latitude - map_scale},{longitude + map_scale},{latitude + map_scale}",
    'width': img_size,
    'height': img_size,
    'format': 'image/png'
}

response = requests.get(gebco_wms_url, params=params)

print("content type:", response.headers['Content-Type'])
print("content length:", response.content[:100])

capabilities_url = "https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv"
params = {
    'service': 'WMS',
    'version': '1.3.0',
    'request': 'GetCapabilities'
}

response = requests.get(capabilities_url, params=params)
with open('response.xml', 'w') as file:
    file.write(response.text)

exit()
# Check if the request was successful
if response.status_code == 200:
    # Open the image from the response content
    image = Image.open(BytesIO(response.content))
    
    # Display the image using matplotlib
    plt.imshow(image)
    plt.axis('off')  # Hide the axis
    plt.show()
else:
    print("Failed to retrieve the image")