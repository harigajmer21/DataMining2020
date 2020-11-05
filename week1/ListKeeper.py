class ListKeeper:
    def __init__(self, name, lst):
        # takes two arguments name and list of data as lst
        # then stores in self.store dictionary 
        self.store = {}
        self.store[name] = lst

    def add(self, name, lst):
        # takes two param
        # 1. container name
        # 2. data of container then puts in store dictionary
        if not isinstance(lst, list):
            return "Please provide only list data type"
        self.store[name] = lst
    
    def show(self):
        # returns names and list of information
        if len(self.store) == 0:
            return "Empty list please use add to store data"
        for name, lst in self.store.items():
            print("Name: {}, containes following list: {}".format(name, lst))
    
    def delete(self, name):
        # removes the container and data
        if name not in self.store:
            return "Sorry, Given name doesn't match the data"
        self.store.pop(name, None)        
        self.show()
    
    def sort(self, name):
        # sorts the list data by container name
        if name not in self.store:
            return "Sorry, Given name doesn't match the data"
        self.store[name].sort()
        self.show()
    
    def append(self, name, lst):
        # add more data insider container lst by given name
        if name not in self.store:
            return "Sorry, Given name doesn't match the data"
        
        if not isinstance(lst, list):
            return "Please provide only list data type"
        self.store[name].extend(lst)
        self.show()
        