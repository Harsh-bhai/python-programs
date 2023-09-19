from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
# if __name__ == '__main__':
    
    
def xpathclick(drivername,xpath):
    varname = drivername.find_element_by_xpath(xpath)
    varname.click()


def xpathkeys(drivername,xpath, parameter):
    varname = drivername.find_element_by_xpath(xpath)
    varname.send_keys(parameter)
    


def openwebsite(drivername,website): #drivername=web
    drivername=webdriver.Chrome()
    drivername.get(website)
    drivername.maximize_window()

def NewTab(drivername,link1):
    drivername.execute_script(f"window.open('{link1}');")


def gettext(drivername,xpath):
    varname = drivername.find_element_by_xpath(xpath).text
    print(varname*100)


def cssclick(drivername,css):
    varname = drivername.find_element_by_css_selector(css)
    varname.click()


def classclick(drivername,Class):
    varname = drivername.find_element_by_class_name(Class)
    varname.click()


def getprice(importedfile,drivername,xpath):
    importedfile.xpathclick(drivername,xpath)
    a=importedfile.gettext()
    importedfile.xpathclick(drivername,xpath)
    b=importedfile.gettext()
    importedfile.xpathclick(drivername,xpath)
    c=importedfile.gettext()
    importedfile.xpathclick(drivername,xpath)
    d=importedfile.gettext()
    return a,b,c,d


def defaultcontent(drivername):
    varname = drivername.switch_to_default_content()


def switchframe(drivername,frame):
    drivername.switch_to_frame(frame)


def hit(key):
    pyautogui.keyDown(key)


def getposition():
    time.sleep(3)
    return(pyautogui.position())
    
    
def clickmouse(x,y):
    pyautogui.click(x,y)