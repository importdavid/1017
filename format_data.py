# This program takes output from the gpt3 playground, formats it like json, and copies it to the clipboard
import pyperclip

with open('datalist.txt', 'r') as data:
    # Remove new lines
    lines = [s.strip('\n') for s in data.readlines()]
    # Remove any blank lines
    lines = [s for s in lines if s != '']
    # Isolate text from numbering
    lines = [f"{s.split('.')[1].lstrip()}. " for s in lines]
    # Insert "Atlas" when appropriate
    lines = [s.replace("A cat", "Atlas") for s in lines]
    # Format to json style
    lines = [f'"{s}",' for s in lines]
    # Remove final comma
    lines[-1] = lines[-1].strip(',')

    # Print json object and copy to clipboard
    clip = "[\n"
    for s in lines: 
        clip += (f"    {s}\n")
    clip += ']'
    pyperclip.copy(clip)