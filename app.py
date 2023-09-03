
import re


def urlchkk(n):
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ipv4_addresses = re.findall(ipv4_pattern, text)
    for address in ipv4_addresses:
        return (address)
    