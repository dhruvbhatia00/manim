from manimlib.imports import *

class Derivation(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "text_config": {"stroke_color": WHITE, "fill_color": BLACK},
    }

    def construct(self):
        assumptions_text = ["Assumptions:", "$M \propto V$", "$BMR \propto A$"]
        assumptions = VGroup(*[TextMobject(text, **self.text_config) for text in assumptions_text]).arrange(DOWN, aligned_edge=LEFT)

        scl_text = ["Square-Cube Law:", "$A \propto x^2$", "$V \propto x^3$"]
        scl = VGroup(*[TextMobject(text, **self.text_config) for text in scl_text]).arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(assumptions))
        assumptions2 = assumptions.copy().scale(0.6).to_edge(UP+LEFT, buff=MED_SMALL_BUFF)
        self.play(Transform(assumptions, assumptions2))
        r1 = SurroundingRectangle(assumptions, color=BLACK)
        self.play(ShowCreation(r1))

        self.play(Write(scl))
        scl2 = scl.copy().scale(0.6).next_to(assumptions2, DOWN, buff=MED_LARGE_BUFF).\
            align_to(assumptions2, LEFT, UP)
        self.play(Transform(scl, scl2))
        r2 = SurroundingRectangle(scl, color=BLACK)
        self.play(ShowCreation(r2))

        text_1 = [["A", "\propto", "x^2"], ["V", "\propto", "x^3"]]
        stext_1 = VGroup(*[TexMobject(*text, **self.text_config) for text in text_1]).arrange(RIGHT, buff=LARGE_BUFF*2).shift(2*UP)
        self.play(TransformFromCopy(scl[1:], stext_1))

        self.wait()
        rtext2 = ["V^\\frac{2}{3}", "\propto", "x^{3 \cdot \\frac{2}{3}}"]
        rstext2 = TexMobject(*rtext2, **self.text_config).move_to(stext_1[1])
        self.play(Transform(stext_1[1], rstext2))

        self.wait()
        rtext2 = ["V^\\frac{2}{3}", "\propto", "x^2"]
        rstext2 = TexMobject(*rtext2, **self.text_config).move_to(stext_1[1])
        self.play(Transform(stext_1[1], rstext2))

        so = TextMobject("So...", **self.text_config).shift(UP*0.5)
        self.play(Write(so))

        final_text = ["BMR", "\propto", "A", "\propto", "V^{\\frac{2}{3}}", "\propto", "M^{\\frac{2}{3}}"]
        sfinal = TexMobject(*final_text, **self.text_config).shift(DOWN)
        self.play(Write(sfinal[2:5]))
        self.wait()
        self.play(Indicate(assumptions[1]))
        self.play(Write(sfinal[5:]))
        self.play(Indicate(assumptions[2]))
        self.play(Write(sfinal[:2]))
        self.wait()
        self.play(FadeOut(sfinal[2:6]))

        final2_text = ["BMR", "\propto", "M^{\\frac{2}{3}}"]
        sfinal2 = TexMobject(*final2_text, **self.text_config).shift(DOWN)
        self.play(Transform(sfinal[:2], sfinal2[:2]),
                  Transform(sfinal[-1], sfinal2[-1]))

        self.wait(2)