from transformers import pipeline

model = pipeline(
"text2text-generation",
model="google/flan-t5-base"
)