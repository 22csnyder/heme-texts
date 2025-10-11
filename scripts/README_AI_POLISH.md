# AI Hematopathology Text Polishing System

This system provides Espanso text triggers specifically designed for hematopathology report writing and professional communication.

## Setup

1. Make sure your OpenAI API key is set in your environment or in the API keys file
2. Install dependencies: `uv sync`
3. Restart Espanso to load the new triggers

## Usage

### Espanso Triggers

- `::path` - Format hematopathology reports (Final Diagnosis, Clinical History, Microscopic Description)
- `::flow` - Generate complete flow cytometry reports from marker information
- `::email` - Polish emails for conciseness and professional tone

### How to Use

1. **Select text** in any application (your notes, dictation, or rough draft)
2. **Copy** the text (Cmd+C)
3. **Type the trigger** (e.g., `::path`)
4. The polished text will replace the trigger

### Direct Script Usage

```bash
# Activate virtual environment
source .venv/bin/activate

# Format pathology reports
python scripts/ai_script.py "sections show atypical cells" --style path

# Generate flow cytometry reports
python scripts/ai_script.py "CD19, CD20, CD5, kappa restriction" --style flow

# Polish emails
python scripts/ai_script.py "need to tell team case is ready" --style email
```

## Features

- **Path Style**: Converts loose notes into proper hematopathology report format
- **Flow Style**: Generates complete flow cytometry reports from marker lists
- **Email Style**: Creates concise, professional, courteous emails
- **Medical Terminology**: Uses proper hematopathology language
- **Cost-Effective**: Uses GPT-4o-mini for lower costs
- **No Meta-Commentary**: Only outputs the polished text, no explanations

## Use Cases

### ::path
- Convert dictation notes to Final Diagnosis sections
- Format clinical history from scattered notes
- Polish microscopic descriptions
- Structure auxiliary test results

### ::flow
- Generate complete flow reports from marker lists
- Fill in standard flow cytometry language
- Create proper interpretation and comment sections
- Add clinical correlation recommendations

### ::email
- Make emails more concise and professional
- Draft emails from described intentions
- Remove unnecessary words while maintaining courtesy
- Improve communication efficiency

## Configuration

The script automatically loads API keys from:
1. `.env` file in the project root
2. `/Users/christophersnyder/Library/CloudStorage/OneDrive-UW/API_KEYS/API_KEY-22csnyder`

## Troubleshooting

- If triggers don't work, restart Espanso
- If API errors occur, check your OpenAI API key
- Make sure the virtual environment is activated when running scripts directly
