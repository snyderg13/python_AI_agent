import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    if len(sys.argv) != 2:
        print("Error: No prompt provided")
        sys.exit(1)

    user_prompt = sys.argv[1]
    print(f"User-provided prompt: {user_prompt}")
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages
    )

    print(response.text)

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")



if __name__ == "__main__":
    main()
