
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if skus is None or skus == "":
            return -1
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15
        }
        offers = {
            "A": (3, 150),
            "B": (2, 45)
        }
        counts = {}
        for ch in skus:
            if ch not in prices:
                return -1
            counts[ch] = counts.get(ch, 0) + 1
        total = 0
        for item, cnt in counts.items():
            if item in offers:
                offer_quality, offer_price = offers[item]
                offer_times = cnt // offer_quality
                remainder = cnt % offer_quality
                total += offer_times * offer_price
                total += remainder * prices[item]
            else:
                total += cnt * prices[item]
        return total
print(CheckoutSolution.checkout("A"))
print(CheckoutSolution.checkout("AAA"))
print(CheckoutSolution.checkout("AAA"))



