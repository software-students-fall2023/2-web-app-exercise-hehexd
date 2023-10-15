class Event:
    #event_type, title, time, quantity, description,category]
    def __init__(self, properties):
        self.type = properties[0]
        self.title = properties[1]
        self.time = properties[2]
        self.quantity = properties[3]
        self.description = properties[4]
        self.category = properties[5]
    def is_category(self, category):
        return self.category.lower() == category.lower()
    