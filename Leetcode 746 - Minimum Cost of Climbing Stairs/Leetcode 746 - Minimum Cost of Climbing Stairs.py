# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    ## Bottom Up Recursion
    # def helper(self, cost: List[int], idx: int):
    #     if idx >= len(cost):
    #         return 0
    #     return cost[idx] + min(self.helper(cost, idx+1), self.helper(cost, idx+2))

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     return min(self.helper(cost, 0), self.helper(cost, 1))

    ## Top Down Recursion
    # def helper(self, cost: List[int], idx: int):
    #     if idx < 0:
    #         return 0
    #     return cost[idx] + min(self.helper(cost, idx-1), self.helper(cost, idx-2))

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     return min(self.helper(cost, len(cost) - 1), self.helper(cost, len(cost) - 2))
        
        
# Time Complexity: O(2^n)
# Space Complexity: O(n)


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [None] * len(cost)
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # for i in range(2, len(cost)):
        #     dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        # return min(dp[-1], dp[-2])
    
# Time Complexity: O(n)
# Space Complexity: O(n)

        # Append a zero at the end of the list to represent reaching the top of the stairs
        cost.append(0)
        
        # Iterate from the second-to-last step down to the first step, len(cost) - 3 because we appended 0 to the list
        for i in range(len(cost) - 3, -1, -1):
            # Update the cost at step i to be the cost of step i plus the minimum cost of reaching the next step or the step after next
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        # The result is the minimum cost of starting at step 0 or step 1
        return min(cost[0], cost[1])

# Time Complexity: O(n)
# Space Complexity: O(1)