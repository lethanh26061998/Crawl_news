dict_data = {
# 1 item bao gom cac truong du lieu: title, content, time, tag, outlink, search_input, next_page, isloadmore,links
<<<<<<< HEAD
# #1-next: ok -> ok
# 'https://vietnammoi.vn':
#     [
#     '//h1[@id="title-article"]',
#     ['//div[@class="sapo margin-20-bottom"]', '//div[@class="entry-body"]//p'],
#     '//span[@class="time left"]/span',
#     '',
#     ['//ul[@class="related-news margin-25-bottom detailpopup"]//li//a'],
#     '//*[@id="search"]',
#     '(//ul[@class="pager right margin-25-top"]/li)[last()]',
#     '',
#     '//ul[@class="news-stream clearafter"]/li/a'
# ],
=======
#1-next: ok -> ok
'https://vietnammoi.vn':
    [
    '//h1[@id="title-article"]',
    ['//div[@class="sapo margin-20-bottom"]', '//div[@class="entry-body"]//p'],
    '//span[@class="time left"]/span',
    '',
    ['//ul[@class="related-news margin-25-bottom detailpopup"]//li//a'],
    '//*[@id="search"]',
    '(//ul[@class="pager right margin-25-top"]/li)[last()]',
    '',
    '//ul[@class="news-stream clearafter"]/li/a'
],
>>>>>>> c0c5acdd8507d0c42c9c10b127f9daf407b46b95
#2-xem them: ok
# 'https://tuoitre.vn':
#     ['//h1[@class="article-title"]',
#     ['//div[@class="main-content-body"]//h2[@class="sapo"]', '//div[@id="main-detail-body"]//p'],
#     '//div[@class="date-time"]',
#     '//ul[@class="tags-wrapper"]//li//a',
#     ['//div[@class="box-worldcup-2018 typeother"]//ul//li//a'],
#     '//*[@id="search-frm"]/input',
#     '',
#     '//div[@class="readmore fl"]//a',
#     '//ul[@class="list-news-content"]/li/a'
# ],
#3-next: ok
<<<<<<< HEAD
# 'https://vov.vn':
# [
#     '//h2[@class="article__title"]',
#     ['//div[@class="article__head"]//h4//div', '//div[@class="text-long"]/p'],
#     '//div[@class="article__time"]//a',
#     '//div[@class="tags"]//a',
#     ['//div[@class="news-list__content"]/div/div/a'],
#     '//*[@id="edit-keyword"]',
#     '//li[@class="pager__item pager__item--next"]//a',
#     '',
#     '//div[@class="views-element-container"]//div/div/div/a'
=======
'https://vov.vn':
[
    '//h2[@class="article__title"]',
    ['//div[@class="article__head"]//h4//div', '//div[@class="text-long"]/p'],
    '//div[@class="article__time"]//a',
    '//div[@class="tags"]//a',
    ['//div[@class="news-list__content"]/div/div/a'],
    '//*[@id="edit-keyword"]',
    '//li[@class="pager__item pager__item--next"]//a',
    '',
    '//div[@class="views-element-container"]//div/div/div/a'
],
#4-xem them: 
# 'https://kenh14.vn':
# [
    # '//h1[@class="kbwc-title"]',
    # ['//h2[@class="knc-sapo"]', '//div[@class="knc-content"]//p'],
    # '//span[@class="kbwcm-time"]',
    # '//ul[@class="knt-list"]//li//a',
    # ['//div[@class="knc-rate-link"]//a', '//div[@class="adm_sponsor5_content_box"]//div[@class="adm_sponsor5_new-header"]//a'],
    # '//*[@id="searchinput"]',
    # '',
    # '//*[@id="lastPage"]',
    # '//ul[@class="knsw-list"]/li//div/a',
>>>>>>> c0c5acdd8507d0c42c9c10b127f9daf407b46b95
# ],
# #4-xem them: 
'https://kenh14.vn':
[
    '//h1[@class="kbwc-title"]',
    ['//h2[@class="knc-sapo"]', '//div[@class="knc-content"]//p'],
    '//span[@class="kbwcm-time"]',
    '//ul[@class="knt-list"]//li//a',
    ['//div[@class="knc-rate-link"]//a', '//div[@class="adm_sponsor5_content_box"]//div[@class="adm_sponsor5_new-header"]//a'],
    '//*[@id="searchinput"]',
    '',
    '//div[@class="view-more-detail clearboth"]//a',
    '//ul[@class="knsw-list"]/li//div/a',
],
#5-next: ok
'https://timkiem.vnexpress.net/':
[
    '//h1[@class="title-detail"]',
    ['//p[@class="description"]', '//article[@class="fck_detail "]//p'],
    '//span[@class="date"]',
    '//div[@class="tags"]//h2//a',
    ['//ul[@class="list-news  gaBoxLinkDisplay"]/li/a'],
    '//*[@id="search_q"]',
    '(//div[@class="button-page flexbox"]/a)[last()]',
    '',
    '//div[@class="width_common list-news-subfolder"]/article//div//a'
],
# 'https://ncov.moh.gov.vn':
# [
    # '//h3[@class="header-title"]//span',
    # ['//div[@class="journal-content-article"]//p'],
    # '//span[@class="text-ngayxam-page"]',
    # '',
    # []
# ],
}
