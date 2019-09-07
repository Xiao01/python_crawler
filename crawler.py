
#代码来源：https://www.cnblogs.com/xuehaiwuya0000/p/10734004.html
# -*- coding: UTF-8 -
# 爬取豆瓣网站关于python的书籍，爬虫完一页后，点击后页菜单循环爬虫
# 缺点：逐页点击并获得数据较费时
import time
from selenium import webdriver


class url_surf(object):
    def surf_web(self, url):
        num = 1
        driver = webdriver.Chrome("/Users/xjq/Downloads/chromedriver")
        driver.get(url)
        time.sleep(5)

        while 1:
            ele = driver.find_elements_by_class_name(r"detail")
            file = open('python_data3.csv', 'a', encoding='utf-8')
            file.write('_openid,title,bookurl \n')
            for i in ele:
                print('ele: %s' % i)
                title = i.find_element_by_class_name("title-text")
                bookurl = title.get_attribute('href')
                file.write('oaqqm5GeNdxCFzEjeFcqDTCGGRtk,'+title.text +','+ bookurl)
                file.write('\n')
                print(num, bookurl)
            num += 1
            print('is searching page: %s' % num)
            try:  # 搜索到最后一页，next没办法点击或者没有后页的标签，则确认已结束
                next_page = driver.find_element_by_class_name('next')
                next_page.click()
            except:
                file.close()
                print('game over')
                break
            time.sleep(5)


if __name__ == "__main__":
    url = "https://book.douban.com/subject_search?search_text=Java+&cat=1001&start=0"
    a = url_surf()
    a.surf_web(url) # 爬取豆瓣网站关于python的书籍，爬虫完一页后，点击后页菜单循环爬虫
