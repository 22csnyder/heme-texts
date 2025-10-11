#!/usr/bin/env python3
"""
AI Text Polishing Script
Usage: python ai_script.py "your text here" [--style STYLE]
"""

import argparse
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import openai

# Load environment variables
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Also try loading from the API keys directory
api_key_path = "/Users/christophersnyder/Library/CloudStorage/OneDrive-UW/API_KEYS/API_KEY-22csnyder"
if os.path.exists(api_key_path):
    load_dotenv(dotenv_path=api_key_path)

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_polish_prompt(text, style="path"):
    """Generate the appropriate prompt based on style preference."""
    
    base_prompts = {
        "path": """
You are a hematopathologist assistant. Rewrite the following text into proper hematopathology report format. This could be a Final Diagnosis section, Clinical History section, Microscopic Description section, or auxiliary test results.

Use professional pathology language with:
- Precise medical terminology
- Neutral, objective tone
- Standard pathology report structure
- Proper formatting for the section type
- Clinical correlation recommendations where appropriate

Do NOT include any explanatory text, comments, or meta-commentary. Only output the polished report text.

Text to format:
""",
        "flow": """
You are a hematopathologist assistant specializing in flow cytometry reports. Generate a complete flow cytometry report based on the provided markers and information.

Format as a professional flow cytometry report with:
- Clear Interpretation section
- Detailed Comment section with immunophenotype description
- Clinical correlation recommendations
- Proper medical terminology for flow cytometry
- Standard report structure like the examples provided

If only partial marker information is provided, fill in reasonable additional markers and create a complete report. Use the standard flow cytometry report format.

Do NOT include any explanatory text, comments, or meta-commentary. Only output the complete flow cytometry report.

Text to format:
""",
        "email": """
You are a professional email assistant. Rewrite the following text into a concise, professional, and courteous email.

Focus on:
- Making it concise and to the point
- Professional and courteous tone
- Clear communication
- Removing unnecessary words
- Appropriate email etiquette

If the text describes what the user wants to communicate but lacks proper wording, draft a complete email based on the described intention.

Do NOT include any explanatory text, comments, or meta-commentary. Only output the polished email text.

Text to format:
"""
    }
    
    return base_prompts.get(style, base_prompts["path"]) + f"\n\n{text}"

def polish_text(text, style="path"):
    """Use OpenAI to polish the given text."""
    try:
        prompt = get_polish_prompt(text, style)
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using the more cost-effective model
            messages=[
                {"role": "system", "content": "You are a hematopathologist assistant that helps format medical reports and communications."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,  # Increased for longer reports
            temperature=0.2  # Lower temperature for more consistent medical output
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Polish hematopathology text using AI")
    parser.add_argument("text", help="Text to polish")
    parser.add_argument("--style", choices=["path", "flow", "email"], 
                       default="path", help="Style of polishing")
    
    args = parser.parse_args()
    
    if not args.text.strip():
        print("Error: No text provided to polish")
        sys.exit(1)
    
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables")
        sys.exit(1)
    
    polished_text = polish_text(args.text, args.style)
    print(polished_text)

if __name__ == "__main__":
    main()
