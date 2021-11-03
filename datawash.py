import json
import logging

import numpy as np
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)
keyword = ["Nose", "LEye", "REye", "LEar", "REar", "LShoulder", "RShoulder", "LElbow", "RElbow", "LWrist", "RWrist",
           "LHip", "RHip", "LKnee", "Rknee", "LAnkle", "RAnkle"]


def get_gravity(point_a, point_b, point_c):
    """
    直角坐标系计算三角形重心
    :param 三个点的坐标
    :return: [x,y]
    """
    x_ = (point_a[0] + point_b[0] + point_c[0]) / 3
    y_ = (point_a[1] + point_b[1] + point_c[1]) / 3
    gravity = [x_, y_]
    return gravity


class DataWash:
    def __init__(self, data_path):
        """
        :param data_path:json 输入数据json
        """
        self.data_path = data_path
        self.keyword = keyword

    def process(self):
        """
        :rtype: object
        :return: list[dist] 包含每一帧图片信息的list
        """
        try:
            with open(self.data_path, 'r') as load_f:
                data_dict = json.load(load_f)
                point_array = []
                for item in range(len(data_dict)):
                    # Nose = data_dict[item]['keypoints'][0:2]
                    # LHip = data_dict[item]['keypoints'][33:35]
                    # RHip = data_dict[item]['keypoints'][36:38]
                    Lankle = data_dict[item]['keypoints'][45:47]
                    Rankle = data_dict[item]['keypoints'][48:50]
                    # RHip = data_dict[item]['keypoints'][36:38]
                    # gravity = get_gravity(Nose, LHip, RHip)
                    absAnkels = abs(Lankle[1] - Rankle[1])
                    point_array.append([1, abs(Lankle[1] - Rankle[1])])
            return point_array

        except Exception as e:
            logger.error("data wash error : %s " % e)

# datawash = DataWash('data/AlphaPose/alphapose-results2.json')
# data = datawash.process()
# print(data)
#
# # plot
# x = np.array(data)
# x_ = np.arange(0,len(data),1)
# y_ = x[:, 1]
# plt.plot(x_ , y_)
# plt.show()
