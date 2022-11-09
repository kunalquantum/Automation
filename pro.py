import time
import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('C:\chromedriver.exe')

browser.implicitly_wait(2)
browser.maximize_window()
browser.get('https://www.instagram.com/')

time.sleep(1)

username_input = browser.find_element(By.CSS_SELECTOR,  "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys("k_dark___")
password_input.send_keys("Kunal12345")
#login button
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(12)#waiting for the page to load
#not now for account information saving
try:
     no=browser.find_element(By.XPATH, '//button[text()="Save Info"]')
     time.sleep(2)
     no.click()
#waitig for page to load
     time.sleep(12)
except:
    pass
try:

     noo=browser.find_element(By.XPATH, '//button[text()="Not Now"]')
     time.sleep(2)
     noo.click()
     #waitig for page to load
     time.sleep(2)
except:
 pass





 intr=['mesmorizing', 'beautiful','amazzedd!!' ]
def test():
            profilelist=[ 'virat.kohli']
            intr=['mesmorizing', 'beautiful','amazzedd!!' ]
            my=['<<<<<happy birthday King KOHLI>>>> from kunal']
            #story()


            for i in range (len(profilelist)):
            #follow  #follow
                s = browser.find_element(By.XPATH, '//*[local-name()="svg"and @aria-label="Search"]')
                time.sleep(3)
                s.click()
                time.sleep(3)
            # s.click()
                time.sleep(2)

                S = browser.find_element(By.XPATH, '//input[@placeholder="Search"]')
                S.send_keys((profilelist[i]))
                time.sleep(2)
                c = 0
                while c < 2:
                    S.send_keys(Keys.ENTER)
                    c = c + 1
                    time.sleep(2)

                time.sleep(2)
                try:
                    follow=browser.find_element(By.XPATH, '//button[@class="_acan _acap _acas"]')
                    follow.click()
                    time.sleep(3)
                except:
                    pass
                meh1=browser.find_element(By.XPATH,'//button[@class="_acan _acap _acat"]')
                time.sleep(3)
                meh1.click()
                time.sleep(3)
                meh=browser.find_element(By.XPATH,'//textarea[@placeholder="Message..."]')
                meh.click()
                time.sleep(3)
                meh.send_keys(random.choice(my))
                time.sleep(3)
                send = browser.find_element(By.XPATH, '//button[text()="Send"]')
                send.click()
                time.sleep(2)
                profile=browser.find_element(By.XPATH,'//div[@class="_ab8w  _ab94 _ab95 _ab9h _ab9m _ab9p _abcm"]')
                profile.click()
                time.sleep(3)

                '''home=browser.find_element(By.XPATH,'//*[local-name()="svg"and @aria-label="Home"]')
                home.click()'''




            #pic selection
                pic=browser.find_element(By.XPATH,'//div[@class="_aagw"]')
                pic.click()
                time.sleep(3)

                for i in range(2):

                        #like=browser.find_element(By.XPATH,'//*[name()="svg"  and @aria-label="Like"]')

                        #like.click()

                        comment()
                        next=browser.find_element(By.XPATH, '//*[name()="svg" and @class="_ab6-" and @aria-label="Next"]')
                        next.click()

                        time.sleep(5)


                close = browser.find_element(By.XPATH, '//*[@aria-label="Close"]')
                close.click()
                time.sleep(3)
            home()
            story()
            home()
            notification()
            logout()
            close.click()
            #liking the page
            #like=browser.find_element(By.XPATH, '//button[@class="_abl-"]//*[@aria-label="Like"]')
          #time.sleep(4)
            #like=browser.find_element(By.XPATH, '//*[name()="svg"and @aria-label="Like"]')
            #like.click()

            #time.sleep(4)

def option():
    time.sleep(4)
    option1=browser.find_element(By.XPATH, '//*[name()="svg" and @aria-label="Options"]')
    option1.click()
def logout():
    pro=browser.find_element(By.XPATH,'//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _aak1 _a6hd"]')
    pro.click()
    time.sleep(3)
    option1 = browser.find_element(By.XPATH, '//*[name()="svg" and @aria-label="Options"]')
    option1.click()
    time.sleep(3)
    logo=browser.find_element(By.XPATH, '//button[text()="Log Out"]')
    logo.click()
    time.sleep(3)

def home():
    time.sleep(3)
    home = browser.find_element(By.XPATH, '//*[local-name()="svg"and @aria-label="Home"]')
    home.click()
def comment():
    intr = ['mesmorizing', 'beautiful', 'amazzedd!!']
    time.sleep(4)
    comment = browser.find_element(By.XPATH, '//textarea[@aria-label="Add a comment…"]')
    comment.click()
    time.sleep(3)
    comment2 = browser.find_element(By.XPATH, '//textarea[@placeholder="Add a comment…"]')
    comment2.click()
    time.sleep(2)
    comment2.send_keys(random.choice(intr))
    send=browser.find_element(By.XPATH,'//div[@class="_aacl _aaco _aacw _aad0 _aad6 _aade"]')
    send.click()
def story():
    st=browser.find_element(By.XPATH,'//div[@class="_aamb _aamc"  ]')
    st.click()
    time.sleep(2)
    try:
        play=browser.find_element(By.XPATH,'//*[name()="svg" and @aria-label="Play"]')
        play.click()
    except:
        pass
    for i in range(12):
            ne=browser.find_element(By.XPATH,'//button[@aria-label="Next"]')
            ne.click()
            time.sleep(12)
            try:
                play = browser.find_element(By.XPATH, '//*[name()="svg" and @aria-label="Play"]')
                play.click()
            except:
                pass
    cl=browser.find_element(By.XPATH,'//*[name()="svg" and @aria-label="Close"]')
    cl.click()
def notification():
    time.sleep(2)
    notif=browser.find_element(By.XPATH,'//*[name()="svg" and @aria-label="Notifications"]')
    notif.click()
    time.sleep(5)
    home()


























#follow_like_comment()


test()
#f()
home()
logout()
