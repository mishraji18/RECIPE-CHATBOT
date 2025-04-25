import tkinter as tk
from tkinter import messagebox

class RecipeChatbot:
    def __init__(self):
        self.recipes = {
            "pasta": {
                "ingredients": ["pasta", "tomato sauce", "cheese", "garlic", "olive oil"],
                "instructions": "Boil pasta. In a separate pan, sauté garlic in olive oil, add tomato sauce. Mix with pasta and add cheese."
            },
            "kheer": {
                "ingredients": ["Rice", "milk", "Cardamom", "butter", "sugar", "Cashew nuts", "almonds"],
                "instructions": "Boil rice in milk. Add sugar, cardamom, and nuts. Cook until thickened."
            },
            "salad": {
                "ingredients": ["lettuce", "tomatoes", "cucumber", "olive oil", "lemon juice", "salt"],
                "instructions": "Chop vegetables. Toss with olive oil, lemon juice, and salt."
            },
            "smoothie": {
                "ingredients": ["banana", "strawberries", "yogurt", "milk", "honey"],
                "instructions": "Blend all ingredients until smooth."
            },
            "daal": {
                "ingredients": ["toor dal or moong dal", "Water", "Turmeric powder", "garlic", "oil", "Salt"],
                "instructions": "Boil dal with turmeric and salt. Prepare a tadka with spices, onion, tomato, and garlic. Mix with the dal, simmer, and garnish with cilantro."
            },
            "litti": {
                "ingredients": ["whole wheat flour", "water", "salt", "ghee", "spices"],
                "instructions": "Knead dough, make small balls, fill with spiced mixture, roll out, and cook on a hot griddle."
            },
            "chokha": {
                "ingredients": ["eggplant", "potatoes", "tomatoes", "onions", "spices"],
                "instructions": "Roast vegetables, mash together with spices, and serve with litti."
            },
            "chole bhature": {
                "ingredients": ["chickpeas", "flour", "yogurt", "spices", "onions"],
                "instructions": "Soak chickpeas overnight, cook with spices. Make dough for bhature, roll out, and deep fry."
            },
            "paneer tikka": {
                "ingredients": ["paneer", "yogurt", "spices", "bell peppers", "onions"],
                "instructions": "Marinate paneer and vegetables in yogurt and spices, skewer, and grill."
            },
            "masala dosa": {
                "ingredients": ["rice", "urad dal", "potatoes", "spices", "mustard seeds"],
                "instructions": "Soak rice and dal, grind to a batter, ferment. Cook on a hot griddle, fill with spiced potatoes."
            },
            "idli": {
                "ingredients": ["rice", "urad dal", "water", "salt"],
                "instructions": "Soak rice and dal, grind to a batter, ferment. Steam in idli molds."
            },
            "samosa": {
                "ingredients": ["potatoes", "peas", "flour", "spices", "oil"],
                "instructions": "Make dough, prepare filling with spiced potatoes and peas, shape into triangles, and deep fry."
            },
            "bhel puri": {
                "ingredients": ["puffed rice", "vegetables", "tamarind chutney", "spices"],
                "instructions": "Mix puffed rice with chopped vegetables, add chutney and spices."
            },  
            "pav bhaji": {
                "ingredients": ["mixed vegetables", "butter", "pav bread", "spices"],
                "instructions": "Mash cooked vegetables with spices, serve with buttered pav bread."
            },
            "dal makhani": {
                "ingredients": ["black lentils", "butter", "cream", "spices"],
                "instructions": "Cook lentils overnight, add spices, butter, and cream. Simmer until thick."
            },
            "matar paneer": {
                "ingredients": ["paneer", "peas", "tomatoes", "spices"],
                "instructions": "Cook peas and tomatoes with spices, add paneer, simmer until done."
            },
            "sattu paratha": {
                "ingredients": ["whole wheat flour", "sattu (roasted gram flour)", "spices", "water"],
                "instructions": "Make dough, prepare filling with sattu and spices, roll out, and cook on a hot griddle."
            },
            "rasgulla": {
                "ingredients": ["chhena (paneer)", "sugar", "water", "cardamom"],
                "instructions": "Make chhena, form into balls, boil in sugar syrup flavored with cardamom."
            },
            "gulab jamun": {
                "ingredients": ["milk powder", "flour", "sugar", "ghee", "cardamom"],
                "instructions": "Make dough with milk powder and flour, shape into balls, fry in ghee, and soak in sugar syrup."
            },
            "seviyan": {
                "ingredients": ["vermicelli", "milk", "sugar", "cardamom", "nuts"],
                "instructions": "Roast vermicelli, boil in milk, add sugar and cardamom, garnish with nuts."
            },
            "puri": {
                "ingredients": ["whole wheat flour", "water", "salt", "oil"],
                "instructions": "Make dough, roll into small circles, and deep fry until puffed."
            },
            "bhindi masala": {
                "ingredients": ["okra", "onions", "spices", "oil"],
                "instructions": "Sauté okra and onions with spices until cooked."
            },
            "paneer butter masala": {
                "ingredients": ["paneer", "butter", "cream", "tomatoes", "spices"],
                "instructions": "Cook tomatoes with spices, add paneer, butter, and cream. Simmer until done."
            },
            "palak paneer": {
                "ingredients": ["spinach", "paneer", "spices", "cream"],
                "instructions": "Blanch spinach, blend to a paste, cook with spices, add paneer and cream."
            },
            "biryani": {
                "ingredients": ["rice", " vegetables", "spices", "yogurt", "onions"],
                "instructions": "Marinate vegetables, layer with rice and spices, cook on low heat until done."
            },
        }

    def get_recipe(self, dish):
        dish = dish.lower()
        if dish in self.recipes:
            recipe = self.recipes[dish]
            return f"Ingredients: {', '.join(recipe['ingredients'])}\n\nInstructions: {recipe['instructions']}"
        else:
            return "Sorry, I don't know that recipe. Please try another one."


# GUI using Tkinter
def search_recipe():
    dish_name = entry.get().strip()
    if dish_name:
        result = bot.get_recipe(dish_name)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, f"🍽 Recipe for {dish_name.capitalize()}:\n\n{result}")
    else:
        messagebox.showwarning("Input Error", "Please enter a dish name.")

# Create chatbot instance
bot = RecipeChatbot()

# Create main window
root = tk.Tk()
root.title("Recipe Chatbot")
root.geometry("680x530")
root.configure(bg="#fef9e7")  # Light creamy background

# Widgets with color
label = tk.Label(root, text="Enter a dish name:", bg="#fef9e7", fg="#2e4053", font=("Helvetica", 12, "bold"))
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 11))
entry.pack(pady=5)

search_button = tk.Button(root, text="Get Recipe", command=search_recipe, bg="#5dade2", fg="white", font=("Arial", 10, "bold"))
search_button.pack(pady=10)

text_area = tk.Text(root, wrap=tk.WORD, height=15, width=60, bg="#fdf2e9", fg="#1b2631", font=("Courier", 10))
text_area.pack(padx=10, pady=10)

# Run the GUI
root.mainloop()

