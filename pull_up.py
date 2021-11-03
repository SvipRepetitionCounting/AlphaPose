import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

keyword = ["Nose", "LEye", "REye", "LEar", "REar", "LShoulder", "RShoulder", "LElbow", "RElbow", "LWrist", "RWrist",
           "LHip", "RHip", "LKnee", "Rknee", "LAnkle", "RAnkle"]


def find_apex(y_):
    y_min = min(y_)
    y_max = max(y_)
    distance = None  # 相邻峰值之间的最小水平距离，越小去噪越严格
    height_base = y_min + (y_max - y_min) * 0.1  # 峰值的最小高度
    prominence = (y_max - height_base) * 0.1  # 相邻两个波峰的最小突起程度
    peaks, properties = find_peaks(y_, height=height_base, distance=distance, prominence=prominence)
    return peaks


def get_gravity(a, b, c):
    """
    直角坐标系计算三角形重心
    :param 三个点的坐标
    :return: [x,y]
    """
    x_ = (a[0] + b[0] + c[0]) / 3
    y_ = (a[1] + b[1] + c[1]) / 3
    gravity = [x_, y_]
    return gravity


def pullup_count(data_path):
    with open(data_path, 'r') as load_f:
        data_dict = json.load(load_f)
        gravities = []
        for item in range(len(data_dict)):
            Nose = data_dict[item]['keypoints'][0:2]
            LShoulder = data_dict[item]['keypoints'][15:17]
            RShoulder = data_dict[item]['keypoints'][18:20]
            gravity = get_gravity(Nose, LShoulder, RShoulder)
            gravities.append(gravity)

        x_ = np.arange(0, len(gravities), 1)
        y_ = np.array((gravities))[:, 1]
        peaks = find_apex(y_)
        count = len(peaks)
        plt.plot(x_, y_)
        plt.plot(peaks, y_[peaks], color='red')
        plt.show()
        print('count: ', count)

        return count


# json_path = 'lenovo/pull_up_10.json'
# count = get_count(json_path)
