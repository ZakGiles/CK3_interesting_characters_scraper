from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

url = "https://ck3.paradoxwikis.com/Interesting_characters"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
people = [l.text for l in soup.find_all("b")][:-1]

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