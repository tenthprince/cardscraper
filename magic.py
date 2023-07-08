import csv
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Path to the CSV file
csv_file_path = 'cardlist.csv'

# Create a CSV file to store the scraped data
csv_filename = 'card_prices.csv'

# Prepare CSV file header
csv_header = ['Card Name', 'Card Number', 'Rarity', 'Market Price', 'Foil Price']

# Create a list to store the scraped data
scraped_data = []

# Configure ChromeOptions
chrome_options = Options()
# Remove the --headless argument
chrome_options.add_argument("--headless")

# Path to your ChromeDriver executable
chrome_driver_path = 'C:/chromedriver/chromedriver.exe'

# Start the WebDriver
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# Set maximum wait time for locating elements
wait = WebDriverWait(driver, 20)

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        # Extract the URL from the row
        card_url = row[0]

        # Skip if the URL is empty
        if not card_url:
            continue

        # Load the card's page
        driver.get(card_url)

        # Perform any necessary actions to trigger JavaScript rendering
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the card name element to be present in the DOM
        card_name_element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "h1.product-details__name")))

        # Extract the card name
        card_name = card_name_element.text.strip()

        # Wait for the card details element to be present in the DOM
        card_details_element = wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "ul.product__item-details__attributes")))

        # Extract the card details
        card_details = card_details_element.text.strip()

        # Extract the card number
        card_number = ''
        card_number_match = re.search(r'#:(\w+)', card_details)
        if card_number_match:
            card_number = card_number_match.group(1)

        # Extract the rarity
        rarity = ''
        rarity_match = re.search(r'Rarity:\s*([A-Z]+)', card_details)
        if rarity_match:
            rarity = rarity_match.group(1)

        # Wait for the price elements to be present in the DOM
        price_elements = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "div.charts-price")))

        # Extract the regular price
        market_price = price_elements[0].text if price_elements else 'N/A'

        # Extract the foil price if available
        foil_price = price_elements[1].text if len(price_elements) > 1 else 'N/A'

        # Adjust the card_url
        adjusted_card_url = card_url.rsplit('/', 1)[0] + '/'

        # Add the adjusted_card_url to the scraped data list
        scraped_data.append([card_name, card_number, rarity, market_price, foil_price, adjusted_card_url])

# Quit the WebDriver
driver.quit()

# Save the scraped data in the CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_header)
    writer.writerows(scraped_data)

print(f"Scraped data saved in '{csv_filename}'")
