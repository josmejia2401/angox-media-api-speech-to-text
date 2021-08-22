class CacheAny:
    
    def __init__(self, max_cache=None):
        self.__max_cache = max_cache
        self.__dict = {}
    
    def get(self, k):
        if k is None:
            raise Exception('key is required')
        if k in self.__dict:
            return self.__dict[k]
        return None

    def add(self, k, v):
        if k is None:
            raise Exception('key is required')
        vk = self.get(k)
        if vk:
            raise Exception('the key already exists')
        self.__dict[k] = v

    def put(self, k, v):
        if k is None:
            raise Exception('key is required')
        self.__dict[k] = v

    def pop(self, k):
        if k is None:
            raise Exception('key is required')
        vk = self.get(k)
        if vk:
            return self.__dict.pop(k)
        return None

    def remove(self, k):
        if k is None:
            raise Exception('key is required')
        vk = self.get(k)
        if vk:
            del self.__dict[k]

    def clear(self):
        self.__dict.clear()