
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
            "A": {3, 150},
            "B": {2, 45}
        }
        counts = {}
        for ch in skus:
            if ch not in prices:
                return -1
            counts[ch] = counts.get(ch, 0) + 1
        total 

