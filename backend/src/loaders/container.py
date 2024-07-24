class Container():
    def __init__(self) -> None:
        self.services = {}

    def register(self, key, instance):
        print("Registered: " + key)
        self.services[key] = instance

    def resolve(self, key):
        return self.services.get(key)