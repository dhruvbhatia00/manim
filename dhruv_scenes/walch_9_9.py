from manimlib.imports import *

def plane_func(init_point, a_dir, b_dir):
    if isinstance(init_point, list):
        init_point = np.array(init_point)

    if np.linalg.norm(a_dir) != 1:
        a_dir = a_dir/np.linalg.norm(a_dir)
    if np.linalg.norm(b_dir) != 1:
        b_dir = b_dir/np.linalg.norm(b_dir)

    return lambda u,v: np.array(init_point + interpolate(-3, 3, u)*a_dir + interpolate(-3, 3, v)*b_dir)

def get_intersect(eye_location, init_point, x_dir, y_dir, vertex):
    dir = vertex - eye_location

    A = np.transpose(np.array([x_dir, y_dir, dir]))
    b = eye_location - init_point
    x = np.linalg.solve(A, b)
    t = - x[2]

    return eye_location + t*dir

def to_plane_coords(eye_location, init_point, x_dir, y_dir, vertex):
    dir = vertex - eye_location

    A = np.transpose(np.array([x_dir, y_dir, dir]))
    b = eye_location - init_point
    x = np.linalg.solve(A, b)
    u = -x[1]
    v = x[0]
    return np.array([u, v, 0])

def points_func_plane_coords(points, eye_location, init_point, x_dir, y_dir):
    return np.array(map(lambda p: to_plane_coords(eye_location, init_point, x_dir, y_dir, p), points))

def perp_plane(eye_loc, vertices, prop):
    center = sum(vertices) / len(vertices)
    dir = center - eye_loc
    init_point = eye_loc + prop * dir
    x_dir = np.cross(dir, OUT)
    x_dir = x_dir / np.linalg.norm(x_dir)
    y_dir = np.cross(x_dir, dir)
    y_dir = y_dir / np.linalg.norm(y_dir)

    return [init_point, x_dir, y_dir]

