from ai_models import model

def generate_questions(text):

    prompt=f"""
Generate 5 quiz questions from this topic.

{text}
"""

    result=model(prompt,max_length=200)

    return result[0]["generated_text"]