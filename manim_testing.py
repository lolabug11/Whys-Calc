from manimlib import *

class Test(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        axis = Axes()
        text = Text("Hello World")
        self.add(axis)
        self.play(ShowCreation(square))
        self.wait(4)
        self.play(Transform(square,circle),run_time=3)
        self.wait(3.5)
        self.play(Transform(circle,text),run_time=2)

def get_points(formula,range1):
    points = []
    range1 *= 1000
    for i in range(int(range1)):
        y = eval(formula,{'x': i/100})
        points.append((i,y))
    return points


class Test2(Scene):

    def construct(self):

        axis = Axes(x_range=[0,500],y_range=[0,240])
        self.add(axis)
        cord_pair = get_points('15*x**2 + 10*x + 5',100)
        graph = VMobject()
        graph.set_points_as_corners([
            axis.c2p(*point) for point in cord_pair
        ])
        self.play(ShowCreation(graph),run_time=10)