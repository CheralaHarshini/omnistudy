from ai_models import model

def analyze_medical(text):

    prompt=f"""
Explain the medical report or symptoms.

{text}

Include:
possible condition
precautions
"""

    result=model(prompt,max_length=300)

    return result[0]["generated_text"]