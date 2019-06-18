# Crawl-album-cover
Project Overview: Catch the album cover of TheBeatles Netease Cloud Music
Use packages: selenium, BeautifulSoup, requests
Crawl process: 1) Connect to Chrome using selenium .webdriver, request url
           2) Connect to the iframe frame of the web page and get html
           3) Analyze html using BeautifulSoup
           4) Save the picture and name it according to the information about the album
Result: Climbing 120 pictures and naming it takes about 20min
