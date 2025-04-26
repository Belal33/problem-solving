# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
def aragams(word,arr):
  # res = [w  for w in arr if  set(w) == set(word) if len(w)==len(word) ]
  res = []
  for w in arr :
    if len(w)==len(word):
      if  set(w) == set(word):
        res.append(w)
  return res
print(aragams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))