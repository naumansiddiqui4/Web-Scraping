from bs4 import BeautifulSoup
import requests
import urllib #urllib is a package that collects several modules for working with URLs
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
name = input("Enter the keyword:")

def get_source(url):
    try:
        session = HTMLSession() #used to initialize the GET request
        response = session.get(url) #gets the response from the URL
        return response
    except requests.exceptions.RequestException as e:
        print(e)
def scrape_google(keyword):
    keyword = urllib.parse.quote_plus(keyword) #removes special characters and converts the spaces in the keyword with '+' sign as well
    response = get_source("https://www.google.co.uk/search?q=" + keyword)
    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')
    for url in links:
        if url.startswith(google_domains):
            links.remove(url)
    return links
print(scrape_google(name)+ '\n')