from manimlib.imports import *
import os
import pyclbr

class PlotTwoGraphsAtOnce(GraphScene):
    CONFIG = {
        "y_max" : 40,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 1,
        "x_axis_width": 6,
        "y_axis_height": 3,
        "axes_color" : GRAY,
    }
    def construct(self):
        self.graph_origin = -0.5 * DOWN + 3 * LEFT
        self.setup_axes(animate=True)
        graph_up = self.get_graph(lambda x : x**2,
                                    color = GOLD_A,
                                    x_min = 0,
                                    x_max = 3
                                    )
        f1 = TexMobject(r"f(x) = {x}^2", color = GOLD_A)
        f1.scale(0.7)
        label_coord1 = self.input_to_graph_point(3,graph_up)
        f1.next_to(label_coord1,RIGHT+UP)
        up_dot = Dot(self.input_to_graph_point(0, graph_up))
        up_dot.save_state()

        def up_updater(mob, alpha):
            up_dot.restore()
            up_dot.move_to(self.input_to_graph_point(alpha*3, graph_up) + 4* UP)

        def down_updater(mob, alpha):
            down_dot.restore()
            down_dot.move_to(self.input_to_graph_point(alpha*3, graph_down))

        self.graph_origin = 3.5 * DOWN + 3 * LEFT
        self.setup_axes(animate=True)
        graph_down = self.get_graph(lambda x : x**3,
                                    color = BLUE_D,
                                    x_min = 0,
                                    x_max = 3
                                    )
        graphs=VGroup(graph_up,graph_down)
        f2 = TexMobject(r"f(x) = {x}^3", color = BLUE_D)
        f2.scale(0.7)
        label_coord2 = self.input_to_graph_point(3,graph_down)
        f2.next_to(label_coord2,RIGHT+UP)
        down_dot = Dot(self.input_to_graph_point(0, graph_down))
        down_dot.save_state()


        self.play(
            ShowCreation(graphs),
            run_time = 2,
        )
        self.play(ShowCreation(f1), ShowCreation(f2))
        self.play(ShowCreation(up_dot), ShowCreation(down_dot))
        self.play(UpdateFromAlphaFunc(up_dot, up_updater), UpdateFromAlphaFunc(down_dot, down_updater))
        self.wait(3)


class VTGraphs(GraphScene):
    CONFIG = {
        "y_max" : 40,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 1,
        "x_axis_width": 6,
        "y_axis_height": 3,
        "axes_color" : GRAY,
    }
    def construct(self):
        self.graph_origin = -0.5 * DOWN + 3 * LEFT
        self.setup_axes(animate=True)
        graph_up = self.get_graph(lambda a : a**2,
                                    color = GOLD_A,
                                    x_min = 0,
                                    x_max = 3
                                    )
        f1 = TexMobject(r"f(x) = {x}^2", color = GOLD_A)
        f1.scale(0.7)
        label_coord1 = self.input_to_graph_point(3,graph_up)
        f1.next_to(label_coord1,RIGHT+UP)
        up_dot = Dot(self.input_to_graph_point(0, graph_up))
        up_dot.save_state()

        def up_updater(mob):
            #up_dot.restore()
            mob.move_to(self.input_to_graph_point(x.get_value(), graph_up) + 4* UP)

        def down_updater(mob):
            #down_dot.restore()
            mob.move_to(self.input_to_graph_point(x.get_value(), graph_down))

        self.graph_origin = 3.5 * DOWN + 3 * LEFT
        self.setup_axes(animate=True)
        graph_down = self.get_graph(lambda a : a**3,
                                    color = BLUE_D,
                                    x_min = 0,
                                    x_max = 3
                                    )
        graphs=VGroup(graph_up,graph_down)
        f2 = TexMobject(r"f(x) = {x}^3", color = BLUE_D)
        f2.scale(0.7)
        label_coord2 = self.input_to_graph_point(3,graph_down)
        f2.next_to(label_coord2,RIGHT+UP)
        down_dot = Dot(self.input_to_graph_point(0, graph_down))
        down_dot.save_state()

        x = ValueTracker(0)
        x_tex = DecimalNumber(x.get_value()).add_updater(lambda v: v.set_value(x.get_value()))
        x_label = TexMobject("x = ")
        x_label.next_to(x_tex, LEFT, buff=0.4, aligned_edge=x_label.get_bottom())

        group = VGroup(x_tex, x_label).scale(1).move_to(5 * LEFT)

        y1_tex = DecimalNumber(x.get_value()**2).add_updater(
            lambda v: v.set_value(x.get_value()**2))
        y1_label = TexMobject("f_1(x) = ")
        y1_label.next_to(y1_tex, LEFT, buff=0.4, aligned_edge=y1_label.get_bottom())

        group1 = VGroup(y1_tex, y1_label).scale(1).move_to(5 * RIGHT + 2 * UP)

        y2_tex = DecimalNumber(x.get_value()**3).add_updater(
            lambda v: v.set_value(x.get_value()**3))
        y2_label = TexMobject("f_1(x) = ")
        y2_label.next_to(y2_tex, LEFT, buff=0.4, aligned_edge=y2_label.get_bottom())

        group2 = VGroup(y2_tex, y2_label).scale(1).move_to(5 * RIGHT - 2 * UP)


        self.play(
            ShowCreation(graphs),
            run_time = 2,
        )
        self.play(ShowCreation(f1), ShowCreation(f2))
        up_dot.add_updater(up_updater)
        down_dot.add_updater(down_updater)
        self.play(ShowCreation(up_dot), ShowCreation(down_dot), Write(group), Write(group1), Write(group2))
        #self.play(UpdateFromAlphaFunc(up_dot, up_updater), UpdateFromAlphaFunc(down_dot, down_updater))
        self.play(
            x.set_value, 3,
            #rate_func=linear,
            run_time=3
        )
        self.wait()


