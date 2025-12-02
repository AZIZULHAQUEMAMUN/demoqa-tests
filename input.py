from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait, Select 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains 
from webdriver_manager.chrome import ChromeDriverManager 
import time 
import os
 
def setup_driver(): 
    service = Service(ChromeDriverManager().install()) 
    driver = webdriver.Chrome(service=service) 
    driver.maximize_window() 
    return driver 
 
 
def fill_text_inputs(driver): 
    driver.get("https://demoqa.com/text-box") 
    time.sleep(1) 
    name_text = driver.find_element(By.ID, "userName") 
    name_text.send_keys("Azizur Rahman") 
    time.sleep(1) 
    email_text = driver.find_element(By.ID, "userEmail") 
    email_text.send_keys("ontor@example.com") 
    time.sleep(1) 
    driver.find_element(By.ID, "currentAddress").send_keys("Dhaka, Bangladesh") 
    time.sleep(1) 
    address = driver.find_element(By.ID, "permanentAddress") 
    address.send_keys("Dhaka, Bangladesh") 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    driver.find_element(By.ID, "submit").click() 
    time.sleep(1) 
 
    output_name = driver.find_element(By.ID, "name").text 
    assert "Azizur Rahman" in output_name, "Name not found in output" 
    print(" Text input filled and submitted.") 
 
 
def handle_radio(driver): 
    # Radio Button 
    driver.get("https://demoqa.com/radio-button") 
    time.sleep(2) 
    radio_btn = driver.find_element(By.XPATH, "//*[@for='yesRadio']") 
    radio_btn.click() 
    output = driver.find_element(By.XPATH, "//span[@class='text-success']").text 
    assert output == "Yes", "Radio button selection failed" 
    print(" Radio button selected.") 
    time.sleep(1) 
 
 
def handle_checkbox(driver): 
    # Checkbox 
    driver.get("https://demoqa.com/checkbox") 
    time.sleep(1) 
    checkbox = driver.find_element(By.XPATH, "//input[@id='tree-node-home']/parent::label") 
    checkbox.click() 
    time.sleep(1) 
    result = driver.find_element(By.ID, "result").text 
    assert "desktop" in result.lower(), "Checkbox selection failed" 
    time.sleep(1) 
    print(" Checkbox selected.") 
 
 
def handle_buttons(driver): 
    driver.get("https://demoqa.com/buttons") 
    time.sleep(1) 
    action = ActionChains(driver) #ActionChains is a Selenium utility that allows you to perform advanced user interactions 
 
    double_btn = driver.find_element(By.ID, "doubleClickBtn") 
    right_btn = driver.find_element(By.ID, "rightClickBtn") 
 
    time.sleep(1) 
    action.double_click(double_btn).perform() 
    time.sleep(1) 
    action.context_click(right_btn).perform() 
 
    dbl_msg = driver.find_element(By.ID, "doubleClickMessage").text 
    rgt_msg = driver.find_element(By.ID, "rightClickMessage").text 
 
    assert "double click" in dbl_msg, " Double click failed" 
    assert "right click" in rgt_msg, " Right click failed" 
    time.sleep(1) 
 
    print(" Double-click and right-click handled.") 
 
 
def hover_action(driver): 
    driver.get("https://demoqa.com/tool-tips") 
    time.sleep(1) 
    hover_btn = driver.find_element(By.ID, "toolTipButton") 
    action = ActionChains(driver) #ActionChains is a Selenium utility that allows you to perform advanced user interactions 
    action.move_to_element(hover_btn).perform() 
    time.sleep(1) 
    print(" Mouse hover performed successfully.") 
 
 
def upload_file(driver): 
    driver.get("https://demoqa.com/upload-download") 
    file_input = driver.find_element(By.ID, "uploadFile") 
    time.sleep(1) 
    file_input.send_keys(__file__) 
    uploaded_path = driver.find_element(By.ID, "uploadedFilePath").text 
    # assert uploaded_path.endswith("web_interactions.py"), " File not uploaded" 
    # Fixed assertion to match current filename
    assert uploaded_path.endswith("input.py"), f" File not uploaded: {uploaded_path}"
    # Uploads this script file itself 
    print(" File uploaded.") 
 
 
