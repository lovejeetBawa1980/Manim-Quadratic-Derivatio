# Manim Quadratic Formula Project

This project demonstrates the derivation of the quadratic formula using Manim, a mathematical animation engine. The animations are designed to be smooth and visually appealing, featuring elegant color gradients.

## Project Structure

- `scenes/quadratic_formula.py`: Contains the main scene for the Manim project, defining the `QuadraticFormulaScene` class which handles the setup and animations for the quadratic formula derivation.
- `assets/fonts`: Directory for custom font files used in the animations.
- `assets/images`: Directory for images used in the animations.
- `requirements.txt`: Lists the dependencies required for the project, including the Manim library.
- `manim.cfg`: Configuration settings for Manim, specifying options such as output directory and resolution.

## Installation

To set up the project, ensure you have Python installed, then install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Animations

To run the animations, navigate to the project directory and use the following command:

```bash 
manim -pql scenes/quadratic_formula.py QuadraticFormulaScene

```

This command will render the `QuadraticFormulaScene` in low quality and open the output video file.

## Overview of the Quadratic Formula

The quadratic formula is used to find the roots of a quadratic equation of the form:
\[ ax^2 + bx + c = 0 \]

The formula is given by:

\[ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \]

This project visually explains the derivation of this formula step by step, enhancing understanding through animations. 