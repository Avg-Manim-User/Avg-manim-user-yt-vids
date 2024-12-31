from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class Short1(Scene):
    def construct(self):
        text1 = Text("How to solve:").shift(UP*4)
        text2 = MathTex(r"2^x = x^{32}").shift(UP*3)
        text3 = MathTex(r"\left(2^x\right)^{\frac{1}{x}} = \left(x^{32}\right)^{\frac{1}{x}}").shift(UP*2)
        text4 = MathTex(r"2 = x^{\frac{32}{x}}").shift(UP)
        text5 = MathTex(r"2^{\frac{1}{32}} = \left(x^{\frac{32}{x}}\right)^{\frac{1}{32}}")
        text6 = MathTex(r"2^{\frac{1}{32}} = x^{\frac{1}{x}}").shift(DOWN*1)
        text7 = MathTex(r"2^{\frac{8}{8\cdot 32}} = x^{\frac{1}{x}}").shift(DOWN*2)
        text8 = MathTex(r"2^{8\cdot \frac{1}{8\cdot 32}} = x^{\frac{1}{x}}").shift(DOWN*3)
        text9 = MathTex(r"256^{\frac{1}{256}} = x^{\frac{1}{x}}").shift(DOWN*3)
        text10 = MathTex(r"x = 256").shift(DOWN*3)
        text11 = Text("Thanks for watching!").shift(DOWN)
        group1 = VGroup(text1, text2, text3, text4, text5, text6, text7)
        self.add(text1, text2)
        self.wait(3)
        self.play(Write(text3))
        self.wait(2.5)
        self.play(Write(text4))
        self.wait(2.5)
        self.play(Write(text5))
        self.wait(2.5)
        self.play(Write(text6))
        self.wait(2.5)
        self.play(Write(text7))
        self.wait(2.5)
        self.play(Write(text8))
        self.wait(2.5)
        self.play(ReplacementTransform(text8, text9))
        self.wait(3.5)
        self.play(ReplacementTransform(text9, text10))
        self.wait(2.5)
        self.play(
            text10.animate().move_to(ORIGIN).scale(1.5),
            FadeOut(group1),
            run_time= 1
            )
        self.play(Write(text11))
        self.wait(5)



        
