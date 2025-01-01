import sys
import os


def main():
	splash_screen()
	blocks = initialize_blocks()

	while True:
		clear_console()

		display_menu()
		choice = get_user_choice()

		if choice == 1:
			display_blocks(blocks)
			input("Press Enter to return to the menu...")
		elif choice == 2:
			search_block(blocks)
		elif choice == 3:
			add_block(blocks)
		elif choice == 4:
			delete_block(blocks)
		elif choice == 5:
			sort_blocks(blocks)
		elif choice == 6:
			print("Exiting BlockWorks. Goodbye!")
			sys.exit()


def splash_screen():
	clear_console()
	print("=" * 50)
	print("\033[1;37;41m              Welcome to BlockWorks               \033[0m")
	print("=" * 50)
	print("\033[1;36m  A Program for Managing Blocks and Components  \033[0m")
	print("\n\033[1;33m  Loading...\033[0m")
	print("=" * 50)
	input("Press Enter to continue to the main menu...")


def display_menu():
	print("=" * 30)
	print("\033[1;37;41m    BlockWorks Main Menu      \033[0m")
	print("=" * 30)

	print("\033[36m1. View All Blocks\033[0m")
	print("\033[36m2. Search Blocks\033[0m")
	print("\033[36m3. Add Blocks\033[0m")
	print("\033[36m4. Delete Blocks\033[0m")
	print("\033[36m5. Sort Blocks\033[0m")
	print("\033[1;36m6. Exit\033[0m")

	print("=" * 30)


def get_user_choice():
	while True:
		try:
			choice = int(input("Enter your choice: "))
			if 1 <= choice <= 6:
				return choice
			else:
				print("Invalid choice. Please choose a number between 1 and 6.")
		except ValueError:
			print("Invalid input. Please enter a number.")


def clear_console():
	if os.name == 'nt':  # Windows
		os.system('cls')
	else:
		os.system('clear')  # Linux


def confirm_action(prompt="Are you sure? (yes/no): "):
	while True:
		user_input = input(prompt).strip().lower()
		if user_input == "yes":
			return True
		elif user_input == "no":
			return False
		else:
			print("Invalid input. Please enter 'yes' or 'no'.")


def display_blocks(blocks):
	clear_console()

	print("=" * 30)
	print("\033[1;37;41m         Block List           \033[0m")
	print("=" * 30)

	if not blocks:
		print("No blocks available.")
	else:
		for block in blocks:
			print(f"Block: \033[1;33m{block['name']}\033[0m")
			print("-" * 30)
			for component, quantity in block['components'].items():
				print(f"  \033[36m{component}\033[0m: \033[32m{quantity}\033[0m")
			print("=" * 30)


def search_block(blocks):
	search_term = input("Enter the name of the block or a component to search: ").lower()
	found_blocks = []

	for block in blocks:
		if search_term in block['name'].lower():
			found_blocks.append(block)

	if found_blocks:
		display_blocks(found_blocks)
		input("Press Enter to return to the menu...")
	else:
		input("No matching blocks found. Press Enter to return to the menu...")


def add_block(blocks):
	available_components = [
		"Steel Plates", "Motors", "Computers", "Display",
		"Construction Components", "Large Steel Tube", "Small Steel Tube", "Power Cells",
		"Reactor Components", "Interior Plates", "Medical Components"
	]

	block_name = input("Enter the name of the new block: ").strip()

	if not block_name:
		print("Block name cannot be empty. Please try again.")
		input("Press Enter to return to the menu...")
		return blocks

	if any(block['name'].lower() == block_name.lower() for block in blocks):
		print(f"A block with the name '{block_name}' already exists. Please enter a unique name.")
		input("Press Enter to return to the menu...")
		return blocks

	components = {}

	for component in available_components:
		while True:
			try:
				quantity = int(input(f"Enter the quantity for {component}: ").strip())

				if quantity < 0:
					print("Quantity cannot be negative. Please try again.")
					continue

				if quantity > 0:
					components[component] = quantity
				break
			except ValueError:
				print("Please enter a valid number for the quantity.")

	if not components:
		print("No components entered for this block. The block will not be added.")
		input("Press Enter to return to the menu...")
		return blocks

	new_block = {
		"name": block_name,
		"components": components
	}

	display_blocks([new_block])

	if confirm_action("Do you want to add this block to the list? (yes/no): "):
		blocks.append(new_block)
		print(f"Block '{block_name}' has been added successfully.")
	else:
		print("Block was not added.")

	input("Press Enter to return to the menu...")
	return blocks


def delete_block(blocks):
	block_name = input("Enter the exact name of the block to delete: ").strip()

	if not block_name:
		print("Block name cannot be empty. Please try again.")
		input("Press Enter to return to the menu...")
		return blocks

	found_block = None
	for block in blocks:
		if block_name.strip().lower() == block['name'].lower():
			found_block = block
			break

	if found_block:
		display_blocks([found_block])

		if confirm_action(f"Are you sure you want to delete the block '{found_block['name']}'? (yes/no): "):
			blocks.remove(found_block)
			print(f"Block '{found_block['name']}' has been deleted.")
		else:
			print("Block not deleted.")
	else:
		print(f"No block found with the exact name '{block_name}'.")

	input("Press Enter to return to the menu...")
	return blocks


def sort_blocks(blocks):
	print("Choose sort order:")
	print("1. Ascending (A-Z)")
	print("2. Descending (Z-A)")

	choice = input("Enter your choice: ").strip()

	if choice == "1":
		sorted_blocks = sorted(blocks, key=lambda block: block['name'].lower())
	elif choice == "2":
		sorted_blocks = sorted(blocks, key=lambda block: block['name'].lower(), reverse=True)
	else:
		input("Press Enter to return to the menu...")
		return

	display_blocks(sorted_blocks)
	input("Press Enter to return to the menu...")


def initialize_blocks():
	blocks = [
		{
			"name": "Assembler",
			"components": {
				"Steel Plates": 10,
				"Motors": 5,
				"Computers": 5,
				"Display": 3,
				"Construction Components": 20,
				"Large Steel Tube": 1
			}
		},
		{
			"name": "Reactor (Small)",
			"components": {
				"Steel Plates": 20,
				"Power Cells": 10,
				"Computers": 5,
				"Construction Components": 5,
				"Reactor Components": 1
			}
		},
		{
			"name": "Large Cargo Container",
			"components": {
				"Steel Plates": 60,
				"Construction Components": 10,
				"Interior Plates": 5,
				"Motors": 4,
				"Large Steel Tubes": 2,
				"Computers": 1
			}
		},
		{
			"name": "Oxygen Generator",
			"components": {
				"Steel Plates": 15,
				"Computers": 5,
				"Interior Plates": 2,
				"Motors": 5,
				"Large Steel Tube": 1,
				"Construction Components": 5
			}
		},
		{
			"name": "Medbay",
			"components": {
				"Steel Plates": 100,
				"Computers": 10,
				"Motors": 10,
				"Construction Components": 5,
				"Medical Components": 5,
				"Display": 5,
				"Interior Plates": 3
			}
		}
	]

	return blocks


if __name__ == '__main__':
	main()
