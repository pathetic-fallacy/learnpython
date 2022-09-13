#-*- coding: utf-8 -*-

### do_logging.py

import logging
logging.basicConfig(level=logging.INFO) # 允许指定记录信息的级别，debug,info,warning,error，可输出不同级别的inxi
### 最后统一控制输出哪个级别的信息,可将一条语句同时输出到不同的地方，console和文件等

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)