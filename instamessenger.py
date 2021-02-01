from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def user_input():
    username = input("Username: ")
    password = input("Password: ")
    return username, password


def inputting_data(userid, pass_inputted):
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(f"tanishq._.iam")
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(f"4U@h&D4a")
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com")
sleep(2)
usrnm, passwrd = user_input()
inputting_data(usrnm,passwrd)
sleep(3)
try:
    driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "][@tabindex="0"]').click()
except:
    print("simply continued")
driver.find_element_by_class_name("cq2ai").click()
try:
    driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "][@tabindex="0"]').click()
except:
    print("simply continued")
sleep(1)
driver.find_element_by_xpath('//a[@class="xWeGp"][@href="/direct/inbox/"]').click()