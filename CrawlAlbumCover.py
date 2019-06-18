from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os

class AlbumCover():

    def __init__(self):
        self.init_url = "http://music.163.com/#/artist/album?id=101988&limit=120&offset=0" #the URL
        self.folder_path = "C:\D\TheBeatles" #Storage path

    #save image
    def save_img(self, url, file_name):  
        print('Start requesting the image address, the process will be a bit long')
        img = self.request(url)
        print('Start saving pictures')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, 'Picture saved successfully！')
        f.close()

    #Packaged requests
    def request(self, url): 
        r = requests.get(url)  #Return a response object
        return r

    #Create a folder
    def mkdir(self, path):  
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('Folder name：', path)
            os.makedirs(path)
            print('Created successfully！')
            return True
        else:
            print(path, 'The folder already exists')
            return False

    # Get a list of file names in the folder
    def get_files(self, path):  
        pic_names = os.listdir(path)
        return pic_names

    def spider(self):
        print("Start!")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path='D:\Anaconda3\chromedriver\chromedriver', chrome_options=chrome_options)
        driver.get(self.init_url)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source

        self.mkdir(self.folder_path)  
        print('Start switching folders')
        os.chdir(self.folder_path)  # Switch the path to the folder created above

        file_names = self.get_files(self.folder_path)  # Get all file names in the folder, type is list

        all_li = BeautifulSoup(html, 'lxml').find(id='m-song-module').find_all('li')
        # print(type(all_li))

        for li in all_li:
            album_img = li.find('img')['src']
            album_name = li.find('p', class_='dec')['title']
            album_date = li.find('span', class_='s-fc3').get_text()
            end_pos = album_img.index('?')
            album_img_url = album_img[:end_pos]

            photo_name = album_date + ' - ' + album_name.replace('/', '').replace(':', ',') + '.jpg'
            print(album_img_url, photo_name)

            if photo_name in file_names:
                print('Image already exists')
            else:
                self.save_img(album_img_url, photo_name)

album_cover = AlbumCover()
album_cover.spider()
