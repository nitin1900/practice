#my code...almost everything copy-pasted from ai...

import math

user = input("Enter your message: ").lower()

# Step 1: normalize,copy-pasted from duck ai...
clean = [char for char in user if char.isalnum()]

# Step 2: calculate grid size,copy-pasted from duck ai...
columns = math.ceil(math.sqrt(len(clean)))
rows = math.ceil(len(clean) / columns)

# Step 3: build grid,copy-pasted from duck ai...
grid = [clean[i:i+columns] for i in range(0, len(clean), columns)]

# Step 4: read column-wise with padding,copy-pasted from duck ai and chatgpt...
result = []
for col_idx in range(columns):
    column_chars = ""
    for row_idx in range(rows):
        if row_idx < len(grid) and col_idx < len(grid[row_idx]):
            column_chars += grid[row_idx][col_idx]
        else:
            column_chars += " "   # padding
    result.append(column_chars)

# Step 5: formatted output,copy-pasted from duck ai...
print("Output:", ' '.join(result))

#solution...

def cipher_text(plain_text):
    cipher_text = ''
    plain_text = ''.join(c for c in plain_text.lower() if c.isalnum())

    r = round(len(plain_text) ** 0.5)
    if len(plain_text) > r*r:
        c = r + 1
    else:
        c = r

    for cpos in range(c):
        for step in range(r):
            try:
                cipher_text += plain_text[cpos + step*c]
            except IndexError:
                cipher_text += ' '
        cipher_text += ' '

    return cipher_text[:-1]