
from manimlib.imports import *

import mpmath
mpmath.mp.dps = 7


def zeta(z):
    max_norm = FRAME_X_RADIUS
    try:
        return np.complex(mpmath.zeta(z))
    except:
        return np.complex(max_norm, 0)

def d_zeta(z):
    epsilon = 0.01
    return (zeta(z + epsilon) - zeta(z))/epsilon



class ZetaTransformationScene(ComplexTransformationScene):
    CONFIG = {
        "anchor_density" : 35,
        "min_added_anchors" : 10,
        "max_added_anchors" : 300,
        "num_anchors_to_add_per_line" : 75,
        "post_transformation_stroke_width" : 2,
        "default_apply_complex_function_kwargs" : {
            "run_time" : 5,
        },
        "x_min" : 1,
        "x_max" : int(FRAME_X_RADIUS+2),
        "y_min": 1,
        "y_max": int(FRAME_Y_RADIUS + 2),
        "extra_lines_x_min" : -2,
        "extra_lines_x_max" : 4,
        "extra_lines_y_min" : -2,
        "extra_lines_y_max" : 2,
    }
    def prepare_for_transformation(self, mob):
        for line in mob.family_members_with_points():
            #Find point of line cloest to 1 on C
            if not isinstance(line, Line):
                line.insert_n_curves(self.min_added_anchors)
                continue
            p1 = line.get_start()+LEFT
            p2 = line.get_end()+LEFT
            t = (-np.dot(p1, p2-p1))/(get_norm(p2-p1)**2)
            closest_to_one = interpolate(
                line.get_start(), line.get_end(), t
            )
            #See how big this line will become
            diameter = abs(zeta(complex(*closest_to_one[:2])))
            target_num_curves = np.clip(
                int(self.anchor_density*np.pi*diameter),
                self.min_added_anchors,
                self.max_added_anchors,
            )
            num_curves = line.get_num_curves()
            if num_curves < target_num_curves:
                line.insert_n_curves(target_num_curves-num_curves)
            line.make_smooth()

    def add_extra_plane_lines_for_zeta(self, animate = False, **kwargs):
        dense_grid = self.get_dense_grid(**kwargs)
        if animate:
            self.play(ShowCreation(dense_grid))
        self.plane.add(dense_grid)
        self.add(self.plane)

    def get_dense_grid(self, step_size = 1./16):
        epsilon = 0.1
        x_range = np.arange(
            max(self.x_min, self.extra_lines_x_min),
            min(self.x_max, self.extra_lines_x_max),
            step_size
        )
        y_range = np.arange(
            max(self.y_min, self.extra_lines_y_min),
            min(self.y_max, self.extra_lines_y_max),
            step_size
        )
        vert_lines = VGroup(*[
            Line(
                self.y_min*UP,
                self.y_max*UP,
            ).shift(x*RIGHT)
            for x in x_range
            if abs(x-1) > epsilon
        ])
        vert_lines.set_color_by_gradient(
            self.vert_start_color, self.vert_end_color
        )
        horiz_lines = VGroup(*[
            Line(
                self.x_min*RIGHT,
                self.x_max*RIGHT,
            ).shift(y*UP)
            for y in y_range
            if abs(y) > epsilon
        ])
        horiz_lines.set_color_by_gradient(
            self.horiz_start_color, self.horiz_end_color
        )
        dense_grid = VGroup(horiz_lines, vert_lines)
        dense_grid.set_stroke(width = 1)
        return dense_grid

    def add_reflected_plane(self, animate = False):
        reflected_plane = self.get_reflected_plane()
        if animate:
            self.play(ShowCreation(reflected_plane, run_time = 5))
        self.plane.add(reflected_plane)
        self.add(self.plane)

    def get_reflected_plane(self):
        reflected_plane = self.plane.copy()
        reflected_plane.rotate(np.pi, UP, about_point = RIGHT)
        for mob in reflected_plane.family_members_with_points():
            mob.set_color(
                Color(rgb = 1-0.5*color_to_rgb(mob.get_color()))
            )
        self.prepare_for_transformation(reflected_plane)
        reflected_plane.submobjects = list(reversed(
            reflected_plane.family_members_with_points()
        ))
        return reflected_plane

    def apply_zeta_function(self, **kwargs):
        transform_kwargs = dict(self.default_apply_complex_function_kwargs)
        transform_kwargs.update(kwargs)
        self.apply_complex_function(zeta, **kwargs)

class TestZetaOnHalfPlane(ZetaTransformationScene):
    CONFIG = {
        "anchor_density" : 15,
    }
    def construct(self):
        self.add_transformable_plane()
        self.add_extra_plane_lines_for_zeta()
        self.prepare_for_transformation(self.plane)
        print(sum([
            mob.get_num_points()
            for mob in self.plane.family_members_with_points()
        ]))
        print(len(self.plane.family_members_with_points()))
        self.apply_zeta_function()
        self.wait()

class TestZetaOnFullPlane(ZetaTransformationScene):
    def construct(self):
        self.add_transformable_plane(animate = True)
        self.add_extra_plane_lines_for_zeta(animate = True)
        self.add_reflected_plane(animate = True)
        self.apply_zeta_function()


class TestZetaOnLine(ZetaTransformationScene):
    def construct(self):
        line = Line(UP+20*LEFT, UP+20*RIGHT)
        self.add_transformable_plane()
        self.plane.submobjects = [line]
        self.apply_zeta_function()
        self.wait(2)
        self.play(ShowCreation(line, run_time = 10))
        self.wait(3)