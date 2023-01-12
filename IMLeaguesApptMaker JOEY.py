from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
import datetime as dt
import time 

#open web driver with preferred settings 
options = webdriver.ChromeOptions()
options.add_argument("headless")               #run without opening viewer
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1 })

# TIMESLOT LINK ASSIGN FUNCTION -- I will soon implement method for entering date and generating 'key', but for now I do it manually. 
def assignLink():
    #get date 
    #compare date to base date
    #get base number
    #manipulate base number and set it equal to 'key'
    key = str(2832223)
    return 'https://www.imleagues.com/spa/fitness/f8aadecc31574832ba2544f6e6165f80/registerevent?eventId=' + key

#assign path to chromedriver with preferred settings
PATH = "/Users/joeyhoward/Desktop/IMLeaguesApptMaker/chromedriver 2"
driver = webdriver.Chrome(chrome_options = options, executable_path= PATH)
#open browser
driver.get("https://www.imleagues.com/spa/account/login")


#enter username and press next
element = WebDriverWait(driver,35).until(
    EC.presence_of_element_located((By.ID, "email"))
    )
element.send_keys('jhoward39@fordham.edu')

element = driver.find_element_by_id("btnBeforeLogin")
driver.execute_script("arguments[0].click();", element)

#enter password and press next
element = WebDriverWait(driver,35).until(
    EC.presence_of_element_located((By.ID, "password"))
    )
element.send_keys("*********")

element = driver.find_element_by_id("btnBeforeLogin")
driver.execute_script("arguments[0].click();", element)

time.sleep(1)

#call method to generate link to desired timeslot
driver.get(assignLink())

#check waiver
# element = WebDriverWait(driver,10).until(
#     EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div[1]/label/input"))
#     )
# element.click()

#accept waiver
element = WebDriverWait(driver,35).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td/div/div[2]/button"))
    )
driver.execute_script("arguments[0].click();", element)

#input FIDN
element = driver.find_element_by_xpath("//*[@id='imlBodyMain']/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div/input")
element.send_keys("A17612557")

#click sign up 
element = WebDriverWait(driver,35).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='imlBodyMain']/div/div[1]/div[2]/div[1]/div/div/div[2]/div[4]/div/div/button"))
    )
driver.execute_script("arguments[0].click();", element)

#wait 5 seconds and exit the driver
time.sleep(5)
driver.quit()
