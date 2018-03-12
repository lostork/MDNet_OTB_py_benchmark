from config import *
import numpy as np
import scripts.butil

# sys.path.insert(0,"./trackers/OMDNet/modules/")
sys.path.insert(0,"./trackers/FMDNet/tracking/")  # TODO: maybe use abs path is better
# import numpy as np
import os
import sys
# import time
# import argparse
# import json
# from PIL import Image
# import matplotlib.pyplot as plt
#
# import torch
# import torch.utils.data as data
# import torch.optim as optim
# from torch.autograd import Variable
# print sys.path
# sys.path.insert(0,'../modules')
# from sample_generator import *
# from data_prov import *
# from model import *
# from bbreg import *
# from options import *
# from gen_config import *
import run_tracker

def run_FMDNet(seq, rp, bSaveImage):
    # TODO: run_mdnet check : init train ok, loop tracking ok. gpu, display, update(2, short and long) not checked

    os.chdir("./tracking/")
    # print os.path.abspath('.')
    # run_tracker.test()
    # print os.path.abspath('.')
    # print sys.path
    #
    img_list = seq.s_frames
    init_bbox = np.array(seq.init_rect, dtype=np.float64)  # TODO: unc with np.float64
    gt = np.array(seq.gtRect, dtype=np.float64)  # TODO: unc with np.float64

    # TODO: become unicode.
    # savefig_dir = "../result_fig/" + seq.name   # TODO: unc with plus between str and unicode. unc with the '_0' in seq.name
    display = False

    result, result_bb, fps = run_tracker.run_mdnet(img_list, init_bbox, gt=gt, savefig_dir='', display=display)

    res = {}
    res['res'] = result_bb.round().tolist()
    res['type'] = 'rect'
    res['fps'] = fps
    return res
    # seq_home = '../dataset/OTB'
    # save_home = '../result_fig'
    # result_home = '../result'
    #
    # seq_name = args.seq
    # img_dir = os.path.join(seq_home, seq_name, 'img')
    # gt_path = os.path.join(seq_home, seq_name, 'groundtruth_rect.txt')
    #
    # # print os.getcwd()
    # img_list = os.listdir(img_dir)
    # img_list.sort()
    # img_list = [os.path.join(img_dir, x) for x in img_list]
    #
    # gt = np.loadtxt(gt_path, delimiter=',')
    # init_bbox = gt[0]
    #
    # savefig_dir = os.path.join(save_home, seq_name)
    # result_dir = os.path.join(result_home, seq_name)
    # if not os.path.exists(result_dir):
    #     os.makedirs(result_dir)
    # result_path = os.path.join(result_dir, 'result.json')

    # seq.init_rect = matlab.double(seq.init_rect)
