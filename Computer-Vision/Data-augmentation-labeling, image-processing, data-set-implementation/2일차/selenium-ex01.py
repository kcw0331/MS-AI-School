# pip install selenium==4.2.0
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request
"""
폴더 구성
"""
def create_folder(directory): # 디렉토리가 있는 경우 생성하고 없는 경우 넘어가라
    # 폴더 생성
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError :
        print("error : Creating directory ... " + directory)

"""
키워드 입력, chromedriver 실행
"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

keywords = "사과"
chromedriver_path = "./chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path, options = options)
driver.implicitly_wait(3)

#####
##### 키워드 입력 selenium 실행
#####
driver.get("https://www.google.co.kr/imghp?h1=ko")

# 방법 1
# input -> /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input  # xpath를 쓰는 경우도 있다.
# botton -> /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button
keyword = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
keyword.send_keys(keywords)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button').click()

# 방법 2
# elem = driver.find_element_by_name("q")
# elem.send_keys(keyword)
# elem.send_keys(Keys.RETURN) # 리턴을 하면 버튼을 누른 것 처럼 된다.

##### 스크롤 #####
print(keywords + '스크롤 중 .......') 
elem = driver.find_element_by_tag_name('body')
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN) # 페이지를 아래로 내려준다. 
    time.sleep(0.2) # 웹 페이지가 너무 빨리 내려가면 봇이 잡아낸다.

try :
    # //*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input
    driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input').click()
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
except :
    pass
links = []
images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")

for image in images:
    if image.get_attribute('src') != None:
        links.append(image.get_attribute('src'))
print(keywords + "찾은 이미지 개수 :", len(links))
# print(links)
time.sleep(2)
# <image src= "base64" # 컴퓨터가 읽기 편하게 만든게 base64이다.

""" 데이터 다운로드 """
create_folder('./' + keywords + '_img_download')
for index, i in enumerate(links):
    # print(index)
    url = i
    start = time.time()
    urllib.request.urlretrieve(
        url, "./" + keywords + "_img_download/" + keywords + "_" + str(index) + ".jpg")
    print(str(index) + "/" + str(len(links)) + " " + keywords +
            " 다운로드 -----", str(time.time() - start)[:5] + '초')

print(keywords + "다운로드 완료 !!")