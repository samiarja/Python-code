class Solution:
    def reverse(self,x):
        #initialze r = 0
        res = 0
        #if input value was greater than zero
        if x >= 0:
            #make position true
            pos = True
        else:
            #make position false
            pos = False
            #input value is negative
            x = -x
            #make forever loop for input value not equal to zero
        while x != 0:
            #if res was a very large number 
            if res > 1000000:
                #return 0
                return 0
            else:
                #pop operation
                pop = x%10
                #push operation
                res = res*10 + pop
                x = x/10
            if pos:
                return res
            else:
                return -res
            
