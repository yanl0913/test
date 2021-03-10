from selenium import webdriver


class BasePage(object):
    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def locator(self, locator):
        return self.driver.find_element(*locator)

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    # 访问URL
    def visit(self, url):
        self.driver.get(url)