class ProjectShape(ThreeDScene):
    eye_loc = (0 *DOWN + 1*OUT + 4*RIGHT) * 1
    # "polygon_vertices": [RIGHT + 3 * UP, RIGHT + 4 * UP, LEFT + 4 * UP, LEFT + 3 * UP],
    verts = [RIGHT + 3 * UP, RIGHT + 5 * UP, LEFT + 5 * UP, LEFT + 3 * UP,
                             RIGHT + 3 * UP + 2*OUT, RIGHT + 5 * UP + 2*OUT, LEFT + 5 * UP + 2*OUT, LEFT + 3 * UP + 2*OUT]

    direc = eye_loc - sum(verts)/len(verts)
    eye_loc = sum(verts)/len(verts) + 100000*direc
    prop = 2

    CONFIG = {
        "eye_location": eye_loc,
        "polygon_vertices": verts,
        "camera_config": {"background_color": WHITE},
        "plane_init_point": perp_plane(eye_loc, verts, prop)[0],
        "plane_x_dir": perp_plane(eye_loc, verts, prop)[1],
        "plane_y_dir": perp_plane(eye_loc, verts, prop)[2],
        "show_eye_loc": True,
        "show_3D": True,
        "show_drawing": False,
        "show_2D": True,
        "plane_config": {
            "axis_config": {
                "stroke_color": BLACK,
                "stroke_width": 2,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": SMALL_BUFF,
                "label_direction": DR,
                "number_scale_val": 0.5,
            },
            "background_line_style": {
                "stroke_color": LIGHT_GREY,
                "stroke_width": 2,
                "stroke_opacity": 1,
            },
            "x_min": -5,
            "x_max": 5,
            "y_min": -3,
            "y_max": 3,
        },
        "axis_config": {
            "color": BLACK,
            "stroke_color": BLACK,
            "include_tip": True,
            "exclude_zero_from_default_numbers": True,
            "x_axis_label": "x",
        },
        "shape_config": {
            "stroke_color": BLACK,
            "fill_color": GREY,
            "fill_opacity": 0.7,
        },
        "eye_config": {
            "fill_color": BLACK,
            "fill_opacity": 1.0,
            "checkerboard_colors": [BLACK, BLACK],
            "radius": 0.1,
        },
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK}
    }



    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES,theta=-90*DEGREES)
        axes = ThreeDAxes(axis_config = self.axis_config)
        #self.play(ShowCreation(axes))

        if self.show_3D:
            self.add(axes)

        if self.show_3D and self.show_drawing:
            num_plane = self.num_plane(self.plane_init_point, self.plane_x_dir, self.plane_y_dir, **self.plane_config)

        eye = Sphere(**self.eye_config).move_to(self.eye_location)
        if self.show_3D:
            self.add(eye)

        eye_line_x = DashedVMobject(Line(self.eye_location[1] * UP, self.eye_location[1] * UP + self.eye_location[0] * RIGHT, stroke_color=BLACK, stroke_width=1))
        eye_line_y = DashedVMobject(Line(self.eye_location[0] * RIGHT, self.eye_location[1] * UP + self.eye_location[0] * RIGHT, stroke_color=BLACK, stroke_width=1))
        eye_line_z = DashedVMobject(Line(self.eye_location[1] * UP + self.eye_location[0] * RIGHT, self.eye_location, stroke_color=BLACK, stroke_width=1))
        eye_lines = VGroup(eye_line_x, eye_line_y, eye_line_z)
        if self.show_eye_loc:
            self.play(ShowCreation(eye_lines))


        # shape1 = Polygon(*self.polygon_vertices, **self.shape_config)
        #dot1 = Dot(shape1.get_center(), color=BLACK)#.rotate(PI/2, axis=RIGHT)
        #label1 = TextMobject("A", **self.text_config).next_to(dot1, RIGHT+UP, buff=SMALL_BUFF)#.rotate(PI/2, axis=RIGHT)
        #shape1 = VGroup(shape1, dot1, label1)

        shape1 = Cube().move_to(np.array([0, 4, 1]))
        if self.show_3D:
            self.add(shape1)

        new_vertices = []
        for vertex in self.polygon_vertices:
            if self.show_3D and self.show_drawing:
                self.play(ShowCreation(DashedVMobject(Line(self.eye_location, vertex, stroke_color=BLACK, stroke_width=1))))
            intersect = get_intersect(self.eye_location, self.plane_init_point, self.plane_x_dir, self.plane_y_dir, vertex)
            new_vertices.append(intersect)

        shape2 = Polygon(new_vertices[0], new_vertices[4], new_vertices[7], new_vertices[3], color=BLACK)
        #dot2 = Dot(shape2.get_center(), color=BLACK).rotate(PI/2, axis=RIGHT)
        #label2 = TextMobject("B", **self.text_config).rotate(PI / 2, axis=RIGHT).next_to(dot2, RIGHT+OUT, buff=SMALL_BUFF/2)
        #shape2 = VGroup(shape2, dot2, label2)
        if self.show_3D and self.show_drawing:
            self.play(ShowCreation(shape2))

        shape3 = Polygon(new_vertices[1], new_vertices[5], new_vertices[6], new_vertices[2], color=BLACK)
        if self.show_3D and self.show_drawing:
            self.play(ShowCreation(shape3))

        line1 = Line(new_vertices[0], new_vertices[1], color=BLACK)
        line2 = Line(new_vertices[3], new_vertices[2], color=BLACK)
        line3 = Line(new_vertices[4], new_vertices[5], color=BLACK)
        line4 = Line(new_vertices[7], new_vertices[6], color=BLACK)
        lines = VGroup(line1, line2, line3, line4)
        if self.show_3D and self.show_drawing:
            self.play(ShowCreation(lines))

        if self.show_3D:
            self.move_camera(phi=55 * DEGREES,theta=-75 * DEGREES, run_time=1)

        if self.show_2D:
            self.clear()

        new_new_vertices = list(map(lambda vert: to_plane_coords(
            self.eye_location, self.plane_init_point, self.plane_x_dir, self.plane_y_dir, vert), self.polygon_vertices))

        if self.show_2D:
            self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)

        shape2 = Polygon(new_new_vertices[0], new_new_vertices[4], new_new_vertices[7], new_new_vertices[3], color=BLACK)
        if self.show_2D:
            self.play(ShowCreation(shape2))

        shape3 = Polygon(new_new_vertices[1], new_new_vertices[5], new_new_vertices[6], new_new_vertices[2], color=BLACK)
        if self.show_2D:
            self.play(ShowCreation(shape3))

        line1 = Line(new_new_vertices[0], new_new_vertices[1], color=BLACK)
        line2 = Line(new_new_vertices[3], new_new_vertices[2], color=BLACK)
        line3 = Line(new_new_vertices[4], new_new_vertices[5], color=BLACK)
        line4 = Line(new_new_vertices[7], new_new_vertices[6], color=BLACK)
        lines = VGroup(line1, line2, line3, line4)
        if self.show_2D:
            self.play(ShowCreation(lines))

        projection = VGroup(shape2, shape3, lines)
        if self.show_2D:
            self.play(projection.move_to, ORIGIN)
        self.wait(5)


    def num_plane(self, init_point, x_dir, y_dir, **kwargs):
        num_plane = NumberPlane(**kwargs)

        num_plane.move_to(init_point)

        x_rot_axis = np.cross(RIGHT, x_dir)
        x_rot_angle = np.arccos(np.clip((np.dot(RIGHT, x_dir)/np.linalg.norm(x_dir)), -1, 1))
        # self.play(num_plane.rotate, x_rot_angle, x_rot_axis)
        num_plane.rotate(x_rot_angle, x_rot_axis)

        secret_y = Dot(UP + init_point)
        secret_y.rotate(x_rot_angle, x_rot_axis, about_point=init_point)
        current_y_dir = secret_y.get_center() - init_point

        y_rot_axis = np.cross(current_y_dir, y_dir)
        y_rot_angle = np.arccos(np.clip((np.dot(current_y_dir, y_dir) / np.linalg.norm(y_dir)), -1, 1))
        # self.play(num_plane.rotate, y_rot_angle, y_rot_axis)
        num_plane.rotate(y_rot_angle, y_rot_axis)

        final_rot_axis = np.cross(x_dir, y_dir)
        num_plane.rotate(PI, final_rot_axis)

        num_plane.shift((self.plane_config["x_max"] + self.plane_config["x_min"])/2 * x_dir)
        num_plane.shift((self.plane_config["y_max"] + self.plane_config["y_min"])/2 * y_dir)

        self.play(ShowCreation(num_plane))
        return num_plane






