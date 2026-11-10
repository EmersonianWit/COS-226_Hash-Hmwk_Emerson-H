# COS 226 - Hash Something Out

This project uses `MOCK_DATA.csv`, which contains 15,000 movie records, to compare different hash table designs. Hash Table 1 uses movie titles as keys, while Hash Table 2 uses movie quotes. When a key appears more than once, the matching movie records are stored together. Each program reports the number of unused buckets, the number of collisions, and the time required to build the table. A collision is counted each time an occupied node or bucket is checked during insertion.

For Attempt 1, I created a linked-list hash table using movie titles. Its hash function only uses the length of each title, which caused many titles to be placed in the same buckets. The result was 2,297,436 collisions and 14,906 unused buckets. In Attempt 2, I kept the same table and linked-list method but changed the hash function so that it uses each character's value and position. This reduced collisions to 9,496 and left 7,247 buckets unused. Using more information from each title greatly improved the distribution.

For Attempt 3, I used movie quotes with linear probing. The hash function adds the numerical values of the characters but does not consider their order. This resulted in 91,702,598 collisions and 5,120 unused buckets. In Attempt 4, I kept linear probing and the same table size but changed the hash function to consider each character's position. Collisions dropped to 29,029. The number of unused buckets stayed the same because the table stored the same number of unique quotes.

For Attempt 5, I returned to the movie-title linked-list table from Attempt 2 and increased its size from 15,013 to 20,011 buckets. This reduced collisions from 9,496 to 8,170, but increased the number of unused buckets from 7,247 to 11,595. The larger table gave titles more room, but it also used more space.

Overall, the character-position hash function performed much better than using only the title length or adding character values without considering their order. Attempt 2 had far fewer collisions than Attempt 1, and Attempt 4 greatly improved on Attempt 3. Attempt 5 reduced collisions a little further than Attempt 2, but left more buckets unused.
