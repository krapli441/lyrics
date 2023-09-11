from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 웹 드라이버 설정
driver = webdriver.Chrome()

# 웹 페이지 접근
driver.get('https://www.melon.com/song/detail.htm?songId=8271355')

# 웹 페이지 스크린샷 저장
driver.save_screenshot('melon.png')

load_more_button_selector = 'div.wrap_lyric button.button_more'

load_more_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, load_more_button_selector))
)

# 버튼 클릭
load_more_button.click()

# # 가사를 가져오기 위한 CSS 선택자
lyrics_selector = 'div#d_video_summary'

# CSS 선택자를 이용하여 웹 페이지에서 헤드라인 뉴스를 가져옴
lyrics = driver.find_elements(by=By.CSS_SELECTOR, value=lyrics_selector)
print(f'수집한 가사 : {lyrics_selector}')

# 가져온 가사를 출력
for index, headline in enumerate(lyrics):
    print(f"{index+1}. {headline.text.strip()}")

# 원하는 데이터 가져오기
page_title = driver.title
print(f'페이지의 타이틀: {page_title}')