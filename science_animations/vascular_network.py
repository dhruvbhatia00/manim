from manimlib.imports import *

class NodeVessel(VGroup):
    def __init__(self, radius, length, num_branches):
        self.radius = radius
        self.length = length
        self.num_branches = num_branches
        self.children = VGroup()
        self.parent = None
        self.angle = 0
        self.layers = [VGroup(self)]


        el = Ellipse(height = self.radius*2, width = self.radius * 4/3, fill_opacity = 1)
        top = Line(ORIGIN, self.length * RIGHT, color=RED)
        top.move_to(el.get_top() + top.get_width()/2 * RIGHT)
        bottom = Line(ORIGIN, self.length * RIGHT, color=RED)
        bottom.move_to(el.get_bottom() + bottom.get_width()/2 * RIGHT)
        rect_points = [top.get_start(), top.get_end(), bottom.get_end(), bottom.get_start()]
        rect = Polygon(*rect_points, color=RED, fill_opacity=0.4, stroke_width=0)
        rect.add_to_back()


        self.el = el
        self.top = top
        self.bottom = bottom
        self.rect = rect
        self.vessel = VGroup(self.el, self.top, self.bottom, self.rect)

        VGroup.__init__(self, self.vessel, self.children)

    def get_lumen_start(self):
        return self.el.get_center()

    def get_lumen_end(self):
        return (self.top.get_right() + self.bottom.get_right())/2

    def add_layer(self):
        self.layers.append(VGroup())
        if len(self.children) != 0:
            for child in self.children:
                child.add_layer()
                self.layers[-1].add(child.layers[-1])
        else:
            for i in range(self.num_branches):
                new_node = NodeVessel(self.radius/self.num_branches, self.length/self.num_branches, self.num_branches)
                new_node.parent = self
                new_node.angle = -self.num_branches * (PI / 16) / 2 + (i + 0.5) * (PI / 16)

                new_node.move_to(self.el.get_bottom() + self.length * math.cos(self.angle) * RIGHT)
                new_node.shift(new_node.get_center() - new_node.get_lumen_start())
                new_node.shift(self.radius*2/self.num_branches * (i+0.5) * UP)
                new_node.shift(self.length * math.sin(self.angle) * UP)


                new_node.top.rotate(new_node.angle, about_point=new_node.top.get_left())
                new_node.bottom.rotate(new_node.angle, about_point=new_node.bottom.get_left())
                rect_points = [new_node.top.get_start(), new_node.top.get_end(), new_node.bottom.get_end(), new_node.bottom.get_start()]
                new_node.rect.become(Polygon(*rect_points, color=RED, fill_opacity=0.4, stroke_width=0))
                new_node.rect.add_to_back()

                self.layers[-1].add(new_node.layers[-1])
                self.children.add(new_node)
        return self

    def add_layers(self, num_layers):
        for _ in range(num_layers):
            self.add_layer()
        return self

    def get_last_layer(self):
        return self.layers[-1]



class SelfSimilarity(MovingCameraScene):
    CONFIG = {
        "camera_config": {"background_color": "#2F2F2E",},
        "text_config": {"stroke_color": "#2F2F2E", "fill_color": BLACK},
        "back": r"C:\Manim\manim-26_05_2020\science_animations\blackboard_texture.png",
    }

    def construct(self):
        back = ImageMobject(self.back).scale(4)
        self.add(back)
        #text1 = TextMobject("Vascular Networks are Self-Similar", **self.text_config)

        network = NodeVessel(1, 5, 3).add_layers(2).move_to(ORIGIN)
        self.play(ShowCreation(network))
        self.wait(2)

        network2 = NodeVessel(1, 5, 3).add_layers(1).move_to(2*DOWN).align_to(network, LEFT, alignment_vect=UP)
        self.play(network.shift, 2*UP)
        self.play(TransformFromCopy(network.children[1], network2), run_time= 1.4)
        self.wait()
        network2.add_layer()
        self.play(ShowCreation(network2.get_last_layer()))
        #self.play(Write(text1))
        self.wait(2)

        self.play(network.move_to, ORIGIN,
                  network2.move_to, ORIGIN,
                  FadeOut(network2))
        self.remove(network2)

        self.wait(2)

        network3 = NodeVessel(2, 10, 4).add_layers(4).move_to(2.5*DOWN)
        self.play(network.shift, 2*UP)
        self.play(Write(network3), run_time=1.5)
        self.play(self.camera_frame.set_width, 20,
                  VGroup(network, network3).move_to, ORIGIN,
                  back.scale, 1.40625)

        self.wait(2)


class Test(MovingCameraScene):
    CONFIG = {

    }

    def construct(self):
        network = NodeVessel(1, 10, 3).add_layers(4).move_to(2*LEFT)
        self.play(ShowCreation(network))

        self.wait()

        self.play(self.camera_frame.set_width, 20)
        self.wait(5)
