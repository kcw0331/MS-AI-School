from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
import time
import os
import urllib.request
import pandas as pd

def create_folder(directory): # 디렉토리가 있는 경우 생성하고 없는 경우 넘어가라
    # 폴더 생성
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError :
        print("error : Creating directory ... " + directory)

# 검색 키워드 호출
key = pd.read_csv('./keyword.txt', encoding = 'utf-8', names=['keyword'])
keywords = [] # 리스트를 만들어서 여기에 append해준다.
[keywords.append(key['keyword'][x]) for x in range(len(key))]
print(keywords)

def image_download(keywords) :
    create_folder("./" + keywords + "_high_reolution") # 폴더가 생성이 된다.

    # 크롬 드라이브 호출
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    chromedriver = "./chromedriver.exe"
    driver = webdriver.Chrome(chromedriver, options = options)
    driver.implicitly_wait(3)

    # 검색 
    print('검색 >> ', keywords) # 해당하는 키워드가 나오게 된다.
    driver.get("https://www.google.co.kr/imghp?h1=ko") # 이 사이트에 가서 검색을 검색한다.
    keyword = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    keyword.send_keys(keywords)
    keyword.send_keys(Keys.RETURN) # 키워드를 눌러준다.
    
    # 스크롤 내리기 -> 결과 더보기 버튼 클릭
    print(keywords + '스크롤 중 .......') 
    elem = driver.find_element_by_tag_name('body')
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN) # 페이지를 아래로 내려준다. 
        time.sleep(0.2) # 웹 페이지가 너무 빨리 내려가면 봇이 잡아낸다.

    try :
        # //*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input').click()
        for i in range(100):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
    except :
        pass
    images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    print(keywords + "찾은 이미지 개수 : ", len(images))

    links = []
    for i in range(1, len(images)):
        try :
            # //*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img
            # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img
            driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').click()
            links.append(driver.find_element_by_xpath('//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute("src"))
            print(keywords + '링크 수집 중 ... number : ' + str(i) + '/' + str(len(images)))
        except :
            continue

    fordidden = 0
    for index, i in enumerate(links):
        try :
            url = i
            start = time.time()
            urllib.request.urlretrieve(url, "./" + keywords + "_high_resolution/" + keywords + "_" + str(index-fordidden) + ".jpg")
            print(str(index + 1) + "/" + str(len(links)) + ' ' + keywords + '다운로드 중 ..... Download time : ' + str(time.time()-start)[:5] + '초')
        except :
            fordidden += 1
            continue
# =====================================================
# 실행
# =====================================================
if __name__ == '__main__':
    pool = Pool(processes=3)
    pool.map(image_download, keywords)

