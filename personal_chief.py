from langchain_community.llms import Ollama

# 1. Lire les ingrédients
with open("ingredients.txt", "r") as f:
    ingredients = [line.strip() for line in f.readlines()]
ingredients_str = ", ".join(ingredients)

# 2. Construir le prompt
prompt = f"""
Tu es un grand chef. Voici les ingrédients disponibles : {ingredients_str}.
Propose une recette originale en utilisant uniquement ces ingrédients. 
Donne un nom à la recette, les étapes, et un conseil du chef.
"""


llm = Ollama(model="mistral")  


response = llm(prompt)

#  la réponse
print(" Recette générée :\n")
print(response)
# Sauvegarde de la recette 
with open("recette.txt", "w", encoding="utf-8") as out_file:
    out_file.write(response)

print("\n Recette enregistrée dans 'recette.txt'")