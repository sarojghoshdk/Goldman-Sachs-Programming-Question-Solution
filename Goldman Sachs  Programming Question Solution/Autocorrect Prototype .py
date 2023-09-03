from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    
    return anagram_groups

def getSearchResults(words, queries):
    anagram_groups = group_anagrams(words)
    result = []

    for query in queries:
        sorted_query = ''.join(sorted(query))
        
        if sorted_query in anagram_groups:
            anagrams = sorted(anagram_groups[sorted_query])
            result.append(anagrams)
    
    return result

# Example usage:
n = 6
words = ["allot", "cat", "peach", "dusty", "act", "cheap"]
q = 3
queries = ["tac", "study", "peahc"]
results = getSearchResults(words, queries)
for r in results:
    print(r)
