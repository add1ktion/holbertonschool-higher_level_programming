#!/usr/bin/python3
"""VerboseList: list with operation notifications"""


class VerboseList(list):
    """List subclass that logs append/extend/remove/pop operations"""

    def append(self, item):
        """Add item with notification"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list with notification"""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """Remove item with notification"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item with notification"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        super().pop(index)
