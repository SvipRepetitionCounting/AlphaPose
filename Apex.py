# -*- coding: utf-8 -*-
"""找峰值"""
import os
from datawash import DataWash
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import moviepy.editor as mp
# 本地视频位置
from moviepy.video.VideoClip import TextClip


def find_apex(data):
    points = np.array(data)
    x_ = np.arange(0, len(points), 1)
    y_ = points[:, 1]
    y_min = min(y_)
    y_max = max(y_)
    distance = None  # 相邻峰值之间的最小水平距离，越小去噪越严格
    height_base = y_min + (y_max - y_min) * 0.6  # 峰值的最小高度
    prominence = (y_max - height_base) * 0.5  # 相邻两个波峰的最小突起程度，越小去噪越严格
    peaks, properties = find_peaks(y_, height=height_base, distance=distance, prominence=prominence)
    # print(" Apex : ", len(peaks))
    # print(peaks)
    # print(properties)
    # plt.plot(x_, y_)
    # plt.plot(peaks, y_[peaks], color='red')
    # plt.show()
    num_peaks = len(peaks)

    return num_peaks


def final_out(path):
    # path = r'.\Data\train'

    file_list = os.listdir(path)
    # acc1, acc2, acc3 = 0, 0, 0
    # num_peaks = []
    for file in file_list:
        if '.json' in file:
            # target = int(file.split('.')[0].split('_')[1])
            datawash = DataWash(os.path.join(path, file))
            data = datawash.process()
            num_peaks = find_apex(data)
            # if abs(num_peaks - target) <= 1:
            #     acc1 += 1
            # if abs(num_peaks - target) <= 2:
            #     acc2 += 1
            # if abs(num_peaks - target) <= 3:
            #     acc3 += 1
            print('The number of jump rope in this video :{0}'.format(num_peaks))
            return num_peaks
    # print('Accuracy in error 1 : {0}%  ({1}/{2})'.format(100. * acc1 / len(file_list), acc1,
    #                                                      len(file_list)))
    # print('Accuracy in error 2 : {0}%  ({1}/{2})'.format(100. * acc2 / len(file_list), acc2,
    #                                                      len(file_list)))
    # print('Accuracy in error 3 : {0}%  ({1}/{2})'.format(100. * acc3 / len(file_list), acc3,
    #                                                      len(file_list)))


# subclip视频截取开始时间和结束时间
def add_num(number, input_filename, output_filename):
    video = mp.VideoFileClip(input_filename)
    duration_video = video.duration
    txt = "JUMP ROPE:" + str(number)
    # 制作文字，指定文字大小和颜色
    txt_clip = (TextClip(txt, fontsize=40, color='red')
                .set_position('right', 'top')  # 水印内容居中
                .set_duration(duration_video)
                )  # 水印持续时间

    result = mp.CompositeVideoClip([video, txt_clip])  # 在视频上覆盖文本
    result.write_videofile(output_filename, fps=25)  # fps:视频文件中每秒的帧数
    video.close()
    result.close()
