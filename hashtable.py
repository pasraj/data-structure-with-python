class HashTable:
    def __init__(self):
        self.MAX = 100
        self.list_item = [None for i in range(self.MAX)]


    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        return h%100

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.list_item[h]=value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.list_item[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.list_item[h]=None

    
t = HashTable()
t["march 6"] = 310
t["march 7"] = 420

print("Value of string 'march 6' is :",t["march 6"])
print("Value of string 'march 7' is :",t["march 7"])

del t["march 7"]

print("Value of string 'march 7' is after delete:",t["march 7"])