from manimlib.imports import *

class FractionSymbol(Scene):
    def construct(self):
        A = TexMobject(r"A", " \\over ", "B").scale(3)
        #B = TexMobject(r"\divisionsymbol").scale(3)
        self.play(Write(A))

        self.play(Transform(A[0], TexMobject(r"\cdot").scale(3).shift(0.2*UP)),
                  Transform(A[2], TexMobject(r"\cdot").scale(3).shift(0.5*DOWN)))

        self.wait(5)

class PiePieces(Scene):
    CONFIG = {
        "circ_rad": 3,
        "numerator":4,
        "denominator": 7,
        "indicate": True,
    }

    def construct(self):
        im = VGroup()

        C = Circle(radius=self.circ_rad, fill_opacity=0.25)
        im.add(C)
        self.play(ShowCreation(C))
        sec = Sector(outer_radius = self.circ_rad, angle = TAU* self.numerator/ self.denominator, color=YELLOW, fill_opacity=0.5)
        im.add(sec)

        lines = VGroup()
        for i in range(self.denominator):
            angle = TAU / self.denominator
            l = Line(ORIGIN, self.circ_rad*RIGHT).rotate_about_origin(i*angle)
            lines.add(l)

        im.add(lines)
        self.play(ShowCreation(lines))
        #self.wait(2)

        if self.indicate:
            self.play(FadeIn(sec))
            self.play(im.shift, 2*LEFT)
            #self.play(Indicate(sec))
            frac = TexMobject(str(self.numerator), "\\over ", str(self.denominator)).scale(3).shift(3*RIGHT)
            frac[0].set_color(YELLOW)
            frac[2].set_color(RED)
            self.play(Indicate(sec), Write(frac[0]))
            self.wait(1)
            pie = VGroup(C, lines)
            self.play(Indicate(pie, color=RED), Write(frac[1:3]))


        self.wait(3)


class PizzaCompare(Scene):
    CONFIG = {
        "num_sectors": 3,
        "radius": 2.5,
    }

    def construct(self):
        circ = Circle(radius=self.radius, color=RED, fill_opacity=0.5, stroke_width=0)
        angle = TAU/self.num_sectors

        lines = VGroup()
        for i in range(self.num_sectors):
            l = Line(ORIGIN, self.radius * RIGHT).rotate_about_origin(i * angle)
            lines.add(l)

        sectors = VGroup()
        for i in range(self.num_sectors):
            sect = Sector(outer_radius = self.radius, color=RED, start_angle=angle*i, angle=angle, fill_opacity=0.5)
            sectors.add(sect)

        #text1 = TextMobject("We cut the pizza into ", "$" + str(self.num_sectors) + "$", " equal slices").move_to(3.5*DOWN)

        self.play(ShowCreation(circ))
        #self.play(Write(text1))
        self.play(ShowCreation(lines))
        self.remove(circ)
        self.add(sectors)

        sectors.save_state()
        sectors_move_out = []
        for sect in sectors:
            dir = sect.get_center() - ORIGIN
            dir = dir/np.linalg.norm(dir)
            sectors_move_out.append(ApplyMethod(sect.shift, 0.3*dir))

        self.play(*sectors_move_out, FadeOut(lines))
        self.wait()

        labels = VGroup()
        for sect in sectors:
            lab = TexMobject("\\frac{1}{3}").move_to(sect.get_center())
            labels.add(lab)

        #text2 = TextMobject("Each slice is $1$ out of $3$ parts of the whole").move_to(text1)
        #self.play(ReplacementTransform(text1, text2))
        self.play(Write(labels))
        self.wait(2)

        self.play(FadeOut(labels), sectors.restore, FadeIn(lines)) #Uncreate(text2)

        #text3 = TextMobject("You get $2$ slices, while your friend gets $1$ slice").shift(3.5*DOWN)

        left = VGroup(sectors.submobjects[1], sectors.submobjects[2], lines[2])
        right = sectors.submobjects[0]

        #self.play(Write(text3))
        self.play(ShrinkToCenter(lines[0]), ShrinkToCenter(lines[1]),
                  left.shift, 3.5*LEFT,
                  right.shift, 3.5*RIGHT)

        labels = VGroup()
        for sect in sectors:
            lab = TexMobject("\\frac{1}{3}").move_to(sect.get_center())
            labels.add(lab)

        self.play(Write(labels))
        self.wait()

        two_thirds = TexMobject("\\frac{2}{3}").scale(1.25).move_to(lines[2].get_center())
        left_lab = VGroup(labels[1], labels[2])
        self.play(FadeOut(lines[2]), ReplacementTransform(left_lab, two_thirds))

        gt = TexMobject(">").scale(2).shift(0.5*RIGHT)
        self.play(Write(gt)) #Uncreate(text3)
        self.wait()

        two_thirds_copy = two_thirds.copy().scale(2/1.25).move_to(LEFT)
        right_lab = labels[0]
        right_copy = right_lab.copy().scale(2).move_to(RIGHT)

        self.play(FadeOut(sectors),
                  Transform(two_thirds, two_thirds_copy),
                  Transform(right_lab, right_copy),
                  gt.move_to, ORIGIN)

        self.wait(2)



class Trial(Scene):
    def construct(self):
        mango = ImageMobject(r"C:\Manim\manim-26_05_2020\ecce\mango.png")

        self.play(FadeIn(mango))
        d = Dot(mango.get_center())
        self.play(Write(d))

        self.wait(5)


