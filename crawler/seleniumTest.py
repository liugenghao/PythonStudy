__Author__ = 'Bill Lau'
#自动化测试工具，解决JavaScript动态渲染问题，模拟点击、拖拽、滚动等操作
from pyquery import PyQuery
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
browser = webdriver.Chrome(chrome_options=options)

try:
    # browser.get('https://www.baidu.com')
    # browser.get('https://www.taobao.com')
    browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    browser.switch_to.frame('iframeResult')
    browser.implicitly_wait(2)#隐式等待
    #拖拽
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source,target)
    actions.perform()
    # list = browser.find_elements_by_css_selector('.service-bd li')
    # print(list)
    # soup = BeautifulSoup(browser.page_source, 'lxml')
    # doc = PyQuery(browser.page_source)
    # links = doc('a')
    # input = browser.find_element_by_id('kw')
    # input = browser.find_element_by_id('q')
    #查找页面中的元素
    # input_second = browser.find_element_by_css_selector('#q')
    # input_third = browser.find_element_by_xpath('//*[@id="q"]')
    # print(input,input_second,input_third)
    #向元素输入信息
    # input.send_keys('Python')
    #触发回车事件
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser,10)#显示等待，10秒内加载。。。
    # wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    # print(browser.current_url)
    # print(browser.get_cookies())
    # print(soup.select('a[data-cid="1"]'))
    # for item in soup.select('a[data-cid="1"]'):
    #     print(item['href'])
    #     print(item.get_text())
finally:
    pass
    # browser.close()