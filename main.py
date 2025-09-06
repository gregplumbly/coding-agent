import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    parser.add_argument("prompt", help="The prompt to send to the model")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    # Parse arguments
    args = parser.parse_args()
    prompt = args.prompt
    verbose = args.verbose
    
    # Create messages list with user prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    if verbose:
        print(f"User prompt: {prompt}")
    
    # Generate content using Gemini API
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    
    print("\nGemini Response:")
    print(response.text)
    
    # Print token consumption information only if verbose
    if verbose and hasattr(response, 'usage_metadata') and response.usage_metadata:
        usage = response.usage_metadata
        input_tokens = usage.prompt_token_count
        output_tokens = usage.candidates_token_count
        
        print(f"Prompt tokens: {input_tokens}")
        print(f"Response tokens: {output_tokens}")


if __name__ == "__main__":
    main()
