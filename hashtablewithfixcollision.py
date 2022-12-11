class HashTable:
    def __init__(self):
        self.MAX = 10
        self.list_item = [[] for i in range(self.MAX)]


    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        return h%10

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.list_item[h]):
            if len(element) == 2 and element[0]==key:
                self.list_item[h][idx]=(key, value)
                found = True
                break
        if not found:
            self.list_item[h].append((key, value))
            

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.list_item[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.list_item[h]):
            if element[0] == key:
                del self.list_item[h][idx]


t = HashTable()

t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457

print(t.list_item)

print(t["march 7"])
print(t["march 8"])

del t["march 8"]

print(t["march 8"])