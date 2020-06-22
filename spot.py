from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time , getpass , os
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
username='vwin.py'

password=getpass.getpass(' password >>>> ')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http:www.instagram.com')
def wait_load(name):
    while True:
        try:
            user=driver.find_element_by_name(name)
        except NoSuchElementException:
            continue
        return user

	
	
	
def get_it_out(a):
    return a[0:a.index('>')-1]		
    	
def get_it_in(a):   
    return a+' >>>>>UNFOLLOWED YOU'
        	
        	
def scroll():
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    last_ht , ht = 0 , 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(20)
        ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;
        """, scroll_box)


def xpath(xp):
    while True:
        try:
            xpathel=driver.find_element_by_xpath(xp)
        except NoSuchElementException:
            continue
        return xpathel

def css(c):
    while True:
        try:
            xpathel=driver.find_elements_by_css_selector(c)
        except NoSuchElementException:
            continue
        return xpathel

user=wait_load('username')
pwd=wait_load('password')
user.send_keys(username)
pwd.send_keys(password)

login_btn=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')

login_btn.click()
time.sleep(4)

driver.get('https://www.instagram.com/vwin.py')


followers_botton=xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
num_followers=xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('innerHTML')

followers_botton.click()



time.sleep(20)
def get_followers():
    followers=css(".wo9IH .notranslate")
#	followers=css('._0imsa')
    inner=[]
    for i in followers:
        inner.append(i.get_attribute('innerHTML'))
    return inner	

def compair(a):
    c=[]
    for i in a :
        if not i.endswith(' >>>>>UNFOLLOWED YOU'):
            c.append(i)
    for i in c:
        if i not in my_followers:
            return False
    return True


scroll()


my_followers=get_followers()

file=open("followers.txt",'r')

old_version_followers=file.readlines()

file.close()

for i in old_version_followers:
    old_version_followers[old_version_followers.index(i)]=i[0:-1]

disi=compair(old_version_followers)
    
if disi:
    print('NOTHING HAS CHANGED')
else:
    print('Hello THERE IM RUNNING !!')
    for i in my_followers:
        if i not in old_version_followers and get_it_in(i) not in old_version_followers:
            print(i + ' is Following you')
            old_version_followers.append(i)
    for i in old_version_followers:
        if i.endswith(' >>>>>UNFOLLOWED YOU'):
            if get_it_out(i) in my_followers :
                print(get_it_out(i)+' FOLLOWED YOU AGAIN AFTER UNFOLLOWING YOU')
                old_version_followers[old_version_followers.index(i)]=get_it_out(i)
        else:
            if i not in my_followers:
                print(i+' UNFOLLOWED YOU')
                old_version_followers[old_version_followers.index(i)]=i+' >>>>>UNFOLLOWED YOU'	


for i in range(len(old_version_followers)):
    old_version_followers[i]+='\n'
file=open('followers.txt','w')
for i in old_version_followers:
    file.write(i)
file.close()
driver.close()
#It's over just right here

