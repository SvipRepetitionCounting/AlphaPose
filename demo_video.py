import os

import Apex
# from label_trans import *
import os

data_dir = '/root/AlphaPose/demo_data/'
video_filename = 'student_1.mp4'

if __name__ == '__main__':
    # python AlphaPose to json
    # cmd_alpha = 'python scripts/demo_inference.py '
    # cmd_cfg = ' --cfg configs/coco/resnet/256x192_res50_lr1e-3_1x.yaml  '
    # cmd_checkpoint = '--checkpoint /root/AlphaPose/pretrained_models/fast_res50_256x192.pth '
    # video_dir = os.path.join(data_dir, video_filename)
    # outdir = os.path.join(data_dir, os.path.splitext(video_filename)[0])
    # cmd_save = ' --save_video '
    # video2json = cmd_alpha + cmd_cfg + cmd_checkpoint + \
    #              ' --video ' + video_dir + \
    #              ' --outdir ' + outdir + \
    #              cmd_save
    outdir = r'/root/AlphaPose/demo_data/student_male_2'
    # json to video
    # if os.system(video2json) == 0:
    if 1:

        # python json to data
        # move_data(outdir, 'AlphaPose_' + video_filename)
        number = Apex.final_out(outdir)
        out_filename = 'AlphaPose_' + video_filename
        # num_videos = os.path.join(outdir, out_filename)
        num_videos = r'/root/AlphaPose/demo_data/AlphaPose_student_2.mp4'
        Apex.add_num(number, num_videos, outdir + '_num_demo.mp4')
    # else:
    #     print('cmd AlphaPose.py error')
