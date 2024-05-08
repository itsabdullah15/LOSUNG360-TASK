# Web Scraping Amazon Product Details (LOSUNG360-TASK)

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
