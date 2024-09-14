from bs4 import BeautifulSoup
import requests

#Initialize variables
nextChapter = "/fiction/21220/mother-of-learning/chapter/301778/1-good-morning-brother"
breakLoop = False
fstItr = False

#Loop that prints a chapter per iteration
while breakLoop == False:
    #Scrape data from website and find chapter title and text
    response = requests.get("https://www.royalroad.com" + nextChapter)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1", attrs={"class":"font-white break-word"})
    text = soup.findAll("div", attrs={"class":"chapter-inner chapter-content"})

    #Print title and chapter text
    print(title.text)
    
    for line in text:
        print(line.text)
    
    #Find next chapter button and initialize variables for loop
    link = soup.findAll("a", attrs={"class":"btn btn-primary col-xs-12"})
    currChapter = nextChapter
    i = 0
    
    #Loop through list of buttons to get next chapter
    for x in link:
        #First iteration sequence
        if(fstItr==False):
            nextChapter = x.get("href")
            fstItr = True
            continue
        #Skip previous button
        if(i == 0):
            i = 1
            continue
        #Obtain next chapter link and reset i
        if(i == 1):
            nextChapter = x.get("href")
            i = 0
            break
    
    #Loop end condition
    if(currChapter == nextChapter):
        breakLoop = True
        break

