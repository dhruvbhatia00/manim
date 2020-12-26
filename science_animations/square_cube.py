from manimlib.imports import *

class SquareScale(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "text_config": {"stroke_color": WHITE, "fill_color": BLACK},
    }

    def construct(self):
        s1 = VGroup()

        for i in range(2):
            line = VGroup()
            for j in range(2):
                s = Square(side_length=0.5, color=BLUE, stroke_width=1, fill_opacity=1)
                line.add(s)
            line.arrange(RIGHT, buff=-0)
            s1.add(line)
        s1.arrange(DOWN, buff=0)
        b1 = BraceLabel(s1, "x", DOWN, **self.text_config)

        s2 = VGroup()

        for i in range(2):
            line = VGroup()
            for j in range(2):
                s = Square(side_length=0.5, color=BLUE, stroke_width=1, fill_opacity=1)
                line.add(s)
            line.arrange(RIGHT, buff=-0)
            s2.add(line)
        s2.arrange(DOWN, buff=0).move_to(2*RIGHT)
        b2 = BraceLabel(s2, "x", DOWN, **self.text_config)

        self.play(GrowFromCenter(s1))
        self.play(GrowFromCenter(b1))
        self.wait()
        self.play(s1.shift, 2*LEFT,
                  b1.shift, 2*LEFT)
        self.play(TransformFromCopy(s1, s2),
                  TransformFromCopy(b1, b2))
        self.wait()

        s3 = s2.copy().scale(2)
        self.play(Transform(s2, s3),
                  Transform(b2, BraceLabel(s3, "2 \cdot x", DOWN, **self.text_config)))
        self.wait(2)


        move_out = []
        for line in s2:
            for s in line:
                dir = s.get_center() - s2.get_center()
                move_out.append(ApplyMethod(s.shift, dir*0.3))

        self.play(*move_out)

        self.wait(3)

class CubeScale(ThreeDScene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "text_config": {"stroke_color": WHITE, "fill_color": BLACK},
    }

    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.04)

        s1 = VGroup()

        for i in range(2):
            plane = VGroup()
            for j in range(2):
                line = VGroup()
                for k in range(2):
                    s = Cube(side_length=0.5, color=BLUE, stroke_width=1, fill_opacity=1)
                    line.add(s)
                line.arrange(RIGHT, buff=-0)
                plane.add(line)
            plane.arrange(DOWN, buff=0)
            s1.add(plane)
        s1.arrange(OUT, buff=0)

        b1 = BraceLabel(s1, "x", DOWN, **self.text_config)

        s2 = VGroup()

        for i in range(2):
            plane = VGroup()
            for j in range(2):
                line = VGroup()
                for k in range(2):
                    s = Cube(side_length=0.5, color=BLUE, stroke_width=1, fill_opacity=1)
                    line.add(s)
                line.arrange(RIGHT, buff=-0)
                plane.add(line)
            plane.arrange(DOWN, buff=0)
            s2.add(plane)
        s2.arrange(OUT, buff=0).move_to(2*RIGHT)
        b2 = BraceLabel(s2, "x", DOWN, **self.text_config)

        self.play(GrowFromCenter(s1))
        self.play(GrowFromCenter(b1))
        self.wait()
        self.play(s1.shift, 2 * LEFT,
                  b1.shift, 2 * LEFT)
        self.play(TransformFromCopy(s1, s2),
                  TransformFromCopy(b1, b2))
        self.wait()

        s3 = s2.copy().scale(2)
        self.play(Transform(s2, s3),
                  Transform(b2, BraceLabel(s3, "2 \cdot x", DOWN, **self.text_config)))
        self.wait(2)


        move_out = []
        move_in = []
        for plane in s2:
            for line in plane:
                for s in line:
                    dir = s.get_center() - s2.get_center()
                    move_out.append(ApplyMethod(s.shift, dir * 0.3))
                    move_in.append(ApplyMethod(s.shift, dir * -0.3))

        self.stop_ambient_camera_rotation()
        #self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        # self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)

        self.play(*move_out)
        self.play(*move_in)

        self.wait(3)


class Both(ThreeDScene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "text_config": {"stroke_color": WHITE, "fill_color": BLACK},
    }

    def construct(self):
        s1 = VGroup()

        for i in range(2):
            line = VGroup()
            for j in range(2):
                s = Square(side_length=0.5, color=BLUE, stroke_width=1, fill_opacity=1)
                line.add(s)
            line.arrange(RIGHT, buff=-0)
            s1.add(line)
        s1.arrange(DOWN, buff=0)
        b1 = BraceLabel(s1, "x", DOWN, **self.text_config)

        s2 = VGroup()

        for i in range(2):
            line = VGroup()
            for j in range(2):
                s = Square(side_length=0.5, color=BLUE, stroke_width=1, fill_opacity=1)
                line.add(s)
            line.arrange(RIGHT, buff=-0)
            s2.add(line)
        s2.arrange(DOWN, buff=0).move_to(2 * RIGHT)
        b2 = BraceLabel(s2, "x", DOWN, **self.text_config)

        self.play(GrowFromCenter(s1))
        self.play(GrowFromCenter(b1))
        self.wait()
        self.play(s1.shift, 2 * LEFT,
                  b1.shift, 2 * LEFT)
        self.play(TransformFromCopy(s1, s2),
                  TransformFromCopy(b1, b2))
        self.wait()

        s3 = s2.copy().scale(2)
        self.play(Transform(s2, s3),
                  Transform(b2, BraceLabel(s3, "2 \cdot x", DOWN, **self.text_config)))
        self.wait()

        move_out = []
        move_in = []
        for line in s2:
            for s in line:
                dir = s.get_center() - s2.get_center()
                move_out.append(ApplyMethod(s.shift, dir * 0.3))
                move_in.append(ApplyMethod(s.shift, dir * -0.3))

        self.play(*move_out)
        self.play(*move_in)

        self.wait(1)

        self.play(*[FadeOut(sub) for sub in self.mobjects])

        self.move_camera(phi=60 * DEGREES, theta=-90 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.08)

        s1 = VGroup()

        for i in range(2):
            plane = VGroup()
            for j in range(2):
                line = VGroup()
                for k in range(2):
                    s = Cube(side_length=0.5, color=BLUE, stroke_width=1, fill_opacity=1)
                    line.add(s)
                line.arrange(RIGHT, buff=-0)
                plane.add(line)
            plane.arrange(DOWN, buff=0)
            s1.add(plane)
        s1.arrange(OUT, buff=0).shift(2*LEFT)

        B1 = BraceLabel(s1, "x", DOWN, **self.text_config)

        s2 = VGroup()

        for i in range(2):
            plane = VGroup()
            for j in range(2):
                line = VGroup()
                for k in range(2):
                    s = Cube(side_length=0.5, color=BLUE, stroke_width=1, fill_opacity=1)
                    line.add(s)
                line.arrange(RIGHT, buff=-0)
                plane.add(line)
            plane.arrange(DOWN, buff=0)
            s2.add(plane)
        s2.arrange(OUT, buff=0).move_to(2 * RIGHT).scale(2)
        b2 = BraceLabel(s2, "2 \cdot x", DOWN, **self.text_config)

        self.play(GrowFromCenter(s1), GrowFromCenter(b1), GrowFromCenter(s2), GrowFromCenter(b2))
        self.wait()

        move_out = []
        for plane in s2:
            for line in plane:
                for s in line:
                    dir = s.get_center() - s2.get_center()
                    move_out.append(ApplyMethod(s.shift, dir * 0.3))

        self.play(*move_out)

        self.wait(3)