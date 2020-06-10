class Excelformat:
    def __init__(self):
        self.l = []

    def modify(self, s):
        if (s == 0): return "-"
        return s

    def update(self, datanow, past_calls, past_puts):
        self.l = []
        k = -1
        call_change_in_min = [0, 0, 0, 0, 0]
        puts_change_in_min = [0, 0, 0, 0, 0]
        for i in range(len(datanow)):
            t = datanow[i].li()
            for j in range(3):
                try:
                    call_change_in_min[j] = t[1] - past_calls[j][i]
                    puts_change_in_min[j] = t[-2] - past_puts[j][i]
                except:
                    call_change_in_min[j] = 0
                    puts_change_in_min[j] = 0

            for ind in range(3):
                t.insert((ind + 2), call_change_in_min[ind])
            for ind in range(3):
                t.insert(-1, puts_change_in_min[ind])

            t = list(map(self.modify, t))
            self.l.append(t)

    def postdata(self):
        return self.l
