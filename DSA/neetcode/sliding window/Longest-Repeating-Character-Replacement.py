#copy-paste kiya yeh bhi...
class Solution:

  def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    max_freq = 0
    left = 0

    for right in range(len(s)):
      count[s[right]] = 1 + count.get(s[right], 0)
      max_freq = max(max_freq, count[s[right]])

      # If invalid, shift left by 1 to maintain current maximum window size
      if (right - left + 1) - max_freq > k:
        count[s[left]] -= 1
        left += 1

    # At the end, the maximum window size achieved is simply len(s) - left
    return len(s) - left

#this is for better understanding of code 👇:
class Solution:

  def characterReplacement(self, s: str, k: int) -> int:
    char_counts = {}
    left = 0
    longest_valid_length = 0

    for right in range(len(s)):
      # Step 1: Put the new character s[right] into our counts
      current_char = s[right]
      if current_char in char_counts:
        char_counts[current_char] += 1
      else:
        char_counts[current_char] = 1

      # Step 2: Calculate window stats right now
      window_length = right - left + 1
      most_frequent_count = max(char_counts.values())
      letters_to_replace = window_length - most_frequent_count

      # Step 3: If we need more replacements than our budget k, shrink from the left
      while letters_to_replace > k:
        left_char = s[left]
        char_counts[left_char] -= 1
        left += 1

        # Recalculate after shrinking
        window_length = right - left + 1
        most_frequent_count = max(char_counts.values())
        letters_to_replace = window_length - most_frequent_count

      # Step 4: Now this window is definitely valid, record its size if it's the biggest
      if window_length > longest_valid_length:
        longest_valid_length = window_length

    return longest_valid_length