from selenium import webdriver

# 웹 드라이버 설정
driver = webdriver.Chrome()

# 웹 페이지 접근
driver.get('https://www.naver.com')

# 원하는 데이터 가져오기
page_title = driver.title
print(f'Page Title: {page_title}')