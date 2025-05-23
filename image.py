import sys
import exifread

def extract_gps_info(image_path):
    # Ouvre le fichier image en mode lecture binaire
    with open(image_path, 'rb') as image_file:
        tags = exifread.process_file(image_file)

    # Extraction des données GPS
    gps_latitude = tags.get('GPS GPSLatitude')
    gps_latitude_ref = tags.get('GPS GPSLatitudeRef')
    gps_longitude = tags.get('GPS GPSLongitude')
    gps_longitude_ref = tags.get('GPS GPSLongitudeRef')

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = convert_to_degrees(gps_latitude, str(gps_latitude_ref))
        lon = convert_to_degrees(gps_longitude, str(gps_longitude_ref))
        return lat, lon
    else:
        return None, None

def convert_to_degrees(value, ref):
    # Convertit les coordonnées GPS en degrés décimaux
    d, m, s = [float(x.num) / float(x.den) for x in value.values]
    decimal = d + (m / 60.0) + (s / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def extract_steganography(image_path):
    with open(image_path, 'rb') as ImageFile:
        content = ImageFile.read()
        start_marker = b"-----BEGIN PGP PUBLIC KEY BLOCK-----"
        end_marker = b"-----END PGP PUBLIC KEY BLOCK-----"
        start_offset = content.find(start_marker)
        end_offset = content.find(end_marker, start_offset)
        
        if start_offset != -1 and end_offset != -1:
            pgp_key_block = content[start_offset:end_offset+len(end_marker)].decode('utf-8', errors='ignore')
            return pgp_key_block
        else:
            return "No PGP key found"

def main():
    if len(sys.argv) < 3:
        print("Usage:\n$> image -map image.jpeg\n$> image -steg image.jpeg")
        sys.exit(1)

    command = sys.argv[1]
    image_path = sys.argv[2]

    if command == "-map":
        print(f"Extracting GPS info from {image_path}...")
        lat, lon = extract_gps_info(image_path)
        if lat is not None and lon is not None:
            print(f"Lat/Lon:\t({lat}) / ({lon})")
        else:
            print("No GPS data found in the image.")

    elif command == "-steg":
        print(f"Attempting to extract hidden message from {image_path}...")
        hidden_message = extract_steganography(image_path)
        print(hidden_message)

    else:
        print("Invalid command. Use -map for GPS extraction or -steg for steganography extraction.")

if __name__ == "__main__":
    main()
