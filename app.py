
import re
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
# import distance

def ipSearch(text):
    pattern = r'client-ip=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    match = re.search(pattern, text)
    
    if match:
        client_ip = match.group(1)
        return printDetails(client_ip)
    else:
        return "None"

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    return (f"IP Address: {res.ip_address} \n" + f"Location: {res.city}, {res.region}, {res.country} \n" + f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")

