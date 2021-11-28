class ArrayExpr:
    def __init__(self, arr, start=0, end=-1) -> None:
        self.arr = arr
        l = len(arr)
        if end is None:
            end = l
        self.start = start if start >= 0 else l + start
        self.end = end if end >= 0 else l + end
        assert(self.start <= self.end)
        assert(0 <= self.start < l)
        assert(0 <= self.end <= l)
    
    def evaluate(self, field):
        return "".join([self.arr[i].outputs[field].evaluate() for i in range(self.start, self.end)])

    def len(self, field):
        return self.fieldlen(field) * (self.end - self.start)

    def fieldlen(self, field):
        l = self.end - self.start
        if l == 0:
            return 0
        return len(self.arr[self.start].outputs[field])
