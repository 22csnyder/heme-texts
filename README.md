# Heme-Texts

## Purpose
This is intended to assist and educate those in clinical hematopathology with note taking and specimen descriptions at a resident level and above. 

## TODO 
  - [ ] regex matching for 34f -> 34-year-old female
  - [ ] regex matching for 15m -> 15-year-old male




## Details
This project started in April 2025 by Chris Snyder MD PHD

Presently, heme-texts/ is symbolic link to $ESPANSO_CONFIG/match/heme-texts/.

## Trigger Configuration Rules
- For triggers that end with a semicolon (e.g., "hgb;"), the `word: true` property should not be included
- This is because semicolon-terminated triggers are designed to match within words, not as whole words

- For triggers that are separated by a slash (e.g., "w/o"), the `word: true` property should be included. 
- This is because the slash-separated triggers are designed to match whole words, not within words.

- For trigger / replace pairs that merely ammount to auto-capitalization with minor formatting, no slashes "/" nor semicolons ";" shall be used, and the `word: true` property should be included since "spell check" only makes sense for once the whole word is declared.

## Age and Gender Regex Pattern
The following regex patterns are used for age and gender matching:

1. Standard format (verbose):
```
(\d{1,3})-?(?:year-?old|yo)\s+(?:male|female|m|f)
```

2. Concise format (naked):
```
\b(\d{1,3})([mf])\b
```

3. Bracketed format (safest):
```
:(\d{1,3})([mf]):
```

Examples that will match:
- Standard: `34-year-old female`, `34 year old female`, `34yo female`
- Naked: `34f`, `15m`
- Bracketed: `:34f:`, `:15m:`

Examples that will NOT match:
- `34female` (no space)
- `34 f` (space between)
- `34-year-old` (missing gender)
- `female 34` (wrong order)
- `1234f` (too many digits)
- `34x` (invalid gender)

## License
This tool is provided as-is and make to claims to accuracy.
