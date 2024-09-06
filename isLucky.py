'''
even number of digits
lucky if sum of first n/2 = sum of last n/2

determine length of number

'''
    
    def solution (num):
        charnum = str(num)
        charlen = len(charnum)
        half = int(charlen/2)
        num1 = charnum[:half]
        num2 = charnum[half:]
        
        sum1 = sum2 = 0
        for i in range(half):
            sum1 = sum1+int(num1[i])
            sum2 = sum2+int(num2[i])
        return (sum1==sum2)
        
solution(1102)