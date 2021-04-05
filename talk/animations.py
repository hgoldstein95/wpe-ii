from manim import *  # pylint: disable=unused-wildcard-import


config.background_color = WHITE

ACM_BLUE = "#0055C9"


class ReportTex(MathTex):
    KEYWORDS = ["shift", "of", "reset", "let", "in"]

    def __init__(self, *tex_strings, **kwargs):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{xcolor}")
        template.add_to_preamble(r"\usepackage[T1]{fontenc}")
        template.add_to_preamble(r"\usepackage[libertine]{newtxmath}")
        template.add_to_preamble(r"\usepackage[tt=false]{libertine}")
        template.add_to_preamble(
            r"\definecolor[named]{ACMDarkBlue}{cmyk}{1,0.58,0,0.21}"
        )

        super().__init__(*tex_strings, tex_template=template, color=BLACK, **kwargs)

        for keyword in self.KEYWORDS:
            self.set_color_by_tex(r"\textsf{" + keyword + r"}", ACM_BLUE)


class ShiftResetExample(Scene):
    def construct(self):

        tex = ReportTex(r"\textsf{let}", "~x = 4~", r"\textsf{in}", "~x + 3")
        self.add(tex)

        self.wait(3)
