import urllib.request
from threading import Thread
import time
import random
__doc__ ="""

* Class supported dowload img based urls from web

"""
class DownloadImagesFromUrls():
    def __init__(self, nThreads, urls, destinate_folder):
        self.nThreads = nThreads
        self.urls = urls
        self.n = len(urls)
        self.destinate_folder = destinate_folder
        
    # Thread call function 
    def download_url(self, start, end):

        for i in range(start, end):
            a = random.random()
            try:
                urllib.request.urlretrieve(self.urls[i], f"{self.destinate_folder}/{a}.jpg")
            except:
                print(f"cannot access {self.urls[i]}")
            print('.', end=" ")         
                 
    def __call__(self):

        threads = []
        batch = self.n//self.nThreads
        for i in range(0, self.n, batch):
            start = i
            end = i + batch

            if end >= self.n:
                end = self.n 

            threads.append(Thread(target=self.download_url, args = (start, end)))

        start = time.time()
        for i in range(self.nThreads):
            threads[i].start()
        for i in range(self.nThreads):
            threads[i].join() 
        end = time.time()

        print(f"\nTime handle download urls = {end - start:.2f}s\n", )