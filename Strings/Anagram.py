def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)  # Simple sort


from collections import Counter
def are_anagrams_count(s1, s2):
    return Counter(s1) == Counter(s2)

print(are_anagrams("listen", "silent"))  # True