from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import random


browser=webdriver.Chrome()

browser.get("https://ck3.paradoxwikis.com/Interesting_characters")
time.sleep(1)
html = browser.page_source
browser.close()
soup = BeautifulSoup(html, "html.parser")
people=[]
for li in soup.find_all("li"):
    b = li.find("b")
    if b:
        people.append(li.find("b").text)
    

with open("interesting_characters.csv", "w", encoding="utf-8") as file:
    for l in people:
        file.write(l+"\n")
    file.close()

while True:
    again = input("Pick a random interesting character? Y/N: ")
    if again.lower() == "y":
        print("\nA random interesting character:")
        print(people[random.randint(0,len(people)-1)])
        print()
    else:
        break