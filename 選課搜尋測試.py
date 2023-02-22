#import
import time, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
t1 = time.time()
PATH = 'C:\Program Files (x86)\chomedriver.exe'
driver = webdriver.Chrome(PATH)
#載入台藝大選課系統
driver.get("https://uaap.ntua.edu.tw/ntua/")
print('成功進入「'+ driver.title + '」網站')

#登入
xf = driver.find_element('xpath', '/html/frameset/frame[2]')
driver.switch_to.frame(xf)

account = driver.find_element('name','uid')
account.clear()
account.send_keys('10810317')

password = driver.find_element('name','pwd')
password.clear()
password.send_keys('Iam10810317')

driver.find_element('name','chk').click()
time.sleep(1)
print('成功登入')

driver.switch_to.default_content()

#網路選課>線上加選
xf = driver.find_element('xpath', '/html/frameset/frameset/frame[1]')
driver.switch_to.frame(xf)

driver.find_element('id','sspan1').click()
driver.find_element('xpath','/html/body/span/table/tbody/tr[1]/td[2]/span/table/tbody/tr[1]/td[2]/span/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div').click()
print('網路選課>線上加選')

driver.switch_to.default_content()

"""只有初選才會用到
#我已知道
xf = driver.find_element('xpath', '/html/frameset/frameset/frame[2]')
driver.switch_to.frame(xf)

driver.find_element('xpath','/html/body/div[1]/div[3]/div/button').click()
print('我已知道')
"""
driver.switch_to.default_content()

#搜尋情緒與壓力管理
xf = driver.find_element('xpath', '/html/frameset/frameset/frame[2]')
driver.switch_to.frame(xf)

clsname = driver.find_element('name','clsname')
clsname.clear()
clsname.send_keys('情緒與壓力管理')

driver.find_element('name','esel_unt1').click()
driver.find_element('xpath','/html/body/form/table[2]/tbody/tr[8]/td[2]/select/option[1]').click()
driver.find_element('xpath','/html/body/form/table[2]/tbody/tr[8]/td[2]/input[2]').click()
print('正在搜尋課名')

driver.switch_to.default_content()

#請勾選加選科目後再按下「確定送出」。
xf = driver.find_element('xpath', '/html/frameset/frameset/frame[2]')
driver.switch_to.frame(xf)

#若已額滿，立即中止程式
try:
    driver.find_element('id','check1').click()
except NoSuchElementException:
    print("已額滿")
    driver.quit()
    sys.exit(0)

driver.find_element('id','sent_add1').click()
print('勾選科目確定送出')
time.sleep(1)

driver.switch_to.default_content()

#關閉webdriver
driver.quit()

t2 = time.time()
print(t2-t1)
