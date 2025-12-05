

class ClassifierAgent:
    def __init__(self, categories):
        self.categories = categories

    def classify(self, file_name):
        # Simple classification logic based on file extension
        extension = file_name.split('.')[-1].lower()
        for category, extensions in self.categories.items():
            if extension in extensions:
                return category
        return "Uncategorized"