class Loop(Scene):
    def construct(self):
        loop = VMobject()
        self.loop = loop
        points = [
            3*RIGHT,
            2*RIGHT+UP,
            3*RIGHT + 3*UP,
            UP,
            2*UP+LEFT,
            2*LEFT + 2*UP,
            3*LEFT,
            2*LEFT+DOWN,
            3*LEFT+2*DOWN,
            2*DOWN+RIGHT,
            LEFT+DOWN,
        ]



        loop.set_points_smoothly(points)
        dots = VGroup(*map(Dot, points))

        sdot = Dot().set_color(RED)

        sdot.move_to(points[0])
        sdot.save_state()

        def sdot_updater(mob, alpha):
            sdot.restore()
            sdot.move_to(loop.point_from_proportion(alpha))


        self.play(ShowCreation(dots), ShowCreation(sdot))
        self.play(Write(loop))
        self.play(UpdateFromAlphaFunc(sdot, sdot_updater), run_time=8)
        self.play(FadeOut(sdot), FadeOut(dots))

        line = Line(3*LEFT + DOWN, 3*RIGHT + DOWN)

        self.play(Transform(loop, line))
        self.wait(10)


class PathHomotopy(Scene):
    def construct(self):
        path1_points = [
            3*LEFT + 2* DOWN,
            2*LEFT
            -3*LEFT + 1* UP,
            2 * DOWN,
            -2 * LEFT -3 * UP,
        ]

        path1 = VMobject()
        path1.set_points_smoothly(path1_points)

        path2_points =[
            3*LEFT + 2*DOWN,
            -2*LEFT + 3*UP,
            3 * UP,
            -2*LEFT - 3* UP,
        ]


        path2 = VMobject()
        path2.set_points_smoothly(path2_points)

        dots = VGroup(Dot(3*LEFT + 2*DOWN), Dot(-2*LEFT - 3*UP))
        label1 = TextMobject("A").next_to(dots[0], DOWN, buff=MED_SMALL_BUFF)
        label2 = TextMobject("B").next_to(dots[1], DOWN, buff=MED_SMALL_BUFF)

        group = VGroup(Dot(3*LEFT + 2*DOWN), Dot(-2*LEFT + -3*UP), label1, label2)

        self.play(ShowCreation(group))
        self.play(*[
            ShowCreation(Dot(p).set_color(YELLOW)) for p in path1_points
        ])
        self.play(Write(path1), Write(path2))
        self.wait(3)
        self.play(TransformFromCopy(path1, VMobject().set_points_smoothly(path2_points)) ,runtime=2)
        self.wait(4)

class BezierFigure8(Scene):
    def construct(self):
        test = [
            LEFT, RIGHT, UP + RIGHT,
        ]

        points = [
            ORIGIN,
            1*LEFT + 1*UP,
            2 * LEFT,
            1 * LEFT + 1 * DOWN,
            ORIGIN,
            1 * RIGHT + 1 * UP,
            2 * RIGHT,
            1 * RIGHT + 1 * DOWN,
            ORIGIN,
        ]

        left_points = [
            1 * RIGHT + 1 * DOWN,
            ORIGIN,
            1 * LEFT + 1 * UP,
            2 * LEFT,
            1 * LEFT + 1 * DOWN,
            ORIGIN,
            1 * RIGHT + 1 * UP,
        ]

        right_points = [
            1 * LEFT + 1 * DOWN,
            ORIGIN,
            1 * RIGHT + 1 * UP,
            2 * RIGHT,
            1 * RIGHT + 1 * DOWN,
            ORIGIN,
            1 * LEFT + 1 * UP,
        ]

        curve = VMobject().set_points_smoothly(points).shift(UP)

        curve_left = curve.get_subcurve(-0.125, 0.625, True)
        curve_right = curve.get_subcurve(0.25 + 0.125, 0.125, True)


        self.play(Write(curve))
        self.play(ApplyMethod(curve_left.shift, 3*DOWN + 2*LEFT), ApplyMethod(curve_right.shift, 3*DOWN + 2*RIGHT))
        self.wait(2)