def plane_func2(init_point, a_dir, b_dir):
    if isinstance(init_point, list):
        init_point = np.array(init_point)

    if np.linalg.norm(a_dir) != 1:
        a_dir = a_dir/np.linalg.norm(a_dir)
    if np.linalg.norm(b_dir) != 1:
        b_dir = b_dir/np.linalg.norm(b_dir)

    return lambda u,v: np.array(init_point + interpolate(-3, 3, u)*a_dir + interpolate(-3, 3, v)*b_dir)

def get_intersect2(eye_location, init_point, x_dir, y_dir, vertex):
    dir = vertex - eye_location

    A = np.transpose(np.array([x_dir, y_dir, dir]))
    b = eye_location - init_point
    x = np.linalg.solve(A, b)
    t = - x[2]

    return eye_location + t*dir

def to_plane_coords2(eye_location, init_point, x_dir, y_dir, vertex):
    dir = eye_location - vertex

    A = np.transpose(np.array([x_dir, y_dir, dir]))
    b = eye_location - init_point
    x = np.linalg.solve(A, b)
    u = x[0]
    v = x[1]
    return np.array([u, v, 0])

def points_func_plane_coords2(points, eye_location, init_point, x_dir, y_dir):
    return np.array(map(lambda p: to_plane_coords(eye_location, init_point, x_dir, y_dir, p), points))

def perp_plane2(eye_loc, vertices, prop):
    center = sum(vertices)/len(vertices)
    dir = center - eye_loc
    init_point = eye_loc + prop*dir
    x_dir = np.cross(dir, OUT)
    x_dir = x_dir / np.linalg.norm(x_dir)
    y_dir = np.cross(x_dir, dir)
    y_dir = y_dir/np.linalg.norm(y_dir)

    return [init_point, x_dir, y_dir]

