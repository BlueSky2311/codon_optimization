from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
# Start a new Chrome WebDriver session
#options = Options()
#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.3")
driver = webdriver.Chrome()
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# Open the CSV file
with open('C:/Users/darkh/Downloads/JCat_test.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Read the first DNA sequence in the CSV file
    row = next(reader)
    gene_name = row[1]  # The gene name is in the second column
    dna_sequence = row[5]  # The DNA sequence is in the sixth column

    # Navigate to the VectorBuilder website
    driver.get('https://en.vectorbuilder.com/tool/codon-optimization.html')

    # Wait until the div with the class 'seq-editor' is present on the page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.seq-editor')))

    # Find the CodeMirror div
    code_mirror = driver.find_element(By.CSS_SELECTOR, '.CodeMirror')

    # Use JavaScript to input text into the CodeMirror editor
    driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);", code_mirror, dna_sequence)

    # Use JavaScript to select the 'Protein sequence' radio button
    driver.execute_script("document.getElementById('radio2').checked = true;")

    # Get all option elements within the select element
    options = driver.find_elements(By.TAG_NAME, 'option')

    # Loop through all options
    for option in options:
        # If the option's text content is 'Escherichia coli str. K-12 substr. MG1655'
        if option.text.strip() == 'Escherichia coli str. K-12 substr. MG1655':
            # Select this option
            option.click()
            break

    # Find all checkboxes within elements with the class ‘checkbox long-list’ and check each one
    checkboxes = driver.find_elements(By.CSS_SELECTOR, '.checkbox.long-list input[type=checkbox]')
    for checkbox in checkboxes:
        # Scroll the checkbox into view
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)

        # Use JavaScript to click the checkbox
        driver.execute_script("arguments[0].click();", checkbox)

# Find the 'Submit' button using XPath and click it
driver.execute_script('document.querySelector(\'button[ng-click="submit()"]\').click();')

# Wait for the new page to load
#WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

# Now you should be on the new page
#print(driver.current_url)  # Prints the URL of the new page
time.sleep(20)
# Comment out the following line to prevent the browser from closing
# driver.quit()
