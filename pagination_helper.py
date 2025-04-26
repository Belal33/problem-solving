# class PaginationHelper:
#     def __init__(self, collection, items_per_page):
#         self._item_count = len(collection)
#         self.items_per_page = items_per_page

#     def item_count(self):
#         return self._item_count

#     def page_count(self):
#         return -(self._item_count // -self.items_per_page)

#     def page_item_count(self, page_index):
#         return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
#             if 0 <= page_index < self.page_count() else -1

#     def page_index(self, item_index):
#         return item_index // self.items_per_page \
#             if 0 <= item_index < self._item_count else -1


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = list(collection)
        self.items_per_page = items_per_page
        self.pages = []
        self.items_num = len(self.collection)
        while self.collection:
            p = []
            for i in range(self.items_per_page):
                if self.collection:
                    p.append(self.collection.pop(0))
            self.pages.append(p)

    def item_count(self):
        return self.items_num

    def page_count(self):
        return len(self.pages)

    def page_item_count(self, page_index):
        return len(self.pages[page_index]) if page_index < len(self.pages) else -1

    def page_index(self, item_index):
        res = (item_index) // self.items_per_page
        if res < len(self.pages) and res > -1:
            return (
                res
                if res < len(self.pages[res]) and item_index < self.items_num
                else -1
            )
        else:
            return -1


collection = range(1, 25)

helper = PaginationHelper(collection, -1)
print(helper.page_index(46))
