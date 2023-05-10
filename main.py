import os
import requests
from bs4 import BeautifulSoup

urlproxi: str = "https://proxy.scrapeops.io/v1/"
url: str = "https://www.textileinfomedia.com/business/uk/textile-mill"
headers: dict = {
    "user-agent " : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/112.0.0.0 Mobile Safari/537.36",

}

API_KEY = 'c74f90e6-255e-4b11-8245-7446e9df8fef'


def getList(url: str):     # get_quotes
    res = requests.get(
        urlproxi,
        params={
            'api_key': API_KEY,
            'url': url,
        }
    )
    print(res)
    if res.status_code == 200:
        # print(f"Ok !!, status code is : {res.status_code}")
        soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")

        # proses scraping
        contents = soup.find_all("div", attrs={"class", "col-md-12 tm-detail-block"})
        # print(contents)
        for content in contents:
            name = content.find("h3", attrs={"class", "m-t-10"})
            if name is None:
                name.extract()
            name = name.text.strip()

            # detailInners = content.find("div", attrs={"class", "tm-detail-inner-desc"}).text.strip()
            # i = 0
            # for detailInner in detailInners:
            #     if i == 1:
            #         bidang= detailInner.text
            #         if bidang is None:
            #             bidang.extract()
            # i = i + 1

            print(f"name : {name}")
            #print(f"Bidang: {bidang}")



    else:
        print(f"Not Ok !!, status Code is : {res.status_code}")

if __name__ == "__main__":
    if url is not None:
        getList(url)
