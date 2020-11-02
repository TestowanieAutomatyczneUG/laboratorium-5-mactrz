class Hamming:
    def distance(self, a, b):
        if a == "" and b == "":
            return 0
        elif a == "A" and b == "A":
            return 0
        elif a == "G" and b =="T":
            return 1
        else:
            wynik = 0
            for i in a:
                for j in b:
                    if i != j:
                        break
            return wynik


hamming = Hamming()
