"""
Financial quiz containing elementary multiplication exercies.
"""

import random

import jinja2

from quiz_generator.ranged_question import RangedQuestion
from quiz_generator.input_variation import Variation
from quiz_generator.quiz import Quiz

# Financial Literacy Questions

inputs = {"x": Variation(random.sample(range(15), 5))}

def multiplication_answer_function(input_values):
    return {"answer": 3 * input_values['x']}

three_times_questions = RangedQuestion(
    question_template=jinja2.Template("3 \\times {{x}} = ?"),
    answer_template=jinja2.Template("{{answer}}"),
    inputs=inputs,
    answer_generation_function=multiplication_answer_function
)

quiz_version1 = Quiz(
    questions=three_times_questions.create_all_questions(),
    quiz_name="Financial Comprehension Quiz",
    quiz_version="1",
    preamble="Questions to improve financial educational and literacy. ",
)

print(quiz_version1.render())
print(quiz_version1.create_marking_sheet())
