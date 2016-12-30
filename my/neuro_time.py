#-*- using:utf-8 -*-
import time
import neuro,neuro_batch

def get_elapse(name,module):
    start = time.time()
    module.main()
    elapsed_time = time.time() - start
    print (name,"elapse",elapsed_time,"[sec]")

if __name__ == '__main__':
    get_elapse("batch",neuro_batch)
    get_elapse("neuro",neuro)
