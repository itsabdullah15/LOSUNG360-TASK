# Web Scraping Amazon Product Details (LOSUNG360-TASK)

# About Task

This project involves scraping data using the `Playwright library`, a powerful tool for browser automation. The code includes comprehensive `error handling` to handle various exceptions that may arise during the scraping process.

Additionally, the project utilizes concurrency in Python through asyncio and aiohttp. Concurrency allows multiple tasks to be executed concurrently, improving performance and efficiency. By leveraging asyncio and aiohttp, the code can perform asynchronous HTTP requests, enabling faster data retrieval and processing.


# Prerequisites

- Python 3.x installed on your system
- Asynchronous libraries installed:
  - asyncio
  - aiohttp
- Pandas library installed (`pip install pandas`)
- Playwright library installed (`pip install playwright`)
- Additional dependencies:
  - `constant.py` containing constants like `FILE_PATH`, `OUTPUT_FILE_PATH`,`ORIGINAL_PRICE_XPATH`, `DISCOUNT_PRICE_XPATH`, `PRODUCT_PRICE_XPATH`, `ASIN_REGEX` and `PRODUCT_NAME_REGEX`.
  - `get_data.py` containing functions for extracting data like `ASIN`, `product_name`, `original_price`, `discounted_price`, `product_rating`.
- The output data is saved in `Output.csv` file.