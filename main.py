from selenium import webdriver
from time import sleep
import sys
import time
import urllib.request
import moviepy.editor as me
#驱动路径 记得前面加r 防止字符转义
#!!!注意这里必须把驱动程序中的路径写完整，后面必须加上这个chromedriver.exe  否则会报错 执行不成功

def allbackfunc(blocknum, blocksize, totalsize):
    '''回调函数

    @blocknum: 已经下载的数据块

    @blocksize: 数据块的大小

    @totalsize: 远程文件的大小

    '''

    percent = 100.0 * blocknum * blocksize / totalsize

    if percent > 100:

        percent = 100

        #格式化输出，%相当于转义

    print ("%.2f%%"% percent)

def addMusic(video, audio):
    # 读取视频    
    videoclip = me.VideoFileClip(video)
    audioclip = me.AudioFileClip(audio)
    # 设置视频的音频   
    new_audioclip = me.CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    # 保存视频
    videoclip.write_videofile("output_video.mp4", threads = 8, fps=24)

def scray_site():
    driver = webdriver.Chrome('./chromedriver')
    #用driver打开百度页面  后面的地址是百度的地址
    url = 'https://www.ixigua.com/7083014337547371049'
    audio_str = 'return window.atob(window._SSR_HYDRATED_DATA.anyVideo.gidInformation.packerData.video.videoResource.dash_120fps.dynamic_video.dynamic_audio_list.pop().main_url);'

    video_str = 'return window.atob(window._SSR_HYDRATED_DATA.anyVideo.gidInformation.packerData.video.videoResource.dash_120fps.dynamic_video.dynamic_video_list.pop().main_url);'


    driver.get(url)
    time.sleep(5)
    audio_url = driver.execute_script(audio_str)
    video_url = driver.execute_script(video_str)
    #退出驱动程序
    driver.quit()
    urllib.request.urlretrieve(video_url, './video.mp4', allbackfunc)
    urllib.request.urlretrieve(audio_url, './audio.mp4', allbackfunc)


if __name__ == "__main__":
    addMusic("video.mp4", "audio.mp4")
    pass




