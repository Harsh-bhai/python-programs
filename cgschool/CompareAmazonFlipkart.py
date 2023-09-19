import myfuncs
import time
from selenium import webdriver
searchitem=input('''=======================================================
                     |  ENTER ITEM TO SEARCH ON BOTH AMAZON AND FLIPKART |
                    =======================================================
                    :  ''')

flipkart='https://www.flipkart.com/'
amazon='https://www.amazon.in/'
web=webdriver.Chrome()
web.get(flipkart)
# web.implicitly_wait(3)
web.maximize_window()
try:
    myfuncs.xpathclick(web,'/html/body/div[2]/div/div/button')
except :
    pass    

myfuncs.xpathclick(web,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
myfuncs.xpathkeys(web,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input',searchitem)
myfuncs.xpathclick(web,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
# try:
#     try:
#         myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[3]/div/div[1]')
#         a=myfuncs.gettext()
#         myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/a[3]/div/div[1]')
#         b=myfuncs.gettext()
#         myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/a[3]/div/div[1]')
#         c=myfuncs.gettext()
#         myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div/a[3]/div/div[1]')
#         d=myfuncs.gettext()
#     except :
#         myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[3]/div[1]/div[1]')
#         b=myfuncs.gettext()
#         myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/a[3]/div[1]/div[1]')
#         a=myfuncs.gettext()
#         myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/a[3]/div[1]/div[1]')
#         c=myfuncs.gettext()
#         myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div/a[3]/div[1]/div[1]')
#         d=myfuncs.gettext()
        
    
# except :
#     myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
#     a=myfuncs.gettext()
#     myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
#     b=myfuncs.gettext()
#     myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[4]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
#     c=myfuncs.gettext()
#     myfuncs.xpathclick(web,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[5]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
#     d=myfuncs.gettext()
    
myfuncs.NewTab(web,amazon)
time.sleep(10)
myfuncs.xpathclick(web,'//*[@id="nav-logo-sprites"]')
# time.sleep(3)

# myfuncs.clickmouse(768,128)
# web.switch_to_frame('ape_Gateway_right-2_desktop_iframe')
# try:
myfuncs.xpathclick(web,'//*[@id="twotabsearchtextbox"]')
myfuncs.xpathkeys(web,'//*[@id="twotabsearchtextbox"]',searchitem)
myfuncs.xpathclick(web,'//*[@id="nav-search-submit-button"]')
# except:
#     myfuncs.xpathkeys(web,'//*[@id="twotabsearchtextbox"]',searchitem)
#     myfuncs.xpathclick(web,'//*[@id="nav-search-submit-button"]')
    
# myfuncs.defaultcontent(web)
