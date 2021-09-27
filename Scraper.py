import requests
import connector
from bs4 import BeautifulSoup
x=input("Enter The Number Of Pages You Want To Script: ")
dbname=input("Enter The Name Of The Name Of The database: ")
url="https://www.oyorooms.com/hotels-in-kolkata/?page="+x
connector.connect(dbname)
req=requests.get(url)
content=req.content
soup=BeautifulSoup(content, "html.parser")
all_hotels=soup.find_all("div", {"class": "hotelCardListing"})
scraped_info_list=[]
for hotel in all_hotels:
    hotel_dict={}
    hotel_dict["name"]=hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
    hotel_dict["address"]=hotel.find("span", {"itemprop": "streetAddress"}).text
    hotel_dict["price"]=hotel.find("span", {"class": "listingPrice__finalPrice"}).text
    try:
        hotel_dict["rating"]=hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
    except AttributeError:
        pass
    parent_amenities_element=hotel.find("div", {"class": "amenityWrapper"})
    amenities_list=[]
    for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
        amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
    hotel_dict["ammenities"]=', '.join(amenities_list[:-1])
    scraped_info_list.append(hotel_dict)
    connector.insert_into_table(dbname,tuple(hotel_dict.values()))
connector.get_hotel_info(dbname)
