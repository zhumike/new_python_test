class duoshuyuansu:
    def majorityEmlment(self, nums):
        count=0
        mostnum = nums[0]
        for n in range(len(nums)):
            if nums[n] == mostnum:
                count=count+1
            else:
                count=count-1
                if count == 0:
                    mostnum = nums[n]
                    count=count+1
        return mostnum
if __name__ == '__main__':
    s1 = duoshuyuansu()
    list1 = [2,2,1,1,1,2,2,]
    result = s1.majorityEmlment(list1)
    print(result)