class TwoDToThreeD(Scene):
    eye_loc = 4*DOWN + 3*OUT
    plane_info = perp_plane2(eye_loc, [4*UP], 0.5)


    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK},
        "axis_config": {
            "color": BLACK,
            "stroke_color": BLACK,
            "include_tip": True,
            "exclude_zero_from_default_numbers": True,
        },
        "function_config": {
            "stroke_color": BLACK
        },
        "eye_location": eye_loc,
        "plane_init_point": plane_info[0],
        "plane_x_dir": plane_info[1],
        "plane_y_dir": plane_info[2],
        "plane_config": {
            "axis_config": {
                "stroke_color": BLACK,
                "stroke_width": 2,
                "include_ticks": True,
                "include_tip": False,
                "line_to_number_buff": SMALL_BUFF,
                "label_direction": DR,
                "number_scale_val": 0.5,
            },
            "background_line_style": {
                "stroke_color": LIGHT_GREY,
                "stroke_width": 2,
                "stroke_opacity": 1,
            },
            "x_min": -6,
            "x_max": 6,
            "y_min": -10,
            "y_max": 20,
        },
    }

    def construct(self):
        #num_plane = self.num_plane(self.plane_init_point, self.plane_x_dir, self.plane_y_dir, **self.plane_config)
        num_plane = NumberPlane(**self.plane_config)
        self.play(ShowCreation(num_plane))

        graph = ParametricFunction(lambda t: np.array([interpolate(-np.sqrt(50), np.sqrt(50), t), interpolate(-np.sqrt(50), np.sqrt(50), t)**2, 0]), **self.function_config)
        self.play(ShowCreation(graph))
        og = num_plane.coords_to_point(0, 0)

        obs = VGroup(num_plane, graph)
       # obs.apply_function()
        self.play(obs.apply_function, lambda point: to_plane_coords2(self.eye_location, self.plane_init_point, self.plane_x_dir, self.plane_y_dir, point))
        self.wait(5)


    def num_plane(self, init_point, x_dir, y_dir, **kwargs):
        num_plane = NumberPlane(**kwargs)

        num_plane.move_to(init_point)

        x_rot_axis = np.cross(RIGHT, x_dir)
        x_rot_angle = np.arccos(np.clip((np.dot(RIGHT, x_dir)/np.linalg.norm(x_dir)), -1, 1))
        # self.play(num_plane.rotate, x_rot_angle, x_rot_axis)
        num_plane.rotate(x_rot_angle, x_rot_axis)

        secret_y = Dot(UP + init_point)
        secret_y.rotate(x_rot_angle, x_rot_axis, about_point=init_point)
        current_y_dir = secret_y.get_center() - init_point

        y_rot_axis = np.cross(current_y_dir, y_dir)
        y_rot_angle = np.arccos(np.clip((np.dot(current_y_dir, y_dir) / np.linalg.norm(y_dir)), -1, 1))
        # self.play(num_plane.rotate, y_rot_angle, y_rot_axis)
        num_plane.rotate(y_rot_angle, y_rot_axis)

        self.play(ShowCreation(num_plane))
        return num_plane


