class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final_price = []
        for i in range(len(prices)):
            discount = prices[i]
            for j in range(i + 1 , len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[i] - prices[j]
                    break

            final_price.append(discount)

        return final_price