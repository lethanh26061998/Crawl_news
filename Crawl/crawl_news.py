import re
import time
import schedule
import csv

try:
	import urlparse
except ImportError:
	import urllib.parse as urlparse
from listweb_search import dict_data
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from pandas import DataFrame

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
	'chromedriver_linux64/chromedriver', chrome_options=options)
# actions = ActionChains(driver)
options.add_argument('--headless')

keys = [
	# "tin hot",
	# "n-cov",
	# "covid-19",
    # "vắc xin covid",
    # "khẩu trang mùa covid",
    # "cách ly",
    # "hồi phục covid",
    # "bầu cử tại mỹ",
    # "tin mới nhất về covid-19",
    # "covid tại châu Âu",
    # "covid tại Vũ Hán",
    # "triệu trứng covid"
	"tin mới",
	"tin nóng",
	"corona",
	"hôm nay",
	"tình hình",
	"ca nhiễm mới",
	"dịch tại Việt Nam",
	"y tế",
	"bệnh viện quá tải",
	"hậu quả covid",
	"xét nghiệm covid",
	"lây lan",
	"miễn dịch"
]
print("===START========")
# txt_site = 'or'.join(list_web)
def get_link(xpath_links):
	arr_links_page = []
	try:
		arr_links = driver.find_elements_by_xpath(xpath_links)
		arr_links_page = [element.get_attribute('href') for element in arr_links]
	except:
		pass
	# arr_links_page = list(set(arr_links_page))
	return arr_links_page

compile_regex = re.compile(r'(Nguồn):? (http://.*)|>>XEM THÊM:.*|\(.*\)\s?-\s|\(.*\)\s?–| NDĐT - ')
def get_info(link, xpath_title, xpath_content, xpath_time, xpath_tag, xpath_outlink):
	title = ''
	content = ''
	time_article = ''
	public_date = 0
	arr_tag = []
	time.sleep(5)
	driver.get(link)
	time.sleep(5)
	title = driver.find_element_by_xpath(xpath_title).text

	try:
		for _ in xpath_content:
			arr_content = driver.find_elements_by_xpath(_)
			for elem in arr_content:
				content += (' '+ elem.text)
		content = re.sub('\s\s+', ' ', content)
		content = compile_regex.sub('',content)

	except:
		content = ''
	
	time_article = driver.find_element_by_xpath(xpath_time).text
	time_article = re.sub(r'([^0-9\s:]+?)', '', time_article).strip()
	arr_time = time_article.split(' ')
	date_article = [elem for elem in arr_time if len(elem) >=4 and elem.find(':')<0][0]
	hour_article = [elem for elem in arr_time if elem.find(':')>=0][0]
	time_article = date_article + ' ' + hour_article
	try:
		public_date = datetime.strptime(time_article, '%d%m%Y %H:%M')
		public_date = public_date.timestamp() * 1000
	except:
		try:
			public_date = datetime.strptime(time_article, '%d%m%Y %H:%M:%S')
			public_date = public_date.timestamp() * 1000
		except:
			public_date = ''
	try:
		arr_tag = driver.find_elements_by_xpath(xpath_tag)
		tag = ''
		for elem in arr_tag:
			tag += (elem.text.strip() +'#')
		tag = tag.replace('##', '#')
	except:
		tag = ''
	if len(xpath_outlink) > 0:
		outlink = []
		for elem in xpath_outlink:
			arr_outlink = driver.find_elements_by_xpath(elem)
			outlink += [elem.get_attribute('href') for elem in arr_outlink]
		outlink = list(set(outlink))
	else:
		outlink = []
	return title, content, time_article, date_article, public_date

def main():
	try:
		for key in keys:
			for url, value in dict_data.items():
				xpath_title, xpath_content, xpath_time, xpath_tag, xpath_outlink, xpath_search, xpath_next, xpath_isloadmore, xpath_links = value[
					0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8]
				driver.get(url)
				time.sleep(2)
				search = driver.find_element_by_xpath(xpath_search)
				search.send_keys(key)
				search.send_keys(Keys.ENTER)
				time.sleep(10)
				current_link = driver.current_url
				##
				if xpath_isloadmore != '':
					# print(url, " === isloadmore")
					try:
						i = 1
						driver.get(current_link)
						load_more = driver.find_element_by_xpath(xpath_isloadmore)
						while load_more:
							i = i + 1
							load_more.click()
							time.sleep(5)
							load_more = driver.find_element_by_xpath(xpath_isloadmore)
							print("load_more", i)
							time.sleep(2)
					except:
						pass	
					print("done load_more!")
					try:
						current_link = driver.current_url
						driver.get(current_link)
						time.sleep(5)
						arr_links = []
						arr_links = get_link(xpath_links)
						# print("arr links load_more: ", arr_links)
						for link in arr_links:
							info_link = get_info(link, xpath_title, xpath_content, xpath_time, xpath_tag, xpath_outlink)
							time.sleep(2)
							writer.writerow(info_link)
						print("Done first page of keyword: ", key, "from website: ", url)
					except:
						pass
					##
				if xpath_next != '':
					arr_links_page = get_link(xpath_links)
					for link in arr_links_page:
						try:
							info_link = get_info(link, xpath_title, xpath_content, xpath_time, xpath_tag, xpath_outlink)
							# print("Info link: ", info_link)
						except:
							pass
						time.sleep(3)
					print("Done first page of keyword: ", key, "from website: ", url) 
					try:
						i = 1
						driver.get(current_link)
						next_page = driver.find_element_by_xpath(xpath_next)
						print("Done first page!")
						while next_page:
							i = i + 1
							next_page.click()
							time.sleep(5)
							print("Page: ", i, " ,start crawl...!")
							current_link = driver.current_url
							driver.get(current_link)
							arr_links_page_next = []
							arr_links_page_next = get_link(xpath_links)
							for link in arr_links_page_next:
								info_link = get_info(link, xpath_title, xpath_content, xpath_time, xpath_tag, xpath_outlink)
								time.sleep(2)
								writer.writerow(info_link)
							driver.get(current_link)
							next_page = driver.find_element_by_xpath(xpath_next) 
					except:
						pass
					print("Crawled data: ", key, "from website:", url)
			print("===> Crawled data of keyword: ", key, "from all websites")
		print("=======Crawled all data!=======")
	except:
		pass


# schedule.every().hour.do(main)

# while True:
	# schedule.run_pending()
	# time.sleep(1)


if __name__ == "__main__":	
	# driver.close()
	# driver.quit()
	
	start_time = time.time()								
	with open ('crawl_news_test.csv','w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['title', 'content', 'time_article', 'date_article', 'public_date'])
		main()
	finish_time = time.time()
	print("Total run-time: %f s" % (finish_time - start_time))
