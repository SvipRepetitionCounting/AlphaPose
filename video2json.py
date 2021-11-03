import os
def video2json(data_dir,video_filename, pth_dir= '/root/AlphaPose/pretrained_models/fast_res50_256x192.pth'):
    """
    input:
    data_dir: 视频存放路径
    video_filename: 视频名称
    pth_dir:模型pth
    
    e.g.
    data_dir = '/root/AlphaPose/demo_data/'
    video_filename = 'student_male_2.mp4'
    pth_dir= '/root/AlphaPose/pretrained_models/fast_res50_256x192.pth'
    
    output:
    json_path:生成的关键点alphapose.json路径
    keypoint_video_path：生成的关键点检测后视频路径
    
    e.g.
    json_path:='/root/AlphaPose/demo_data/alphapose_result.json'
    keypoint_video_path = '/root/AlphaPose/demo_data/student_male_2.mp4'
    """
    
    video = os.path.join(data_dir, video_filename)
    #outdir = os.path.join(data_dir, os.path.splitext(video_filename)[0])
    outdir=data_dir
    if not outdir:
        outdir='./'
    pth_dir = pth_dir
    cmd_alpha = 'python scripts/demo_inference.py '
    cmd_cfg = '--cfg configs/coco/resnet/256x192_res50_lr1e-3_1x.yaml  '
    cmd_checkpoint = '--checkpoint ' + pth_dir
    cmd_save = ' --save_video '
    video2json = cmd_alpha + cmd_cfg + cmd_checkpoint + \
                 ' --video ' + video + \
                 ' --outdir ' + outdir 
          
    os.system(video2json)


    files = os.listdir(outdir)
    json_path=''
    keypoint_video_path=''
    for file in files:
        if '.json' in file:
            json_path = os.path.join(outdir,file)

    return json_path