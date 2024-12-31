from manim import *
from MF_Tools import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.background_color = DARKER_GRAY

class LambWShort(Scene):
    def construct(self):
        text1 = Tex("Avg Manim User presents:").shift(UP)
        text2 = Tex("Application of the Lambert W function:")
        text3 = MathTex(r"3^x + x = 735").shift(DOWN)
        textgroup1 = VGroup(text1, text2, text3)
        self.play(Write(textgroup1), run_time= 2)
        self.wait(3)
        self.play(
            Unwrite(text1),
            Unwrite(text2),
            text3.animate().shift(UP*4.5),
            run_time=1)
        self.wait(2)

        # start solving
        text4 = MathTex(r"3^x = 735 - x").shift(UP*2.75)
        text5 = MathTex(r"3^x\cdot 3^{735 - x} = (735 - x) \cdot 3^{735-x}").shift(UP*2)
        text6 = MathTex(r"3^{x + 735 - x} = (735 - x) \cdot 3^{735-x}").shift(UP*2)
        text7 = MathTex(r"3^{735} = (735 - x) \cdot 3^{735-x}").shift(UP*2)
        text8 = MathTex(r"3^{735} = (735 - x) \cdot e^{\ln\left(3^{735-x}\right)}").shift(UP*1.25)
        text9 = MathTex(r"3^{735} = (735 - x) \cdot e^{(735 - x)\cdot \ln(3)}").shift(UP*1.25)
        text10 = MathTex(r"3^{735}\cdot \ln(3) = \ln(3)\cdot(735 - x) \cdot e^{(735 - x)\cdot \ln(3)}").shift(UP*1.25).scale(0.9)

        self.play(TransformByGlyphMap(text3, text4,
            ([0, 1], [0, 1]),
            (ir(4, 7), ir(2, 5)),
            ([2], [6]),
            ([3], [7]),
            from_copy= True
        ), run_time= 1.5)
        self.wait(2)
        self.play(TransformByGlyphMap(text4, text5,
            ([0, 1], [0, 1]),
            ([], ir(2,8)),
            ([2], [9]),
            ([], [10]),
            (ir(3, 7), ir(11, 15)),
            ([], ir(16, 23)),
            from_copy= True                              
        ), run_time= 1.5)
        self.wait(2)
        self.play(TransformByGlyphMap(text5, text6,
            ([0, 1], [0, 1]),
            ([2, 3], [2]),
            (ir(4, 8), ir(3, 7)),
            (ir(9, 23), ir(8, 22))
        ), run_time= 1.5)
        self.wait(1.5)
        self.play(TransformByGlyphMap(text6, text7,
            ([0], [0]),
            ([1, 2, 6, 7], []),
            (ir(3, 5), ir(1, 3)),
            (ir(8, 22), ir(4, 18))
            ), run_time= 1)
        self.wait(2)
        self.play(TransformByGlyphMap(text7, text8,
            (ir(0, 12), ir(0, 12)),
            ([], ir(13, 16)),
            (ir(13, 18), ir(17, 22)),
            ([], [23]),
            from_copy= True
        ), run_time= 1)
        self.wait(2)
        self.play(TransformByGlyphMap(text8, text9,
            (ir(0, 13), ir(0, 13)),
            (ir(18, 22), ir(14, 21)),
            (ir(14, 17), ir(22, 25)),
            ([23], [26])
        ), run_time= 1)
        self.wait(2)
        self.play(TransformByGlyphMap(text9, text10,
            (ir(0, 3), ir(0, 3)),
            ([], ir(4, 9)),
            ([4], [10]),
            ([], ir(11, 16)),
            (ir(5, 26), ir(17, 38))
        ), run_time= 1)
        
        # introduce Lamb W
        text11 = MathTex(r"W(ye^y) = y").shift(UP/2)
        text12 = MathTex(r"W\left(3^{735}\cdot \ln(3)\right) = W\left(\ln(3)\cdot(735 - x) \cdot e^{(735 - x)\cdot \ln(3)}\right)").shift(DOWN/4).scale(0.7)
        text13 = MathTex(r"W\left(3^{735}\cdot \ln(3)\right) = \ln(3)\cdot(735 - x)").shift(DOWN)
        text14 = MathTex(r"735 - x = \frac{W\left(3^{735}\cdot \ln(3)\right)}{\ln(3)}").shift(DOWN*2)
        text15 = MathTex(r"x = 735 - \frac{W\left(3^{735}\cdot \ln(3)\right)}{\ln(3)}").shift(DOWN*2)
        self.play(Write(text11))
        self.wait(3/4)
        self.play(Write(text12))
        self.wait(3)
        self.play(Write(text13))
        self.wait(2)
        self.play(Write(text14))
        self.wait(2)
        self.play(TransformByGlyphMap(text14, text15,
            ([4], [0]),
            ([5], [1]),
            (ir(0, 2), ir(2, 4)),
            ([3], [5]),
            (ir(6, 24), ir(6, 24))
        ), run_time= 1)

        # give approximation
        text16 = Tex("We can calculate the Lambert W of a constant:").shift(UP*3/2).scale(0.8)
        text17 = MathTex(r"x = 735 - \frac{800.888}{1.097} = 735 - 729 = 6").shift(UP/2)
        text18 = Tex("Checking the solution:").shift(DOWN/2)
        text19 = MathTex(r"3^6 + 6 = 729 + 6 = 735").shift(DOWN*5/4)
        group1 = VGroup(text13, text12, text11, text10, text7, text4)
        self.play(
            FadeOut(group1),
            text15.animate().shift(UP*9/2),
            run_time= 2
        )
        self.wait(1/2)
        self.play(Write(text16), run_time= 1)
        self.wait(2)
        self.play(Write(text17), run_time= 1)
        self.wait(2)
        self.play(Write(text18), run_time= 1)
        self.wait(2)
        self.play(Write(text19), run_time= 1)
        self.wait(2)


        # outro
        text20 = Tex("Thanks for watching!")
        group2 = VGroup(text3, text15, text16, text17, text18, text19)
        self.play(FadeOut(group2), run_time= 1)
        self.play(Write(text20, run_time= 2), run_time= 1)
        self.wait(3)