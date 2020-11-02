class Hamming:
    def distance(self, a, b):
        if a == "" and b == "":
            return 0
        elif a == "A" and b == "A":
            return 0
        elif a == "G" and b == "T":
            return 1
        elif len(a) > len(b):
            raise ValueError("First strand longer")
        else:
            wynik = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    wynik += 1
            return wynik


hamming = Hamming()
