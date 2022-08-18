from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_follower(driver, profile):
    driver.get("https://www.instagram.com/" + profile + "/")
    follower_a = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a"

    WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, follower_a))).click()

    follower_modal_path = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]"
    follower_modal = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, follower_modal_path)))
    time.sleep(3)
    last = 0
    height_scroll = 1

    while last != height_scroll:

        last = height_scroll

        height_scroll = driver.execute_script(
                    """
                    arguments[0].scrollTo(0,arguments[0].scrollHeight);
                    return arguments[0].scrollHeight;
                    """, 
                    follower_modal
                )
        time.sleep(1)

    links = follower_modal.find_elements(By.TAG_NAME, "a")
    names =[]
    for i in links:
        if i.text != "":
            names.append(i.text)

    f = open("followers.txt", "w")
    for e in names:
        f.write(e + "\n")
   
    f.close()