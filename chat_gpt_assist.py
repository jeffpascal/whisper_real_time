import openai
import asyncio

openai.api_key = "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"

# Initialize a list to hold all messages
all_messages = [{
    "role": "system",
    "content": "You are a helpful assistant for the developer Jeff. Your task is to help Jeff in interview questions by answering them concisely and in a short manner. Make sure your answers are short and easy to read, and keep them to the point. If you do not detect an interview question in the text, answer it with NO QUESTION DETECTED. If it is not a technical question (a question about anything in computer science), answer it with NOT A TECHNICAL QUESTION."
}]


async def generate_corrected_transcript(temperature, transcription):
    
    # Make API call with updated messages
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=temperature,
        messages=all_messages
    )
    
    # Extract the model's response and append it to all_messages
    model_response = response['choices'][0]['message']['content']

    # If the model's response is a technical question, append it to all_messages
    if (not model_response == "NOT A TECHNICAL QUESTION"):
        all_messages.append({
            "role": "user",
            "content": transcription
        })
    
    print("generated text: " + model_response)
    return model_response
