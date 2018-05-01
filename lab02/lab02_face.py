import tkinter # Imports the tkinter library in your program

window = tkinter.Tk() # Create a window to draw graphics on

canvas = tkinter.Canvas(window, width=500, height=500)
# Create a 500x500 pixel canvas

canvas.pack() # Places the canvas in the window

def drawFace():
    """ Draw a face on the canvas """
    # Draw head
    canvas.create_oval(100, 100, 400, 400)

    # TODO: Draw left eye

    # TODO: Draw right eye

    # TODO: Draw mouth


    canvas.create_oval(100, 100, 400, 400, fill="green")

drawFace()
   
