from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

def comment_photo_hashtag(hashtag_list, comment_list, driver, number_comment_for_hashtag):
    comments_total_number = 0
    for i in hashtag_list:
        if comments_total_number > 10:
            break
        url = "https://www.instagram.com/explore/tags/"+ i + "/"
        driver.get(url)
        first_photo = "//h2[contains(text(),'recenti')]/following::a"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_photo))).click()
        
        go_stright_first_time = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button"
        go_stright = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button"

        WebDriverWait(driver, 7).until(
                       EC.presence_of_element_located((By.XPATH, go_stright_first_time))).click()
        form_to_click="/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form"     
        comment_area = "//html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea"
        submit_btn = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button'
        
        
        
        for i in range(0,number_comment_for_hashtag):
            time.sleep(1)  
            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, form_to_click))).click()
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, comment_area))).send_keys(comment_list[random.randint(0,len(comment_list)-1)])
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, submit_btn))).click()
                time.sleep(8)

                comments_total_number+=1
                        
            except:
                print('errore commento')
            
            time.sleep(1)
            WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, go_stright))).click()
                          

