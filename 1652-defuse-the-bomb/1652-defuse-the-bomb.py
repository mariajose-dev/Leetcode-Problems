class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        if k > 0:
            ans[0]=wsum=sum(code[1:k+1])
            for l in range(1,n):
                r=(l+k)%n
                wsum+=-code[l]+code[r]
                ans[l]=wsum
            return ans
       
        ans[0]=wsum=sum(code[-1:k-1:-1])
        for l in range(1,n):
            r=(l-k)%n
            wsum+=-code[-l]+code[-r]
            ans[-l]=wsum
        return ans            


        