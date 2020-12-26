from manimlib.mobject.svg.tex_mobject import *
from manimlib.mobject.matrix import *
import math
import sys
import os

# class TexArrow(VGroup):
#     CONFIG = {
#         "stroke_width":DEFAULT_STROKE_WIDTH,
#         "fill_opacity":0,
#         "arrow_style": "->",
#         "line_decoration":"",
#     }
#
#     def __init__(self, *args, **kwargs):
#         VGroup.__init__(self, **kwargs)
#
#         digest_config(self, kwargs)
#         if len(args) == 0:
#             self.end = RIGHT
#             self.start = ORIGIN
#         elif len(args) == 1:
#             self.start = ORIGIN
#             self.end = args[0]
#         elif len(args) == 2:
#             self.start = args[0]
#             self.end = args[1]
#         else:
#             raise Exception("too many arguments")
#
#         if np.all(self.start == self.end):
#             raise Exception("TexArrow cannot have 0 length")
#
#
#         std_ref = sys.stdout
#         # open up the special null device & it discards everything written to it.
#         sys.stdout = open(os.devnull, 'w')
#
#         #sizing
#         ref_tex = "\\begin{tikzpicture} \\draw[-] (0,0) -- (1,0); \\end{tikzpicture}"
#         ref_line = TexMobject(ref_tex, stroke_width=4, fill_opacity=0)
#         ref_len = ref_line.get_width()
#
#         vector = self.end - self.start
#         self.magnitude = np.linalg.norm(vector)
#         self.tex_len = self.magnitude/ref_len
#
#         #create arrow of appropriate size: not using scaling so that arrow heads/line decorations don't become too big
#         arrow_tex = "\\begin{tikzpicture} \\draw[" + self.arrow_style + ", decorate, decoration={" +\
#                     self.line_decoration + "}] (0,0) -- (" + str(self.tex_len) + ",0); \\end{tikzpicture}"
#
#         self.angle = math.atan2(vector[1], vector[0])
#
#         arrow = TexMobject(arrow_tex, stroke_width=self.stroke_width, fill_opacity=self.fill_opacity)
#         arrow.move_to(self.start + 0.5 * self.magnitude * RIGHT).rotate(self.angle, about_point=self.start)
#
#         self.add(arrow)
#         sys.stdout = std_ref  # resume original stdout stream.
#
#     def set_arrow_style(self, new_style):
#         self.arrow_style = new_style
#         conf = {
#             "stroke_width": self.stroke_width,
#             "fill_opacity": self.fill_opacity,
#             "arrow_style": self.arrow_style,
#             "line_decoration": self.line_decoration,
#         }
#
#         new_arrow = TexArrow(self.start, self.end, **conf)
#         self.become(new_arrow)
#
#     def set_line_decoration(self, new_decoration):
#         self.line_decoration = new_decoration
#         conf = {
#             "stroke_width": self.stroke_width,
#             "fill_opacity": self.fill_opacity,
#             "arrow_style": self.arrow_style,
#             "line_decoration": self.line_decoration,
#         }
#
#         new_arrow = TexArrow(self.start, self.end, **conf)
#         self.become(new_arrow)
#
#     def set_start(self, new_start):
#         self.start = new_start
#         conf = {
#             "stroke_width": self.stroke_width,
#             "fill_opacity": self.fill_opacity,
#             "arrow_style": self.arrow_style,
#             "line_decoration": self.line_decoration,
#         }
#
#         new_arrow = TexArrow(self.start, self.end, **conf)
#         self.become(new_arrow)
#
#     def set_end(self, new_end):
#         self.end = new_end
#         conf = {
#             "stroke_width": self.stroke_width,
#             "fill_opacity": self.fill_opacity,
#             "arrow_style": self.arrow_style,
#             "line_decoration": self.line_decoration,
#         }
#
#         new_arrow = TexArrow(self.start, self.end, **conf)
#         self.become(new_arrow)
#
#     def scale_length(self, scale_factor, keep_tip_fixed=True):
#         if keep_tip_fixed:
#             self.set_end(self.start + scale_factor * self.magnitude * self.get_direction())
#         else:
#             super.scale(self, scale_factor)
#
#     def get_direction(self):
#         ratio = math.tan(self.angle)
#         vector = np.array([1, ratio, 0])
#         return vector/np.linalg.norm(vector)
#
#
#
# class ConnectingArrow(TexArrow):
#     CONFIG = {
#         "node_arrow_buff":MED_SMALL_BUFF
#     }
#
#
#     def __init__(self, mob1, mob2, **kwargs):
#         digest_config(self, kwargs)
#         line = mob2.get_center() - mob1.get_center()
#         direction = line / np.linalg.norm(line)
#
#         h1 = mob1.get_height()
#         w1 = mob1.get_width()
#         h2 = mob2.get_height()
#         w2 = mob2.get_width()
#
#         A = segment_int_rectangle_from_center(mob1.get_center(), mob2.get_center(), w1, h1)
#         B = segment_int_rectangle_from_center(mob2.get_center(), mob1.get_center(), w2, h2)
#         A += self.node_arrow_buff * direction
#         B -= self.node_arrow_buff * direction
#
#         TexArrow.__init__(self, A, B, **kwargs)
#
# def segment_int_rectangle_from_center(start, end, width, height):
#     del_x = end[0] - start[0]
#     del_y = end[1] - start[1]
#     x_min = start[0] - width/2
#     x_max = start[0] + width/2
#     y_min = start[1] - height/2
#     y_max = start[1] + height/2
#
#     p = [-del_x, del_x, -del_y, del_y]
#     q = [start[0] - x_min, x_max - start[0], start[1] - y_min, y_max - start[1]]
#     u = math.inf
#
#     for i in [0, 1, 2, 3]:
#         if p[i] == 0:
#             assert(q[i] >= 0)
#         else:
#             t = q[i]/p[i]
#             if p[i] > 0 and u > t:
#                 u = t
#
#     return start + (end - start)*u

