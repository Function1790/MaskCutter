import detectMaskState as dt

def workingTest():
    while True:
        print(f"Exist >> {dt.isExistMask()}\tSliced >> {dt.isMaskSliced()}")
        
def isSliced():
    detect_count=0
    for i in range(10):
        if dt.isMaskSliced():
            detect_count+=1
    return detect_count/10