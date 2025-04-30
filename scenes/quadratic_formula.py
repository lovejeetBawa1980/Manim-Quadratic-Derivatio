from manim import *

class QuadraticFormulaScene(Scene):
    def construct(self):
        # Set the background color
        self.camera.background_color = "1e1e1e"

        # Add the title
        title = Text("Derivation of the Quadratic Formula", font_size=48, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Display the derivation steps
        self.display_derivation_steps()

    def display_derivation_steps(self):
        steps = [
            "Consider the quadratic equation: ax^2 + bx + c = 0",
            "Divide by a: x^2 + (b/a)x + (c/a) = 0",
            "Complete the square: (x + b/2a)^2 = (b^2 - 4ac) / 4a^2",
            "Take the square root: x + b/2a = ±√((b^2 - 4ac) / 4a^2)",
            "Solve for x: x = -b/2a ± (1/2a)√(b^2 - 4ac)",
            "Final formula: x = (-b ± √(b² - 4ac)) / (2a)"
        ]

        # Display each step with a gradient color
        for i, step in enumerate(steps):
            step_text = Text(step, font_size=28, color=self.get_color_gradient(i, len(steps)))
            step_text.shift(DOWN * (i * 0.8))  # Position each step below the previous one
            self.play(Write(step_text))
            self.wait(1)

    def get_color_gradient(self, index, total_steps):
        # Generate a gradient color from BLUE to GREEN
        return interpolate_color(BLUE, GREEN, index / (total_steps - 1))