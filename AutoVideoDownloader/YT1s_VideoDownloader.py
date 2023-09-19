#sourcecode for yt 1 website


#//*[@id="formatSelect"]/optgroup[1]/option[2]  ---> For 1080p resolution
#//*[@id="formatSelect"]/optgroup[1]/option[3]  ---> For 720p resolution
#//*[@id="formatSelect"]/optgroup[1]/option[4]  ---> For 480p resolution


#currently video downloader is set at 480p


#____SOURCE CODE______
from selenium import webdriver
import time


web=webdriver.Chrome()
web.get("https://yt1s.com/en111")  #link of youtube downloader
filename="D:/Harsh/vscodes python/AutoVideoDownloader/Youtube_Links.txt"  #Textfile used in this program
f = open(filename, "r")  #make sure to replace '\' with '/' in above string
r = f.read()
a=r.split("\n")
l=len(a)
for i in range(l):

    time.sleep(2)
    blanklink=web.find_element_by_xpath('//*[@id="s_input"]')
    blanklink.send_keys(a[i])
    
    

    convert=web.find_element_by_xpath('//*[@id="btn-convert"]')
    convert.click()
    time.sleep(2)

    triangle=web.find_element_by_xpath('//*[@id="formatSelect"]')
    triangle.click()

    resolution=web.find_element_by_xpath('//*[@id="formatSelect"]/optgroup[1]/option[4]')
    resolution.click()

    getlink=web.find_element_by_xpath('//*[@id="btn-action"]')
    getlink.click()

    time.sleep(5)
    download=web.find_element_by_xpath('//*[@id="asuccess"]')
    download.click()

    cnext=web.find_element_by_xpath('//*[@id="cnext"]')
    cnext.click()
    time.sleep(3)

    nextround=web.find_element_by_xpath('/html/body/header/div[1]/a/span')
    nextround.click()
f.close()