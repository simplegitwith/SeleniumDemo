
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# deriver =webdriver.Firefox()
# deriver.get("https://www.instagram.com")
#
# deriver.maximize_window()
# time.sleep(2)
# username = deriver.find_element(By.NAME,"username").send_keys("skyblue7590")
#
# passElement = deriver.find_element(By.NAME,"password").send_keys("739236")
#
# deriver.find_element(By.XPATH,'//body/div[@id='mount_0_0_qy']/div/div/div[@class='x9f619 x1n2onr6 x1ja2u2z']/div[@class='x78zum5 xdt5ytf x1n2onr6 x1ja2u2z']/div[@class='x78zum5 xdt5ytf x1n2onr6']/div[@class='x78zum5 xdt5ytf x1n2onr6 xat3117 xxzkxad']/div[@class='x78zum5 xdt5ytf x10cihs4 x1t2pt76 x1n2onr6 x1ja2u2z']/section[@class='x78zum5 xdt5ytf x1iyjqo2 xg6iff7 x6ikm8r x10wlt62']/main[@role='main']/div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xx7atzb x1n2onr6 x6ikm8r x10wlt62 x1iyjqo2 x2lwn1j xeuugli x1q0g3np xqjyukv x6s0dn4 x1oa3qoh xl56j7k']/div[@class='_ab1y']/div[@class='_ab21']/div[@class='_ab3a']/form[@id='loginForm']/div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xqui205 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']/div[3]').click()
# # #----------------------------------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()        ## driver is object of Firefox class
driver.get("https://www.facebook.com")      ## open website

driver.maximize_window()            ## to maximize window

emailElement = driver.find_element(By.ID, "email")
emailElement.send_keys("sagar@gmail.com")

passElement = driver.find_element(By.ID, "pass")
passElement.send_keys("sagar@123")

loginButton = driver.find_element(By.NAME, "login")
loginButton.click()
# #----------------------------------------------------
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
# driver.get("http://www.youtube.com")
#
# driver.maximize_window()
#
# searchButton = driver.find_element(By.ID, "container").send_keys("cook")
# searchButton.click()
# # #