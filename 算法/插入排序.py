class Sort():
    def insert_sort(self, data):

        for i in range(1, len(data)):
            value = data[i]  # 插入值

            j = i - 1  # 记录插入位置  j+1 代表插入的位置
            while j >= 0:  # 不用 for 循环是因为 j 为 -1 的情况
                if data[j] > value:
                    data[j + 1] = data[j]
                else:
                    break
                j -= 1
            data[j + 1] = value
        return data
if __name__=="__main__":
    demo = Sort()
    arr = [3, 2, 0, 7, 4]
    print(demo.insert_sort(arr))