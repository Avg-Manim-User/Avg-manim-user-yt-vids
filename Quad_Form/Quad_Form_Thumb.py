from manim import *

class QuadFormThumb(Scene):
    def construct(self):
        line1 = Line(UP, DOWN).scale(4)
        text1 = Text("Derivation of the quadratic formula:", font_size=25).shift(UP*3/4 + LEFT*32/9)
        text2 = MathTex(r"x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").shift(DOWN*3/4 + LEFT*32/9)
        ax = Axes(y_range= [-3, 3], x_range= [-2, 4], x_length= 6, y_length= 6, tips= False).shift(RIGHT*32/9)
        par = ax.plot(lambda x: x**2 - 3*x - 3/4, color= RED, x_range= [-.94, 3.94])
        dot1 = Dot(RIGHT*(32/9 - 1.23))
        text3 = MathTex(r"x_1").next_to(dot1, DL)
        dot2 = Dot(RIGHT*(32/9 + 2.23))
        text4 = MathTex(r"x_2").next_to(dot2, DR)
        dot3 = Dot(RIGHT*(32/9 + 1/2))
        text5 = MathTex(r"x_{\text{v}}").next_to(dot3, DOWN).align_to(dot3, LEFT).shift(RIGHT*.2)
        line2 = DashedLine(UP, DOWN).shift(RIGHT*(32/9 + 1/2)).scale(3)
        double_arrow1 = DoubleArrow(start= dot1.get_center(), end= dot3.get_center(), buff= 0, tip_length= .25, color= GREEN)
        text6 = MathTex(r"d").next_to(double_arrow1, UP).shift(DOWN*.2)
        double_arrow2 = DoubleArrow(start= dot3.get_center(), end= dot2.get_center(), buff= 0, tip_length= .25, color= GREEN)
        text7 = MathTex(r"d").next_to(double_arrow2, UP).shift(DOWN*.2)

        group1 = VGroup(line1, line2, text1, text2, ax, par, dot1, dot2, dot3, text3, text4, text5, text6, text7, double_arrow1, double_arrow2)
        self.add(group1)