from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

# create random email
def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

# create random phone
def random_phone():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]


# # load the web
# web = webdriver.Chrome()
# web.get("https://bawabtalsharq.com/register")
#
# # Define variables
# first_name = 'Mahmoud'
# last_name = 'test'
# country_code = 'Egypt'
# # phone = '01066607588'
# phone = random_phone()
# # email = 'mahmoudreda@test.com'
# email = (random_char(9)+"@test.com")
# password = 'test4808Aa$'
# password_confirmation = 'test4808Aa$'
# checkbox = True
#
# # wait 3 sec till the web reloads
# time.sleep(2)
#
# # Fill the form
# first = web.find_element(by=By.XPATH, value='//*[@id="first_name"]')
# first.send_keys(first_name)
#
# last = web.find_element(by=By.XPATH, value='//*[@id="last_name"]')
# last.send_keys(last_name)
#
# country = web.find_element(by=By.XPATH, value='//*[@id="country"]')
# country.send_keys(country_code)
#
# ph = web.find_element(by=By.XPATH, value='//*[@id="phone"]')
# ph.send_keys(phone)
#
# em = web.find_element(by=By.XPATH, value='//*[@id="email"]')
# em.send_keys(email)
#
# pas = web.find_element(by=By.XPATH, value='//*[@id="password"]')
# pas.send_keys(password)
#
# pas_con = web.find_element(by=By.XPATH, value='//*[@id="password-confirm"]')
# pas_con.send_keys(password_confirmation)
#
# check = web.find_element(by=By.XPATH, value='//*[@id="checkbox"]')
# check.click()
#
# submit = web.find_element(by=By.XPATH, value='//*[@id="app"]/main/div/div/div/div/div/div/div[1]/div[2]/div/form/div[7]/div/button')
# submit.click()
#
# confermation_text = web.find_element_by_css_selector('.swal-text')
# print(confermation_text)
# if (confermation_text == "Check your mail, to verify your account"):
#     print("Test was successful")
# else:
#     print("test was not successful")




# # load the web
# web = webdriver.Chrome()
# web.get("https://bawabtalsharq.com/contact-us")
#
# # Define variables
# phone = random_phone()
# email = (random_char(9)+"@test.com")
# subject = 'test'
# message = "kjbglhbly giug ihyglgbsav3546514 ^%$&^%(&)"
#
# time.sleep(1)
#
# # fill the form
# # find_element(by=By.XPATH, value=xpath)
# em = web.find_element(by=By.XPATH, value='/html/body/section/form/div/div/div/div[1]/div[2]/div[1]/input')
# em.send_keys(email)
#
# ph = web.find_element(by=By.XPATH, value='/html/body/section/form/div/div/div/div[1]/div[2]/div[2]/input')
# ph.send_keys(phone)
#
# sub = web.find_element(by=By.XPATH, value='/html/body/section/form/div/div/div/div[1]/div[2]/div[3]/input')
# sub.send_keys(subject)
#
# mes = web.find_element(by=By.XPATH, value='//*[@id="floatingTextarea"]')
# mes.send_keys(message)
#
# send = web.find_element(by=By.XPATH, value='/html/body/section/form/div/div/div/div[1]/div[2]/div[5]/button')
# send.click()
#
# # confermation_text = web.find_element_by_css_selector('.swal-text')
# # print(confermation_text)
# # if (confermation_text == " You mail has been sent successfully "):
# #     print("Test was successful")
# # else:
# #     print("test was not successful")



# load the web
web = webdriver.Chrome()
web.get("https://bawabtalsharq.com/login")

time.sleep(2)

# Define variables
email = 'mahmoud.reda@bawabtalsharq.com'
password = '0146064808'
search_input = 'fire alarm'

## fill the form
# fill email
web.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(email)

# fill password
web.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(password)

# press on login
web.find_element(by=By.XPATH, value='//*[@id="app"]/main/div/div/div/div/div/div/div[1]/div[2]/div/form/div[4]/div/button').click()

# type alarm in search bar
web.find_element(by=By.XPATH, value='//*[@id="myInput3"]').send_keys(search_input)

# click on search
web.find_element(by=By.XPATH, value='//*[@id="basic-addon2"]').click()

# click on the products
web.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div/div/a').click()

# click on request_now
web.find_element(by=By.XPATH, value='//*[@id="request_now"]').click()

# # load the web
# web = webdriver.Chrome()
# web.get("https://bawabtalsharq.com/products/fire-alarm")
#
# time.sleep(2)
# # webdriver.find_element(By.XPATH, '//*[@id="request_now"]').click()
# web.find_element(by=By.XPATH, value='//*[@id="request_now"]').click()
