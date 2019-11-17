class Note:
    def __init__(self, pitch, order, lenght, x, y):
        self.pitch = pitch
        self.string = int(self.pitch / 10)
        self.fret = self.pitch % 10
        self.order = order
        self.lenght = lenght
        self.x = x
        self.y = y


class Staff:
    def __init__(self, lines):
        self.line_1 = lines[4]
        self.line_2 = lines[3]
        self.line_3 = lines[2]
        self.line_4 = lines[1]
        self.line_5 = lines[0]
        self.space_between = abs(self.line_1 - self.line_2)
        self.line_top = self.line_5 - self.space_between
        self.line_bottom_1 = self.line_1 + self.space_between
        self.line_bottom_2 = self.line_1 + 2*self.space_between
        self.line_bottom_3 = self.line_1 + 3*self.space_between

