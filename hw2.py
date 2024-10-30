import data

# Write your functions for each part in the space below.

# Part 1
#Create a rectangle with two given points
#input: two points
#output: returns a Rectangle object defined by the top-left and bottom-right corners.
def create_rectangle(point1, point2):
    x_min = min(point1.x, point2.x)
    x_max = max(point1.x, point2.x)
    y_min = min(point1.y, point2.y)
    y_max = max(point1.y, point2.y)

    top_left = data.Point(x_min, y_max)
    bottom_right = data.Point(x_max, y_min)

    return data.Rectangle(top_left, bottom_right)


# Part 2
#compares two Duration objects if the first one is shorter than second one
#input: two durations
#output: Returns True if duration1 is shorter than duration2
def shorter_duration_than(duration1, duration2):
    return duration1.total_seconds() < duration2.total_seconds()


# Part 3
#remove songs to find those with a duration shorter than a specified duration
#input: a list of songs object and duration
#output: a list of song objects that have a duration shorter than the specified duration
def song_shorter_than(songs:list, duration):
    return [n for n in songs if n.duration.total_seconds() < duration.total_seconds()]

# Part 4
#calculates the total running time of a playlist based on the durations of the songs
#input: a list of Song objects and playlist
#output: total time of the playlist in mins and secs
def running_time(songs, playlist):
    total_minutes = 0
    total_seconds = 0
    for i in playlist:
        if 0 <= i < len(songs):
            duration = songs[i].duration
            total_minutes += duration.minutes
            total_seconds += duration.seconds

    total_minutes += total_seconds // 60
    total_seconds = total_seconds % 60

    return data.Duration(total_minutes, total_seconds)


# Part 5
#validates if a given route is valid based on city links
#input: city_links(list of lists) and route
#output:returns True if the route is valid and False if the route is invalid
def validate_route(city_links, route):
    valid_links = []
    for link in city_links:
        valid_links.append(link)
    if len(route) <= 1:
        return True
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        if not ((city1 in valid_links and city2 in valid_links) or
                [city1, city2] in valid_links or
                [city2, city1] in valid_links):
            return False
    return True



# Part 6
#finds the starting index of the longest contiguous repetition of a single number in a list
#input: A list of integers (list[int])
#output:returns the starting index (int) of the longest contiguous repetition and None if the list is empty
def longest_repetition(nums):
    if not nums:
        return None
    max_length = 1
    current_length = 1
    start_index = 0
    current_start = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                start_index = current_start
            current_length = 1
            current_start = i
    if current_length > max_length:
        start_index = current_start
    return start_index

