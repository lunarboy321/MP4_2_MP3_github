from moviepy.editor import *
# import moviepy.editor
# import moviepy
import moviepy
import moviepy.editor
# import os
from moviepy.editor import afx
# from moviepy.audio
#逐个转换
#保存为MP3

#修改文件夹下所有xml文件中的中文路径
def changesku(inputpath):
    listdir = os.listdir(inputpath)#获得所有文件名
    mp4namelist = [name for name in listdir if name.endswith('.mp4')]
    for file in mp4namelist:

        filepath = os.path.join(inputpath, file)#将根路径与文件名路径组合成绝对路径
        video = VideoFileClip(filepath)
        list_filepath = list(filepath)
        list_filepath[-1] = '3'
        #判断MP3是否已存在
        if list_filepath in listdir:
            continue
        filepath = ''.join(list_filepath)
        print(filepath)
        audio = video.audio
        audio.write_audiofile(filepath)


if __name__ == '__main__':
    # vediopath = 'C:\\CloudMusic\\MV\\MV'  # 这是xml文件的文件夹的绝对地址
    videopath = './video_path'  # 这是xml文件的文件夹的绝对地址
    changesku(videopath)