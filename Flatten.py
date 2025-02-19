# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
# TC - O(n + m) => n is number of integers in the list and m is the number of lists
# SC - O(n + m)
# Complexities - Doubtful

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        self.fixStackTop()
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        self.fixStackTop()
        return len(self.stack) > 0

    def fixStackTop(self):
        while self.stack and not self.stack[-1].isInteger():
            top = self.stack.pop().getList()
            self.stack.extend(top[::-1])


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
