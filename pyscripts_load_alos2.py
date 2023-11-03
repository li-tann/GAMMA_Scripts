import os
import re
import sys

'''
使用方法, 
在terminal中输入: 'python pyscripts_load_alos2.py /mnt/e/REMOTE_SENSING_DATA/ALOS2'
脚本会在argv[1]的地址内, 搜索文件夹(不会遍历), 查找符合要求的文件夹(带有LED_..., IMG_HH...文件的文件夹), 
在内部创建slc, 并执行gamma的par_EORC_PALSAR指令, 将ALOS2数据转换为slc和slc.par, 并放到slc文件夹内。
***执行前记着load_gamma, 开启gamma环境***
'''


ALOS2_IMG=1
ALOS2_LED=0

def get_alos2_file(path):
    '''
    获取path地址下的LED, IMG-HH, date信息, 若没有搜索到则返回空数组["","",""]
    :param path: 地址
    :return: ["LED", "IMG-HH", "date"]
    '''
    files=os.listdir(path)
    out_filepath=["","",""]
    for file in files:
        file_path = os.path.join(path, file)
        if(os.path.isdir(file_path)):
            continue
        # print(file_path)
        if(re.match("^LED",file)):
            out_filepath[ALOS2_LED]=file_path
            datalist = str(file).split('-')
            date=datalist[2]
            out_filepath[2]=date
        if(re.match("^IMG-HH",file)):
            out_filepath[ALOS2_IMG]=file_path

    return out_filepath
    
def load_alos2_data(alos2_filepath):
    '''
    在alos2_filepath地址下创建slc地址, 存放转换后的date.slc和date.slc.par
    '''
    alos_data = get_alos2_file(alos2_filepath)
    if (alos_data[ALOS2_LED]=="" or alos_data[ALOS2_IMG]==""):
        print(" there({}) is not a alos2 folder, return.".format(alos2_filepath))
        return 
    print(" there({}) is a alos2 folder, return.".format(alos2_filepath))

    slc_folder = os.path.join(alos2_filepath,"slc")
    if(not os.path.exists(slc_folder)):
        os.mkdir(slc_folder)

    date=alos_data[2]
    gamma_path = [date+".slc.par",date+".slc"]
    gamma_path = [os.path.join(slc_folder,gamma_path[0]),os.path.join(slc_folder,gamma_path[1])]

    cmd = 'par_EORC_PALSAR {} {} {} {}'.format(alos_data[0],gamma_path[0],alos_data[1],gamma_path[1])
    print(cmd)
    os.system(cmd)


def load_alos2_streamline(rootpath):
    '''
    遍历根目录rootpath, 对根目录内所有文件夹执行load_alos2_data函数, 将满足要求的数据转换为 date.sla & date.sla.par
    '''
    files=os.listdir(rootpath)
    for file in files:
        file_path = os.path.join(rootpath, file)
        if (os.path.isdir(file_path)):
            print(file_path+":")
            load_alos2_data(file_path)
    return 
    
# ------------------------------------------------------------------------------------------------------ #


argc = len(sys.argv)
if(argc<2):
    print('please input folder_path after argv[0]({}).'.format(sys.argv[0]))
    exit()

load_alos2_streamline(sys.argv[1])