class RoadProblem(Scene):
    CONFIG = {
        "show_item_lines": False,
        "show_mark_lines": False,
        "show_horizon": True,
        "show_road": True,
        "show_trees": False,
        "show_marks": True,
        "item_height": 3,
        "item_n":4,
        "mark_n": 8,

        "item_proportion": 0.3,
        "mark_proportion": 0.4,
        "mark_config": {"fill_opacity":1, "color":BLACK},
        "camera_config": {"background_color": WHITE},
        "item_config": {"color": BLACK},
    }

    def construct(self):
        road_left = Line(3.5*DOWN + 3*LEFT, 3.5*UP, color = BLACK)
        road_right = Line(3.5*DOWN + 3*RIGHT, 3.5*UP, color= BLACK)
        road = VGroup(road_left, road_right)



        horizon = Line(6*LEFT + 3.5*UP, 6*RIGHT + 3.5*UP, color=BLACK)
        if self.show_horizon:
            self.play(FadeIn(horizon))

        if self.show_road:
            self.play(ShowCreation(road))

        og_tree = Tree(**self.item_config)
        tree_height = og_tree.get_height()
        og_tree.scale(self.item_height/tree_height)
        og_tree.next_to(3.5*DOWN + 3*LEFT, LEFT, buff = 0)
        og_tree.shift(og_tree.get_height()/2*UP)
        #self.play(ShowCreation(og_tree))

        tree_bottom_line = Line(og_tree.get_bottom(), 3.5*UP, color=BLACK)
        tree_top_line = Line(og_tree.get_top(), 3.5*UP, color=BLACK)

        tree_lines = VGroup(tree_bottom_line, tree_top_line)
        if self.show_item_lines:
            self.play(ShowCreation(tree_lines))


        tree_proportion = self.item_proportion
        tree_n = self.item_n - 1
        trees = [og_tree]
        for i in range(tree_n):
            tree = og_tree.deepcopy()
            loc = tree_bottom_line.point_from_proportion(1 - (1-tree_proportion)**(i+1))
            tree.scale((1-tree_proportion)**(i+1))
            tree.next_to(loc, UP, buff=0, aligned_edge=DOWN)
            trees.append(tree)
            #self.play(ShowCreation(tree))

        if self.show_trees:
            self.play(*[ShowCreation(tr) for tr in trees])

        mark_left_line = Line(3.5 * DOWN + 0.2 * LEFT, 3.5 * UP, color=BLACK)
        mark_right_line = Line(3.5 * DOWN + 0.2 * RIGHT, 3.5 * UP, color=BLACK)
        mark_lines = VGroup(mark_left_line, mark_right_line)
        if self.show_mark_lines:
            self.play(ShowCreation(mark_lines))

        mark_vertices = [[] for _ in range(self.mark_n)]

        mark_proportion = self.mark_proportion
        mark_len_prop = mark_proportion *0.4
        for i in range(self.mark_n):
            remaining = (1-mark_proportion)**(i)
            right_down = mark_right_line.point_from_proportion(1-remaining)
            right_up = mark_right_line.point_from_proportion((1-remaining) + (mark_len_prop*remaining))
            left_up = mark_left_line.point_from_proportion((1-remaining) + (mark_len_prop*remaining))
            left_down = mark_left_line.point_from_proportion(1-remaining)
            mark_vertices[i] = [right_down, right_up, left_up, left_down]

        if self.show_marks:
            self.play(*[ShowCreation(Polygon(*vert, **self.mark_config)) for vert in mark_vertices])

        #self.play(FadeOut(mark_lines), FadeOut(tree_lines))

        self.wait(5)


