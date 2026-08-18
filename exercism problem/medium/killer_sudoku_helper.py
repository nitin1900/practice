#copy-paste from ai...

import itertools

def combinations(target, size, exclude):
    # Step 1: list candidates 1-9, exclude any numbers already in row/col/box
    candidates = [i for i in range(1, 10) if i not in exclude]
    
    # Step 2: generate all combinations of the given size
    combos = itertools.combinations(candidates, size)
    
    # Step 3: keep only combinations that sum to target
    valid_combos = [list(combo) for combo in combos if sum(combo) == target]
    
    return valid_combos

# ===== Interactive part =====
print("Welcome to Killer Sudoku Cage Solver!")
target = int(input("Enter the cage total (target sum): "))
size = int(input("Enter the number of cells in the cage: "))
exclude_input = input("Enter numbers to exclude (comma separated), or press Enter if none: ")

# Convert input to a list of integers, handle empty input
exclude = [int(x) for x in exclude_input.split(",") if x.strip().isdigit()] if exclude_input else []

# Compute valid combinations
result = combinations(target, size, exclude)

# Show output
if result:
    print(f"\nValid combinations for target {target}, size {size}, excluding {exclude}:")
    for combo in result:
        print(combo)
else:
    print(f"\nNo valid combinations found for target {target} with the given constraints.")

#solution...

import itertools

def combinations(target, size, exclude):
    candidates = [i for i in range(1, min(target, 9) + 1) if i not in exclude]
    return [list(combo) 
            for combo 
            in itertools.combinations(candidates, size)
            if sum(combo) == target]
        
