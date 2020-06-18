login = ""
password  = ""

from selenium import webdriver
import time

browser = webdriver.Chrome("G:\insta\chromedriver.exe")

all = 100

browser.get("https://www.instagram.com/")

# вход в аккаунт
browser.get("https://www.instagram.com/accounts/login/")
browser.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys("login")
browser.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys("password")
browser.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
time.sleep(3)

# Действия на сайте
browser.get("https://www.instagram.com/natgeo/")
time.sleep(3)
browser.find_element_by_xpath("//section/main/div/header/section/ul/li[2]/a").click()
time.sleep(2)
element = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[2]/div/div[1]")

browser.execute_script("argument[0].scrollTop = argument[0].scrollHeight/%s" %6, element)
time.sleep(0.8)
browser.execute_script("argument[0].scrollTop = argument[0].scrollHeight/%s" %4, element)
time.sleep(0.8)
browser.execute_script("argument[0].scrollTop = argument[0].scrollHeight/%s" %3, element)
time.sleep(0.8)
browser.execute_script("argument[0].scrollTop = argument[0].scrollHeight/%s" %2, element)
time.sleep(0.8)
browser.execute_script("argument[0].scrollTop = argument[0].scrollHeight/%s" %1.4, element)
time.sleep(0.8)

pers = []
t = 0.7
num_scroll = 0

#persons = browser.find_elements_by_xpath("")
#for i in range(5)
#    pers.append(str(persons[i].get_attribute('href')))

while len(pers) < all:
    num_sccroll += 1
    browser.execute_script("argument[0].scrollTop = argument[0].scrollHeight", element)

if num_scroll % 10 ==0:
    print("!")
    # сохранение пользователей
    persons = browser.find_element_by_xpath("")
    for i in range(len(persons)):
        pers.append(str(persons[i].get_atribute('href')))

time.sleep(t)

# создание файла со списком пользователей
f = open("G:\insta\persons_list.txt")
for person in pers:
    f.write(person)
    f.write("\n")
    f.close()

browser.execute_script("argument[0].scrollTop = argument[0].scrollHeight", element)
time.sleep(0.8)
