import random

def longest_linked_list_chain(keys, buckets, loops=10):
    '''
    rolls 'keys' number of random keys into 'buckets' number of buckets and count collisions

    run 'loops' number of times
    '''
    for i in range(loops):
        key_counts = {}
        for i in range(buckets):
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1
        # tally up and find the largest linked list chain (index where we had the most collisions)
        largest_number = 0    
        for key in key_counts:
            if key_counts[key] > largest_number:
                largest_number = key_counts[key]
        print(f"Longest linked list chain for {keys} keys in {buckets} buckets (Load Factor: {keys/buckets:.2f}: {largest_number})")

# longest_linked_list_chain(7, 10, 5)
# longest_linked_list_chain(70, 100, 5)
# longest_linked_list_chain(700, 1000, 5)
# longest_linked_list_chain(7000, 10000, 5)
# longest_linked_list_chain(70000, 100000, 5)
# longest_linked_list_chain(700000, 1000000, 5)
longest_linked_list_chain(9000000, 10000000, 5)