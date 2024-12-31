from manim import *

class LambWThumb1(Scene):
    def construct(self):
        text1 = Tex("Can you solve?").shift(UP*2).scale(3)
        text2 = MathTex("3^x + x = 735").scale(3)
        text3 = Tex("without guessing").shift(DOWN*2).scale(3)
        self.add(text1, text2, text3)

class LambWThumb2(Scene):
    def construct(self):
        text1 = Tex("Using Lambert W").shift(UP*2).scale(3)
        text2 = MathTex("3^x + x = 735").shift(DOWN*2).scale(3)
        text3 = Tex("to solve:").scale(3)
        self.add(text1, text2, text3)
