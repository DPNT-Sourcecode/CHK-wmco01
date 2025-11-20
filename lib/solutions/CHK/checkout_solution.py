
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if skus is None:
            return -1
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15
        }
        offers = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)]
        }
        counts = {}
        for ch in skus:
            if ch not in prices:
                return -1
            counts[ch] = counts.get(ch, 0) + 1
        total = 0
        if "E" in counts:
            free_b = counts["E"] // 2
            if "B" in counts:
                counts["B"] = max(0, counts["B"] - free_b)

        for item, cnt in counts.items():
            if item in offers:
                remaining = cnt
                for quality, price in offers[item]:
                    times = remaining // quality
                    total += times * price
                    remaining -= times * quality
                    
                    
            else:
                total += cnt * prices[item]
        return total
# solution = CheckoutSolution()
# print(solution.checkout("A"))
# print(solution.checkout("AAA"))
# print(solution.checkout("AAAA"))
# print(solution.checkout("ABCD"))
# print(solution.checkout("AAABBB"))
# print(solution.checkout("AAAABB12"))
# print(solution.checkout(""))
