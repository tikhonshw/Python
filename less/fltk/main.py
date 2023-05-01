import fltk

# Define the callback function for the button
def hello_cb(widget):
    fltk.message("Hello, world!")

# Create the button and set its properties
button = fltk.Button(10, 10, 100, 30, "Click me!")
button.callback(hello_cb)

# Create the window and add the button to it
window = fltk.Fl_Window(220, 100, "Hello, world!")
window.begin()
button.draw()
window.end()

# Show the window and start the event loop
window.show()
fltk.run()
