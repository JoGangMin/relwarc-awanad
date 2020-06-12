from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
import json
import time
import re
with open("config.json","r",encoding='utf-8') as file:
    config_file = json.load(file)

def get_driver():
    driver = webdriver.Chrome('/Users/jogangmin/Desktop/danawa/chromedriver')   #(config_file['chrome_driver_path'])
    return driver



def search_proeuct_page(driver, page_url):
    driver.get(page_url)
    driver.implicitly_wait(5)

    # 쇼핑몰 상품리뷰 클릭
    review_tap = driver.find_elements_by_css_selector(".sub_tab.sub_tab_v2 > .tab_list > .tab_item a")[1]
    # company_review = review_tap.find_elements_by_css_selector(".tab_item a")[1]
    review_tap.click()

    # 쇼핑몰 상품 개수 가져오기
    try:
        comment_count_elemnt = driver.find_element_by_css_selector('#danawa-prodBlog-companyReview-button-tab-companyReview > span > strong')
        comment_count = int(re.sub("\,","",comment_count_elemnt.get_attribute('innerText')))
    except:
        comment_count = 0

    print(f"댓글 개수:{comment_count}")

    # 상품평 다음페이지를 누르는 횟수 정함
    roop_count = int(comment_count/100)
    if comment_count%100:
        roop_count += 1

    print("totla page num:",roop_count)

    #10페이지 탐색하고 다음 뎃글 페이지를 로딩
    comment_list =[]
    for i in range(roop_count):
        print(i)

        # 페이지 개수 탐색
        page_num_div = driver.find_element_by_css_selector(".nums_area")
        page_num = len(page_num_div.find_elements_by_css_selector('.page_num'))

        # 1페이지부터 넘어감
        for j in range(page_num):
            page_elenent_div = driver.find_element_by_css_selector(".nums_area")
            page_elenent_div.find_elements_by_css_selector('.page_num')[j].click()
            print('page',j)
            #제품 정보 수집
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.CSS_SELECTOR, '.danawa-prodBlog-companyReview-clazz-more'))))
            time.sleep(1.5)
            
            reivew_div_element = driver.find_element_by_css_selector('.rvw_list')
            reivew_list = reivew_div_element.find_elements_by_css_selector(".danawa-prodBlog-companyReview-clazz-more")
            
            for k in reivew_list:
                comment = k.find_element_by_css_selector('.atc')
                comment_list.append(comment.get_attribute('innerText'))


        #페이지 끝에 다다르면 다음 페이지 리스트로 넘어가기
        try:
            next_page_buttion = driver.find_element_by_css_selector('.nav_edge.nav_edge_next.nav_edge_on')
        
        except:
            if driver.find_element_by_css_selector('.nav_edge.nav_edge_next.nav_edge_off'):
                break
        next_page_buttion.click()
        time.sleep(2)

    return comment_list
    
       
  


if __name__ == "__main__":

    # test_url = 'http://prod.danawa.com/info/?pcode=7611343#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=10405512#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=8843078#bookmark_cm_opinion' #리뷰 없음
    # test_url = 'http://prod.danawa.com/info/?pcode=9593169#bookmark_cm_opinion' #리뷰 없음
    # test_url = 'http://prod.danawa.com/info/?pcode=6062066#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=9751677#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=4572084#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=5869359#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=5380452#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=6113727#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=1996972#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=3966353#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=6055410#bookmark_cm_opinion'
    # test_url = 'http://prod.danawa.com/info/?pcode=6769282#bookmark_cm_opinion'
    # test_url = "http://prod.danawa.com/info/?pcode=9805773"
        
    driver = get_driver()
    print(search_proeuct_page(driver, test_url))

    time.sleep(5)
    driver.quit()
