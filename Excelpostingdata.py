class Excelformat:
    def __init__(self):
        self.l = []

    def modify(self, s):
        if (s == 0): return "-"
        return s

    def update(self, Data):
        pass

    def postdata(self):
        return self.l
