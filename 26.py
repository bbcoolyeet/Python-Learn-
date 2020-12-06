class Rect:
    def __init__(self,lens,wid):
        self.lens = lens
        self.wid = wid
    def find_area(self):
        x = self.lens * self.wid
        return x
    def find_peri(self):
        y = self.lens * self.wid * 2
        return y
lens = int(input("lenght pls"))
wid = int(input('width pls'))
r1 = Rect(lens,wid)
print('area:',r1.find_area())
print('perimeter:',r1.find_peri())

