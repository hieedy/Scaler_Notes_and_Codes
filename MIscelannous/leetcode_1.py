class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        # """
#         19 19 1  -3 -3 -39 -47 -57
        # [[25,42],[7,14],[2,32],[25,28],[39,49],[1,50],[29,45],[18,47]]
        # left = 15
        # right = 38

        total_numbers_in_range = right-left+1
        for rang in ranges:
            start = rang[0]
            end = rang[1]
            
            if left >= start and left<=end:
                if right<=end:
                    return True
                else:
                    total_numbers_in_range -= end-left+1
                    left = end+1

            elif right >= start and right<=end:
                total_numbers_in_range -= right-start+1
                right = start-1
            elif left < start and right > end:
                total_numbers_in_range -= end-start+1 
         

        return total_numbers_in_range == 0




A = [[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49],[1,49]]
left = 2
right = 50
sol = Solution()
print(sol.isCovered(A,left,right))