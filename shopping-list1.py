dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"] 
}
for keys, values in dict.items():
    print(f"Idę do {keys.capitalize()}")
    print(f"Kupuję tam {[v.capitalize() for v in values]}")
