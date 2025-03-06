import spacy
import re
from transformers import pipeline

# Load spaCy model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# Load Hugging Face text-generation model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def extract_named_entities(text):
    """Extract named entities from the text to create better MCQs."""
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents if ent.label_ in ["PERSON", "ORG", "GPE", "DATE"]]
    return entities

def clean_generated_mcq(text):
    """Extract the MCQ from the generated response."""
    # Regular expression to extract the question and options
    match = re.search(r"(.*?)[\n:]?\s*(A\..*?|a\..*?)\n?(B\..*?|b\..*?)\n?(C\..*?|c\..*?)\n?(D\..*?|d\..*?)", text, re.DOTALL)
    if match:
        question = match.group(1).strip()
        options = [match.group(i).strip() for i in range(2, 6)]
        return f"{question}\n\nOptions:\n{options[0]}\n{options[1]}\n{options[2]}\n{options[3]}"
    return text  # Fallback if regex fails

def generate_mcqs(text):
    """Generate multiple-choice questions using named entities and Hugging Face model."""
    entities = extract_named_entities(text)
    mcqs = []

    if not entities:
        return ["No relevant entities found for MCQ generation."]

    for entity in entities:
        prompt = (
            f"Generate a multiple-choice question about '{entity}' from this text: {text}\n"
            f"Provide 4 answer choices labeled A, B, C, and D. Mark the correct answer."
        )
        response = generator(prompt, max_length=150, num_return_sequences=1)

        # Clean the generated text
        mcq_text = clean_generated_mcq(response[0]['generated_text'].strip())
        mcqs.append(mcq_text)

    return mcqs
