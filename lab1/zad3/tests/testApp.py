from src.App import song
import unittest


class SongTest(unittest.TestCase):
    def test_one_verse_first(self):
        self.assertEqual(song.sing(2), "On the second day of Christmas my true love gave to me: two Turtle Doves, "
                                       "and a Partridge in a Pear Tree.")

    def test_one_verse_zero(self):
        self.assertEqual(song.sing(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear "
                                       "Tree.")

    def test_one_verse_second(self):
        self.assertEqual(song.sing(3), "On the third day of Christmas my true love gave to me: three French Hens, "
                                       "two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_one_verse_third(self):
        self.assertEqual(song.sing(4), "On the fourth day of Christmas my true love gave to me: four Calling Birds, "
                                       "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_one_verse_fourth(self):
        self.assertEqual(song.sing(5), "On the fifth day of Christmas my true love gave to me: five Gold Rings, "
                                       "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a"
                                       " Pear Tree.")

    @unittest.skip
    def test_one_verse_fifth(self):
        self.assertEqual(song.sing(6), "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, "
                                       "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                                       "and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_one_verse_sixth(self):
        self.assertEqual(song.sing(7), "On the seventh day of Christmas my true love gave to me: seven "
                                       "Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                                       "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_one_verse_seventh(self):
        self.assertEqual(song.sing(8), "On the eighth day of Christmas my true love gave to me: eight "
                                       "Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                                       "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a "
                                       "Pear Tree.")

    @unittest.skip
    def test_one_verse_eighth(self):
        self.assertEqual(song.sing(9), "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, "
                                       "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
                                       "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                                       "and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_one_verse_ninth(self):
        self.assertEqual(song.sing(10), "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, "
                                        "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, "
                                        "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, "
                                        "two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_one_verse_tenth(self):
        self.assertEqual(song.sing(11), "On the eleventh day of Christmas my true love gave to me: eleven Pipers "
                                        "Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
                                        "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling "
                                        "Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_one_verse_eleventh(self):
        self.assertEqual(song.sing(12), "On the twelfth day of Christmas my true love gave to me: twelve Drummers "
                                        "Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, "
                                        "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
                                        "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                                        "and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_verses_1_3(self):
        self.assertEqual(song.sing(1, 3), "On the second day of Christmas my true love gave to me: two Turtle Doves, "
                                          "and a Partridge in a Pear Tree.\n\nOn the third day of Christmas my true "
                                          "love gave to me: three French Hens, two Turtle Doves, and a Partridge in a "
                                          "Pear Tree.\n\nOn the fourth day of Christmas my true love gave to me: four "
                                          "Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a "
                                          "Pear Tree.")

    @unittest.skip
    def test_whole_song(self):
        self.assertEqual(song.sing(1, 12), "On the first day of Christmas my true love gave to me: a Partridge in a "
                                           "Pear Tree.\n\nOn the second day of Christmas my true love gave to me: two "
                                           "Turtle Doves, and a Partridge in a Pear Tree.\n\nOn the third day of "
                                           "Christmas my true love gave to me: three French Hens, two Turtle Doves, "
                                           "and a Partridge in a Pear Tree.\n\nOn the fourth day of Christmas my true "
                                           "love gave to me: four Calling Birds, three French Hens, two Turtle Doves, "
                                           "and a Partridge in a Pear Tree.\n\nOn the fifth day of Christmas my true "
                                           "love gave to me: five Gold Rings, four Calling Birds, three French Hens, "
                                           "two Turtle Doves, and a Partridge in a Pear Tree.\n\nOn the sixth day of "
                                           "Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                                           "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge "
                                           "in a Pear Tree.\n\nOn the seventh day of Christmas my true love gave to "
                                           "me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                                           "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge "
                                           "in a Pear Tree.\n\nOn the eighth day of Christmas my true love gave to "
                                           "me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
                                           "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                                           "and a Partridge in a Pear Tree.\n\nOn the ninth day of Christmas my true "
                                           "love gave to me: nine Ladies Dancing, eight Maids-a-Milking, "
                                           "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling "
                                           "Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear "
                                           "Tree.\n\nOn the tenth day of Christmas my true love gave to me: ten "
                                           "Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
                                           "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling "
                                           "Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear "
                                           "Tree.\n\nOn the eleventh day of Christmas my true love gave to me: eleven "
                                           "Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, "
                                           "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
                                           "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                                           "and a Partridge in a Pear Tree.\n\nOn the twelfth day of Christmas my "
                                           "true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, "
                                           "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
                                           "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling "
                                           "Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear "
                                           "Tree.")

    @unittest.skip
    def test_disallow_negative_first(self):
        with self.assertRaisesWithMessage(ValueError):
            song.sing(-1, 2)

    @unittest.skip
    def test_disallow_negative_second(self):
        with self.assertRaisesWithMessage(ValueError):
            song.sing(1, -2)

    @unittest.skip
    def test_disallow_greater_then_12(self):
        with self.assertRaisesWithMessage(ValueError):
            song.sing(13)

    @unittest.skip
    def test_disallow_greater_then_12_range(self):
        with self.assertRaisesWithMessage(ValueError):
            song.sing(3, 15)

    @unittest.skip
    def test_disallow_first_bigger_then_second(self):
        with self.assertRaisesWithMessage(ValueError):
            song.sing(6, 2)

    @unittest.skip
    def test_disallow_different_types(self):
        with self.assertRaisesWithMessage(ValueError):
            song.sing("1")

    @unittest.skip
    def test_disallow_zero(self):
        with self.assertRaisesWithMessage(ValueError):
            song.sing(0)

    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")
