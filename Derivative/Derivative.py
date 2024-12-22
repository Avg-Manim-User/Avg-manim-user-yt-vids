from manim import *
from MF_Tools import ir, TransformByGlyphMap

class Derivative(Scene):
    def construct(self):
        # intro
        text1 = Tex("Avg Manim User presents:", font_size= 60).shift(UP)
        text2 = Tex("Derivation of the derivative:", font_size= 60)
        text3 = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}").shift(DOWN*5/4)
        dot1 = Dot([-6.8, 0, 0], radius= 0)
        textgroup1 = VGroup(text1, text2, text3)
        self.play(Write(textgroup1), run_time= 2)
        self.wait(3)
        self.play(FadeOut(textgroup1), run_time= 1)
        self.wait(.25)

        # def derivative
        line1 = Line(UP, DOWN).scale(4)
        text4 = Text("The derivative is defined as the\nslope of a function at a single point", font_size= 25).shift(UP*3).align_to(dot1, LEFT)
        self.play(
            Write(text4),
            FadeIn(line1),
            run_time= 1
        )

        # draw graph
        ax = Axes(y_range= [-3, 3], x_range= [-3, 3], x_length= 6, y_length= 6, tips= False).shift(RIGHT*32/9)
        func1 = ax.plot(lambda x: x**3 + 2*x**2 - x - 1, color= RED, x_range= [-2.64, 1.25])
        self.play(
            Create(ax),
            Create(func1),
            run_time= 3
        )

        # add point A
        point1 = ax.c2p(0.22, -1.11)
        dot2 = Dot(point1)
        text5 = always_redraw(lambda: MathTex(r"A").next_to(dot2, DOWN, buff=0.2))
        self.play(
            FadeIn(dot2),
            Write(text5),
            run_time= 1
        )

        # add text
        text6 = Text("To approximate the slope at point A,\nyou can a pick a point B that is close to A,\nand calculate the slope inbetween A & B", font_size= 25).shift(UP*2).align_to(dot1, LEFT)
        self.play(Write(text6), run_time= 1)
        self.wait(3)

        # add point B
        point2 = ax.c2p(1, 1) 
        dot3 = Dot(point2)
        text7 = always_redraw(lambda: MathTex(r"B").next_to(dot3, DL, buff= 0.2))
        self.play(
            FadeIn(dot3),
            Write(text7),
            run_time= 1
        )

        # approximate slope
        text8 = MathTex(r"f'(x_A) \approx \frac{y_B - y_A}{x_B - x_A}").shift(UP*.9).align_to(dot1, LEFT)
        self.play(Write(text8), run_time= 1)

        # generalise
        text9 = Text("We can rewrite this by describing point A\nrelative to point B", font_size= 25).shift(DOWN*.2).align_to(dot1, LEFT)
        text10 = MathTex(r"f'(x_A) \approx \frac{f(x_A + h) - f(x_A)}{x_A + h - x_A}").shift(DOWN*1.1).align_to(dot1, LEFT)
        text11 = MathTex(r"f'(x_A) \approx \frac{f(x_A + h) - f(x_A)}{h}").shift(DOWN*1.1).align_to(dot1, LEFT)
        text12 = MathTex(r"\text{Where: }h = x_B - x_A").shift(DOWN*2).align_to(dot1, LEFT)
        self.play(Write(text9), run_time= 1)
        self.wait(3)
        self.play(Write(text10), run_time= 1)
        self.wait(2)
        self.play(
            TransformByGlyphMap(
                text10, text11,
                (ir(0, 20), ir(0,20)),
                (ir(21,27), [21])
            ),
            run_time= 1
        )
        self.wait(2)
        self.play(Write(text12), run_time= 1)
        self.wait(2)

        # derive derivative
        text13 = Text("This approximation improves as h gets\nsmaller, but h can't equal 0 because then\nyou'd divide by 0", font_size=25).shift(DOWN*3).align_to(dot1, LEFT)
        textgroup2 = VGroup(text8, text9, text11, text12, text13)
        self.play(Write(text13), run_time= 1)
        self.wait(1)
        self.play(
            FadeOut(text4),
            FadeOut(text6),
            textgroup2.animate().shift(UP*2),
        )
        self.wait(1)
        text14 = Text("Because of this we define the derivative\nas this approximation as h approaches 0,\nbut never reaches it:", font_size= 25).shift(DOWN*2.1).align_to(dot1, LEFT)
        self.play(Write(text14), run_time= 1)
        text3.move_to(ORIGIN).shift(DOWN*3.2).align_to(dot1, LEFT)
        self.play(Write(text3), run_time= 1)
        self.wait(3)

        # introduce example of x^2
        text15 = Tex("For example:").shift(UP*3)
        group1 = VGroup(text3, text5, text7, text8, text9, text11, text12, text13, text14, ax, func1, dot2, dot3, line1)
        self.play(
            FadeOut(group1),
            Write(text15),
            run_time= 2
        )

        # example
        text16 = MathTex(r"f(x) = x^2").shift(UP*2)
        text3.move_to(ORIGIN).shift(UP)
        text17 = MathTex(r"f'(x) = \lim_{h\to 0} \frac{(x+h)^2 - x^2}{h}").shift(UP)
        text18 = MathTex(r"f'(x) = \lim_{h\to 0} \frac{x^2 + 2xh + h^2 - x^2}{h}").shift(DOWN*1/3)
        text19 = MathTex(r"f'(x) = \lim_{h\to 0} \frac{2xh + h^2}{h}").shift(DOWN*1/3)
        text20 = MathTex(r"f'(x) = \lim_{h\to 0} 2x + h").shift(DOWN*5/3)
        text21 = MathTex(r"f'(x) = 2x").shift(DOWN*9/3)
        self.play(Write(text16), run_time= 1)
        self.wait(2)
        self.play(Write(text3), run_time= 1)
        self.wait(2)
        self.play(
            TransformByGlyphMap(
                text3, text17,
                (ir(0, 11), ir(0, 11)),
                ([12], []),
                (ir(13, 17), ir(12, 16)),
                ([], [17]),
                ([18], [18]),
                ([19, 20], []),
                ([21,22], [19, 20]),
                ([23, 24], [21, 22])
            ),
            run_time= 1
        )
        self.wait(2)
        self.play(Write(text18), run_time= 1)
        self.wait(2)
        self.play(
            TransformByGlyphMap(
                text18, text19,
                (ir(0, 11), ir(0, 11)),
                (ir(12, 14), []),
                (ir(15, 20), ir(12, 17)),
                (ir(21, 23), []),
                ([24, 25], [18, 19])
            ),
            run_time= 1
        )
        self.wait(2)
        self.play(Write(text20), run_time= 1)
        self.wait(2)
        self.play(Write(text21), run_time= 1)
        self.wait(2)


        # outro
        text22 = Tex("Thanks for watching!").shift(RIGHT*32/9 + DOWN*2)
        textgroup3 = VGroup(text15, text16, text17, text19, text20, text21)
        self.play(FadeOut(textgroup3), run_time= 1)
        self.play(Write(text22, run_time= 2), run_time= 1)
        self.wait(5)