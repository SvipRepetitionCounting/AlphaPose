import json
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

keyword = ["Nose", "LEye", "REye", "LEar", "REar", "LShoulder", "RShoulder", "LElbow", "RElbow", "LWrist", "RWrist",
           "LHip", "RHip", "LKnee", "Rknee", "LAnkle", "RAnkle"]


def find_apex(y_):
    y_min = min(y_)
    y_max = max(y_)
    distance = 45  # 相邻峰值之间的最小水平距离，越小去噪越严格
    height_base = y_max * 0.98  # 峰值的最小高度
    prominence = (y_max - height_base) * 0.9  # 相邻两个波峰的最小突起程度
    peaks, properties = find_peaks(y_, height=height_base, distance=distance, prominence=prominence)

    return peaks


def get_distance(data_path):
    with open(data_path, 'r') as load_f:
        data_dict = json.load(load_f)
        Distance = []
        for item in range(len(data_dict)):
            LShoulder = data_dict[item]['keypoints'][15:17]
            RShoulder = data_dict[item]['keypoints'][18:20]
            LHip = data_dict[item]['keypoints'][33:35]
            RHip = data_dict[item]['keypoints'][36:38]
            midShoulder= [(data_dict[item]['keypoints'][15] + data_dict[item]['keypoints'][18]) / 2,
                        (data_dict[item]['keypoints'][16] + data_dict[item]['keypoints'][19]) / 2]
            midHip = [(data_dict[item]['keypoints'][33] + data_dict[item]['keypoints'][36]) / 2,
                       (data_dict[item]['keypoints'][34] + data_dict[item]['keypoints'][37]) / 2]
            # distance = math.sqrt(((midShoulder[0] - midHip[0]) ** 2) + ((midShoulder[1] - midHip[1]) ** 2))

            distance = abs(midShoulder[1]-midHip[1])

            Distance.append(-distance)

        return Distance


def situp_count(path):
    distance = get_distance(path)
    x_ = np.arange(0, len(distance), 1)
    y_ = np.array(distance)
    peaks = find_apex(y_)
    count = len(peaks)
#     plt.plot(x_,y_)
#     plt.plot(peaks, y_[peaks], color='red')
#     plt.show()
    print('count: ', count)


# json_path = 'lenovo/situp_15.json'
# get_count(json_path)
