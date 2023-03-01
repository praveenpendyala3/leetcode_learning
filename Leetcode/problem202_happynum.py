class Solution:
    def isHappy(self, n: int) -> bool:

        def happyNum(num,nums_in=[]):
            if num in nums_in:
                return False

            if num==1:
                return True

            nums_in.append(num)

            tmp = 0
            while num != 0:
                tmp = tmp + (num%10)**2
                num = num//10

            return happyNum(tmp,nums_in)

        return happyNum(n)

            
                
            