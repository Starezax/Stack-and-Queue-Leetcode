class MyStack(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        outp = self.queue1.pop(0)
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return outp

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1
