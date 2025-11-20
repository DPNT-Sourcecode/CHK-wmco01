
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if skus is None:
            return -1
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10,
            "G": 20,
            "H": 10,
            "I": 35,
            "J": 60,
            "K": 70,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 20,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 17,
            "Y": 20,
            "Z": 21
        }
        offers = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
            "H": [(10, 80), (5, 45)],
            "P": [(5, 200)],
            "K": [(2, 120)],
            "P": [(5, 200)],
            "Q": [(3, 80)],
            "V": [(3, 130), (2, 90)],
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
        if "F" in counts:
            free_f = counts["F"] // 3
            counts["F"] = counts["F"] - free_f
        if "N" in counts:
            free_m = counts["N"] // 3
            if "M" in counts:
                counts["M"] = max(0, counts["M"] - free_m)
        if "R" in counts:
            free_q = counts["R"] // 3
            if "Q" in counts:
                counts["Q"] = max(0, counts["Q"] - free_q)
        if "U" in counts:
            free_u = counts["U"] // 4
            counts["U"] = counts["U"] - free_u

        group_items = ["S", "T", "X", "Y", "Z"]
        group_counts = []

        for item in group_items:
            for item in counts:
                for _ in range(counts[item]):
                    group_counts.append(prices[item])
                counts[item] = 0
        
        group_counts.sort(reverse=True)

        while len(group_counts) >= 3:
            total += 45
            group_counts = group_counts[3:]

        

        for item, cnt in counts.items():
            if item in offers:
                remaining = cnt
                for quality, price in offers[item]:
                    times = remaining // quality
                    total += times * price
                    remaining -= times * quality
                total += remaining * prices[item]
            else:
                total += cnt * prices[item]
        return total
solution = CheckoutSolution()
# print(solution.checkout("A"))
# print(solution.checkout("AAA"))
# print(solution.checkout("AAAA"))
# print(solution.checkout("ABCD"))
# print(solution.checkout("AAABBB"))
# print(solution.checkout("AAAABB12"))
# print(solution.checkout(""))
# print(solution.checkout("A"))
# print(solution.checkout("AAA"))
# print(solution.checkout("AAAAA"))
# print(solution.checkout("AAAAAA"))
# print(solution.checkout("AAAAAAAA"))
# print(solution.checkout("EEB"))
# print(solution.checkout("EEBB"))
# print(solution.checkout("ABCDE"))
# print(solution.checkout("A123"))
# print(solution.checkout("F"))
# print(solution.checkout("FF"))
# print(solution.checkout("FFF"))
# print(solution.checkout("FFFF"))
# print(solution.checkout("FFFFF"))
# print(solution.checkout("FFFFFF"))

print(solution.checkout("BB"))
# print(solution.checkout("FF"))
# print(solution.checkout("FFF"))
# print(solution.checkout("FFFF"))
# print(solution.checkout("FFFFF"))
# print(solution.checkout("FFFFFF"))
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------




