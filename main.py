import time

import pyfiglet
from pyfiglet import *
from selenium import webdriver
import os
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://visa.vfsglobal.com/kaz/en/svk/application-detail"

driver.get(url)
time.sleep(70)
main_button = "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button"
visa_blank = '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[1]/mat-form-field/div/div[1]/div[2]'
visa_astana = '//*[@id="mat-option-0"]'
appointment_category = '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[2]/mat-form-field/div/div[1]'
short_term = '//*[@id="mat-option-15"]'
short_term_almaty = '//*[@id="mat-option-10"]'
sub_category = '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[3]/mat-form-field/div/div[1]/div[3]'
tourist_category = '//*[@id="mat-option-7"]'
button = '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button'
almaty_visa = '//*[@id="mat-option-1"]/span'
tourist_category_almaty = '//*[@id="mat-option-13"]'
while True:
    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, visa_blank)) \
        .perform()
    time.sleep(6)
    #clicking to visa blank
    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, visa_astana)) \
        .perform()
    time.sleep(5)

    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, sub_category)) \
        .perform()
    time.sleep(2)
    
    #clicking to sub category

    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, tourist_category)) \
        .perform()
    time.sleep(15)

    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, button)) \
        .perform()
    time.sleep(10)

    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, visa_blank)) \
        .perform()
    time.sleep(6)

    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, almaty_visa)) \
        .perform()
    time.sleep(5)

    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, appointment_category)) \
        .perform()
    time.sleep(5)

    #clicking to appointment category
    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, short_term_almaty)) \
        .perform()
    time.sleep(10)
    
    #clicking to short term 

    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, sub_category)) \
        .perform()
    time.sleep(3)
    
    #clicking to sub category

    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, tourist_category_almaty)) \
        .perform()
    time.sleep(10)

    ActionChains(driver) \
        .click(driver.find_element(By.XPATH, button)) \
        .perform()
    time.sleep(10)


