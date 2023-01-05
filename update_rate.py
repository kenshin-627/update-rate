import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import streamlit as st
import os

def main():
    # 自分のスマメイトのurl
    my_url = f"https://smashmate.net/user/{settings.MY_ID}/"
    
    # Chromeのドライバーの設定
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    # レート表示用のプレースホルダー
    rate_holder = st.empty()
    
    while True:
        try:
            # 自分のスマメイトのページからレート情報とってきて表示(5秒休憩)
            driver.get(my_url)
            rate = driver.find_elements(By.CLASS_NAME, "rate_text")[0].text.split()[0]
            rate_holder.markdown(f"# {rate}")
            print(rate)
            time.sleep(5)
        except KeyboardInterrupt:
            break
    driver.close()
    
if __name__ == "__main__":
    main()