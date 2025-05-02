import spacy
nlp = spacy.load('en_core_web_md')

# text = "SpaCy processes text efficiently."
# doc = nlp(text) # nlp is the loaded model, e.g., spacy.load("en_core_web_sm")

# # The 'doc' object contains the tokens
# print(f"Number of tokens: {len(doc)}")

# # Access individual tokens
# first_token = doc[0]
# print(f"First token: {first_token.text}")
# print(f"Is the first token alphabetic? {first_token.is_alpha}")
# print(f"Is the last token punctuation? {doc[-1].is_punct}")




#######################

# text = "Apple is looking at buying U.K. startup for $1 billion"
# doc = nlp(text)

# print("Token --- POS Tag (Simple) --- POS Tag (Detailed)")
# print("-" * 50)
# for token in doc:
#     # Print the token text, the simple POS tag, and the detailed tag
#     print(f"{token.text:<10} --- {token.pos_:<15} --- {token.tag_}")

    ###########


# text = "Apple is looking at buying U.K. startup for $1 billion in 2024."
# doc = nlp(text)

# print("Entities Found:")
# print("Text --- Label")
# print("-" * 30)
# if doc.ents:
#     for ent in doc.ents:
#         # Print the entity text and its label
#         print(f"{ent.text:<15} --- {ent.label_}")
# else:
#     print("No entities found by this model.")



#################################################

# text = "SpaCy is designed specifically for running NLP applications efficiently."
# doc = nlp(text)

# print("Token --- Lemma --- Is Stop Word?")
# print("-" * 40)
# for token in doc:
#     print(f"{token.text:<10} --- {token.lemma_:<10} --- {token.is_stop}")

# # Example: Filtering Stop Words and getting Lemmas
# filtered_lemmas = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
# print("\nFiltered Lemmas (No Stop Words, Only Alpha):")
# print(filtered_lemmas)

#################################

doc1 = nlp("I like cats")
doc2 = nlp("I like dogs")
doc3 = nlp("I like cars")

token_cat = doc1[2] # 'cats'
token_dog = doc2[2] # 'dogs'
token_car = doc3[2] # 'cars'

print(f"Similarity(cats, dogs): {token_cat.similarity(token_dog):.4f}")
print(f"Similarity(cats, cars): {token_cat.similarity(token_car):.4f}")
print(f"Similarity(dogs, cars): {token_dog.similarity(token_car):.4f}")