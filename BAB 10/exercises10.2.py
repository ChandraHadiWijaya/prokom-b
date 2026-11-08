from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'
contents = path.read_text()

print("--- Mengganti Kata 'Python' Menjadi 'C' ---")
modified_contents = contents.replace('Python', 'C')
print(modified_contents)
