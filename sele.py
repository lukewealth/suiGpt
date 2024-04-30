import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a browser session
driver = webdriver.Chrome()  # Or specify the path to your WebDriver executable

# Navigate to the webpage
driver.get("https://github.com/Ovodo/pool/blob/main/jackpot.move")

try:
    # Wait for the dynamic content to load (if necessary)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "read-only-cursor-text-area")))

    # Find the element with the dynamic content
    dynamic_content_element = driver.find_element(By.ID, "read-only-cursor-text-area")

    # Extract the text content
    text_content = dynamic_content_element.text.split("#[test_only]")[0]
    

    # Serialize the text content into a dictionary
    content_dict = {"messages":[{"role":"assistant","content": text_content}]}

    # Convert the dictionary to a JSON string with pretty formatting
    # json_string = json.dumps(content_dict, indent=4)

    # Print the JSON string
    print(content_dict)
finally:
    # Close the browser session
    driver.quit()
