import threading
import ShotTaker


class ShotsTaker(threading.Thread):

    def __init__(self,threadNum ,queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.taker = ShotTaker.ShotTaker()
        self.threadNum = threadNum

    def destroy(self):
        self.taker.destroy()

    def run(self):
        while True :
            task = self.queue.get()
            if task is None:
                break
            print "thread %d is taking screenshot of url %s and saving it in path %s"%(self.threadNum,task.url,task.out_path)
            self.taker.take(task.url,task.out_path)
        self.destroy()

class Task:
    def __init__(self,url,out_path):
        self.url = url
        self.out_path = out_path