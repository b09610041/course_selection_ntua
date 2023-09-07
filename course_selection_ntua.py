import time, os
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#帳號密碼(打在分號中間)
class_name_1 = "課名"
uid = "帳號"
pwd = "密碼"

#開始時間
t1 = time.time()

def function1(user_id, user_password, class_name, check="check1"):
    print()
    print(class_name)
    print(f'目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    t2 = time.time()
    t = round(t2-t1)
    x = int(t/60)
    print(f"執行次數：{x}次")
    m = t/60
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    m = int(m)
    h = int(h)
    d = int(d)
    print(f"執行時間：{d}日{h}時{m}分")      
         
    #webdriver路徑
    driver = webdriver.Chrome("chromedriver.exe")
    
    #載入台藝大選課系統
    driver.get("https://uaap.ntua.edu.tw/ntua/")

    #登入
    xf = driver.find_element('xpath', '/html/frameset/frame[2]')
    driver.switch_to.frame(xf)

    account = driver.find_element('name','uid')
    account.clear()
    account.send_keys(user_id)

    password = driver.find_element('name','pwd')
    password.clear()
    password.send_keys(user_password)

    driver.find_element('name','chk').click()
    time.sleep(1)

    driver.switch_to.default_content()

    #網路選課>線上加選
    xf = driver.find_element('xpath', '/html/frameset/frameset/frame[1]')
    driver.switch_to.frame(xf)

    driver.find_element('id','sspan1').click()
    driver.find_element('xpath','/html/body/span/table/tbody/tr[1]/td[2]/span/table/tbody/tr[1]/td[2]/span/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div').click()

    driver.switch_to.default_content()

    #搜尋課名
    xf = driver.find_element('xpath', '/html/frameset/frameset/frame[2]')
    driver.switch_to.frame(xf)

    clsname = driver.find_element('name','clsname')
    clsname.clear()
    clsname.send_keys(class_name)

    driver.find_element('name','esel_unt1').click()
    driver.find_element('xpath','/html/body/form/table[2]/tbody/tr[8]/td[2]/select/option[1]').click()
    driver.find_element('xpath','/html/body/form/table[2]/tbody/tr[8]/td[2]/input[2]').click()

    driver.switch_to.default_content()

    #請勾選加選科目後再按下「確定送出」。
    xf = driver.find_element('xpath', '/html/frameset/frameset/frame[2]')
    driver.switch_to.frame(xf)

    #若已額滿，立即中止程式
    try:
        driver.find_element('id',check).click()
    except NoSuchElementException:
            print(class_name + "已額滿\n")
            driver.quit()
    else:
        driver.find_element('id','sent_add1').click()
        print(class_name + '選課成功')
        time.sleep(1)
        driver.switch_to.default_content()
        #關閉webdriver並停止工作
        driver.quit()
        os._exit(0)


# 指定時區（一定要指定，否則會失敗）
scheduler = BlockingScheduler(timezone="Asia/Shanghai")

# 每１分鐘執行選課一
job1 = scheduler.add_job(function1, 'interval', minutes=1, args=[uid,pwd,class_name_1])
print(f'目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

#間隔30秒執行選課二
time.sleep(30)
job2 = scheduler.add_job(function1, 'interval', minutes=1, args=[uid,pwd,class_name_1,"check2"])
print(f'目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


scheduler.start()

print('Schedule started ...')  # 這行不會被執行
