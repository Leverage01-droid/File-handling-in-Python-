# file_process.py
import os

INPUT = "input.txt"
OUTPUT = "output.txt"

# If input file missing, let's create a sample
if not os.path.exists(INPUT):
    print(f"{INPUT} not found.")
    create = input("Create a sample input.txt now? (yes/no): ").strip().lower()
    if create == "yes":
        sample_text = (
            "Hello"
            "i'm Bagdi, learning software development"
            "Join me at PLP academy"
            "Where we transform ideas into products, and knowledge into profession"
            "Keep practicing and you will get better every day!"
        )
        with open(INPUT, "w", encoding="utf-8") as f:
            f.write(sample_text)
        print(f"Sample {INPUT} created. Re-running will process it.")
    else:
        print("Please create 'input.txt' with at least five lines and re-run this script.")
    raise SystemExit

# Read the file
try:
    with open(INPUT, "r", encoding="utf-8") as f:
        text = f.read()
except Exception as e:
    print("Error reading input file:", e)
    raise SystemExit

# Count words 
words = text.split()
word_count = len(words)

# Convert to uppercase
upper_text = text.upper()

# Prepare output content and write to output.txt
output_content = f"WORD COUNT: {word_count}\n\n{upper_text}"

try:
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(output_content)
except Exception as e:
    print("Error writing output file:", e)
    raise SystemExit

# Success message
print(f"Success! {OUTPUT} created. Word count = {word_count}")
