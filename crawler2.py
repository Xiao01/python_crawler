#代码来源：https://www.cnblogs.com/xuehaiwuya0000/p/10734004.html
# -*- coding: UTF-8 -
# 爬取豆瓣网站关于python的书籍，采用多线程爬虫
# 缺点：爬虫速度，很快，但爬完一次后，提示需要登录账号，被反爬虫了
import time
from multiprocessing import Pool
from selenium import webdriver


class url_surf(object):
    def __init__(self, url):
        self.url = url

    def surf_web(self, a):
        num = a
        driver = webdriver.Chrome("/Users/xjq/Downloads/chromedriver")
        file = open('python_data2.csv', 'a', encoding='utf-8')
        file.write('title,bookurl \n')
        while 1:
            driver.get(self.create_url(num))
            time.sleep(5)
            ele = driver.find_elements_by_class_name(r"detail")
            for i in ele:
                print('ele: %s' % i)
                title = i.find_element_by_class_name("title-text")
                bookurl = title.get_attribute('href')
                file.write(title.text +','+ bookurl)
                file.write('\n')
                print(num, bookurl)
            num += 10
            print('is searching page: %s' % num)
            try:  # 搜索到最后一页，next没办法点击或者没有后页的标签，则确认已结束
                next_page = driver.find_element_by_class_name('next')
            except:
                # file.close()
                print(num, ':game over')
                break
            time.sleep(5)

    def create_url(self, k):
        return self.url + str(int(k * 15 - 15))


if __name__ == "__main__":
    url = "https://book.douban.com/subject_search?search_text=%E5%B0%8F%E7%A8%8B%E5%BA%8F&cat=1001&start="
    a = url_surf(url)
    pool = Pool(5)
    for i in range(1, 11):
        pool.apply_async(a.surf_web, (i,))
    pool.close()
    pool.join()