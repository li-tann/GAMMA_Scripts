# GAMMA_Scripts
GAMMA scripts by python or shell

## pyscripts_load_alos2.py

使用方法, 
在terminal中输入: 'python pyscripts_load_alos2.py /mnt/e/REMOTE_SENSING_DATA/ALOS2'
脚本会在`argv[1]`的地址内, 搜索文件夹(不会遍历), 查找符合要求的文件夹(带有LED_..., IMG_HH...文件的文件夹), 
在内部创建slc, 并执行gamma的par_EORC_PALSAR指令, 将ALOS2数据转换为slc和slc.par, 并放到slc文件夹内。

**执行前记着load_gamma, 开启gamma环境**

## load_alos2.sh

未完工, 计划实现和pyscripts相同的效果