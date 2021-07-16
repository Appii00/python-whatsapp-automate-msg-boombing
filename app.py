from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager  # 1st changer


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())  # 2nd change
    driver.get('https://web.whatsapp.com/')

    name = "Unbeatable IT Champs 🏆"# please enter a name what you saved in your contects and make sure you unachevied that contect
    msg = "Me fenil madarchod hu\n ji ha hu aur rahunga"
    count = 200 #here you can set msg count...................... 

    input('Enter any key after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    # The classname of message box may vary.
    msg_box = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        # The classname of send button may vary.
        button = driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[3]/button')
        button.click()
    print('Bombing Complete!!')


main()
