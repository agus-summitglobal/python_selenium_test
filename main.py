import time
from selenium import webdriver


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.gsmarena.com/")
        title = driver.title
        print(title)
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
