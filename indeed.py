import requests
import json
import re
from bs4 import BeautifulSoup
def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('/Users/fange/Desktop/indeed/indeed.csv', 'a', encoding='UTF-8') as f:
        #/Users/fange/Desktop/indeed/indeed.csv   （fange）改成你自己电脑的路径 桌面新建一个文件夹
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()
page = 0
while page<60: #修改大小可以爬很多页60代表前6页 70-》7
    page = page+10
    url = 'https://au.indeed.com/jobs?q=&l=New+South+Wales&start=' + str(page)
    html = requests.get(url)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, 'html.parser')


        results = soup.find_all('div', class_=['row','result'])
        #获取每一个小块工作信息
        for result in results:
            jobtitle = result.find('div',class_='title').a.text
            jobtitle = jobtitle.replace(',','')
            jobtitle = jobtitle.replace('[','')
            company = result.find('span',class_='company')
            if company == None:
                company = 'Null'
            else:
                company = company.text
                company = company.replace(',','')
            location = result.find('div',class_="location accessible-contrast-color-location")
            if location == None:
                location = 'Null'
            else:
                location = location.text
                location = location.replace(',','-')
            salary = result.find('span',class_='salaryText')
            if salary == None:
                salary = 'Null'
            else:
                salary = salary.text
                salary = salary.replace(',','')

            summary = result.find('div',class_='summary').text

            summary = summary.replace(',',' ')
            summary = summary.replace(']','')

            jobdetail=jobtitle,company,location,salary,summary
            #组装最后结果
            jobdetail = [x.strip() for x in jobdetail]
            # 去除所有空格和/n
            write_item_to_file(jobdetail)
            #写文件


























