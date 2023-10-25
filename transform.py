import os
import openai

openai.api_key = os.getenv("key")

openai.api_key = openai_api_key

def generate_ai_news(book_title):
  user_message=f"Crie uma mensagem sobre a importância do livro '{book_title}' (max. 200 caracteres)"

  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {
        "role": "system",
        "content": "Você é um especialista em marketing editorial."
      },
      {
        "role": "user",
        "content": user_message
      }
    ]
  )

  ai_response = completion.choices[0].message['content']
  return ai_response

def access_generated_title():
  try:
      with open("generated_title.txt", "r") as file:
          generated_title = file.read()
      return generated_title
  except FileNotFoundError:
      return None

def main():
    book_title = access_generated_title()
    print(f"O título do livro gerado é: {book_title}")
    ai_response = generate_ai_news(book_title)
    print(ai_response)