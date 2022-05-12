# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # import KEYS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import random
import string
import connect_db

# Update mahmoudredabs@gmail.com in the db
# os.system('python file.py')
connect_db.update_mahmoudredabs()


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
first_name = 'Mahmoud'
last_name = 'test'
country = 'Egypt'
# phone = '01066607588'
phone = random_phone()
email = 'mahmoudredabs@gmail.com'
# email = (random_char(9)+"@test.com")
password = 'Pa$$w0rd!'
checkbox = True



### Register
# load the driver
driver = webdriver.Chrome()
driver.get("https://bawabtalsharq.com/register")

# wait 2 sec till the driver reloads
driver.implicitly_wait(3)

## Fill the form
# first name
driver.find_element(by=By.XPATH, value='//*[@id="first_name"]').send_keys(first_name)
# last name
driver.find_element(by=By.XPATH, value='//*[@id="last_name"]').send_keys(last_name)
# country
driver.find_element(by=By.XPATH, value='//*[@id="country"]').send_keys(country)
# phone
driver.find_element(by=By.XPATH, value='//*[@id="phone"]').send_keys(phone)
# email
driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(email)
# password
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(password)
# password confirm
driver.find_element(by=By.XPATH, value='//*[@id="password-confirm"]').send_keys(password)
# check
driver.find_element(by=By.XPATH, value='//*[@id="checkbox"]').click()
# submit
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div/div/div/div/div/div/div[1]/div[2]/div/form/div[7]/div/button').click()
try:
    # element_present = EC.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[3]/div/button')
    WebDriverWait(driver, 30).until(connect_db.verify_mail())
except TimeoutException:
    print("Timed out waiting for page to load")

## Press OK
driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[3]/div/button').click()


confermation_text = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]')
# print(confermation_text.text)
if (confermation_text.text == "Check your mail, to verify your account"):
    print("Register was successful")
else:
    print("Register was not successful")

