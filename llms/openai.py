from openai import OpenAI
from openai.types.chat import ChatCompletion
from settings import settings

api_key = settings.API_LLM_KEY
client = OpenAI(api_key=api_key)


def generate_response(prompt) -> ChatCompletion:
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=200
        )
        print(">>>>>>>>>>", response)
        return response

    except Exception as e:
        print(f"An error occurred: {e}")
        return None