def lemniscate(a):
    x = lambda t: (a * np.sqrt(2) * np.cos(2*PI*t))/(1 + (np.sin(2*PI*t))**2)
    y = lambda t: (a * np.sqrt(2) * np.cos(2*PI*t) * np.sin(2*PI*t))/(1 + (np.sin(2*PI*t))**2)
    return lambda t: np.array([x(t), y(t), 0])

def circ(r):
    x = lambda t: r * np.cos(2*PI*t)
    y = lambda t: -r * np.sin(2*PI*t)
    return lambda t: np.array([x(t), y(t), 0])

class ParamFigure8(Scene):
    def construct(self):
        t2c = {"{S}": BLUE,
               "{A}": YELLOW,
               "{B}": RED,
               "{\\cap}": ORANGE}

        lem = ParametricFunction(lemniscate(1)).scale(3).set_color(BLUE)
        S = TexMobject(r"{S}", tex_to_color_map=t2c).scale(2.5).next_to(lem, DOWN, buff=MED_SMALL_BUFF)
        curve = VGroup(lem, S)

        self.play(ShowCreation(lem), Write(S))
        self.play(curve.scale, 1/2.5, curve.shift, 3*UP)

        left = ParametricFunction(lambda t: lemniscate(1)(t * 0.68 + 0.16)).scale(3/2.5).set_color(YELLOW).move_to(lem, LEFT)
        right = left.copy().rotate(PI, about_point=left.point_from_proportion((0.25 - 0.16) / 0.68)).set_color(RED)
        int = VGroup(lem.get_subcurve(0.16, 0.34).set_color(ORANGE),
                     lem.get_subcurve(0.66, 0.84).set_color(ORANGE))


        left_tear = ParametricFunction(lambda t: lemniscate(1)(t * 0.5 + 0.25)).scale(3 / 2.5).set_color(YELLOW).move_to(lem, LEFT)
        right_tear = left_tear.copy().rotate(PI, about_point=left_tear.point_from_proportion(0)).set_color(RED)

        left_circle = ParametricFunction(circ(0.5)).scale(3 / 2.5).set_color(YELLOW)
        right_circle = left_circle.copy().rotate_about_origin(PI).set_color(RED)

        odot = Dot(lem.point_from_proportion(0.25)).set_color(ORANGE)

        self.play(FadeIn(left), FadeIn(right), FadeIn(int))


        A = TexMobject(r"{A}").set_color(YELLOW)
        A2 = TexMobject(r"A \simeq S^1").set_color(YELLOW)
        B = TexMobject(r"{B}").set_color(RED)
        B2 = TexMobject(r"B \simeq S^1").set_color(RED)
        AintB = TexMobject("{A} {\\cap} {B}").set_color(ORANGE)
        AintB2 = TexMobject("A \cap B \simeq *").set_color(ORANGE)
        union = TexMobject("{\\cup}")

        self.play(left.shift, 2*DOWN + 3*LEFT, right.shift, 2*DOWN, 3*RIGHT, int.shift, 2*DOWN)
        left.save_state()
        int.save_state()
        right.save_state()

        left_tear.shift(2*DOWN + 3*LEFT)
        right_tear.shift(2*DOWN, 3*RIGHT)
        odot.shift(2*DOWN)
        left_circle.move_to(left_tear.get_center())
        right_circle.move_to(right_tear.get_center())


        A.next_to(left, DOWN, buff=MED_SMALL_BUFF)
        A2.next_to(left_circle, DOWN, buff=MED_SMALL_BUFF)
        B.next_to(right, DOWN, buff=MED_SMALL_BUFF)
        B2.next_to(right_circle, DOWN, buff=MED_SMALL_BUFF)
        AintB.next_to(int, DOWN, buff=MED_SMALL_BUFF)
        AintB2.move_to(AintB.get_center())
        labels = VGroup(*map(lambda l: l.scale(1), [A, B, AintB]))
        self.play(FadeInFromDown(labels))

        self.play(ReplacementTransform(left, left_tear), ReplacementTransform(right, right_tear))
        self.play(ReplacementTransform(left_tear, left_circle), ReplacementTransform(right_tear, right_circle),
                  ReplacementTransform(A, A2), ReplacementTransform(B, B2))
        self.play(ReplacementTransform(int, odot), ReplacementTransform(AintB, AintB2))
        self.play(curve.to_edge, LEFT)

        grp1 = VGroup(left_circle, odot, right_circle)
        grp2 = VGroup(left.restore(), int.restore(), right.restore()).arrange(RIGHT, buff=1.5).to_edge(RIGHT).shift(lem.get_center()[1]*UP)
        self.play(ReplacementTransform(grp1, grp2), ApplyMethod(A2.next_to, left, DOWN, buff=MED_SMALL_BUFF),
                  ApplyMethod(B2.next_to, right, DOWN, buff=MED_SMALL_BUFF),
                  ApplyMethod(AintB2.next_to, int, DOWN, buff=MED_SMALL_BUFF))

        A = TexMobject(r"A").set_color(YELLOW).shift(UP + RIGHT)
        B = TexMobject(r"B").set_color(RED).shift(DOWN + LEFT)
        AintB = TexMobject(r"A \cap B").set_color(ORANGE).shift(UP + LEFT)
        newS = TexMobject(r"A \cup B").set_color(BLUE).shift(DOWN + RIGHT)
        ar1 = ConnectingArrow(AintB, A)
        ar2 = ConnectingArrow(AintB, B)
        ar3 = ConnectingArrow(A, newS)
        ar4 = ConnectingArrow(B, newS)
        cd = VGroup(A, B, AintB, newS, ar1, ar2, ar3, ar4).shift(DOWN)

        self.play(Write(cd))

        self.play(ApplyWave(A2), ApplyWave(B2))
        self.play(Transform(A, TexMobject(r"S^1").set_color(YELLOW).move_to(A.get_center())),
                  Transform(B, TexMobject(r"S^1").set_color(RED).move_to(B.get_center())))
        self.play(ApplyWave(AintB2))
        self.play(Transform(AintB, TexMobject(r"*").set_color(ORANGE).move_to(AintB.get_center())),
                  Transform(ar1, ConnectingArrow(TexMobject(r"*").set_color(ORANGE).move_to(AintB.get_center()), A)))

        pi_1_text = TextMobject("Applying $\pi_1$...").shift(3*DOWN)
        self.play(Write(pi_1_text))
        self.play(Transform(A, TexMobject(r"\pi_1(S^1)").set_color(YELLOW).move_to(A.get_center())),
                  Transform(B, TexMobject(r"\pi_1(S^1)").set_color(RED).move_to(B.get_center())),
                  Transform(AintB, TexMobject(r"\pi_1(*)").set_color(ORANGE).move_to(AintB.get_center())),
                  Transform(newS, TexMobject(r"\pi_1(S)").set_color(BLUE).move_to(newS.get_center())),
                  Transform(ar1, ConnectingArrow(TexMobject(r"\pi_1(*)").move_to(AintB.get_center()),
                                                 TexMobject(r"\pi_1(S^1)").move_to(A.get_center()))),
                  Transform(ar2, ConnectingArrow(TexMobject(r"\pi_1(*)").move_to(AintB.get_center()),
                                                 TexMobject(r"\pi_1(S^1)").move_to(B.get_center()))),
                  Transform(ar3, ConnectingArrow(TexMobject(r"\pi_1(S^1)").move_to(A.get_center()),
                                                 TexMobject(r"\pi_1(S)").move_to(newS.get_center()))),
                  Transform(ar4, ConnectingArrow(TexMobject(r"\pi_1(S^1)").move_to(B.get_center()),
                                                 TexMobject(r"\pi_1(S)").move_to(newS.get_center())))
                  )
        self.play(FadeOut(pi_1_text))
        self.wait(1)

        text1 = TextMobject(r"A pushout square of groups").shift(3*DOWN)

        self.play(Transform(A, TexMobject(r"\mathbb{Z}").set_color(YELLOW).move_to(A.get_center())),
                  Transform(B, TexMobject(r"\mathbb{Z}").set_color(RED).move_to(B.get_center())),
                  Transform(AintB, TexMobject(r"*").set_color(ORANGE).move_to(AintB.get_center())),
                  Transform(ar1, ConnectingArrow(TexMobject(r"*").move_to(AintB.get_center()),
                                                 TexMobject(r"\mathbb{Z}").move_to(A.get_center()))),
                  Transform(ar2, ConnectingArrow(TexMobject(r"*").move_to(AintB.get_center()),
                                                 TexMobject(r"\mathbb{Z}").move_to(B.get_center()))),
                  Transform(ar3, ConnectingArrow(TexMobject(r"\mathbb{Z}").move_to(A.get_center()),
                                                 TexMobject(r"\pi_1(S)").move_to(newS.get_center()))),
                  Transform(ar4, ConnectingArrow(TexMobject(r"\mathbb{Z}").move_to(B.get_center()),
                                                 TexMobject(r"\pi_1(S)").move_to(newS.get_center()))),
                  Write(text1))

        self.wait(2)
        self.play(FadeOut(cd), FadeOut(text1))
        self.play(Write(TextMobject(r"The Fundamental Group $\pi_1(S) = \mathbb{Z} \otimes \mathbb{Z}$").shift(DOWN)))

        self.wait(5)

