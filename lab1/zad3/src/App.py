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
        if b is None:
            if a == 2:
                return self.text[1]
            elif a == 1:
                return self.text[0]
            elif a == 3:
                return self.text[2]
            elif a == 4:
                return self.text[3]
            elif a == 5:
                return self.text[4]
            elif a == 6:
                return self.text[5]
            elif a == 7:
                return self.text[6]
            elif a == 8:
                return self.text[7]
            elif a == 9:
                return self.text[8]

song = Song()