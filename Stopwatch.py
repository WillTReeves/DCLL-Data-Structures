from datetime import datetime

class stopwatch:
    def __init__(self):
        pass
    def start(self):
        A = datetime.now()
        return A
    def end(self):
        B = datetime.now()
        return B
    def read(self,start,end):
        time = end - start
        return time
