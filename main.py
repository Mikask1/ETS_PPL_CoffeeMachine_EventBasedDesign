import asyncio
from CoffeeMachine import CoffeeMachineSystem
from Event import EventBus, OrderEvent, ReportEvent, TurnOffEvent

async def main():
    coffee_machine = CoffeeMachineSystem(water=300, milk=200, coffee=100)
    event_dispatcher = EventBus()

    event_dispatcher.add_listener("OrderEvent", coffee_machine)
    event_dispatcher.add_listener("ReportEvent", coffee_machine)
    event_dispatcher.add_listener("TurnOffEvent", coffee_machine)

    await event_dispatcher.publish(ReportEvent())
    await event_dispatcher.publish(OrderEvent("Espresso"))
    await event_dispatcher.publish(OrderEvent("Latte"))
    await event_dispatcher.publish(ReportEvent())
    await event_dispatcher.publish(TurnOffEvent())

if __name__ == "__main__":
    asyncio.run(main())
