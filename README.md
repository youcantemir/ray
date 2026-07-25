# Password Checker

Password Checker is a Python console application that evaluates password quality using several independent checks.

Instead of relying on a single score, the application analyzes password length, character diversity, estimated entropy and whether the password appears in a list of commonly used passwords.

## Features

- Password strength estimation
- Entropy calculation
- Dictionary lookup
- Character diversity analysis
- Text report export

## Example

Password

Winter2026!

Strength

Strong

Entropy

65.2 bits

Contains

✔ Uppercase

✔ Lowercase

✔ Numbers

✔ Symbols

Dictionary Match

No

Run

```bash
python main.py
```

