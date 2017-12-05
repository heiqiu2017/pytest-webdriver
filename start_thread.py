# -*- coding: utf-8 -*-
import threading
from Utils.logg import log_message
def thread_start(dr_obj,func,*args):
    """
    :param dr_obj: driver 对象:str obj / list obj
    :param func: 被调用测试函数
    :param args: 测试函数需要参数
    :return:
    """
    # param example: (a,b,c....)
    log = log_message(log_dir='../log')
    thread_lis = []
    if isinstance(dr_obj,list):
        for i in dr_obj:
            log.info_log(i)
            param = [o for o in args]
            param.insert(0,i)
            th = threading.Thread(target=func, args=tuple(param))
            th.start()
            thread_lis.append(th)
    else:
        param = [o for o in args]
        param.insert(0, dr_obj)
        th = threading.Thread(target=func, args=tuple(param))
        th.start()
        thread_lis.append(th)
    for o in thread_lis:
        o.join()