"""One Line, One Laugh — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: my smart speaker heard me talking in my sleep and keeps bringing it up.
TEXT = "My smart speaker heard me talking in my sleep and now it will not stop bringing it up at breakfast."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