def spiral(r):
    x = lambda t: r * np.cos(2*PI*t*8)
    y = lambda t: -r * np.sin(2*PI*t*8)
    z = lambda t: 4 - (1-t)*8
    return lambda t: np.array([x(t), y(t), z(t)])

def torus(a, b):
    x = lambda u, v: (a*np.cos(u) + b)*np.cos(v)
    y = lambda u, v: (a*np.cos(u) + b)*np.sin(v)
    z = lambda u, v: a*np.sin(u)
    return lambda u, v: np.array([x(u,v), y(u,v), z(u,v)])

def mobius(R):
    x = lambda u, v: (R + u * np.cos(0.5 * v)) * np.cos(v)
    y = lambda u, v: (R + u * np.cos(0.5 * v)) * np.sin(v)
    z = lambda u, v: u * np.sin(0.5 * v)
    return lambda u, v: np.array([x(u,v), y(u,v), z(u,v)])



class CoveringSpaces(SpecialThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=60 * DEGREES,theta=45*DEGREES)
        self.play(ShowCreation(axes))
        # circle = ParametricFunction(circ(1)).set_color(RED)
        # self.play(ShowCreation(circle))
        # spir = ParametricFunction(spiral(1)).set_color(BLUE)
        # self.play(ShowCreation(spir))
        # #self.play(FadeOut(axes))
        # stuff = VGroup(circle, spir)
        # self.move_camera(phi=69*DEGREES, theta=0*DEGREES)
        # self.play(ApplyMethod(stuff.scale, 2))

        mobi = ParametricSurface(mobius(2), u_min=-1, u_max=1, v_min=0, v_max=2*PI)
        self.play(ShowCreation(mobi))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)


