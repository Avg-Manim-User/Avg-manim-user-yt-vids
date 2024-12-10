from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # animate pythagorean theorom up
        text = Text("Proof of:").shift(UP)
        text1 = MathTex(r"a^2 + b^2 = c^2")
        self.play(Write(text1), Write(text), run_time=1)
        self.wait(2)
        self.play(text1.animate().shift(UP*13/4), Unwrite(text), run_time= 1.5)

        # animate triangle
        a = ValueTracker(3/2)
        b = ValueTracker(4/2)
        triangle1 = Polygon([0, 3/2, 0], [-4/2, 0, 0], ORIGIN, color= WHITE).set_fill(RED, opacity= 0.25)
        triangle1.shift(RIGHT*4/4 + DOWN*3/4)
        self.play(DrawBorderThenFill(triangle1))

        # animate labels of triangle
        text2 = MathTex(r"a").next_to(triangle1, RIGHT)
        text3 = MathTex(r"b").next_to(triangle1, DOWN)
        text4 = MathTex(r"c").shift(UL*.3)
        line1 = Line(LEFT, RIGHT)
        line2 = Line(DOWN, UP)
        rightangle = RightAngle(line1, line2, quadrant= (-1, 1), length= 0.2).align_to(triangle1, DR)
        self.play(Write(text2), Write(text3), Write(text4), FadeIn(rightangle), runtime= 1)

        self.wait(1)

        # replace triangle with square
        square1 = Square(a.get_value()+b.get_value())
        trianglegroup1 = VGroup(text2, text3, text4, rightangle, triangle1)
        self.play(FadeOut(trianglegroup1), run_time= 1)
        self.play(FadeIn(square1))

        # add labels
        text5 = MathTex(r"a + b")
        text6 = text5.copy().next_to(square1, LEFT)
        text5.next_to(square1, UP)
        self.play(Write(text5), Write(text6), run_time = 1)

        # add squares, replace labels
        text7 = text2.copy().next_to(square1, UP).shift(LEFT*1)
        text2.next_to(square1, LEFT).shift(UP*1)
        text8 = text3.copy().next_to(square1, UP).shift(RIGHT*3/4)
        text3.next_to(square1, LEFT).shift(DOWN*3/4)
        textgroup1 = VGroup(text2, text7, text8, text3)
        self.play(Unwrite(text5), Unwrite(text6), run_time= 1)
        square2 = Square(3/2, color= WHITE).set_fill(GREEN, opacity=.25)
        square3 = Square(4/2, color= WHITE).set_fill(BLUE, opacity=.25)
        square2.shift(UL*4/4)
        square3.shift(DR*3/4)
        self.play(DrawBorderThenFill(square2), DrawBorderThenFill(square3), Write(textgroup1, run_time= 1), run_time= 2)

        # add labels
        text9 = MathTex(r"a^2").move_to(square2)
        text10 = MathTex(r"b^2").move_to(square3)
        text11 = MathTex(r"ab").shift(RIGHT*3/4 + UP)
        text12 = text11.copy().shift(DL*7/4)
        textgroup2 = VGroup(text9, text10, text11, text12)
        self.play(Write(textgroup2), run_time= 1)

        # shift everything left
        group1 = VGroup(textgroup1, textgroup2, square1, square2, square3)
        self.play(group1.animate().shift(LEFT*3), run_time= 2)

        self.wait(1)

        # describe area
        text13 = MathTex(r"A = (a + b)^2").align_to(ORIGIN, LEFT)
        text14 = MathTex(r"A = a^2 + 2ab + b^2").align_to(ORIGIN, LEFT)
        self.play(Write(text13), run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(text13, text14), run_time=1)
        self.play(text14.animate().shift(UP*7/4))

        self.wait(1)

        # remove labels, add triangles
        self.play(Unwrite(textgroup2))
        triangle2 = triangle1.copy().shift(LEFT*9/4 + UP)
        triangle3 = triangle2.copy().rotate(PI)
        triangle4 = triangle3.copy().rotate(TAU/4, about_point= [-13/4, 1/4, 0]).shift(DOWN*2)
        triangle5 = triangle4.copy().rotate(PI)
        trianglegroup2 = VGroup(triangle2, triangle3, triangle4, triangle5)
        self.play(FadeIn(trianglegroup2))

        self.wait(1)

        # remove squares, transform triangles, change labels
        self.play(FadeOut(square2, square3), run_time= 1)
        self.play(
            triangle2.animate().rotate(TAU/4, about_point= [-5/4, 7/4, 0]).shift(LEFT*3/2),
            triangle3.animate().shift(LEFT*3/2),
            triangle5.animate().rotate(-TAU/4, about_point= [-13/4, -7/4, 0]),
            text7.animate().shift(RIGHT*8/4),
            text8.animate().shift(LEFT*6/4),
            run_time= 2
        )

        self.wait(1)

        # add square
        square4 = Square(5/2).set_fill(YELLOW, opacity=.25).rotate(np.arctan(3/4)).shift(LEFT*3)
        self.play(FadeIn(square4), run_time= 1)

        # add labels
        text15 = MathTex(r"\frac{1}{2}ab", font_size= 30).move_to(triangle2).move_to(triangle2).shift(UP/2 + RIGHT/4)
        text16 = text15.copy().move_to(triangle3).shift(LEFT/2 + UP/4)
        text17 = text15.copy().move_to(triangle4).shift(DOWN/2 + LEFT/4)
        text18 = text15.copy().move_to(triangle5).shift(RIGHT/2 + DOWN/4)
        text19 = MathTex(r"c^2").move_to(square4)
        textgroup3 = VGroup(text15, text16, text17, text18, text19)
        self.play(Write(textgroup3), run_time= 1)

        # describe area
        text20 = MathTex(r"A = 4 \cdot \frac{1}{2}ab + c^2").align_to(ORIGIN, LEFT)
        text21 = MathTex(r"A = 2ab + c^2").align_to(ORIGIN, LEFT)
        text22 = MathTex(r"a^2 + 2ab + b^2 = 2ab + c^2").align_to(ORIGIN, LEFT)
        text23 = text1.copy().align_to(ORIGIN, LEFT).shift(DOWN*13/4)
        self.play(Write(text20), run_time= 1)
        self.wait(2)
        self.play(ReplacementTransform(text20, text21), run_time= 1)
        self.play(text21.animate().shift(UP*7/8), run_time= 1)
        self.wait(1)
        self.play(Write(text22), run_time= 1)
        self.wait(4)
        self.play(ReplacementTransform(text22, text23), run_time= 1)
        self.wait(1)
        
        # zoom in
        group2 = VGroup(text14, text21, text23, trianglegroup2, textgroup3, textgroup1, square4, square1)
        self.play(
            FadeOut(group2),
            text1.animate().move_to(ORIGIN).scale(4),
            run_time= 2
        )

        self.wait(3)
