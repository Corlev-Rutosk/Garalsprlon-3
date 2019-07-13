from player import Player
import world
from collections import OrderedDict

def play():
	print("Welcome to Garalsprlon 3")
	dude = Player()
	while True:
	
		if dude.enter_city == 1:
			room = world.city_tile_at(dude.x, dude.y)
		else:
			room = world.tile_at(dude.x, dude.y)
		print (room.intro_text())
		choose_action(room, dude)

def get_available_actions(room, dude):
	actions = OrderedDict()
	if world.tile_at(room.x, room.y - 1):
		action_adder(actions, 'n', dude.move_north, "Go north")
	if world.tile_at(room.x, room.y + 1):
		action_adder(actions, 's', dude.move_south, "Go south")
	if world.tile_at(room.x + 1, room.y):
		action_adder(actions, 'e', dude.move_east, "Go east")
	if world.tile_at(room.x - 1, room.y):
		action_adder(actions, 'w', dude.move_west, "Go west")
		
	if room == world.world_map[2][2]:
		action_adder(actions, 'm', dude.enter_city, "Enter city")
		
	return actions
	
	
def action_adder(action_dict, hotkey, action, name):
	action_dict[hotkey.lower()] = action
	action_dict[hotkey.upper()] = action
	print("{}: {}".format(hotkey, name))

def choose_action(room, dude):
	action = None
	while not action:
		available_actions = get_available_actions(room, dude)
		action_input = input("Action: ")
		action = available_actions.get(action_input)
		if action:
			action()
		else:
			print("Invalid action!")
			

play()