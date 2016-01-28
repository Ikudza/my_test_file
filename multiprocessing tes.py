from __future__ import unicode_literals
from multiprocessing import Process
from multiprocessing import freeze_support, Pool, cpu_count


def recfromreadblob(tet, tt):
    print tt
    ss = []
    for t in tet:
        ss.append[t]
    print 'good', len(ss)
    return


def testing():
    readBlob = ['12'] * 100
    print readBlob
    freeze_support()
    pool = Pool(processes=cpu_count(), maxtasksperchild=1)
    step = 10
    for i in xrange(0, len(readBlob), step):
        print i
        pool.apply(recfromreadblob,
                   args=(readBlob[i:min(len(readBlob), i+step)],
                   len(readBlob)-i))
    pool.close()
    pool.join()
    pool.terminate()
    return




if __name__ == '__main__':
    break_con(conn)
