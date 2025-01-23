import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import xml.etree.ElementTree as ET

# Define the variables
layer = 'GEBCO_LATEST'  # Ensure this layer exists in the capabilities document
longitude = 0.0
latitude = 0.0
map_scale = 1.0
img_size = 256

gebco_wms_url = "https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv"

# GetMap request
params = {
    'service': 'WMS', 
    'version': '1.3.0',
    'request': 'GetMap',
    'layers': layer,
    'crs': 'EPSG:4326',  # Ensure this CRS is supported
    'bbox': f"{longitude - map_scale},{latitude - map_scale},{longitude + map_scale},{latitude + map_scale}",
    'width': img_size,
    'height': img_size,
    'format': 'image/png'
}

response = requests.get(gebco_wms_url, params=params)

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
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

# GetCapabilities request
capabilities_url = "https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv"
params = {
    'service': 'WMS',
    'version': '1.3.0',
    'request': 'GetCapabilities'
}

response = requests.get(capabilities_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML response
    root = ET.fromstring(response.content)
    
    # Print a summary of the XML structure
    print("XML Summary:")
    for child in root:
        print(f"Tag: {child.tag}, Attributes: {child.attrib}")
    
    # Save the response text to a file
    with open('response.xml', 'w') as file:
        file.write(response.text)
else:
    print("Failed to retrieve the capabilities")
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)