import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        input_points = [data.Point(2, 2), data.Point(10, 10)]
        result = hw2.create_rectangle(input_points[0], input_points[1])
        expected_top_left = data.Point(2, 10)
        expected_bottom_right = data.Point(10, 2)
        self.assertEqual(expected_top_left.x, result.top_left.x)
        self.assertEqual(expected_top_left.y, result.top_left.y)
        self.assertEqual(expected_bottom_right.x, result.bottom_right.x)
        self.assertEqual(expected_bottom_right.y, result.bottom_right.y)


    # Part 2
    def test_duration_shorter_than_1(self):
        duration1 = data.Duration(1, 20)
        duration2 = data.Duration(2, 31)
        expected =  True
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(expected, result)

    def test_duration_shorter_than_2(self):
        duration1 = data.Duration(3, 20)
        duration2 = data.Duration(2, 31)
        expected =  False
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(expected, result)



    # Part 3
    def test_song_shorter_than(self):
        song1 = data.Song("Ariana Grande", "Bang", data.Duration(3, 30))
        song2 = data.Song("Jennie Kim", "Mantra", data.Duration(4, 15))
        song3 = data.Song("Riley", "Oscar Winning Tears", data.Duration(2, 50))

        songs = [song1, song2, song3]
        duration = data.Duration(4, 0)

        expected_titles = ["Ariana Grande", "Riley"]
        result_songs = hw2.song_shorter_than(songs, duration)

        result_titles = [song.artist for song in result_songs]
        self.assertEqual(expected_titles, result_titles)


    # Part 4
    def test_running_time(self):
        song1 = data.Song("Ariana Grande", "Bang", data.Duration(3, 30))
        song2 = data.Song("Jennie Kim", "Mantra", data.Duration(4, 15))
        song3 = data.Song("Riley", "Oscar Winning Tears", data.Duration(2, 50))
        songs = [song1, song2, song3]
        playlist = [0, 2, 1, 0]
        expected_duration = data.Duration(14, 5)
        result_duration = hw2.running_time(songs, playlist)
        self.assertEqual(expected_duration, result_duration)



    # Part 5
    def setUp(self):
        self.city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']]

    def test_valid_route(self):
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        expected = True
        result = hw2.validate_route(self.city_links, route)
        self.assertEqual(expected, result)


    # Part 6
    def test_longest_repetition_normal(self):
        nums = [1, 1, 2, 2, 1, 1, 1, 3]
        expected = 4
        result = hw2.longest_repetition(nums)
        self.assertEqual(expected, result)






if __name__ == '__main__':
    unittest.main()
