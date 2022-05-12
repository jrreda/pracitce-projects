from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # import KEYS
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import random
import string

# create random email
def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

# create random phone
def random_phone():
    n = '00000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]


# Define variables
name = 'test'
country = 'Egypt'
# phone = '01066607588'
phone = random_phone()
email = 'mahmoudredabs@gmail.com'
# email = (random_char(9)+"@test.com")
password = 'Pa$$w0rd!'
checkbox = True
image_path = os.getcwd()+"/messi.jpeg"
test_string = "test test test testttt 2131 ST."
website = "https://www.test.com"


### Register
# load the driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://bawabtalsharq.com/vendor/register")

time.sleep(2)           # wait 3 sec till the driver reloads

##### Fill the form
### 1st step - Company Details
# first name
driver.find_element(by=By.XPATH, value='//*[@id="first_name"]').send_keys(name)
# last name
driver.find_element(by=By.XPATH, value='//*[@id="last_name"]').send_keys(name)
# password
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(password)
# password confirm
driver.find_element(by=By.XPATH, value='//*[@id="password_confirmation"]').send_keys(password)
# upload image
driver.find_element(by=By.XPATH, value='//*[@id="file-upload"]').send_keys(image_path)
# Owner name
driver.find_element(by=By.NAME, value='owner_name').send_keys(name)
# Company name
driver.find_element(by=By.NAME, value='name_en').send_keys(name)
# country
driver.find_element(by=By.XPATH, value='//*[@id="country"]/option[4]').click()
# Company phone
driver.find_element(by=By.NAME, value='phone').send_keys(phone)
# Company email
driver.find_element(by=By.NAME, value='email').send_keys(email)
# Company Addres
driver.find_element(by=By.NAME, value='address_en').send_keys(test_string)
# Company Insudtry
driver.find_element(by=By.NAME, value='company_field').send_keys(test_string)
# Official website
driver.find_element(by=By.NAME, value='website').send_keys(website)
# Commercial Registration No.
driver.find_element(by=By.NAME, value='commercial_registration').send_keys(test_string)
# Tax Id
driver.find_element(by=By.NAME, value='tax_id').send_keys(test_string)
# Press next
time.sleep(2)           # wait 3 sec till the driver reloads
next = driver.find_element(by=By.XPATH, value='//*[@id="pills-home"]/div[2]/div[2]/a')
driver.execute_script("arguments[0].click();", next)

### 2nd Step - Other Details
# Number of products
driver.find_element(by=By.NAME, value='num_products').send_keys(564651)
# Average Production Capacity
driver.find_element(by=By.NAME, value='average_production').send_keys(2545156)
# Certifications
time.sleep(2)                               # driver.implicitly_wait(2)
iframe_cert = driver.find_element(by=By.ID, value='certificates_ifr')
driver.switch_to.frame(iframe_cert)        # switch to iframe
text_area_cert = driver.find_element(by=By.XPATH, value='//*[@id="tinymce"]')
text_area_cert.clear()                     # clear the text area
text_area_cert.send_keys(test_string)
text_area_cert.send_keys(Keys.ENTER)
text_area_cert.send_keys(test_string)
driver.switch_to.default_content()          # return to original iframe
time.sleep(2)                               # driver.implicitly_wait(2)
# About Company
iframe_about = driver.find_element(by=By.ID, value='description_en_ifr')
driver.switch_to.frame(iframe_about)        # switch to iframe
text_area_about = driver.find_element(by=By.XPATH, value='//*[@id="tinymce"]')
text_area_about.clear()                     # clear the text area
text_area_about.send_keys(test_string)
text_area_about.send_keys(Keys.ENTER)
text_area_about.send_keys(test_string)
driver.switch_to.default_content()          # return to original iframe
time.sleep(2)                               # driver.implicitly_wait(2)
# submit
# driver.find_element(by=By.XPATH, value='//*[@id="beVendorSubmitBtn"]').click()
submit = driver.find_element(by=By.XPATH, value='//*[@id="beVendorSubmitBtn"]')
driver.execute_script("arguments[0].click();", submit)

## press OK on the pop-up
# driver.find_element(by=By.CLASS_NAME, value='swal-button--confirm').click()
# submit = driver.find_element(by=By.CLASS_NAME, value='swal-button--confirm')
# driver.execute_script("arguments[0].click();", submit)
