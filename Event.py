class Event:
    def __init__(self, name):
        self.name = name
    
    def handle(self, subscriber):
        pass

class OrderEvent(Event):
    def __init__(self, coffee_type):
        super().__init__("OrderEvent")
        self.coffee_type = coffee_type

    def handle(self, subscriber):
        if self.coffee_type == "Espresso":
            subscriber.resources["water"] -= 50
            subscriber.resources['coffee'] -= 30
            subscriber.profit += 2
        elif self.coffee_type == "Latte":
            subscriber.resources["water"] -= 100
            subscriber.resources['coffee'] -= 30
            subscriber.resources['milk'] -= 50
            subscriber.profit += 3
        elif self.coffee_type == "Cappuccino":
            subscriber.resources["water"] -= 100
            subscriber.resources['coffee'] -= 30
            subscriber.resources['milk']  -= 50
            subscriber.profit += 3.5

class ReportEvent(Event):
    def __init__(self):
        super().__init__("ReportEvent")
    
    def handle(self, subscriber):
        print("Water level:", subscriber.resources["water"])
        print("Coffee level:", subscriber.resources["coffee"])
        print("Milk level:", subscriber.resources["milk"])
        print("Profit generated:", subscriber.profit)

class TurnOffEvent(Event):
    def __init__(self):
        super().__init__("TurnOffEvent")
    
    def handle(self, subscriber):
        print("Turning off...")
        
class EventBus:
    def __init__(self):
        self.subscribers = {}

    def add_listener(self, event_type, subscriber):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)

    async def publish(self, event):
        event_type = event.name
        if event_type in self.subscribers:
            for subscriber in self.subscribers[event_type]:
                await subscriber.handle_event(event)