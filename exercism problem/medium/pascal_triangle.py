#my code copy-paste from ai...

def rows(num):
    # 1. Safety Check
    if num < 0:
        raise ValueError("number of rows is negative")
        
    # 2. Base Cases (The starting points)
    if num == 0:
        return []
    if num == 1:
        return [[1]]
        
    # 3. The Time Machine (Recursion)
    triangle = rows(num - 1)
    
    # 4. Grab the very last row 
    prev_list = triangle[-1]
    
    # 5. ----- YOUR ENGINE -----
    final = []
    final.append(prev_list[0])
    
    for i in range(len(prev_list) - 1):
        k = prev_list[i] + prev_list[i + 1]
        final.append(k)
        
    final.append(prev_list[-1])
    # --------------------------
    
    # 6. Attach your newly built row to the bottom
    triangle.append(final)
    
    return triangle

# --- Interactive Test ---
num = int(input("Enter the row: "))
print(rows(num))

#solution...

"""Solve Pascal's Triangle."""
def rows(row_count: int) -> list[list[int]]:
    """Return Pascal's Triangle using recursion (slow)."""
    if row_count < 0:
        raise ValueError("count must be a counting number")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    prior = rows(row_count - 1)
    return prior + [[1] + [a + b for a, b in zip(prior[-1][:-1], prior[-1][1:])] + [1]]
def fast_rows(row_count: int) -> list[list[int]]:
    """Return Pascal's Triangle efficiently."""
    out = [[1]]
    for _ in range(row_count - 1):
        out.append([1] + [a + b for a, b in zip(out[-1][:-1], out[-1][1:])] + [1])
    return out[:row_count]
  
