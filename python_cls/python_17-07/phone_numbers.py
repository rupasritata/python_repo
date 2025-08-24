import phonenumbers
import requests
from geopy.geocoders import Nominatim
from phonenumbers import geocoder
import folium

# Function to get approximate location info from phone number using phonenumbers
def get_phone_region(phone_number_str):
    number = phonenumbers.parse(phone_number_str, None)
    region = phonenumbers.region_code_for_number(number)  # Country code, e.g. 'IN' for India
    location_desc = phonenumbers.geocoder.description_for_number(number, 'en')  # Generic location name
    return region, location_desc

# Function to get coordinates (latitude, longitude) from a location description
def get_coordinates(location_desc):
    geolocator = Nominatim(user_agent="phone_locater")
    location = geolocator.geocode(location_desc)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# Alternatively, you can use Numverify API for more precise data (requires API key)
def get_numverify_location(phone_number_str, access_key):
    url = f"http://apilayer.net/api/validate?access_key={access_key}&number={phone_number_str}"
    response = requests.get(url)
    data = response.json()
    if data['valid']:
        return data['location'], data['country_code']
    else:
        return None, None

# Example Phone Numbers (Use E.164 format preferably)
phone1 = "+919876543210"  # Example Indian number
phone2 = "+14155552671"   # Example US number

# Step 1: Get region and description using phonenumbers
region1, desc1 = get_phone_region(phone1)
region2, desc2 = get_phone_region(phone2)

print(f"Phone 1 region: {region1}, location description: {desc1}")
print(f"Phone 2 region: {region2}, location description: {desc2}")

# Step 2: Get coordinates of the location description
coord1 = get_coordinates(desc1)
coord2 = get_coordinates(desc2)

print(f"Phone 1 approximate coordinates: {coord1}")
print(f"Phone 2 approximate coordinates: {coord2}")

# Step 3: Map visualisation (if both coordinates found)
if coord1 and coord2:
    folium_map = folium.Map(location=coord1, zoom_start=4)
    
    folium.Marker(coord1, popup=f"Phone 1: {desc1}", icon=folium.Icon(color='green')).add_to(folium_map)
    folium.Marker(coord2, popup=f"Phone 2: {desc2}", icon=folium.Icon(color='red')).add_to(folium_map)
    
    folium.PolyLine([coord1, coord2], color="blue", weight=2.5, opacity=1).add_to(folium_map)
    
    folium_map.save("phone_to_phone_map.html")
    print("Map saved as phone_to_phone_map.html")
else:
    print("Could not find coordinates for one or both phone numbers.")
