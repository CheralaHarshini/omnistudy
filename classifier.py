from ai_models import model

def classify(text):

    prompt=f"""
Classify this text as one of these:
notes
medical
legal

{text}
"""

    result=model(prompt,max_length=10)

    return result[0]["generated_text"]