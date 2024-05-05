import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a browser session
driver = webdriver.Chrome()  # Or specify the path to your WebDriver executable

# Navigate to the webpage
driver.get("https://github.com/Ovodo/pool/blob/main/sources/liquidity_pool.move")

try:
    # Wait for the dynamic content to load (if necessary)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "read-only-cursor-text-area")))

    # Find the element with the dynamic content
    dynamic_content_element = driver.find_element(By.ID, "read-only-cursor-text-area")

    # Extract the text content
    text_content = dynamic_content_element.text.split("// Tests - ")[0]
    

    # Serialize the text content into a dictionary
    content_dict = {"messages":[{"role": "system", "content": "SuiAI is a chat agent that’s proficient in the Move smart contract language"}, {"role": "user", "content": "Create a smart contract module for a DEX (Decentralized exchange) on the Sui blockchain."},{"role":"assistant","content": text_content}]}

    # Convert the dictionary to a JSON string with pretty formatting
    # json_string = json.dumps(content_dict, indent=4)

    # Print the JSON string
    print(content_dict)
finally:
    # Close the browser session
    driver.quit()
