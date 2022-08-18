from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def like_photo_hashtag(hashtag_list, driver):
    for i in hashtag_list:
        url = "https://www.instagram.com/explore/tags/"+ i + "/"
        driver.get(url)
        first_photo = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]"
        WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, first_photo))).click()
        go_stright_first_time = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button"
       
        WebDriverWait(driver, 7).until(
                       EC.presence_of_element_located((By.XPATH, go_stright_first_time))).click()
        
        for j in range(0,15):

            go_stright = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button"

            
            like_btn = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"
            like_or_not = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[1]/*[1]'
            
            try:
                result = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, like_or_not)))
                
                if "Non" in result.get_attribute("aria-label"):
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, go_stright))).click()
                    print('gia messo')
                else:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, like_btn))).click()
            except:
                print('errore')

            time.sleep(2)
           
                          
            WebDriverWait(driver, 5).until(
                       EC.presence_of_element_located((By.XPATH, go_stright))).click()