class Mango1(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE,},
        "file_name": r"C:\Manim\manim-26_05_2020\ecce\mango.png",
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK},
    }

    def construct(self):
        lines = VGroup()
        mangoes = VGroup()
        boxes = VGroup()
        for j in range(3):
            line = VGroup()
            for i in range(4):
                pic = ImageMobject(self.file_name).scale(0.75)
                pic.move_to(7/3 * i * RIGHT + 3.5*LEFT +  2*j * DOWN + 2 * UP)
                line.add(pic)
                mangoes.add(pic)
            box = Square(color=BLACK).move_to( 2*j * DOWN + 2 * UP)
            box.stretch(4.5, 0)
            boxes.add(box)
            line.add(box)
            lines.add(line)

        outer_box_coords = [boxes[0].get_corner(UP+LEFT), boxes[0].get_corner(UP+RIGHT),
                            boxes[-1].get_corner(DOWN+RIGHT), boxes[-1].get_corner(DOWN+LEFT)]

        outer_box = Polygon(*outer_box_coords, color=BLACK)
        self.add(mangoes)
        self.play(ShowCreation(outer_box))
        self.wait()
        self.play(FadeIn(boxes))
        self.remove(outer_box)

        self.play(lines[0].shift, 0.75*UP,
                  lines[-1].shift, 0.75*DOWN)


        self.wait(2)


class Mango2(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE,},
        "file_name": r"C:\Manim\manim-26_05_2020\ecce\mango.png",
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK},
    }

    def construct(self):
        mangoes = VGroup()
        boxes = VGroup()
        parts = VGroup()
        for i in range(4):
            pic = ImageMobject(self.file_name).scale(0.75)
            pic.move_to(7/3 * i * RIGHT + 3.5*LEFT)
            mangoes.add(pic)
            box = Square(color=BLACK).stretch(7/6, 0).move_to(7/3 * i * RIGHT + 3.5*LEFT)
            part = VGroup().add(pic).add(box)
            boxes.add(box)
            parts.add(part)
            # if i != 3:
            #     lin = DashedLine(ORIGIN, 2*UP, color=BLACK).move_to(7/3 * i * RIGHT + 3.5*LEFT + 7/6*RIGHT)
            #     line.add(lin)
        outer_box = Square(color=BLACK)
        outer_box.stretch(7/1.5, 0)

        self.add(mangoes)
        self.play(ShowCreation(outer_box))
        self.wait()
        self.play(FadeIn(boxes))
        self.remove(outer_box)
        self.play(parts[0].shift, 0.75*LEFT,
                  parts[1].shift, 0.25*LEFT,
                  parts[2].shift, 0.25*RIGHT,
                  parts[3].shift, 0.75*RIGHT)


        self.wait(2)


class Mango3(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE,},
        "file_name": r"C:\Manim\manim-26_05_2020\ecce\mango.png",
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK},
    }

    def construct(self):
        im = VGroup()
        for i in range(3):
            for j in range(2):
                path = "C:\Manim\manim-26_05_2020\ecce\\"
                pic = ImageMobject(path + r"mango2_0" + str(j+1) + "_0" + str(i+1) + ".png").scale(0.75)
                pic.move_to(2*(1.5 * i * RIGHT + 1.5*LEFT + 2*j *DOWN + UP))
                im.add(pic)

        self.add(im)


class Paratha(Scene):
    CONFIG = {
        "radius": 2,
        "num_pieces": 2,
        "num_to_right": 1,
    }

    def construct(self):
        circ = Circle(radius=self.radius, color=GREY_BROWN, fill_opacity=1, stroke_width=0)
        angle = TAU / self.num_pieces

        sectors = VGroup()
        for i in range(self.num_pieces):
            sect = Sector(outer_radius=self.radius, color=GREY_BROWN, start_angle=angle * i, angle=angle, fill_opacity=1)
            sectors.add(sect)

        lines = VGroup()
        for i in range(self.num_pieces):
            l = Line(ORIGIN, self.radius * RIGHT).rotate_about_origin(i * angle)
            lines.add(l)

        self.play(ShowCreation(circ))
        self.add(sectors)
        self.play(ShowCreation(lines))
        self.remove(circ)

        self.wait()

        labels = VGroup()
        for sect in sectors:
            lab = TexMobject("\\frac{1}{" + str(self.num_pieces) + "}").move_to(sect.get_center())
            labels.add(lab)

        right = VGroup(*sectors[:self.num_to_right], *labels[:self.num_to_right], lines[1:self.num_to_right])
        left = VGroup(*sectors[self.num_to_right:], *labels[self.num_to_right:], lines[self.num_to_right+1:])

        self.play(Write(labels))

        if self.num_to_right <= (self.num_pieces / 2.0):
            self.play(ApplyMethod(right.shift, 3.5*RIGHT),
                      ApplyMethod(left.shift, 3.5*LEFT),
                      FadeOut(lines[0]), FadeOut(lines[self.num_to_right]))
        else:
            self.play(ApplyMethod(right.shift, -3.5 * RIGHT),
                      ApplyMethod(left.shift, -3.5 * LEFT),
                      FadeOut(lines[0]), FadeOut(lines[self.num_to_right]))

        self.wait(5)