class Tester(Scene):
    CONFIG = {
        "matrix_config": {
            "v_buff": 1.5*1.3,
            "h_buff": 1.5*1.3,
            "bracket_h_buff": MED_SMALL_BUFF,
            "bracket_v_buff": MED_SMALL_BUFF,
            "add_background_rectangles_to_entries": False,
            "include_background_rectangle": False,
            #"element_to_mobject": TexMobject,
            "element_to_mobject_config": {},
            "element_alignment_corner": DR,
            "brackets": False,
        },
        "element_to_mobject_config": {},
        "text_config": {"background_stroke_color": WHITE, "fill_color": DARK_BLUE},
    }

    def matrix_to_mob_matrix(self, matrix):
        return np.vectorize(TexMobject)(
            matrix, **self.element_to_mobject_config
        )

    def construct(self):
        A = Polygon(ORIGIN, 3 * RIGHT, 2 * RIGHT + 2 * UP, fill_opacity=1)
        self.play(ShowCreation(A))

        B = BraceLabel(A, r"\text{triangle}", RIGHT, **self.text_config)
        self.play(ShowCreation(B))

        self.wait(5)


def rect_func(u, v):
    x = 2*PI*u
    y = 6*PI*v
    z = 0
    return np.array([x, y, z])

def cylinder_func(u, v):
    x = np.cos(2*PI*u + 5*PI/4) + np.cos(PI/4)
    y = 6*PI*v
    z = np.sin(2*PI*u + 5*PI/4) + np.cos(PI/4)
    return np.array([x, y, z])

def homotopy_func(u, v, t):
    return (1-t)*rect_func(u, v) + t*cylinder_func(u, v)


class Tester3D(SpecialThreeDScene):
    def construct(self):
        axes = self.get_axes()
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        self.play(ShowCreation(axes))

        rect = ParametricSurface(rect_func)
        #rect.save_state()

        def homotopy(mob, alpha):
            #mob.restore()
            mob.become(ParametricSurface(lambda u, v: homotopy_func(u, v, alpha)))

        self.play(UpdateFromAlphaFunc(rect, homotopy))
        #self.begin_ambient_camera_rotation(rate=2)

        self.wait(5)


class FleasOnACircle(Scene):
    CONFIG = {
        "circle_radius": 5,
    }

    def flea(self, name, color):
        body = Circle(radius=0.3, stroke_color=color, fill_color=color, fill_opacity=1)
        title = TextMobject(name)
        return VGroup(body, title)


    def construct(self):
        circle = Circle(radius=self.circle_radius)
        self.play(ShowCreation(circle))

        a = self.flea("A", GREEN).move_to(self.circle_radius*RIGHT)
        b = self.flea("B", BLUE).move_to(self.circle_radius*UP)
        c = self.flea("C", PURPLE).move_to(self.circle_radius*LEFT)
        d = self.flea("D", YELLOW).move_to((self.circle_radius*DOWN))

        fleas = [a, b, c, d]
        flea_grp = VGroup(*fleas)
        self.play(*[ShowCreation(f) for f in fleas])

        def flea_updater(mob, dt):
            for flea in flea_grp:
                next = None
                for i in range(len(fleas)):
                    if fleas[i] == flea:
                        next = fleas[(i+1)%4]

                if next == None:
                    return

                direction = next.get_center() - flea.get_center()
                unit_dir = direction/np.linalg.norm(direction)

                flea.shift(unit_dir*dt)

        flea_grp.add_updater(flea_updater)
        self.add_foreground_mobject(flea_grp)

        self.wait(5)

