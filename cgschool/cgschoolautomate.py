from selenium import webdriver
import time

# //*[@id="mainContent_btnSearch"]

# //*[@id="mainContent_ddlSubject"]/option[4]    maths
# //*[@id="mainContent_ddlSubject"]/option[3]    english

# //*[@id="mainContent_ddlClass"]/option[2]    class 6
# //*[@id="mainContent_ddlClass"]/option[3]    class 7
# //*[@id="mainContent_ddlClass"]/option[4]    class 8

# //*[@id="mainContent_ddlSection"]/option[2]   section a
# //*[@id="mainContent_ddlSection"]/option[3]   section b


def xpathclick(drivername, xpath):
    varname = drivername.find_element_by_xpath(xpath)
    varname.click()


def xpathkeys(drivername, xpath, parameter):
    varname = drivername.find_element_by_xpath(xpath)
    varname.send_keys(parameter)


def idkeys(drivername, id, parameter):
    varname = drivername.find_element_by_id(id)
    varname.send_keys(parameter)


web = webdriver.Chrome()
web.get("https://cgschool.in/")
web.maximize_window()

filename = "D:/Harsh/vscodes python/cgschool/student.txt"
mobileNumber = "46456165484165"
password = "687845346435"
s=5000

xpathclick(web, '//*[@id="menuzord-right"]/div/div[2]/div[2]/ul/li[3]/a')
xpathkeys(web, '//*[@id="txtuserid"]', mobileNumber)
xpathkeys(web, '//*[@id="txtpassword"]', mobileNumber)
xpathclick(web, '//*[@id="btnLogin"]')
xpathclick(web, '//*[@id="mainContent_RptSelectLogin_btnSelectLogin_1"]')
xpathclick(
    web,
    '//*[@id="form1"]/div[3]/div/div[3]/div[1]/div/div/div/div/div[1]/div/div[1]/a/i',
)
time.sleep(1)
xpathclick(web, '//*[@id="liTeacher"]/a')
xpathclick(web, '//*[@id="lividyarthi"]/a')
xpathclick(web, '//*[@id="lividyarthi"]/ul/li[3]/a')
time.sleep(2)
web.execute_script("window.scrollTo(0, 1000)")
xpathclick(web, '//*[@id="mainContent_ddlClass"]')
time.sleep(1)
xpathclick(web, '//*[@id="mainContent_ddlClass"]/option[4]')
time.sleep(1)
xpathclick(web, '//*[@id="mainContent_ddlSection"]')
xpathclick(web, '//*[@id="mainContent_ddlSection"]/option[2]')
time.sleep(1)
xpathclick(web, '//*[@id="mainContent_ddlSubject"]')
xpathclick(web, '//*[@id="mainContent_ddlSubject"]/option[3]')
time.sleep(1)
xpathclick(web, '//*[@id="mainContent_btnSearch"]')
# time.sleep(2)
web.execute_script(f"window.scrollTo(0,10000)")
f = open(filename, "r")  # make sure to replace '\' with '/' in above string
r = f.read()
a = r.split("\n")
l = len(a)
for i in range(45):
    # for j in range(1):
    xpathclick(web, f'//*[@id="mainContent_RptStudentList_Chksingle_{i}"]')
    time.sleep(3)
    web.execute_script(f"window.scrollTo(0, {s})")
    # time.sleep(5)
    # web.execute_script(f"window.scrollTo(0, {s})")
    # time.sleep(1)


    idkeys(web, f'"mainContent_RptStudentList_txtSection1_{i}"]',a[i].split()[0])
    idkeys(web, f'"mainContent_RptStudentList_lblProject_{i}"]',"10")
    idkeys(web, f'"mainContent_RptStudentList_lblSection2_{i}"]',"10")
    idkeys(web, f'"mainContent_RptStudentList_lblSection3_{i}"]',a[i].split()[1])
    s+=2000
    web.execute_script(f"window.scrollTo(0, {s})")

        


f.close()
# //*[@id="mainContent_RptStudentList_Chksingle_0"]
# "mainContent_RptStudentList_Chksingle_0"