from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import os
import time


def BadgeFinder(GameID):
    driver = webdriver.Edge()
    driver.get(f"https://www.roblox.com/games/{GameID}/")

    def buttonExists():
        try:
            driver.find_element(By.CSS_SELECTOR, "button[ng-click='$ctrl.seeMore()']")
            return True
        except NoSuchElementException:
            return False


    while buttonExists(): 
        button = driver.find_element(By.CSS_SELECTOR, "button[ng-click='$ctrl.seeMore()']")
        button.click()
        time.sleep(0.6)

    elem = driver.find_elements(By.CSS_SELECTOR,"div[ng-bind='badge.awardedCount']")
    bname = driver.find_elements(By.CSS_SELECTOR,"div[ng-bind='badge.name']")

    elemValue = []
    for name,value in zip(bname,elem):
        elemValue.append((name.text,int(value.text)))

    elemSorted = sorted(elemValue, key=lambda x: x[1])
    os.system("cls")
    print(f" The badge with least number of owners is: \n {elemSorted[0][0]} : {elemSorted[0][1]} \n The badge with most number of owners is: \n {elemSorted[-1][0]} : {elemSorted[-1][1]}")
    driver.quit()

BadgeFinder(int(input("Enter Game id: ")))
