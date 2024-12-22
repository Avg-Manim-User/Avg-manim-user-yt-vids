from manim import *

class QuadForm(Scene):
    def construct(self):
        # intro
        text1 = Text("Avg Manim User presents:").shift(UP)
        text2 = Text("Derivation of the quadratic formula")
        text3 = MathTex(r"x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").shift(DOWN*5/4)
        textgroup1 = VGroup(text1, text2, text3)
        self.play(Write(textgroup1), run_time= 2)
        self.wait(3)
        self.play(FadeOut(textgroup1), run_time= 1)
        self.wait(.25)

        # add text
        text4 = Text("The quadratic formula solves for the \nroots of a 2nd degree polynomial:", font_size= 25).shift(UP*2)
        text5 = MathTex(r"f(x) = ax^2 + bx + c = 0")
        textgroup2 = VGroup(text4, text5).shift(LEFT*32/9)
        line1 = Line(UP, DOWN).scale(4)
        self.play(Write(textgroup2), FadeIn(line1), run_time= 2)

        # draw parobala, axes
        ax = Axes(y_range= [-3, 3], x_range= [-2, 4], x_length= 6, y_length= 6, tips= False)
        par = ax.plot(lambda x: x**2 - 3*x - 3/4, color= RED, x_range= [-.94, 3.94])
        graph = VGroup(ax, par).shift(RIGHT*32/9)
        self.play(Create(ax), Create(par), run_time= 3)

        # shift/add text
        text6 = Text("The roots are where the graph \ncrosses the y-axis", font_size= 25).shift(LEFT*32/9)
        self.play(
            text4.animate().shift(UP),
            text5.animate().shift(UP*2),
            run_time= 1
        )
        self.wait(3)
        self.play(Write(text6), runtime = 2)

        # indicate x_inctercepts
        dot1 = Dot(RIGHT*(32/9 - 1.23))
        text7 = MathTex(r"x_1").next_to(dot1, UR)
        dot2 = Dot(RIGHT*(32/9 + 2.23))
        text8 = MathTex(r"x_2").next_to(dot2, UL)
        dotgroup1 = VGroup(dot1, dot2, text7, text8)
        self.play(FadeIn(dotgroup1), run_time= 1)
        self.play(
            Indicate(dot1),
            Indicate(dot2),
            text6.animate().shift(UP),
            run_time= 2
            )

        # indicate vertex
        text9 = Text("The x of the vertex is in the \ncenter of the roots, and satisfies:", font_size= 25).shift(LEFT*32/9)
        dot3 = Dot(RIGHT*(32/9 + 1/2))
        text10 = MathTex(r"x_{\text{v}}").next_to(dot3, DOWN).align_to(dot3, LEFT).shift(RIGHT*.2)
        line2 = DashedLine(UP, DOWN).shift(RIGHT*(32/9 + 1/2)).scale(3)
        self.play(
            FadeIn(dot3),
            FadeIn(text10),
            FadeIn(line2),
            Write(text9),
            run_time = 1
            )
        self.wait(1)
        
        # derive x_v
        text11 = MathTex(r"f'(x_{\text{v}}) = 0").shift(LEFT*32/9 + DOWN)
        text12 = MathTex(r"f'(x) = 2ax + b = 0").shift(LEFT*32/9 + DOWN*2)
        text13 = MathTex(r"2ax = -b").shift(LEFT*32/9 + DOWN*3)
        textgroup3 = VGroup(text11, text12, text13)
        textgroup4 = VGroup(text4, text5, text6, text9, textgroup3)
        text14 = MathTex(r"x_{\text{v}} = -\frac{b}{2a}").shift(LEFT*32/9 + DOWN*3)
        self.play(Write(text11), run_time= 1)
        self.wait(2)
        self.play(Write(text12), run_time= 1)
        self.wait(2)
        self.play(Write(text13), run_time= 1)
        self.wait(2)
        self.play(
            textgroup4.animate.shift(UP),
            FadeOut(text4),
            run_time= 1
            )
        self.play(Write(text14), run_time= 1)
        textgroup5 = VGroup(text6, text9, textgroup3)
        self.play(
            FadeOut(textgroup5),
            text14.animate().shift(UP*5),
            run_time= 1
        )

        # rewrite f(x) and show x_1 * x_2 = c
        text15 = Text("f(x) can also be rewritten as:", font_size=25).shift(LEFT*32/9 + UP)
        text16 = MathTex(r"f(x) = a(x - x_1)(x - x_2)").shift(LEFT*32/9)
        text17 = MathTex(r"= ax^2 - (x_1 + x_2)ax + ax_1x_2").shift(LEFT*32/9 + DOWN)
        text18 = Text("By comparing coefficients we see:", font_size=25).shift(LEFT*32/9 + DOWN*2)
        text19 = MathTex(r"x_1x_2 = \frac{c}{a}").shift(LEFT*32/9 + DOWN*3)
        textgroup6 = VGroup(text15, text16, text17, text18, text5)
        self.play(Write(text15), run_time= 1)
        self.wait(1)
        self.play(Write(text16), run_time= 1)
        self.wait(2)
        self.play(Write(text17), run_time= 1)
        self.wait(2)
        self.play(Write(text18), run_time= 1)
        self.wait(2)
        self.play(Write(text19), run_time= 1)
        self.wait(3)
        self.play(
            FadeOut(textgroup6),
            text19.animate().shift(UP*6 + RIGHT*16/9),
            text14.animate().shift(UP + LEFT*16/9),
            run_time= 1
        )

        # show d
        darrow1 = DoubleArrow(start= dot1.get_center(), end= dot3.get_center(), buff= 0, tip_length= .25, color= GREEN)
        text20 = MathTex(r"d").next_to(darrow1, UP).shift(DOWN*.2)
        darrow2 = DoubleArrow(start= dot3.get_center(), end= dot2.get_center(), buff= 0, tip_length= .25, color= GREEN)
        text21 = MathTex(r"d").next_to(darrow2, UP).shift(DOWN*.2)
        self.play(
            text7.animate().next_to(dot1, DL),
            text8.animate().next_to(dot2, DR),
            Create(darrow1),
            Create(darrow2),
            Write(text20),
            Write(text21),
            run_time= 1
            )
        
        # solve for d
        text22 = MathTex(r"x_1 = x_{\text{v}} - d \wedge x_2 = x_{\text{v}} + d").shift(UP*3/2 + LEFT*32/9)
        text23 = MathTex(r"x_1x_2 = (x_{\text{v}} - d)(x_{\text{v}} + d) = \frac{c}{a}").shift(LEFT*32/9)
        text24 = MathTex(r"x_{\text{v}}^2 - d^2 = \frac{c}{a}").shift(DOWN*3/2 + LEFT*32/9)
        text25 = MathTex(r"d^2 = x_{\text{v}}^2 - \frac{c}{a}").shift(DOWN*3 + LEFT*32/9)
        text26 = MathTex(r"d^2 = \left(-\frac{b}{2a}\right)^2 - \frac{c}{a}").shift(DOWN*3 + LEFT*32/9)
        text27 = MathTex(r"d^2 = \frac{b^2}{4a^2} - \frac{4ac}{4a^2}").shift(DOWN*3/2 + LEFT*32/9)
        text28 = MathTex(r"d^2 = \frac{b^2 - 4ac}{4a^2}").shift(DOWN*3 + LEFT*32/9)
        text29 = MathTex(r"d = \sqrt{\frac{b^2 - 4ac}{4a^2}}").shift(DOWN*3/2 + LEFT*32/9)
        text30 = MathTex(r"d = \frac{\sqrt{b^2 - 4ac}}{2a}").shift(DOWN*3 + LEFT*32/9)
        self.play(Write(text22), run_time= 1)
        self.wait(3)
        self.play(Write(text23), run_time= 1)
        self.wait(2)
        self.play(Write(text24), run_time= 1)
        self.wait(2)
        self.play(Write(text25), run_time= 1)
        self.wait(2)
        self.play(ReplacementTransform(text25, text26), run_time= 1)
        self.wait(2)
        self.play(
            FadeOut(text23),
            FadeOut(text24),
            text26.animate().shift(UP*3),
            run_time= 1
        )
        self.wait(1)
        self.play(Write(text27), run_time= 1)
        self.wait(3)
        self.play(Write(text28), run_time= 1)
        self.wait(2)
        self.play(
            FadeOut(text26),
            FadeOut(text27),
            text28.animate().shift(UP*3),
            run_time= 1
        )
        self.wait(1)
        self.play(Write(text29), run_time= 1)
        self.wait(2)
        self.play(Write(text30), run_time= 1)
        self.wait(2)


        # solve for x_{1,2}
        text31 = MathTex(r"x_{1, 2} = x_v \pm d").shift(LEFT*32/9)
        self.play(
            FadeOut(text28),
            FadeOut(text29),
            run_time= 1
        )
        self.play(
            Write(text31),
            text30.animate().shift(UP*3/2),
            run_time= 1
        )
        self.wait(2)
        self.play(
            FadeOut(text22),
            text30.animate().shift(UP*3/2),
            text31.animate().shift(UP*3/2),
            run_time= 1
        )
        self.wait(1)
        text32 = MathTex(r"x_{1, 2} = \frac{-b}{2a} \pm \frac{\sqrt{b^2 - 4ac}}{2a}").shift(DOWN*3/2 + LEFT*32/9)
        text3.shift(DOWN*7/4 + LEFT*32/9)
        self.play(Write(text32), run_time= 1)
        self.wait(2)
        self.play(Write(text3), run_time= 1)
        self.wait(3)

        # pre-outro
        group1 = VGroup(text14, text19, text30, text31, text32, line1, line2, ax, par, darrow1, darrow2, text20, text21, text7, text8, text10, dot1, dot2, dot3)
        text33 = Text("Thanks for watching!").shift(DOWN*2)
        self.play(
            FadeOut(group1),
            text3.animate().move_to(ORIGIN).scale(2),
            run_time= 2
        )
        self.play(Write(text33), run_time= 2)
        self.wait(1)

        # outro
        group2 = VGroup(text3, text33)
        self.play(group2.animate().shift(DOWN*2 + RIGHT*32/9).scale(.5))
        self.wait(5)