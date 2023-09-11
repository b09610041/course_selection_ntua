# 給台藝大學生的自動選課教學

Written by NTU_B09610041
Copyright (c) 2023 

### 2023/9/11更新；新增"選課搜尋測試.py"用於除錯


此教學分為#事前準備與#程式執行兩部分。
因需要長時間開啟電腦，建議使用桌機。

## 事前準備

步驟一：下載python
(Python官網：https://www.python.org/downloads/)

參考教學：https://www.codingspace.school/blog/2021-04-07

步驟二：下載VS code
(VS Code官網：https://code.visualstudio.com/)

參考教學：https://www.citerp.com.tw/citwp2/2021/12/22/vs-code_python_01/

步驟三：下載ChromeDriver
(ChromeDriver官網：https://chromedriver.chromium.org/downloads)

### 2023/9/8更新

目前官網只提供到114.0.5735.90版本的ChromeDriver

114以後的版本在https://googlechromelabs.github.io/chrome-for-testing/

點進網頁找到自己的版本後複製URL並開啟就會自動下載

(不一定要串數字都一樣也可以work)

參考教學：https://ithelp.ithome.com.tw/m/articles/10261845
(但不要執行「4.將chromedriver.exe放到跟python.exe一樣的目錄下」這個動作)

步驟四：下載github程式碼
(https://github.com/b09610041/course_selection_ntua)

點選Code - Download Zip -解壓縮

並將步驟三所下載的chomedriver.exe放到解壓所後的資料夾course_selection_ntua-main

步驟五：打開終端機

Windows:按一下開始 ，在搜尋欄位中輸入「終端機」，然後按一下「終端機」。

Mac:按一下 Dock 中的「啟動台」圖像 ，在搜尋欄位中輸入「終端機」，然後按一下「終端機」。

開啟後輸入

pip install selenium

pip install APSchedular

## 程式執行

步驟一：開啟VS Code

點選左上角file - open folder - 選取資料夾py

步驟二：依照指示輸入課程名稱與帳號密碼

例：

class_name_1 = "大學幸福課"

uid = "10110101"

pwd = "ji32k7au4a83"

步驟三(如有需要)：若該課程有多個時段，且目標課程在選課系統搜尋時的排序不為第一個時

若目標課程在選課系統搜尋時的排序為第二時，將第101行程式碼替換為

job1 = scheduler.add_job(function1, 'interval', minutes=1, args=[uid,pwd,class_name_1, "check2"])

若目標課程在選課系統搜尋時的排序為第三時，將第101行程式碼替換為

job1 = scheduler.add_job(function1, 'interval', minutes=1, args=[uid,pwd,class_name_1, "check3"])

以此類推

步驟四(如有需要)：若左下角的debug標示驚嘆號，點擊後出現"import selenium could not be resolved..."

點選View - Command Palette - 輸入python interpreter - 點選Python: Select interpreter - 點選recommended的選項

步驟五：按下右上角的三角形按鍵開始

Terminal會顯示執行時間與次數。
額滿時顯示額滿並持續執行，選課成功時顯示選課成功並停止執行。
若要手動停止，按下垃圾桶按鍵或直接關閉VS Code。

有任何問題歡迎善用issues功能發問，或來信b09610041@ntu.edu.tw
