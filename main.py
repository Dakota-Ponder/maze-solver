from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # create the main window (root widget)
        self.root = Tk()
        self.root.title("My Window")

        # create a canvas as a data member and set its size 
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)

        # data memer to represent the windows running state 
        self.running = False
    
    def run(self):
        self.running = True
        self.root.mainloop()

    def stop(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    window = Window(800,600)
    window.run()