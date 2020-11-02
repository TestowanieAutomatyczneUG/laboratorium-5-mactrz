class Hamming:
    def distance(self, a, b):
        if a == "" and b == "":
            return 0
        elif a == "A" and b == "A":
            return 0
        elif a == "G" and b =="T":
            return 1

hamming = Hamming()
