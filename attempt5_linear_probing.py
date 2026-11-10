# Attempt 4: Linear Probing with a Good Hash Function
# Uses movie quotes as keys.
# The hash function uses each character and its position.
# Movies with the same quote are stored in the same bucket.
# Collisions count each occupied bucket inspected.

import csv
import time


# Creates the linear probing hash table
class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.records = [None] * size

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
        start_index = index

        # Searches for an empty bucket or matching quote
        while self.keys[index] is not None:
            self.collisions += 1

            # Store duplicate quotes in the same bucket
            if self.keys[index] == key:
                self.records[index].append(record)
                self.record_count += 1
                return

            # Move to the next bucket
            index = (index + 1) % self.size

            if index == start_index:
                raise OverflowError("Hash table is full.")

        # Store the movie in the empty bucket
        self.keys[index] = key
        self.records[index] = [record]

        self.used_buckets += 1
        self.unique_keys += 1
        self.record_count += 1

    # Searches for a movie quote
    def search(self, key):
        if key is None or key.strip() == "":
            return []

        index = self.hash_function(key)
        start_index = index

        # Searches the buckets until the quote is found
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.records[index][:]

            # Move to the next bucket
            index = (index + 1) % self.size

            if index == start_index:
                break

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

        if reader.fieldnames is None or "quote" not in reader.fieldnames:
            raise ValueError("The CSV file must contain a quote column.")

        for record in reader:
            quote = record.get("quote")

            if quote is None or quote.strip() == "":
                skipped_records += 1
            else:
                movies.append(record)

    return movies, skipped_records


# Runs the fourth hash table experiment
def main():
    movies, skipped_records = load_movie_data("MOCK_DATA.csv")

    # Creates a hash table with 20,011 buckets
    table = LinearProbingHashTable(20011)

    start_time = time.perf_counter()

    for movie in movies:
        table.insert(movie["quote"], movie)

    construction_time = time.perf_counter() - start_time

    # Displays the required statistics
    print("Attempt 4: Linear probing with better hash function")
    print("Hash table: Movie quote as key")
    print("Wasted buckets:", table.get_wasted_space())
    print("Collisions:", table.collisions)
    print("Construction time:", round(construction_time, 6), "seconds")


if __name__ == "__main__":
    main()