#
# # load the driver
# driver = webdriver.Chrome()
# driver.get("https://bawabtalsharq.com/login")
#
# time.sleep(3) # wait
#
# # Define variables
# email = 'mahmoud.reda@bawabtalsharq.com'
# password = '0146064808'
# search_input = 'Fire alarm'
# phone = '01069907582'
# subject = 'test'
# message = "kjbglhbly giug ihyglgbsav3546514 ^%$&^%(&)"
# ### RFQ
# test_string = "test test test testttt"
# image_path = os.getcwd()+"/messi.jpeg"
# date = '02-06-2023'
#
#
# ## fill the form
# # fill email
# driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(email)
# # fill password
# driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(password)
# # press on login
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div/div/div/div/div/div/div[1]/div[2]/div/form/div[4]/div/button').click()
# time.sleep(3) # wait
#
# # confermation_text = driver.find_element(by=By.CSS_SELECTOR, value='body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-text')
# # print(confermation_text)
# # if (confermation_text == "Check your mail, to verify your account"):
# #     print("Login was successful")
# # else:
# #     print("Login was not successful")
#
# # #### Contact Us
# # driver.find_element(by=By.XPATH, value='//*[@id="header"]/div[2]/div/div/div[1]/div/ul/li[4]/a').click()
# #
# # ## fill the
# # # phone
# # driver.find_element(by=By.XPATH, value='/html/body/section/form/div/div/div/div[1]/div[2]/div[2]/input').send_keys(phone)
# # # subject
# # driver.find_element(by=By.XPATH, value='/html/body/section/form/div/div/div/div[1]/div[2]/div[3]/input').send_keys(subject)
# # # message
# # driver.find_element(by=By.XPATH, value='//*[@id="floatingTextarea"]').send_keys(message)
# # # click on send
# # driver.find_element(by=By.XPATH, value='/html/body/section/form/div/div/div/div[1]/div[2]/div[5]/button').click()
# # # click on OK
# # driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[3]/div/button').click()
#
# ### Search
# time.sleep(3) # wait
# # type alarm in search bar
# driver.find_element(by=By.XPATH, value='//*[@id="myInput3"]').send_keys(search_input)
# # click on search
# driver.find_element(by=By.XPATH, value='//*[@id="basic-addon2"]').click()
# # click on the products
# driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div/div/a').click()
#
# ##### RFQ
# time.sleep(3) # wait
# # click on request_now
# element = driver.find_element(by=By.CLASS_NAME, value='GTM-request-now')
# driver.execute_script("arguments[0].click();", element)
#
# ### 1st step
# time.sleep(3) # driver.implicitly_wait(10)
#
# # unit
# # driver.find_element(by=By.CLASS_NAME, value='select2-selection__rendered').click().send_keys(keys.ARROW_UP).send_keys(keys.ENTER)
# driver.find_element(by=By.XPATH, value='//*[@id="unit_id"]/option[2]').click()
# # Target Price
# driver.find_element(by=By.XPATH, value='//*[@id="target_price"]').send_keys(1561651)
# # sourcing purpose
# driver.find_element(by=By.XPATH, value='//*[@id="source_propose_id"]/option[2]').click()
# # Company Certificate
# driver.find_element(by=By.XPATH, value='//*[@id="companyCertificate"]').send_keys(test_string)
# # Product Certificate
# driver.find_element(by=By.XPATH, value='//*[@id="productCertificate"]').send_keys(test_string)
# ### Description
# ifr = driver.find_element(by=By.ID, value='details_ifr')
# driver.switch_to.frame(ifr)                 # switch to iframe
# text_area = driver.find_element(by=By.XPATH, value='//*[@id="tinymce"]')
# text_area.clear()                           # clear the text area
# time.sleep(3)                               # wait for 5 sec
# text_area.send_keys(test_string)
# text_area.send_keys(Keys.ENTER)
# text_area.send_keys(test_string)
# driver.switch_to.default_content()          # return to original iframe
# time.sleep(3)                               # driver.implicitly_wait(3)
# # Upload Image
# driver.find_element(by=By.XPATH, value='//*[@id="file-upload"]').send_keys(image_path)
# # Press next
# next = driver.find_element(by=By.XPATH, value='//*[@id="quickForm"]/div[1]/div[11]/button')
# driver.execute_script("arguments[0].click();", next)
#
#
# # ### 2nd step
# time.sleep(3)  # driver.implicitly_wait(10)
#
# # Country
# driver.find_element(by=By.XPATH, value='//*[@id="country_id"]/option[4]').click()
# # # Port destination
# driver.find_element(by=By.XPATH, value='//*[@id="port"]').send_keys(test_string)
# # # Payment Method
# driver.find_element(by=By.XPATH, value='//*[@id="payment_term_id"]/option[4]').click()
#
# # Trade Terms
# driver.find_element(by=By.XPATH, value='//*[@id="trade_term_id"]/option[4]').click()
# # Currency
# driver.find_element(by=By.XPATH, value='//*[@id="currency_id"]/option[4]').click()
# # Shipping Method
# driver.find_element(by=By.XPATH, value='//*[@id="shipping_method_id"]/option[4]').click()
# # Available Data
# driver.find_element(by=By.XPATH, value='//*[@id="endDate"]').send_keys(date)
# # Other Details
# time.sleep(3)                               # driver.implicitly_wait(3)
# iframe_other = driver.find_element(by=By.ID, value='other_requirements_ifr')
# driver.switch_to.frame(iframe_other)        # switch to iframe
# text_area_other = driver.find_element(by=By.XPATH, value='//*[@id="tinymce"]')
# text_area_other.clear()                     # clear the text area
# time.sleep(3)                               # driver.implicitly_wait(3)
# text_area_other.send_keys(test_string)
# text_area_other.send_keys(Keys.ENTER)
# text_area_other.send_keys(test_string)
# driver.switch_to.default_content()          # return to original iframe
# time.sleep(3)                               # driver.implicitly_wait(3)
# # # Press Submit
# # driver.find_element(by=By.XPATH, value='//*[@id="btnSubmit"]').click()
# submit_final_rfq = driver.find_element(by=By.XPATH, value='//*[@id="btnSubmit"]')
# driver.execute_script("arguments[0].click();", submit_final_rfq)
