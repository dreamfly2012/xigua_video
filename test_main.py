import unittest
import os
from main import *

class TestMain(unittest.TestCase):
    def test_addaudio(self):
        video = "video.mp4"
        audio = "audio.mp4"
        addMusic(video, audio)
        self.assertTrue(os.path.exists("out_put.mp4"))

    
    def test_scrapy(self):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        scrapy_site()
        
        self.assertTrue(os.path.exists("video.mp4"))


if __name__ == '__main__':
    unittest.main()
