
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 웹 드라이버 설정
driver = webdriver.Chrome()

# 웹 페이지 접근
driver.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100')

# 더 보기 버튼을 누르기 위한 CSS 선택자
load_more_button_selector = 'div.cluster_more a.cluster_more_inner'

# 더 보기 버튼을 누르는 코드. load_moare_button_selector 요소가 나타날 때까지 10초동안 기다리도록 함.
load_more_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, load_more_button_selector))
)

# 버튼 클릭
load_more_button.click()

# 헤드라인 뉴스 제목을 가져오기 위한 CSS 선택자
headlines_selector = 'ul.sh_list li.sh_item div.sh_text a.sh_text_headline'

# CSS 선택자를 이용하여 웹 페이지에서 헤드라인 뉴스를 가져옴
headlines = driver.find_elements(by=By.CSS_SELECTOR, value=headlines_selector)
# print(f'수집한 헤드라인 : {headlines}')

# 가져온 헤드라인 뉴스 제목을 출력
for index, headline in enumerate(headlines):
    print(f"{index+1}. {headline.text.strip()}")

# 원하는 데이터 가져오기
page_title = driver.title
print(f'페이지의 타이틀: {page_title}')