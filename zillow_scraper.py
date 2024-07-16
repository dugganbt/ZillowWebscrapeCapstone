import requests
from bs4 import BeautifulSoup

"""
    Function to scrape zillow listings of a zillow clone, as they change frequently. 
    Uses BeautifulSoup to extract links, prices and addresses of each listing.
    Returns the data as a tuple of (addresses, prices, links).
"""

def scrape_zillow_listings():

    content = requests.get(f"https://appbrewery.github.io/Zillow-Clone/")

    soup = BeautifulSoup(content.text, "html.parser")

    # find listing container
    listing_containers = soup.find_all(class_="StyledPropertyCardDataWrapper")

    listing_links = []
    listing_prices = []
    listing_addresses = []

    # iterate over containers
    for container in listing_containers:
        try: # other containers not containing the id and class will cause an error

            # retrieve relevant data
            link = container.find('a', class_='StyledPropertyCardDataArea-anchor')['href']
            price = container.find('span', class_='PropertyCardWrapper__StyledPriceLine').get_text().split('+')[0].split('/')[0]
            address = container.find('address').get_text().split("\n")[1].replace('|', '').strip()

            # add relevant data to list
            listing_links.append(link)
            listing_prices.append(price)
            listing_addresses.append(address)

        except AttributeError:
            continue

    return (listing_addresses,listing_prices,listing_links)



