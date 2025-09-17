# === MODEL ===
class Recipe:
    def __init__(self, title, author, recipe_type, description, video_url, ingredients, cuisine):
        self.title = title
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_url = video_url
        self.ingredients = ingredients  # список строк
        self.cuisine = cuisine

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def update_description(self, new_description):
        self.description = new_description

    def update_video_url(self, new_url):
        self.video_url = new_url