class Trial(Scene):
    def construct(self):
        A = Tree(color=RED)
        print(A.get_height())

        self.play(ShowCreation(A))
        self.wait(5)


class Pythagoras(Scene):
    CONFIG = {
        "a": 3,
        "b": 4,
        "shape_config": {
            "fill_opacity": 0.5,
        }
    }

    class RightTri(VGroup):
        def __init__(self, a, b, direction, extra_text=False, **kwargs):
            if direction == "right":
                points = [ORIGIN, a*RIGHT, a*RIGHT + b*UP]
            else:
                points = [ORIGIN, a*LEFT, a*LEFT + b*UP]

            self.triangle = Polygon(*points, **kwargs)
            self.a = a
            self.b = b
            self.c = int(np.sqrt(self.a**2 + self.b**2))

            if extra_text:
                self.a_label = TextMobject("a = 3").next_to(self.triangle, DOWN)
                self.b_label = TextMobject("b = 4").rotate(PI/2)
                self.c_label = TextMobject("c = " + str(self.c))
            else:
                self.a_label = TextMobject("a").next_to(self.triangle, DOWN)
                self.b_label = TextMobject("b")
                self.c_label = TextMobject("c")

            self.angle = np.arcsin(self.b/self.c) if direction == "right" else -np.arcsin(self.b/self.c)

            shift = (0.2*(2*LEFT+UP)) if direction == "right" else (0.2*(UP+2*RIGHT))
            dir = RIGHT if direction == "right" else LEFT
            if extra_text:
                self.b_label.next_to(self.triangle, dir)
                self.c_label.rotate(self.angle).move_to(self.triangle.get_center() + shift)
            else:
                self.b_label.next_to(self.triangle, dir)
                self.c_label.move_to(self.triangle.get_center() + shift)

            self.labels = VGroup(self.a_label, self.b_label, self.c_label)

            VGroup.__init__(self, self.triangle, self.a_label, self.b_label, self.c_label)
            self.move_to(ORIGIN)

    class RightTriPoly(Polygon):
        def __init__(self, a, b, direction, **kwargs):
            if direction == "right":
                points = [ORIGIN, a*RIGHT, a*RIGHT + b*UP]
            else:
                points = [ORIGIN, a*LEFT, a*LEFT + b*UP]


            self.a = a
            self.b = b
            self.c = int(np.sqrt(self.a**2 + self.b**2))
            Polygon.__init__(self, *points, **kwargs)



    def construct(self):
        tri1 = self.RightTri(3, 4, "right", **self.shape_config).shift(UP)
        tri2 = self.RightTri(5, 2, "right", **self.shape_config).shift(UP)
        tri3 = self.RightTri(4, 4, "right", **self.shape_config).shift(UP)

        self.play(Write(tri1))

        goal_1 = TextMobject("We want to prove the Pythagorean Theorem:")
        goal_2 = TextMobject("that $a^2 + b^2 = c^2$ for any right triangle")
        goal = VGroup(goal_1, goal_2).arrange(DOWN).shift(3*DOWN)
        self.play(Write(goal))

        self.play(Transform(tri1, tri2))
        self.wait()
        self.play(Transform(tri1, tri3))
        self.wait()
        self.play(Transform(tri1, self.RightTri(3, 4, "right", **self.shape_config).shift(UP)))

        self.wait(3)

        self.clear()


        left_1 = self.RightTriPoly(3, 4, "right", **self.shape_config).rotate(PI)
        left_2 = self.RightTriPoly(3, 4, "right", **self.shape_config).rotate(3*PI/2).next_to(left_1, DOWN, buff=0, aligned_edge=LEFT)
        left_3 = self.RightTriPoly(3, 4, "right", **self.shape_config).rotate(2*PI).next_to(left_2, RIGHT, buff=0, aligned_edge=DOWN)
        left_4 = self.RightTriPoly(3, 4, "right", **self.shape_config).rotate(PI/2).next_to(left_3, UP, buff=0, aligned_edge=RIGHT)

        left = VGroup(left_1, left_2, left_3, left_4).move_to(ORIGIN).scale(0.8)

        lab_1 = VGroup(TextMobject("a"), TextMobject("b")).arrange(RIGHT, buff=2.6).next_to(left, UP).shift(0.25*LEFT)
        lab_2 = lab_1.copy().arrange(DOWN, buff = 2.6).next_to(left, RIGHT).shift(0.25*UP)
        lab_3 = lab_1.copy().arrange(LEFT, buff = 2.6).next_to(left, DOWN).shift(0.25*RIGHT)
        lab_4 = lab_1.copy().arrange(UP, buff = 2.6).next_to(left, LEFT).shift(0.25*DOWN)
        lab_5 = TextMobject("c").next_to(left, LEFT, buff=0, aligned_edge=UP).shift(0.45*(3.3*RIGHT+3.8*DOWN))
        lab_6 = TextMobject("c").next_to(left, UP, buff=0, aligned_edge=RIGHT).shift(0.45*(3.3*DOWN+3.8*LEFT))
        lab_7 = TextMobject("c").next_to(left, RIGHT, buff=0, aligned_edge=DOWN).shift(0.45*(3.3*LEFT+3.8*UP))
        lab_8 = TextMobject("c").next_to(left, DOWN, buff=0, aligned_edge=LEFT).shift(0.45*(3.3*UP+3.8*RIGHT))
        labs = VGroup(lab_1, lab_2, lab_3, lab_4, lab_5, lab_6, lab_7, lab_8)

        left.add(labs)



        self.play(FadeIn(left))




        self.wait(5)


