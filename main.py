import sys
import Queue
import ShotsTaker

baseUrl = "https://www.fiverr.com/search/gigs?query=%s"
threadCount = 1

def main(searchTerms) :
    print "starting"
    searchTerms = ["logo design","facebook","voice","australian female voice over"]
    queue = Queue.Queue()
    for i in range(threadCount):
        ShotsTaker.ShotsTaker(i,queue).start()
    for term in searchTerms :
        task = ShotsTaker.Task(baseUrl%term,"pics/%s.png"%term)
        queue.put(task)
    for i in range(threadCount):
       queue.put(None)
    return




if __name__ == "__main__":
    main([sys.argv[0]])





