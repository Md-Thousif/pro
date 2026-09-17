# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        low=0
        high=n
        while True:
            mid=low+(high-low)//2
            guess(mid)
            if(guess(mid)==0):
                return mid
            elif(guess(mid)==-1):
                high=mid-1
            elif(guess(mid)==1):
                low=mid+1
        