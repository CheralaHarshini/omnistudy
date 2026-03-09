from ai_models import model

def summarize(text):

    prompt=f"Summarize the following text:\n{text}"

    result=model(prompt,max_length=200)

    return result[0]["generated_text"]