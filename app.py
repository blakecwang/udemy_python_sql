#!/usr/bin/env python

from database import add_entry, get_entries

menu = """Please select an option.
1) Add new entry
2) View entries
3) Exit

Option: """

print("Welcome to your journal!")


def prompt_new_entry():
    entry_content = input("What have you learned today?")
    entry_date = input("Enter the date:")
    add_entry(entry_content, entry_date)


def view_entries():
    entries = get_entries()
    for entry in entries:
        print(f"\ndate: {entry['date']}\ncontent: {entry['content']}\n\n")


while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()

    elif user_input == "2":
        view_entries()

    else:
        print("invalid input, please try again")

print("Goodbye! :)")
