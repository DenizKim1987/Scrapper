import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self):
        self.job_db = []
        self.skills = []
        self.base_urls = [
            "https://berlinstartupjobs.com/skill-areas/{}/",
            "https://web3.career/{}-jobs",
            "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={}"
        ]
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

    def scrap(self, url):
        response = requests.get(url, headers = self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    
    def append_db(self, c, t, d, l, link):
        job_data = {
            "company" : c.text,
            "title" : t.text,
            "description" : d.text,
            "location" : l.text,
            "link" : link,
        }
        self.job_db.append(job_data)

    def scrap_berlin(self, url):
        soup = self.scrap(url)
        jobs = soup.find()
        for job in jobs:
            company = job.find()
            title = job.find()
            description = job.find()
            location = job.find()
            link =job.find().find("a")["href"]
            self.append_db(company, title, description, location, link)

    def scrap_web3(self, url):
        soup = self.scrap(url)
        jobs = soup.find()
        for job in jobs:
            company = job.find()
            title = job.find()
            description = job.find()
            location = job.find()
            link =job.find().find("a")["href"]
            self.append_db(company, title, description, location, link)

    def scrap_wework(self, url):
        soup = self.scrap(url)
        jobs = soup.find()
        for job in jobs:
            company = job.find()
            title = job.find()
            description = job.find()
            location = job.find()
            link =job.find().find("a")["href"]
            self.append_db(company, title, description, location, link)

    

# Flask를 사용해 잡 스크래퍼의 프론트엔드를 구축합니다.
# 유저는 python, javascript, java 등과 같은 용어를 검색할 수 있어야 합니다.
# 스크래퍼는 berlinstartupjobs.com, weworkremotely.com 및 web3.career의 결과를 표시해야 합니다.
# 우리는 이미 berlinstartupjobs.com 스크래퍼에 대한 코드가 있으므로 weworkremotely.com 및 web3.career를 스크래핑하는 코드를 작성해야 합니다.
# 검색 URL은 다음과 같습니다:
# https://berlinstartupjobs.com/skill-areas// where <s> is the search term (i.e https://berlinstartupjobs.com/skill-areas/python/) https://web3.career/-jobs where <s> is the search term (i.e https://web3.career/python-jobs) https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term= where <s> is the search term (i.e https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=python)

