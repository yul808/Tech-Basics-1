#%%
import time
import sys

# Typewriter effect
def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

inventory = []
inventory_limit = 5

items_in_room = [
    {"name": "Rope", "type": "tool"},
    {"name": "Apple", "type": "food"},
    {"name": "Knife", "type": "tool"},
    {"name": "Map", "type": "clue"},
    {"name": "Medicine", "type": "healing", "uses": 1},
    {"name": "Wood", "type": "material"},
    {"name": "Fire Steel", "type": "tool"},
    {"name": "Canteen", "type": "container"},
    {"name": "Banana", "type": "food"}
]

def show_room_items():
    if not items_in_room:
        typewriter("There are no items here.")
    else:
        typewriter("You see:")
        for item in items_in_room:
            typewriter(f"- {item['name']} ({item['type']})")

def show_inventory():
    if not inventory:
        typewriter("Your inventory is empty.")
    else:
        typewriter("Inventory:")
        for item in inventory:
            typewriter(f"- {item['name']} ({item['type']})")

def pick_up(item_name):
    if len(inventory) >= inventory_limit:
        typewriter("Your inventory is full. Drop something first.")
        return
    for item in items_in_room:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            items_in_room.remove(item)
            typewriter(f"You picked up the {item['name']}.")
            return
    typewriter("Item not found.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            items_in_room.append(item)
            typewriter(f"You dropped the {item['name']}.")
            return
    typewriter("You don't have that item.")

def use(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] == "healing":
                typewriter("You used the medicine and feel better.")
                inventory.remove(item)
            elif item["type"] == "food":
                typewriter("You ate the food. Energy restored.")
                inventory.remove(item)
            else:
                typewriter(f"You can't use the {item['name']} like that.")
            return
    typewriter("You don't have that item.")

def examine(item_name):
    for item in inventory + items_in_room:
        if item["name"].lower() == item_name.lower():
            typewriter(f"It's a {item['type']} item named {item['name']}.")
            return
    typewriter("There's nothing like that to examine.")

def make_fire():
    has_wood = any(item["name"].lower() == "wood" for item in inventory)
    has_steel = any(item["name"].lower() == "fire steel" for item in inventory)
    if has_wood and has_steel:
        typewriter("You strike the Fire Steel against the Wood and start a warm fire!")
        # Remove used items
        inventory[:] = [item for item in inventory if item["name"].lower() not in ["wood", "fire steel"]]
    else:
        typewriter("You need both Wood and Fire Steel to make a fire.")

def show_help():
    typewriter("""
Available commands:
- inventory : Show your inventory
- pickup [item] : Pick up an item
- drop [item] : Drop an item
- use [item] : Use an item (if usable)
- examine [item] : Learn more about an item
- look : See items in the area
- make fire : Start a fire using Wood and Fire Steel
- help : Show this help
- quit : Exit the game
""".strip())

def game_loop():
    typewriter("🔥 Welcome to Jungle Explorer! 🔥")
    typewriter("You have just crash landed in an unknown jungle. You better start preparing for the night!")
    typewriter("Type 'help' to see your options.\n")
    while True:
        command = input("> ").strip().lower()
        if command == "help":
            show_help()
        elif command == "inventory":
            show_inventory()
        elif command.startswith("pickup "):
            pick_up(command[7:])
        elif command.startswith("drop "):
            drop(command[5:])
        elif command.startswith("use "):
            use(command[4:])
        elif command.startswith("examine "):
            examine(command[8:])
        elif command == "look":
            show_room_items()
        elif command == "make fire":
            make_fire()
        elif command == "quit":
            typewriter("Goodbye, explorer! Stay safe out there.")
            break
        else:
            typewriter("Unknown command. Type 'help' for options.")

# Start the game loop
if __name__ == "__main__":
    game_loop()

#%%
