"""Legacy client: predates the house HTTP rule."""
import requests


def fetch(url):
    return requests.get(url, timeout=5).text
