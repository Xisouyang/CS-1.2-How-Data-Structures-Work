#!python
from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?

        Best and Worst Case: O(n * l), where n is the number of buckets and
        l is the length of the linked-list inside the bucket. We have to iterate
        through all buckets and each linked-list, bringing it to be l * n operations.

        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        Same as keys function^ """
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket

        values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                values.append(value)
        return values


    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?

        Best and Worst Case: O(n) - must iterate through each bucket, and for
        each bucket iterate through all key value pairs within that bucket's
        linked-list.
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?

        Best and Worst Case: O(1) - This implentation keeps a running count of
        entries within the hashtable. Thus we only need to return that count.
        """
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?

        Best case: O(1) - hash to find specific bucket, and find element at or near head
        of associated linked-list.
        Worst case: O(l) - Same process as above, but element may be near or at the end of
        or not in list, so we iterate through most or all of the list of length l.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda node_key: node_key[0] == key)

        if entry:
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        Same explanation as contains function.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda node_key: node_key[0] == key)

        if entry:
            return entry[1]

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?

        Same runtime explanation as get function, only difference is a
        few extra constant operations, which does not change runtime.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        newNode = (key, value)
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda node_key: node_key[0] == key)

        if entry == None:
            bucket.append(newNode)
            self.size += 1
        else:
            bucket.delete(entry)
            bucket.append(newNode)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?

        Same runtime explanation as get function, only difference is a
        few extra constant operations, which does not change runtime.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda node_key: node_key[0] == key)
        if entry:
            bucket.delete(entry)
            self.size -= 1
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
