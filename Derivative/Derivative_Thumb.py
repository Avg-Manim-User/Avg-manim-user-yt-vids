from manim import *

class DerivativeThumb(Scene):
    def construct(self):
        text1 = Tex("How to derive").scale(3).rotate(PI/10).shift(UP*2 + LEFT*2.5)
        text2 = Tex("the derivative!").scale(3).rotate(PI/10).shift(-1 * (UP*2 + LEFT*2.5))
        text3 = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}").scale(1.5)
        self.add(text1, text2, text3)