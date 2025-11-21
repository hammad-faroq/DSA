import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""

        for ch in searchWord:
            prefix += ch
            # Find the leftmost index where prefix could appear
            i = bisect.bisect_left(products, prefix)

            suggestions = []
            # Check next 3 items after i
            for j in range(i, min(i+3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
                else:
                    break

            result.append(suggestions)

        return result