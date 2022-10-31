from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

PATH = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

#login and create

driver.find_element(By.CLASS_NAME, "login").click()

driver.find_element(By.ID, "email_create").send_keys("test_email7@test_email.com")

driver.find_element(By.ID, "SubmitCreate").click()

time.sleep(6)

#personal information fields

radio1 = driver.find_element(By.ID, "id_gender1")
radio1.click()

driver.find_element(By.ID, "customer_firstname").send_keys("Test")

driver.find_element(By.ID, "customer_lastname").send_keys("User")

driver.find_element(By.ID, "email").click()

driver.find_element(By.ID, "passwd").send_keys("password")


days_selection = Select(driver.find_element(By.ID, "days"))
days_selection.select_by_index(2)

months_selection = Select(driver.find_element(By.ID, "months"))
months_selection.select_by_value("3")

years_selection = Select(driver.find_element(By.ID, "years"))
years_selection.select_by_value("1990")

driver.find_element(By.ID, "newsletter").click()

driver.find_element(By.ID, "optin").click()



#address fields


driver.find_element(By.ID, "firstname").click()

driver.find_element(By.ID, "lastname").click()

driver.find_element(By.ID, "company").send_keys("TestCompany")

driver.find_element(By.ID, "address1").send_keys("Test street, No234, PO Box None")

driver.find_element(By.ID, "address2").send_keys("Ap #56, Floor 7, Building 3SE")

driver.find_element(By.ID, "city").send_keys("Testing")

state_selection = Select(driver.find_element(By.ID, "id_state"))
state_selection.select_by_value("2")

driver.find_element(By.ID, "postcode").send_keys("25487")

driver.find_element(By.ID, "other").send_keys("None required")

driver.find_element(By.ID, "phone").send_keys("+400000000")

driver.find_element(By.ID, "phone_mobile").send_keys("+407000444")

driver.find_element(By.ID, "alias").clear()
driver.find_element(By.ID, "alias").send_keys("Not for now")

driver.find_element(By.ID, "submitAccount").click()


#my account section

driver.find_element(By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[3]/a/span').click()

#check if the addresses tab exists and print result
if(len(driver.find_elements(By.XPATH, '//*[@id="center_column"]/div[1]/div/div')) > 0):
    print("Addresses tab exists")
else:
    print("Addresses tab does not exists")

driver.find_element(By.CLASS_NAME, "logout").click()

time.sleep(2)
driver.quit()