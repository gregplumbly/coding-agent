import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    
    # Generate content using Gemini API
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    
    print("\nGemini Response:")
    print(response.text)
    
    # Print token consumption information
    if hasattr(response, 'usage_metadata') and response.usage_metadata:
        usage = response.usage_metadata
        input_tokens = usage.prompt_token_count
        output_tokens = usage.candidates_token_count
        total_tokens = usage.total_token_count
        
        print(f"  Prompt tokens: {input_tokens}")
        print(f"  Response tokens: {output_tokens}")
        print(f"  Total tokens: {total_tokens}")
    else:
        print("\nToken usage information not available")


if __name__ == "__main__":
    main()
