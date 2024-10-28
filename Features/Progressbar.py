from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (Ensure chromedriver is in your PATH)
driver = webdriver.Chrome()

# Open the target page
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-download-progress-demo")

# Maximize browser window (optional)
driver.maximize_window()

# Start the download by clicking the button
start_button = driver.find_element(By.XPATH, "//button[normalize-space()='Start Download']")
start_button.click()


# Wait until the progress bar reaches 100%
try:
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.XPATH, "//p[@class='counter']"), "100%")
    )
    print("Progress bar reached 100%!")
except Exception as e:
    print(f"Error: {e}")

# Close the browser after the operation
driver.quit()