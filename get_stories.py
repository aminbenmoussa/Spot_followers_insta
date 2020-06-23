import glob
import os
import shutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import getpass
import os
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def wait_load(name):
    while True:
        try:
            user = driver.find_element_by_name(name)
        except NoSuchElementException:
            continue
        return user


def scroll():
    scroll_box = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(20)
        ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, scroll_box)


def xpath(xp):
    time.sleep(2)
    for i in range(5):
        try:
            xpathel = driver.find_element_by_xpath(xp)
        except NoSuchElementException:
            continue
        return xpathel


def css(c):
    while True:
        try:
            xpathel = driver.find_elements_by_css_selector(c)
        except NoSuchElementException:
            continue
        return xpathel
    return False


user = input('User To Spy >>>>>  ')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://storiesig.com/stories/'+user)
user_dir = '/Users/amin/Documents/'+user


if not os.path.isdir(user_dir):
    os.mkdir(user_dir)


stories = css(
    '.jsx-1407646540.container .jsx-1407646540 .jsx-3375929380.download a')
if stories:
    print('THERE\'S ',len(stories),' STORIES AVAILABLE ')
    answer=input('IF YOU WANT TO CONTINUE AND DOWNLOAD THEM HIT ENTER // IF NOT HIT ctrl+C\n			')

    for i in stories:
        i.click()
        time.sleep(3)

    time.sleep(20)


    for i in range(len(stories)):
        list_of_files = glob.glob('/Users/amin/Downloads/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        shutil.move(latest_file, user_dir + '/' + os.path.basename(latest_file))

    driver.close()

    print('Done..............................\n')

    print('Got ', len(stories), ' Stories added')
else:
    driver.close()
    print('-------------------NO STORIES TO SHOW------------------') 