class SimilarTriangleProblem(Scene):
    CONFIG = {

        "shape_config": {"stroke_color": BLACK, "fill_opacity":0.5, "fill_color": GREY},
        "shape_verts": [3*RIGHT + -2*UP, 4*LEFT + 3*UP, 4*LEFT + 2*DOWN],
        "proportion":0.75,

        "big_left": True,
        "big_up": True,
        "big_hyp": True,
        "small_left": True,
        "small_up": True,
        "small_hyp": True,

        "camera_config": {"background_color": WHITE},
        "text_config": {"stroke_color": WHITE, "fill_color": BLACK}
    }

    def construct(self):
        prop = self.proportion

        # useful constants for directions and lengths
        vertices = self.shape_verts
        up_dir = vertices[1] - vertices[0]
        up_angle = math.atan2(-up_dir[1], -up_dir[0])
        up_perp_dir = np.array([up_dir[1], -up_dir[0], 0])
        up_len = np.linalg.norm(up_dir)

        left_dir = vertices[2] - vertices[1]
        left_angle = math.atan2(-left_dir[1], -left_dir[0])
        left_perp_dir = np.array([left_dir[1], -left_dir[0], 0])
        left_len = np.linalg.norm(left_dir)

        hyp_dir = vertices[2] - vertices[0]
        hyp_angle = math.atan2(-hyp_dir[1], -hyp_dir[0])
        hyp_perp_dir = np.array([-hyp_dir[1], hyp_dir[0], 0])
        hyp_len = np.linalg.norm(hyp_dir)



        # big
        big_tri = Polygon(*vertices, **self.shape_config)
        #elements.append(big_tri)

        big_left_text = "$a = " + str(round(left_len, 1)) + "$" if self.big_left else "$a$"
        big_left = TextMobject(big_left_text, **self.text_config).rotate(left_angle)
        big_left.move_to(vertices[1] + 0.5 * left_dir + 0.4 * left_perp_dir/left_len)
        #elements.append(big_left)

        big_up_text = "$b = " + str(round((1-prop)*up_len, 1)) + "$" if self.big_up else "$b$"
        big_up = TextMobject(big_up_text, **self.text_config).rotate(up_angle)
        big_up.move_to(((1+prop)/2) * up_dir + vertices[0] + 0.4 * up_perp_dir/up_len)
        #elements.append(big_up)

        big_hyp_text = "$c =" + str(round((1-prop)*hyp_len, 1)) + "$" if self.big_hyp else "$c$"
        big_hyp = TextMobject(big_hyp_text, **self.text_config).rotate(hyp_angle)
        big_hyp.move_to(((1+prop)/2) * hyp_dir + vertices[0] + 0.4 * hyp_perp_dir/hyp_len)
        #elements.append(big_hyp)

        big = VGroup(big_tri, big_left, big_up, big_hyp)


        # small
        small_vertices = lambda al: [vertices[0], al * up_dir + vertices[0],
                                     al * hyp_dir + vertices[0]]
        small_tri =  Polygon(*small_vertices(self.proportion), **self.shape_config)
        #elements.append(small_tri)

        small_left_text = "$d = " + str(round(prop * left_len, 1)) + "$" if self.small_left else "$d$"
        small_left = TextMobject(small_left_text, **self.text_config).rotate(left_angle)
        small_left.move_to(vertices[0] + prop * up_dir + 0.5 * prop * left_dir + 0.4 * left_perp_dir / left_len)
        #elements.append(small_left)

        small_up_text = "$e = " + str(round((prop) * up_len, 1)) + "$" if self.small_up else "$e$"
        small_up = TextMobject(small_up_text, **self.text_config).rotate(up_angle)
        small_up.move_to(0.5 * prop * up_dir + vertices[0] + 0.4 * up_perp_dir / up_len)
        #elements.append(small_up)

        small_hyp_text = "$f =" + str(round((prop) * hyp_len, 1)) + "$" if self.small_hyp else "$f$"
        small_hyp = TextMobject(small_hyp_text, **self.text_config).rotate(hyp_angle)
        small_hyp.move_to(0.5 * prop * hyp_dir + vertices[0] + 0.4 * hyp_perp_dir / hyp_len)
        #elements.append(small_hyp)

        small = VGroup(small_tri, small_up, small_left, small_hyp)


        # display
        elements = VGroup(big, small).move_to(ORIGIN)
        self.play(Write(elements))

        self.wait(5)


class Function(GraphScene):
    CONFIG = {
        "y_max": 9,
        "y_min": -1,
        "x_max": 4,
        "x_min": -4,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,
        "x_tick_frequency": 1/2,
        "x_axis_width": 9,
        "y_axis_height": 6,
        "x_labeled_nums": np.arange(-4, 4, 1),
        "y_labeled_nums": np.arange(-0, 10, 1),
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "axes_color": GRAY,
        "camera_config": {"background_color": WHITE},
        "x_label_background_color": WHITE,
        "y_label_background_color": WHITE,
        "x_label_fill_color": GREY,
        "y_label_fill_color": GREY,
        "x_label_scale": 1,
        "y_label_scale": 1,
        "x_decimal_number_config": {"num_decimal_places": 0, "background_stroke_color": WHITE, "fill_color": GREY},
        "x_label_num_scale_val": 1,
        "y_decimal_number_config": {"num_decimal_places": 0, "background_stroke_color": WHITE, "fill_color": GREY},
        "y_label_num_scale_val": 0.85,
        "text_config": {"background_stroke_color": WHITE, "fill_color": BLACK}
    }

    def construct(self):
        self.graph_origin = 2 * DOWN
        self.setup_axes(animate=True)

        parab = self.get_graph(lambda x: x**2, color=BLACK, x_min= -3, x_max=3)

        self.play(ShowCreation(parab))

        self.wait(5)