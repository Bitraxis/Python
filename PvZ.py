import tkinter as tk


class DraggableLabel(tk.Label):
    def __init__(self, parent, text, grid_cells):
        super().__init__(parent, text=text, bg="lightblue", padx=5, pady=5)
        self.grid_cells = grid_cells
        self.bind("<Button-1>", self.start_drag)
        self.bind("<B1-Motion>", self.drag)
        self.bind("<ButtonRelease-1>", self.stop_drag)
        self.dragging = False

    def start_drag(self, event):
        self.dragging = True
        self.x_offset = event.x
        self.y_offset = event.y
        self.tkraise()  # Ensure the widget is brought to the top when dragging

    def drag(self, event):
        if self.dragging:
            self.place(x=event.x_root - self.master.winfo_rootx() - self.x_offset,
                       y=event.y_root - self.master.winfo_rooty() - self.y_offset)
            self.highlight_grid()

    def stop_drag(self, event):
        self.dragging = False
        self.snap_to_grid()

    def highlight_grid(self):
        widget_x = self.winfo_x()
        widget_y = self.winfo_y()

        # Reset all grid cells to default color first
        for cell in self.grid_cells:
            cell.configure(bg="lightgrey")

        # Highlight the closest cell
        closest_cell = None
        closest_distance = float('inf')
        for cell in self.grid_cells:
            cell_x, cell_y = cell.winfo_x(), cell.winfo_y()
            distance = ((widget_x - cell_x) ** 2 + (widget_y - cell_y) ** 2) ** 0.5
            if distance < closest_distance:
                closest_distance = distance
                closest_cell = cell

        if closest_cell:
            closest_cell.configure(bg="lightgreen")

    def snap_to_grid(self):
        widget_x = self.winfo_x()
        widget_y = self.winfo_y()
        closest_cell = None
        closest_distance = float('inf')

        # Find the closest grid cell
        for cell in self.grid_cells:
            cell_x, cell_y = cell.winfo_x(), cell.winfo_y()
            distance = ((widget_x - cell_x) ** 2 + (widget_y - cell_y) ** 2) ** 0.5
            if distance < closest_distance:
                closest_distance = distance
                closest_cell = cell

        # Snap the widget to the center of the closest cell
        if closest_cell:
            cell_x, cell_y = closest_cell.winfo_x(), closest_cell.winfo_y()
            cell_width = closest_cell.winfo_width()
            cell_height = closest_cell.winfo_height()
            self.place(x=cell_x + cell_width // 2 - self.winfo_width() // 2,
                       y=cell_y + cell_height // 2 - self.winfo_height() // 2)
            closest_cell.configure(bg="lightgrey")  # Reset color after snapping


class DragAndDropGrid(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Drag-and-Drop Grid with Tkraise")
        self.geometry("600x600")
        
        # Top widget selector
        self.top_frame = tk.Frame(self, height=50)
        self.top_frame.pack(fill=tk.X)

        # Placeholder widgets
        self.grid_cells = []
        for i in range(3):
            label = DraggableLabel(self.top_frame, text=f"Widget {i+1}", grid_cells=self.grid_cells)
            label.pack(side=tk.LEFT, padx=10, pady=5)

        # Create a grid frame
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        # Create a 5x10 grid
        for i in range(5):
            for j in range(10):
                cell = tk.Label(self.grid_frame, text="", width=10, height=5, borderwidth=1, relief="flat")
                cell.grid(row=i, column=j, padx=1, pady=1)
                self.grid_cells.append(cell)


if __name__ == "__main__":
    app = DragAndDropGrid()
    app.mainloop()
