import asyncio
import aiohttp
import random
import pandas as pd
from playwright.async_api import async_playwright
from constant import FILE_PATH,OUTPUT_FILE_PATH
from get_data import ASIN,product_name, original_price, discounted_price, product_rating
import csv


df = pd.read_csv(FILE_PATH) #Reading CSV FILE USING PANDAS
extracted_urls = df['URL'] # Extract URLs from the DataFrame

async def open_urls(extracted_urls):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        async with aiohttp.ClientSession() as session:
            tasks = [process_url(url, browser, session) for url in extracted_urls]
            await asyncio.gather(*tasks)


async def process_url(url, browser, session):
    page = await browser.new_page()
    await page.set_viewport_size({"width": 1920, "height": 1080}) #set browser viewport size
    await page.goto(url) #opening browser
    await asyncio.sleep(random.uniform(2, 5))
    try:
        await extract_product_info(page, url, session)
    except Exception as e:
        print(f"Error processing {url}: {e}")
    finally:
        await page.close() #Closing browser

async def extract_product_info(page, url, session):
    #Calling Function to extract the information
    Amazon_Standard_Identification_Number = await ASIN(page, url)
    PRODUCT_NAME = await product_name(page, url)
    ORIGINAL_PRICE = await original_price(page)
    DISCOUNTED_PRICE = await discounted_price(page)
    PRODUCT_RATING = await product_rating(page)

    print(f'The ASIN is {Amazon_Standard_Identification_Number}')
    print(f'The PRODUCT NAME is {PRODUCT_NAME}')
    print(f'The ORIGINAL PRICE is {ORIGINAL_PRICE}')
    print(f'The DISCOUNTED PRICE is {DISCOUNTED_PRICE}')
    print(f'The PRODUCT RATING is {PRODUCT_RATING}')


     # Write data to CSV file
    with open(OUTPUT_FILE_PATH, 'a', newline='') as csvfile:
        fieldnames = ['URL', 'ASIN', 'PRODUCT_NAME', 'ORIGINAL_PRICE', 'DISCOUNTED_PRICE', 'PRODUCT_RATING']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write headers if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Fill None values with "None" before writing to CSV
        data_to_write = {
            'URL': url,
            'ASIN': Amazon_Standard_Identification_Number if Amazon_Standard_Identification_Number is not None else "None",
            'PRODUCT_NAME': PRODUCT_NAME if PRODUCT_NAME is not None else "None",
            'ORIGINAL_PRICE': ORIGINAL_PRICE if ORIGINAL_PRICE is not None else "None",
            'DISCOUNTED_PRICE': DISCOUNTED_PRICE if DISCOUNTED_PRICE is not None else "None",
            'PRODUCT_RATING': PRODUCT_RATING if PRODUCT_RATING is not None else "None"
        }
        
        writer.writerow(data_to_write)

asyncio.run(open_urls(extracted_urls))
