from selenium import webdriver

# 웹 드라이버 설정
driver = webdriver.Chrome()

# 웹 페이지 접근
driver.get('https://www.naver.com')

# 웹 페이지 스크린샷 저장
driver.save_screenshot('naver_homepage.png')

# 원하는 데이터 가져오기
page_title = driver.title
print(f'페이지의 타이틀: {page_title}')