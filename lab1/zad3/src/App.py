class Song:
    def __init__(self):
        self.text = ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
                     "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a "
                     "Pear Tree.", "On the third day of Christmas my true love gave to me: three French Hens, "
                                   "two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, "
                     "two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, "
                     "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                     "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, "
                     "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                     "and a Partridge in a Pear Tree.",
                     "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, "
                     "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French "
                     "Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, "
                     "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                     "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies "
                     "Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                     "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                     "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, "
                     "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, "
                     "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                     "and a Partridge in a Pear Tree.",
                     "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, "
                     "eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
                     "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French "
                     "Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                     ]
    def sing(self, a, b = None):
        if type(a) != int:
            raise ValueError("Must be a number")
        if a == 0:
            raise ValueError("Incorrect index")
        if a < 0:
            raise ValueError("Can't be negative")
        if a > 12:
            raise ValueError("Can't be bigger than 12")
        if b is None:
            return self.text[a-1]

        else:
            if type(b) != int:
                raise ValueError("Must be a number")
            if b == 0:
                raise ValueError("Incorrect index")
            if b < 0:
                raise ValueError("Can't be negative")
            if b > 12:
                raise ValueError("Can't be bigger then 12")
            if a > b:
                raise ValueError("Incorrect order")
            ans = ""
            for i in range(a - 1, b):
                textadd = self.text[i]
                if i != b-1:
                    textadd += "\n\n"
                ans += textadd
            return ans

song = Song()