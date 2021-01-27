import tkinter
import itertools

class Screen:
    def __init__(self, width, height, title, background):
        #calculate center of screen
        self.zeros = [int(width/2), int(height/2)]

        #initialize tkinter window for displaying graphics
        self.window = tkinter.Tk()
        self.window.title(title)
        self.image = tkinter.Canvas(self.window, width=width, height=height, bg=background)
        self.image.pack()

    def create_polygon(self, vertices, color):
        # create coordinates starting in center of screen
        coords = list(itertools.chain(*[[v0 + self.zeros[0], v1 + self.zeros[1]] for v0,v1 in vertices]))
        # draw triangle on screen
        self.image.create_polygon(coords, fill=color, outline="black")

    def create_arrow(self, points, color):
        a, b = points[0], points[1]
        return self.image.create_line(a[0], a[1], b[0], b[1], fill=color, arrow=tkinter.BOTH)

    def clear(self):
        #clear display
        self.image.delete('all')

    def delete(self, item):
        self.image.delete(item)

    def after(self, time, function):
        #call tk.Tk's after() method
        self.window.after(time, function)
