{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "30019dde",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "from splinter import Browser \n",
    "from bs4 import BeautifulSoup as soup\n",
    "import requests\n",
    "import pandas as pd\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "38259e2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 94.0.4606\n",
      "Get LATEST driver version for 94.0.4606\n",
      "Driver [C:\\Users\\jillp\\.wdm\\drivers\\chromedriver\\win32\\94.0.4606.61\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "cc3c252c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# URL of page to be scraped\n",
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7b29ea79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<div class=\"list_text\">\n",
      "<div class=\"list_date\">September 28, 2021</div>\n",
      "<div class=\"content_title\">Nine Finalists Chosen in NASA's Mars 2020 Rover Naming Contest</div>\n",
      "<div class=\"article_teaser_body\">Nine finalists have been chosen in the essay contest for K-12 students across U.S. to name NASA's next Mars rover. Now you can help by voting for your favorite. </div>\n",
      "</div>\n"
     ]
    }
   ],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "\n",
    "slide_elem = news_soup.select_one('div.list_text')\n",
    "print(slide_elem)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "a77aac96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\">Nine Finalists Chosen in NASA's Mars 2020 Rover Naming Contest</div>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "8c694519",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Nine Finalists Chosen in NASA's Mars 2020 Rover Naming Contest\""
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_title=slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "40c1b520",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Nine finalists have been chosen in the essay contest for K-12 students across U.S. to name NASA's next Mars rover. Now you can help by voting for your favorite. \""
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_p=slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45ad6b1e",
   "metadata": {},
   "source": [
    "JPL Space Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "7bcd4e93",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "1bfde28a",
   "metadata": {},
   "outputs": [],
   "source": [
    "full_image_elem=browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "a83629d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "image_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "822c0a40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "image/featured/mars2.jpg\n"
     ]
    }
   ],
   "source": [
    "img_url_rel = image_soup.find('img', class_= 'fancybox-image').get('src')\n",
    "print(img_url_rel)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7363f309",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87373041",
   "metadata": {},
   "source": [
    "Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "037e3e85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mars - Earth Comparison</td>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 ?? 10^23 kg</td>\n",
       "      <td>5.97 ?? 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-87 to -5 ??C</td>\n",
       "      <td>-88 to 58??C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         0                1                2\n",
       "0  Mars - Earth Comparison             Mars            Earth\n",
       "1                Diameter:         6,779 km        12,742 km\n",
       "2                    Mass:  6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       "3                   Moons:                2                1\n",
       "4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "5          Length of Year:   687 Earth days      365.24 days\n",
       "6             Temperature:     -87 to -5 ??C      -88 to 58??C"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')\n",
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "6034e1a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Description</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mars - Earth Comparison</td>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 ?? 10^23 kg</td>\n",
       "      <td>5.97 ?? 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Description             Mars            Earth\n",
       "0  Mars - Earth Comparison             Mars            Earth\n",
       "1                Diameter:         6,779 km        12,742 km\n",
       "2                    Mass:  6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       "3                   Moons:                2                1\n",
       "4       Distance from Sun:   227,943,824 km   149,598,262 km"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns=['Description', 'Mars', 'Earth']\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "f19ff9ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 ?? 10^23 kg</td>\n",
       "      <td>5.97 ?? 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "Description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.set_index('Description', inplace=True)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "f189799d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>Description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 ?? 10^23 kg</td>\\n      <td>5.97 ?? 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 ??C</td>\\n      <td>-88 to 58??C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table = df.to_html()\n",
    "table"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e9641da",
   "metadata": {},
   "source": [
    "Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "3ff5e145",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://marshemispheres.com/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "a1f691c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemispheres_list  = []\n",
    "\n",
    "links = browser.find_by_css('a.product-item img')\n",
    "\n",
    "for i in range(len(links)): \n",
    "    hemisphere = {}\n",
    "    \n",
    "    browser.find_by_css('a.product-item img')[i].click()\n",
    "    \n",
    "    sample_image = browser.links.find_by_text('Sample').first\n",
    "    hemisphere['img_url'] = sample_image['href']\n",
    "    \n",
    "    hemisphere['title'] = browser.find_by_css('h2.title').text\n",
    "    \n",
    "    hemispheres_list.append(hemisphere)\n",
    "    \n",
    "    browser.back()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "11dc8d15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'https://marshemispheres.com/images/full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemispheres_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "cf641cf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
