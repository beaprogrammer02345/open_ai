import openai
import os

# Load the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
import os

api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print("API Key is set.")
else:
    print("API Key is NOT set.")

def call_openai_api():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the updated model
            messages=[
                {"role": "user", "content": "Who is the most famous chess player?"}
            ],
            max_tokens=50
        )
        return response['choices'][0]['message']['content'].strip()  # Updated response structure
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Call the API function and print the result
result = call_openai_api()
if result:
    print(result)
else:
    print("Failed to get a response.")
