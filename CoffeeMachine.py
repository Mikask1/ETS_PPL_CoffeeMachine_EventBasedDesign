from Event import OrderEvent, ReportEvent, TurnOffEvent

class CoffeeMachineSystem:
    def __init__(self, water, milk, coffee):
        self.resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }
        
        self.profit = 0

    async def handle_event(self, event):
        event.handle(self)
