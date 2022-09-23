#author Hariharan_Mageshanand

import requests
import os
import numpy as np
from torch import slogdet
import json
import numpy as np
def board_parameters(width,height):
    width_url="http://169.254.7.197/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/parameters/grid_width"
    height_url="http://169.254.7.197/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/parameters/grid_height"
    width_val={'value':width}
    height_val={'value':height}
    response=requests.put(width_url,json=width_val)
    print(response.json())
    response=requests.put(height_url,json=height_val)
    print(response.json())
def remove_calib():
    rm_calib="http://169.254.7.197/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/parameters/remove_calibration"
    todo={'args':{}}
    response=requests.put(rm_calib,json=todo)
    print(response.json)

def set_poses(x,y,z,qx,qy,qz,qw,slt):
    set_pose_url="http://169.254.7.197/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/set_pose"
    #print(np.float64(x),np.float64(y),np.float64(z))
    print
    pose={'args':
    {'pose':
    {'position':
    {'x':np.float64(x),
    'y':np.float64(y),
    'z':np.float64(z)},
    'orientation':
    {'x':qx,
    'y':qy,
    'z':qz,
    'w':qw}},
    'slot':slt
    }
    }
    response=requests.put(set_pose_url,json=pose)
    h=response.json()
    print(h)
    return h['response']['status'],h['response']["success"]
def calibrate():
    calibrate_url="http://169.254.7.197/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/calibrate"
    todo={'args':{}}
    response=requests.put(calibrate_url,json=todo)
    h=response.json()
    x=h['response']['pose']['position']['x']
    y=h['response']['pose']['position']['y']
    z=h['response']['pose']['position']['z']
    qx=h['response']['pose']['orientation']['x']
    qy=h['response']['pose']['orientation']['y']
    qz=h['response']['pose']['orientation']['z']
    qw=h['response']['pose']['orientation']['w']
    trans_error=h['response']['translation_error_meter']
    rot_error=h['response']['rotation_error_degree']
    #print(h)
    return(x,y,z,qx,qy,qz,qw,trans_error,rot_error)
