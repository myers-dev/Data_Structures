import sys
sys.path.append('.')

from HashTable import HashTable

ht = HashTable()
ht.insert(2, "London")
ht.insert(7, "Paris")
ht.insert(8, "Cairo")

print("size:", ht.get_size())
ht.delete(2)
print("size:", ht.get_size())
ht.search(2)