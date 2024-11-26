import tkinter as tk
from tkinter import simpledialog, messagebox
from algorithm import Network
from visualization import NetworkVisualizer

class NetworkGUI:
    def __init__(self):
        self.network = Network()
        self.visualizer = None

        # Create the main Tkinter window
        self.root = tk.Tk()
        self.root.title("Distance Vector Algorithm Simulator")
        self.root.configure(bg="#FF6347")  # Set background color to red
        self.root.geometry("500x500")  # Size of the window

        # Set up the user interface elements
        self.setup_ui()

    def setup_ui(self):
        button_style = {
            "bg": "#FF7F7F",  # Light red for buttons
            "fg": "white",
            "font": ("Arial", 12),
            "relief": "raised",
            "bd": 2,
            "width": 20,
        }

        # Main frame inside the window for organization
        self.main_frame = tk.Frame(self.root, bg="#D3D3D3")  # Grayish white background
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Buttons for interaction
        tk.Button(self.main_frame, text="Add Node", command=self.add_node, **button_style).pack(pady=10)
        tk.Button(self.main_frame, text="Add Link", command=self.add_link, **button_style).pack(pady=10)
        tk.Button(self.main_frame, text="Run Algorithm", command=self.run_algorithm, **button_style).pack(pady=10)
        tk.Button(self.main_frame, text="Visualize Network", command=self.visualize_network, **button_style).pack(pady=10)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit, **button_style).pack(pady=10)

    def add_node(self):
        node_name = simpledialog.askstring("Add Node", "Enter the name of the new node:")
        if node_name:
            self.network.add_node(node_name)
            messagebox.showinfo("Success", f"Node '{node_name}' added successfully!")

    def add_link(self):
        node1 = simpledialog.askstring("Add Link", "Enter the first node:")
        node2 = simpledialog.askstring("Add Link", "Enter the second node:")
        cost = simpledialog.askfloat("Add Link", "Enter the cost of the link:")

        if node1 and node2 and cost is not None:
            try:
                self.network.add_link(node1, node2, cost)
                messagebox.showinfo("Success", f"Link added between '{node1}' and '{node2}' with cost {cost}!")
            except KeyError:
                messagebox.showerror("Error", "One or both nodes do not exist. Please add them first.")

    def run_algorithm(self):
        self.network.initialize_routing()
        self.network.run_distance_vector()
        messagebox.showinfo("Simulation Complete", "The Distance Vector Algorithm has completed.")

    def visualize_network(self):
        if not self.visualizer:
            self.visualizer = NetworkVisualizer(self.network)
        self.visualizer.update_and_draw()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NetworkGUI()
    app.run()
