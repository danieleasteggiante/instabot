from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from login_function import login_function
from like_photo_hashtag import like_photo_hashtag
from comment_photo_hashtag import comment_photo_hashtag
from get_follower import get_follower
from get_list_from_file  import get_list_from_file

import sys








if __name__ == "__main__":

    function = input("select function\n 1 - like from list file \n 2 - comment from list file \n 3 - Get follower from list file \n")


    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome("C:\\Users\\dasteggiante\\Documents\\Hacking\\InstaBot\\chromedriver.exe", options=chrome_options)

    username_password_profileName = get_list_from_file('user_password.txt')


    list_hashtags = get_list_from_file('hashtag.txt')
    comment_list = get_list_from_file('comments.txt')
    login_function(username_password_profileName[0],username_password_profileName[1],driver)


    if function == "1":
        like_photo_hashtag(list_hashtags, driver)
    elif function == "2":
        comment_photo_hashtag(list_hashtags, comment_list, driver, number_comment_for_hashtag=4)
    elif function == "3":
        get_follower(driver, username= username_password_profileName[2])

    
    



