# Crawl-album-cover
Project Overview: Catch the album cover of TheBeatles Netease Cloud Music  

Use packages: selenium, BeautifulSoup, requests  

Crawl process:   

&emsp;&emsp;&emsp;1) Connect to Chrome using selenium .webdriver, request url  

&emsp;&emsp;&emsp;2) Connect to the iframe of the web page and get html  

&emsp;&emsp;&emsp;3) Analyze html using BeautifulSoup  

&emsp;&emsp;&emsp;4) Save the picture and name it according to the information about the album  

Result: Climbing 120 pictures and naming it takes about 66.9s

!()[ResultPic/processing.png]  
  
!()[ResultPic/result.png]  
