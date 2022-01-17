# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def test_buy_book():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.amazon.co.uk/books-used-books-textbooks/b/?ie=UTF8&node=266239&ref_=nav_cs_books")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="a-autoid-0"]').click()
    textbox_book_name = driver.find_element(By.ID, "twotabsearchtextbox")
    textbox_book_name.send_keys("the monk who sold his ferrari")
    driver.find_element(By.XPATH, "// input[ @ id = 'nav-search-submit-button']").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'The Monk Who Sold his Ferrari').click()
    sleep(1)
    driver.find_element(By.XPATH, "// input[ @ id = 'add-to-cart-button']").click()
    sleep(10)
    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_buy_book()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
