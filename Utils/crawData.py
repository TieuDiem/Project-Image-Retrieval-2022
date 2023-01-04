
import time
import urllib.request
from threading import Thread
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


__all__=[
    
    "is_valid",
    "get_all_images",
    "main"
    
]
__doc__="""

* Using mutilthread for crawing data

"""
class GetImagesfromPages():
    def __init__(self, nThreads, npage, url_page):
        self.nThreads = nThreads
        self.npage = npage
        self.url_page = url_page

        self.result_urls = []
    
    def is_valid(self, url):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)
    
    def get_all_images(self, url):
        """
        Returns all image URLs on a single `url`
        """
        soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
        urls = []
        for img in soup.find_all("img"):
            img_url = img.attrs.get("data-src")

            if not img_url:
                # if img does not contain src attribute, just skip
                continue

            # make the URL absolute by joining domain with the URL that is just extracted
            img_url = urljoin(url, img_url)
            # remove URLs like '/hsts-pixel.gif?c=3.2.5'
            try:
                pos = img_url.index("?")
                img_url = img_url[:pos]
            except ValueError:
                pass

            # finally, if the url is valid
            if self.is_valid(img_url):
                urls.append(img_url)

        return urls
    
    def main(self, start, end):
        """
        Args:
            start (_type_): interger start page
            end (_type_): interger end page
        """
        for i in range(start,end):
            try:
                self.result_urls.extend(self.get_all_images(self.url_page + str(i)))
            except:
                pass
        
    def __call__(self):
        
        threads = []
        batch = self.npage//self.nThreads
        for i in range(0, self.npage, batch):
            start = i
            end = i + batch
           
            if end >= self.npage:
                end = self.npage + 1
            threads.append(Thread(target=self.main, args = (start, end)))
        
        start = time.time()
        for i in range(self.nThreads):
            threads[i].start()
        for i in range(self.nThreads):
            threads[i].join()
        end = time.time()
        
        print(f"Time handle pages = {end - start:.2f}s", )
    
        return self.result_urls


    
    