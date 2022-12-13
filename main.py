from tkinter import *
from tkinter.ttk import Treeview

# create the root window
root = Tk()

# create a dictionary to store the items and their corresponding values
items = {}

# create a list to store the items
item_list = []

# create a Treeview to display the items and their values
treeview = Treeview(root, columns=("value",))
treeview.heading("#0", text="Item Name")
treeview.heading("value", text="Value")
treeview.pack()


# def edit():
#     x = treeview.get_children()
#     for item in x: ## Changing all children from root item
#         treeview.item(item, text="blub", values=("foo", "bar"))

def delete():
    selected_item = treeview.selection()[0]  ## get selected item
    item_dict = treeview.item(selected_item)
    print(item_dict)
    del items[item_dict['text']]

    index = treeview.index(selected_item)
    # remove the item from the list of item names
    del item_list[index]

    treeview.delete(selected_item)


# function to add a new item to the dictionary, the list, and the Treeview
def add_item():
    # get the item name and value from the Entry widgets
    item_name = item_name_entry.get()
    item_value = int(item_value_entry.get())

    # add the item to the dictionary and the list
    items[item_name] = item_value
    item_list.append(item_name)

    # add the item to the Treeview
    treeview.insert("", END, text=item_name, values=(item_value,))

    # create a button to remove the item
    remove_button = Button(treeview, text="Remove", command=lambda index=len(item_list) - 1: remove_item(index))
    # treeview.insert("", END, text="", remove_button)


# function to calculate the sum of the values in the dictionary
def calc_sum():
    sum = 0
    for item in items:
        sum += items[item]
    sum_text = str(sum)
    sum_label.configure(text=sum_text)


# create a function to remove an item from the Listbox and the dictionary
def remove_item(index):
    # get the name of the item to be removed
    item_name = item_list[index]

    # delete the item from the Listbox
    treeview.delete(index)

    # remove the item from the dictionary
    del items[item_name]

    # remove the item from the list of item names
    del item_list[index]


# create a label and Entry widget for the item name
item_name_label = Label(root, text="Item Name:")
item_name_label.pack()
item_name_entry = Entry(root)
item_name_entry.pack()

# create a label and Entry widget for the item value
item_value_label = Label(root, text="Item Value:")
item_value_label.pack()
item_value_entry = Entry(root)
item_value_entry.pack()

# create a button to add a new item
add_button = Button(root, text="Add Item", command=add_item)
add_button.pack()

# create a button to calculate the sum of the values
sum_button = Button(root, text="Calculate Sum", command=calc_sum)
sum_button.pack()

button_del = Button(root, text="del", command=delete)
button_del.pack()
# button_del = Button(root, text="edit", command=edit)
# button_del.pack()

# create a label to display the sum
sum_label = Label(root, text="sum")
sum_label.pack()

# run the main loop
root.mainloop()
