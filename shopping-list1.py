dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"] 
}
for keys, values in dict.items():
    print(f"Idę do {keys.capitalize()}")
    print(f"Kupuję tam {[v.capitalize() for v in values]}")
total = 0

for i in dict:
    value = dict[i]
    count = len(value)
    total += count
  
print(f"W sumie kupuję {total} rzeczy")

#albo

print(sum(map(len, dict.values())))
