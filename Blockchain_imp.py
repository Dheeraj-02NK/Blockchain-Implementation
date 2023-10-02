import hashlib
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# Function to generate Hash
def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

# Create a block
class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

# Create a Blockchain
class Blockchain:
    def __init__(self):
        hashLast = hashGenerator('Vasista')
        hastStart = hashGenerator('Kashyap')
        genesis = Block('gen_data', hastStart, hashLast)
        self.chain = [genesis]

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data + prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)

def add_block_data():
    data = data_entry.get()
    if data:
        Blk_chn.add_block(data)
        data_entry.delete(0, 'end')  # Clear the input field
        update_display()

def update_display():
    output.delete(1.0, 'end')  # Clear the text widget
    for block in Blk_chn.chain:
        output.insert('end', f'Data: {block.data}\nHash: {block.hash}\nPrevious Hash: {block.prev_hash}\n\n')

Blk_chn = Blockchain()

# Create a Tkinter window
root = tk.Tk()
root.title("Blockchain App")
root.configure(background="#444444")

# Apply a custom theme using ttkthemes
style = ThemedStyle(root)
style.set_theme("equilux")

# Create a frame for adding data
data_frame = ttk.Frame(root)
data_frame.pack(pady=10)

# Create a frame for displaying the blockchain
blockchain_frame = ttk.Frame(root)
blockchain_frame.pack(padx=20, pady=10)

# Create an entry field for user input
data_label = ttk.Label(data_frame, text="Enter Data:")
data_label.grid(row=0, column=0, pady=5)

data_entry = ttk.Entry(data_frame, width=80)
data_entry.grid(row=1, column=0, padx=10, pady=10)

# Create the "Add Block" button with blue background
add_button = ttk.Button(data_frame, text="Add Data", command=add_block_data, style="Blue.TButton")
add_button.grid(row=2, column=0, padx=10, pady=10)

# Create a text widget to display the blockchain data
output = tk.Text(blockchain_frame,
                 height=10,
                 width=60,
                 wrap="none")
output.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Create the "View Blockchain" button with blue background
view_button = ttk.Button(blockchain_frame, text="View Blockchain", command=update_display, style="Blue.TButton")
view_button.grid(row=0, column=0, padx=10, pady=10)

# Create a custom style for blue buttons
style.configure("White.TButton", background="White")

root.mainloop()
