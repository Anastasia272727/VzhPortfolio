from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from faker import Faker
import random
fake = Faker(['ru_RU'])
link = "https://automationexercise.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
Email = fake.email()
Name = fake.first_name()
Password = 1
random_days = random.randint(1, 31)
random_years = random.randint(1900, 2021)
LastName = fake.last_name()
FirstName = fake.first_name()
Address = fake.address()
City = fake.city()
State = fake.region()
Zipcode = fake.postcode()
Mobile_number = fake.phone_number()
signup = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
signup = browser.find_element(By.CSS_SELECTOR, "input[type*=text]").send_keys(Name)
signup = browser.find_element(By.CSS_SELECTOR, "input[data-qa*=signup-email]").send_keys(Email)
signup = browser.find_element(By.CSS_SELECTOR, "button[data-qa*=signup-button]").click()
signup = browser.find_element(By.CSS_SELECTOR, "#id_gender1").click()
signup = browser.find_element(By.CSS_SELECTOR, "input[type*=password]").send_keys(Password)
signup = browser.find_element(By.CSS_SELECTOR, "#days").send_keys(str(random_days))
months = browser.find_element(By.CSS_SELECTOR, "#months")
select = Select(months)
options = select.options
random_months = random.choice(options)
select.select_by_visible_text(random_months.text)
signup = browser.find_element(By.CSS_SELECTOR, "#years").send_keys(str(random_years))
signup = browser.find_element(By.CSS_SELECTOR, "input[data-qa*=first_name]").send_keys(FirstName)
signup = browser.find_element(By.CSS_SELECTOR, "input[data-qa*=last_name]").send_keys(LastName)
signup = browser.find_element(By.CSS_SELECTOR, "input[data-qa*=address]").send_keys(Address)
Country = browser.find_element(By.CSS_SELECTOR, '#country')
country = Select(Country)
options = country.options
random_country = random.choice(options)
country.select_by_visible_text(random_country.text)
signup = browser.find_element(By.CSS_SELECTOR, "#state").send_keys(State)
signup = browser.find_element(By.CSS_SELECTOR, "#city").send_keys(City)
signup = browser.find_element(By.CSS_SELECTOR, "#zipcode").send_keys(Zipcode)
signup = browser.find_element(By.CSS_SELECTOR, "#mobile_number").send_keys(Mobile_number)
signup = browser.find_element(By.CSS_SELECTOR, "button[data-qa*=create-account]").click()
time.sleep(3)
