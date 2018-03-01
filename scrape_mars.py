
# coding: utf-8

# ### Nasa Mars News

# In[26]:


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time


# In[2]:


url ="https://mars.nasa.gov/news/8312/nearly-a-decade-after-mars-phoenix-landed-another-look/"
tweet_url ="https://twitter.com/MarsWxReport?lang=en"


# In[3]:


# Opening up connection, grabbing the page 
uClient = uReq(url)
page_html = uClient.read()
uClient.close()


# In[4]:


#html parsing
page_soup = soup(page_html, "html.parser")


# In[5]:


# Grabs data
containers = page_soup.findAll("div", {"class": "grid_layout"})
#containers


# In[6]:


news_title = containers[0].findAll("h1", {"class":"article_title"})
news_title[0].text.strip()


# In[7]:


news_p = containers[0].findAll("div", {"class":"wysiwyg_content"})
news_p[0].text.strip().replace('\r','').replace('\n','')


# ### Mars Weather

# In[8]:


# Opening up connection, grabbing the page 
uClient = uReq(tweet_url)
page_html = uClient.read()
uClient.close()


# In[9]:


#html parsing
page_soup = soup(page_html, "html.parser")


# In[10]:


# Grabs data
mars_weather = page_soup.findAll("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
mars_weather[0].text


# ### Mars Facts

# In[11]:


# Reading tabular data and creating dataframes.
mars_url = "http://space-facts.com/mars/"
tables = pd.read_html(mars_url)

df = tables[0]
df.columns = [0,1]
df.head(10)


# In[12]:


df= df.rename(columns={0:'Label',1:'Data'})

df.set_index('Data', inplace=True)

df.head(10)


# In[13]:


# Converting table to html table
html_table = df.to_html()
html_table


# In[14]:


# Cleaning table
html_table.replace('\n','')
html_table


# In[15]:


# Saving html file
df.to_html('mars_facts.html')


# In[16]:


# Scraping more Mars facts

# Opening up connection, grabbing the page 
uClient = uReq(mars_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")


# In[17]:


# Grabs facts data
mars_facts = page_soup.findAll("div", {"id":"facts"})
mars_facts[0].text.strip().replace('\n','')


# ### Mars Hemisperes

# In[47]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", 
     "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", 
     "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"},
    {"title": "Schiaparelli Hemisphere",
     "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere",
     "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]

hemisphere_image_urls


# ### JPL Mars Space Images

# In[19]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[ ]:


# Navigate the site and find the image url for the current Featured Mars Image
time.sleep(2)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image_url = soup.find(id= "fancybox-lock")
featured_image_url = image_url.find('img')['src']
#featured_image_url = soup.div.div.article["style"]
#featured_image_url = soup.div.img["src"]
featured_image_url

