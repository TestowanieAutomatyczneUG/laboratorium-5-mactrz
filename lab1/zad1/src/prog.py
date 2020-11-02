class Hamming:
    def distance(self, a, b):
        if a == "" and b == "":
            return 0
        elif len(a) > len(b):
            raise ValueError("First strand longer")
        elif len(b) > len(a):
            raise ValueError("Second strand longer")
        else:
            wynik = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    wynik += 1
            return wynik


hamming = Hamming()