def handle_simple_alert(driver): 
    driver.get("https://demoqa.com/alerts") 
    alert_btn = driver.find_element(By.ID, "alertButton") 
    alert_btn.click() 
    time.sleep(1) 
    WebDriverWait(driver, 5).until(EC.alert_is_present()) 
    alert = driver.switch_to.alert 
    assert "You clicked a button" in alert.text, "Alert not found" 
    alert.accept() 
    print("Simple alert handled.") 
 
 
def handle_timed_alert(driver): 
    driver.get("https://demoqa.com/alerts") 
    alert_btn = driver.find_element(By.ID, "timerAlertButton") 
    alert_btn.click() 
    WebDriverWait(driver,10).until(EC.alert_is_present()) 
    alert = driver.switch_to.alert 
    assert "This alert appeared after 5 seconds" in alert.text 
    time.sleep(1) 
    alert.accept() 
    print("Timed alert handled.") 
 
 
def check_color_change(driver): 
    driver.get("https://demoqa.com/dynamic-properties") 
 
    # Get color before change 
    color_btn = driver.find_element(By.ID, "colorChange") 
    initial_class = color_btn.get_attribute("class") 
 
    time.sleep(6)  # Wait more than 5s for the change to happen 
    updated_class = color_btn.get_attribute("class") 
 
    assert initial_class != updated_class, "Button color did not change." 
    print("'Color Change' button") 
 
 
 
def navigation_example(driver): 
    driver.get("https://demoqa.com") 
    time.sleep(2)  #for better visibility for student 
    driver.get("https://demoqa.com/text-box") 
 
 
    time.sleep(1)   #for better visibility for student 
    driver.back() 
    assert driver.current_url == "https://demoqa.com/", driver.current_url+" is the current url" 
    print(driver.current_url) 
    time.sleep(2)   #for better visibility for student 
 
 
    driver.forward() 
    print(driver.current_url) 
    assert driver.current_url == "https://demoqa.com/text-box", driver.current_url+" is the current url" 
    time.sleep(2)   #for better visibility for student 
 
 
    driver.refresh() 
    print(driver.current_url) 
    time.sleep(2)   #for better visibility for student 
    assert driver.current_url == "https://demoqa.com/text-box", driver.current_url+" is the current url" 
    print(" Browser navigation complete.") 
 
 
 
def take_screenshot(driver): 
    driver.get("https://demoqa.com") 
    driver.save_screenshot("full_page_demoqa.png") 
    print(" Screenshot saved as 'full_page_demoqa.png'") 
 
 
 
 
# =================== Date picker ================================ 
def select_date(driver): 
    driver.get("https://demoqa.com/date-picker") 
    date_input = driver.find_element(By.ID, "datePickerMonthYearInput") 
    date_input.click() 
 
    # Select month 
    month_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")) 
    month_dropdown.select_by_visible_text("May") 
 
    # Select year 
    year_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")) 
    year_dropdown.select_by_visible_text("2025") 
 
    time.sleep(3) 
 
    # Select day 
    day_xpath = "//div[text()='11']" 
    day_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, day_xpath))) 
    day_element.click() 
 
    # Assertion 
    selected_date = date_input.get_attribute("value") 
    assert selected_date == "05/11/2025", f"Date not selected properly: {selected_date}" 
    print(" Date selected: ", selected_date) 

def main(): 
    driver = setup_driver() 
    try: 
        fill_text_inputs(driver) 
        handle_radio(driver) 
        handle_checkbox(driver) 
        handle_buttons(driver) 
        hover_action(driver) 
        handle_simple_alert(driver) 
        handle_timed_alert(driver) 
        check_color_change(driver) 
        navigation_example(driver) 
        take_screenshot(driver) 
        select_date(driver) 
        print("All tests completed successfully.") 
    finally: 
        time.sleep(2) 
        driver.quit() 
        print("Browser closed.") 

if __name__ == "__main__": 
    main()
