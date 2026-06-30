# 1> brute force approch
class Solution:
    def stockbuysell(self,prices):
        maxprofit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                maxprofit=max(maxprofit,profit)
        return maxprofit

sol=Solution()
prices=[7,1,5,3,6,4]
print("Max Profit : ", sol.stockbuysell(prices))

# -------------------------------------------------------------

# 2> optimal Solution
class Solution2:
    def stockbuysell(self,prices):
        min_price=float('inf')
        max_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            else:
                max_profit=max(max_profit,price-min_price)
        return max_profit
    
obj=Solution()
prices=[7,1,5,3,6,4]
print("Max Profit using optimal solution : ",obj.stockbuysell(prices))