# if __name__ == "__main__":
#     module_name = os.path.basename(__file__)
#     path = "C:\Manim\manim-26_05_2020"
#     os.chdir(path)
#     command_A = "python -m manim -pl "
#     command_B = "dhruv_scenes\homotopy.py" + " " + "Tester"
#     os.system(command_A + command_B)

class Pythagoras2(Scene):
    CONFIG = {

    }

    def construct(self):
        class LabelledTriangle(Polygon):
            def __init__(self, *vertices, **kwargs):
                assert len(vertices) == 3
                Polygon.__init__(self, *vertices, **kwargs)

            def get_braces(self):
                vertices = self.get_vertices()
                sides = []
                for i in range(len(vertices)):
                    sides.append(vertices[i] - vertices[i-1])

                side_lengths = list(map(np.linalg.norm, sides))
                perps = list(map(lambda x: np.array([x[1], -x[0], x[2]]), sides))
                len_dir = [[side_lengths[i], perps[i]] for i in range(len(vertices))]
                #len_dir.sort(key=lambda x: x[0])
                texts =['c', "b", 'a']
                labels = VGroup()
                for i in range(len(vertices)):
                    lab = BraceLabel(self, texts[i], len_dir[i][1])
                    labels.add(lab)

                return labels

            def get_labels(self):
                vertices = self.get_vertices()
                sides = []
                for i in range(len(vertices)):
                    sides.append(vertices[i] - vertices[i-1])

                side_lengths = list(map(np.linalg.norm, sides))
                perps = list(map(lambda x: np.array([x[1], -x[0], x[2]])/ np.linalg.norm(np.array([x[1], -x[0], x[2]])), sides))
                len_dir = [[side_lengths[i], perps[i]] for i in range(len(vertices))]
                #len_dir.sort(key=lambda x: x[0])
                texts =['c', "b", 'a']
                labels = VGroup()
                for i in range(len(vertices)):
                    lab = BraceLabel(self, texts[i], len_dir[i][1])
                    lab.brace.set_color(BLACK)
                    lab.label.set_color(WHITE).shift(-0.35*len_dir[i][1])
                    labels.add(lab)

                return labels


        intro = TextMobject("Today we will prove the ", "Pythagoras Theorem!")
        intro[1].set_color_by_gradient(RED, BLUE)
        self.play(Write(intro))
        self.wait(1)
        self.play(intro.shift, 3*UP)

        tri_1 = LabelledTriangle(2*LEFT, RIGHT, RIGHT+4*UP).move_to(0.5*UP)
        labels = tri_1.get_braces()

        self.play(ShowCreation(tri_1))
        self.play(FadeIn(labels))

        goal = TextMobject("That $a^2 + b^2 = c^2$ for ", "any", " right triangle").shift(3*DOWN)
        goal[1].set_color(YELLOW)
        self.play(Write(goal))

        tri_copy = tri_1.copy()
        tri_copy.stretch(2, 0)
        copy_labels = tri_copy.get_braces()

        self.play(Transform(tri_1, tri_copy),
                  Transform(labels, copy_labels))

        tri_copy = tri_1.copy()
        tri_copy.stretch(0.5, 1)
        copy_labels = tri_copy.get_braces()

        self.play(Transform(tri_1, tri_copy),
                  Transform(labels, copy_labels))

        tri_copy = tri_1.copy()
        tri_copy.stretch(0.5, 0)
        copy_labels = tri_copy.get_braces()

        self.play(Transform(tri_1, tri_copy),
                  Transform(labels, copy_labels))

        tri_copy = tri_1.copy()
        tri_copy.stretch(1.5, 0)
        tri_copy.stretch(0.75, 1)
        copy_labels = tri_copy.get_braces()

        self.play(Transform(tri_1, tri_copy),
                  Transform(labels, copy_labels))

        self.play(Uncreate(intro), Uncreate(goal), FadeOut(labels))

        #self.clear()

        square = Square(side_length= tri_1.get_width() + tri_1.get_height())
        self.play(FadeIn(square))
        self.play(ApplyMethod(tri_1.shift, square.get_corner(DOWN+RIGHT)-tri_1.get_corner(DOWN+RIGHT)))

        labels1 = tri_1.get_labels()
        tri_2 = tri_1.copy().rotate(-PI/2)
        self.bring_to_back(tri_2)
        tri_2.shift(square.get_corner(DOWN+LEFT)-tri_2.get_corner(DOWN+LEFT))
        labels2 = tri_2.get_labels()
        self.play(TransformFromCopy(tri_1, tri_2))
        tri_3 = tri_2.copy().rotate(-PI / 2)
        self.bring_to_back(tri_3)
        tri_3.shift(square.get_corner(UP + LEFT) - tri_3.get_corner(UP + LEFT))
        labels3 = tri_3.get_labels()
        self.play(TransformFromCopy(tri_2, tri_3))
        tri_4 = tri_3.copy().rotate(-PI / 2)
        self.bring_to_back(tri_4)
        tri_4.shift(square.get_corner(UP + RIGHT) - tri_4.get_corner(UP + RIGHT))
        labels4 = tri_4.get_labels()
        self.play(TransformFromCopy(tri_3, tri_4))
        tris = VGroup(tri_1, tri_2, tri_3, tri_4)
        labs = VGroup(labels1, labels2, labels3, labels4)
        im = VGroup(square, tris, labs)

        self.wait(0.5)
        self.play(FadeIn(labs), FadeOut(square))
        self.wait(0.5)

        im2 = im.copy()
        im2.shift(3*LEFT).scale(0.75)
        self.play(Transform(im, im2))

        text1 = TextMobject("This is a ", "square", " of side length $a + b$")
        text1[1].set_color(BLUE)
        text1.shift(4*RIGHT)
        text2 = TextMobject("We will investigate its ", "Area", " in two ways")
        text2[1].set_color(YELLOW)
        textA = VGroup(text1, text2).arrange(DOWN).shift(3.5*RIGHT).scale(0.75)

        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))

        self.play(FadeOut(textA))

        text3 = TextMobject("Viewing it as a square...")
        formula1a = TexMobject("A", "=", "(a + b)^2").scale(4/3)
        formula1a[0].set_color(YELLOW)
        textB = VGroup(text3, formula1a).arrange(DOWN).shift(3.5*RIGHT).scale(0.75)
        self.play(Write(text3))
        self.play(Indicate(im.submobjects[0]))
        self.play(Write(formula1a))

        formula1b = TexMobject("A", "=", "a^2 + 2ab + b^2").move_to(formula1a)
        formula1b[0].set_color(YELLOW)
        self.wait(1)
        self.play(Transform(formula1a, formula1b))
        self.wait(1)
        self.play(FadeOut(text3), formula1a.shift, 2*UP)
        self.wait(1)

        text4 = TextMobject("Viewing it as the sum of the $4$ triangles")
        text5 = TextMobject("and the smaller square...")

        formula2a = TexMobject("A", "=", "4 \\cdot \\frac{1}{2}", " ab + ", "c^2").scale(4/3)
        formula2a[0].set_color(YELLOW)
        textC = VGroup(text4, text5, formula2a).arrange(DOWN).shift(3.5*RIGHT + DOWN).scale(0.75)
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Indicate(im.submobjects[1]))
        self.play(Write(formula2a))
        self.wait(1)

        formula2b = TexMobject("A", "=", "2", " ab + ", "c^2").move_to(formula2a)
        formula2b[0].set_color(YELLOW)
        self.play(Transform(formula2a, formula2b))
        self.wait(1)
        self.play(FadeOut(text4), FadeOut(text5), formula2a.shift, 2*UP)

        text6 = TextMobject("So...")
        formula3a = TexMobject("a^2 + ", "2ab", "+ b^2", "=", "2ab", "+ c^2").scale(4/3)
        textD = VGroup(text6, formula3a).arrange(DOWN).scale(0.75).shift(3.5*RIGHT + 1*DOWN)

        formula3b = TexMobject("a^2 + ", "\\cancel{2ab}", "+ b^2", "=", "\\cancel{2ab}", "+ c^2").move_to(formula3a)
        formula3c = TexMobject("a^2 + ", "b^2", "=", "c^2").move_to(formula3b)

        self.play(Write(text6))
        self.play(Write(formula3a))
        self.wait(1)
        self.play(Transform(formula3a, formula3b))
        self.wait(1)
        self.play(Transform(formula3a, formula3c))


        self.wait(5)

