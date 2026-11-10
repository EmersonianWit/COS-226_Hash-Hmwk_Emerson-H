# Attempt 2: Linked List with a Good Hash Function
# Uses movie titles as keys.
# The hash function uses each character and its position.
# Movies with the same title are stored in the same node.
# Collisions count each occupied linked-list node inspected.

import csv
import time


# Creates one node in the linked list
class MovieNode:
    def __init__(self, key, record):
        self.key = key
        self.records = [record]
        self.next = None


# Creates the linked list hash table
class LinkedListHashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size

        self.collisions = 0
        self.used_buckets = 0
        self.unique_keys = 0
        self.record_count = 0

    # Hash function: multiplies each character by its position
    def hash_function(self, key):
        hash_value = 0
        position = 1

        for character in key:
            hash_value += ord(character) * position
            position += 1

        return hash_value % self.size

    # Adds a movie record to the hash table
    def insert(self, key, record):
        if key is None or key.strip() == "":
            return

        index = self.hash_function(key)

        current = self.buckets[index]
        previous = None

        # Search the linked list for the title
        while current is not None:
            self.collisions += 1

            # Store duplicate titles in the same node
            if current.key == key:
                current.records.append(record)
                self.record_count += 1
                return

            previous = current
            current = current.next

        # Create a new node if the title was not found
        new_node = MovieNode(key, record)

        if previous is None:
            self.buckets[index] = new_node
            self.used_buckets += 1
        else:
            previous.next = new_node

        self.unique_keys += 1
        self.record_count += 1

    # Searches for a movie title
    def search(self, key):
        if key is None or key.strip() == "":
            return []

        index = self.hash_function(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.records[:]

            current = current.next

        return []

    # Calculates the number of unused buckets
    def get_wasted_space(self):
        return self.size - self.used_buckets


# Loads movie records from the CSV file
def load_movie_data(filename):
    movies = []
    skipped_records = 0

    with open(filename, "r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None or "movie_title" not in reader.fieldnames:
            raise ValueError("The CSV file must contain a movie_title column.")

        for record in reader:
            title = record.get("movie_title")

            if title is None or title.strip() == "":
                skipped_records += 1
            else:
                movies.append(record)

    return movies, skipped_records


# Runs the second hash table experiment
def main():
    movies, skipped_records = load_movie_data("MOCK_DATA.csv")

    # Creates a hash table with 15,013 buckets
    table = LinkedListHashTable(15013)

    start_time = time.perf_counter()

    for movie in movies:
        table.insert(movie["movie_title"], movie)

    construction_time = time.perf_counter() - start_time

    # Displays the required statistics
    print("Attempt 2: Linked list with better hash function")
    print("Hash table: Movie title as key")
    print("Wasted buckets:", table.get_wasted_space())
    print("Collisions:", table.collisions)
    print("Construction time:", round(construction_time, 6), "seconds")


if __name__ == "__main__":
    main()
