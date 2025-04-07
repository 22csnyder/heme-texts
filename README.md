# Heme-Texts

## Purpose
This is intended to assist and educate those in clinical hematopathology with note taking and specimen descriptions at a resident level and above. 



## Details
This project started in April 2025 by Chris Snyder MD PHD

## Trigger Configuration Rules
- For triggers that end with a semicolon (e.g., "hgb;"), the `word: true` property should not be included
- This is because semicolon-terminated triggers are designed to match within words, not as whole words

- For triggers that are separated by a slash (e.g., "w/o"), the `word: true` property should be included. 
- This is because the slash-separated triggers are designed to match whole words, not within words.

- For trigger / replace pairs that merely ammount to auto-capitalization with minor formatting, no slashes "/" nor semicolons ";" shall be used, and the `word: true` property should be included since "spell check" only makes sense for once the whole word is declared.

## License
This tool is provided as-is and make to claims to accuracy.
