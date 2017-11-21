
import requests
from scrapy.selector import Selector
import pymysql
import re

def obtain_ip():
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    for i in range(15):
        url = "http://www.httpsdaili.com/?stype=1&page={0}".format(i)
        response = requests.get(url, headers=header)
        # response1 = str(response.content, 'utf-8')
        selector = Selector(text=response.text)
        contents = selector.xpath("//tr[@class='odd']")
        for content in contents:
            link = content.xpath("./td[@class='style1']/text()").extract()[0]
            port = content.xpath("./td[@class='style2']/text()").extract()[0]
            type = content.xpath("./td[@class='style4']/text()").extract()[0]
            print(link+" "+port+" "+type)
            compile = re.compile(r"\d+")
            speed_compile = content.xpath("./td[@class='style6']/text()").extract()[0]
            speed = float(compile.match(speed_compile).group())
            save_data(link)
            save_database(link, port, speed)

def save_data(url):
    f = open("list.txt", "ab")
    f.write(("http://"+url+"\n").encode("utf-8"))
    f.close()

def save_database(link,port,speed):
    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="xici", charset="utf8")
    cursor = conn.cursor()
    cursor.execute(
                "insert ip_list(ip, port, speed, proxy_type) VALUES('{0}', '{1}', {2}, 'HTTP')".format(
                    link, port, speed
                )
            )
    conn.commit()

if __name__ == "__main__":
    obtain_ip()
