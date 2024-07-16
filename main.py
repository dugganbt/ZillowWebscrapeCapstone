from zillow_scraper import scrape_zillow_listings
from data_logger import DataLogger
import time

addresses, prices, links = scrape_zillow_listings()


for address, price, link in zip(addresses, prices, links):
    data_logger = DataLogger()
    data_logger.input_data(data=(address,price,link))
    time.sleep(2)