class TexArrow(VGroup):
    CONFIG = {
        "stroke_width":DEFAULT_STROKE_WIDTH,
        "fill_opacity":0,
        "arrow_style": "->",
        "line_decoration":"",
    }

    def __init__(self, *args, **kwargs):
        VGroup.__init__(self, **kwargs)

        digest_config(self, kwargs)
        if len(args) == 0:
            end = RIGHT
            start = ORIGIN
        elif len(args) == 1:
            start = ORIGIN
            end = args[0]
        elif len(args) == 2:
            start = args[0]
            end = args[1]
        else:
            raise Exception("too many arguments")

        if np.all(start == end):
            raise Exception("TexArrow cannot have 0 length")


        std_ref = sys.stdout
        # open up the special null device & it discards everything written to it.
        sys.stdout = open(os.devnull, 'w')

        #sizing TODO - change this to a method
        ref_tex = "\\begin{tikzpicture} \\draw[-] (0,0) -- (1,0); \\end{tikzpicture}"
        ref_line = TexMobject(ref_tex, stroke_width=4, fill_opacity=0)
        ref_len = ref_line.get_width()

        #TODO: change this part to a method
        vector = end - start
        magnitude = np.linalg.norm(vector)
        tex_len = magnitude/ref_len

        #TODO: change this to a method
        #create arrow of appropriate size: not using scaling so that arrow heads/line decorations don't become too big
        arrow_tex = "\\begin{tikzpicture} \\draw[" + self.arrow_style + ", decorate, decoration={" +\
                    self.line_decoration + "}] (0,0) -- (" + str(tex_len) + ",0); \\end{tikzpicture}"
        angle = math.atan2(vector[1], vector[0])
        arrow = TexMobject(arrow_tex, stroke_width=self.stroke_width, fill_opacity=self.fill_opacity)
        arrow.move_to(start + 0.5 * magnitude * RIGHT).rotate(angle, about_point=start)

        self.add(arrow)
        sys.stdout = std_ref  # resume original stdout stream.


    # def get_start(self):
    #     fam = self.get_family()
    #
    #     if self.arrow_style[-1] == "-":
    #         return fam[-1].get_start()
    #     else:
    #         return fam[-2].get_start()
    #
    # def get_end(self):
    #     fam = self.get_family()
    #     if self.arrow_style[-1] == "-":
    #         return fam[-1].get_last_point()
    #     else:
    #         return fam[-2].get_last_point()




class ConnectingArrow(TexArrow):
    CONFIG = {
        "node_arrow_buff":MED_SMALL_BUFF
    }


    def __init__(self, mob1, mob2, **kwargs):
        digest_config(self, kwargs)
        line = mob2.get_center() - mob1.get_center()
        direction = line / np.linalg.norm(line)

        h1 = mob1.get_height()
        w1 = mob1.get_width()
        h2 = mob2.get_height()
        w2 = mob2.get_width()

        A = segment_int_rectangle_from_center(mob1.get_center(), mob2.get_center(), w1, h1)
        B = segment_int_rectangle_from_center(mob2.get_center(), mob1.get_center(), w2, h2)
        A += self.node_arrow_buff * direction
        B -= self.node_arrow_buff * direction

        TexArrow.__init__(self, A, B, **kwargs)

def segment_int_rectangle_from_center(start, end, width, height):
    del_x = end[0] - start[0]
    del_y = end[1] - start[1]
    x_min = start[0] - width/2
    x_max = start[0] + width/2
    y_min = start[1] - height/2
    y_max = start[1] + height/2

    p = [-del_x, del_x, -del_y, del_y]
    q = [start[0] - x_min, x_max - start[0], start[1] - y_min, y_max - start[1]]
    u = math.inf

    for i in [0, 1, 2, 3]:
        if p[i] == 0:
            assert(q[i] >= 0)
        else:
            t = q[i]/p[i]
            if p[i] > 0 and u > t:
                u = t

    return start + (end - start)*u


# class CommutativeDiagram(MobjectMatrix
# ):
#     CONFIG = {
#         "v_buff": 1.3,
#         "h_buff": 1.3,
#         "bracket_h_buff": MED_SMALL_BUFF,
#         "bracket_v_buff": MED_SMALL_BUFF,
#         "add_background_rectangles_to_entries": False,
#         "include_background_rectangle": False,
#         #"element_to_mobject": TexMobject, # already in mobjectmatrix config
#         "element_to_mobject_config": {},
#         "element_alignment_corner": DR,
#         "brackets": False
#     }
#
#     def __init__(self, nodes, edges, **kwargs):
#         MobjectMatrix.__init__(self, edges, **kwargs)
#


