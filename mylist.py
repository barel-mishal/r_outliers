class MyList:
    def __init__(self):
        self.listy = []
        return

    def __str__(self):
        return f'{self.listy}'

    def append(self, item):
        self.listy = [].append(item)
        print(self.listy)
        return self.listy

    # def __iter__(self):
    #     return None


my_list = MyList()
print(my_list.append('google'))
