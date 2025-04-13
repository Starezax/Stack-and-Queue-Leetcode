class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        freq = self.freq[val]

        if freq not in self.group:
            self.group[freq] = []

        self.group[freq].append(val)

        if freq > self.max_freq:
            self.max_freq = freq

    def pop(self):
        """
        :rtype: int
        """
        outp = self.group[self.max_freq].pop()

        self.freq[outp] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return outp

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()