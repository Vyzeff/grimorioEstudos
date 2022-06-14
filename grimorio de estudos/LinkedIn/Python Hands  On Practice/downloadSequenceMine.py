import requests
import re

def downloadSequence(url, output):

    sequence = True
    while sequence:
        downloadCount = 0
        if downloadCount == 0:    
            r = requests.get(url)
            fileName = url.rsplit("/", 1)[1]
            downloadCount += 1   
        else:
            nextUrl1 = url.rsplit("/", 1)[1]
            newUrl2 = re.findall(r'[0-9]+', nextUrl1)

            r = requests.get()         
        with open(f"{output}/{fileName}", "wb") as f:
            f.write(r.content)
        break
    print("Your files were dowloaded successfully.")

if __name__ == "__main__":
    downloadSequence("http://699340.youcanlearnit.net/image001.jpg", "./my_stuff")