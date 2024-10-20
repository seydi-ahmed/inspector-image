from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Load the image
image_path = "/image.jpeg"
image = Image.open(image_path)

# Extract EXIF data
exif_data = image._getexif() if image._getexif() else {}

# Function to parse and display EXIF data including GPS info
def extract_gps_info(exif_data):
    gps_info = {}
    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        if decoded == "GPSInfo":
            for t in value:
                sub_decoded = GPSTAGS.get(t, t)
                gps_info[sub_decoded] = value[t]
    return gps_info

# Function to convert GPS data to degrees
def convert_to_degrees(value):
    d, m, s = value
    return d + (m / 60.0) + (s / 3600.0)

# Extract GPS information
gps_data = extract_gps_info(exif_data)
lat = lon = None

if "GPSLatitude" in gps_data and "GPSLatitudeRef" in gps_data:
    lat = convert_to_degrees(gps_data["GPSLatitude"])
    if gps_data["GPSLatitudeRef"] != "N":
        lat = -lat

if "GPSLongitude" in gps_data and "GPSLongitudeRef" in gps_data:
    lon = convert_to_degrees(gps_data["GPSLongitude"])
    if gps_data["GPSLongitudeRef"] != "E":
        lon = -lon

(lat, lon, gps_data)
