d = {'b': 2, 'a': 1, 'c': 1}

# time complexity nlogn, space complexity n for both
sorted_with_key = dict(sorted(d.items())) 

sorted_with_values = dict(sorted(d.items(), key=lambda x:x[1]))

sorted_with_key_descending = dict(sorted(d.items(), reverse=True)) 

sorted_with_values_descending = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
print(sorted_with_key_descending)
print(sorted_with_values_descending)

print(sorted(d))