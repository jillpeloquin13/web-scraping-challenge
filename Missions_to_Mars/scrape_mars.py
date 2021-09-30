from splinter import Browser 
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com'
    browser.visit(url)

    browser.is_element_present_by_css('div.list_text', wait_time=1)
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')
    slide_elem.find('div', class_='content_title')
    news_title=slide_elem.find('div', class_='content_title').get_text()
    news_p=slide_elem.find('div', class_='article_teaser_body').get_text()


    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    full_image_elem=browser.find_by_tag('button')[1]
    full_image_elem.click()
    html = browser.html
    image_soup = soup(html, 'html.parser')
    img_url_rel = image_soup.find('img', class_= 'fancybox-image').get('src')
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'


    df = pd.read_html('https://galaxyfacts-mars.com')
    df = pd.read_html('https://galaxyfacts-mars.com')[0]
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    table = df.to_html('table.html')


    url = 'https://marshemispheres.com/'
    browser.visit(url)
    hemispheres_list  = []

    links = browser.find_by_css('a.product-item img')

    for i in range(len(links)): 
        hemisphere = {}
        
        browser.find_by_css('a.product-item img')[i].click()
        
        sample_image = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_image['href']
        
        hemisphere['title'] = browser.find_by_css('h2.title').text
        
        hemispheres_list.append(hemisphere)
        
        browser.back()
        
    mars_data = {
        "mars_url": img_url,
        "mars_table": table,
        "mars_title": news_title, 
        "mars_p": news_p, 
        "mars_hl": hemispheres_list
    }

    browser.quit()

    return mars_data