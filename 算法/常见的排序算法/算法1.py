from random import randint
#生成包含随机数字的列表
def generateRandomArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return str(arr)
#判断列表是否有序
def isSorted(alist):
    for i in range(0, len(alist)-1):
        if alist[i] > alist[i+1]:
            return False
    return True
if __name__ == "__main__":
    p = generateRandomArray(101,1,200)
    print(p)