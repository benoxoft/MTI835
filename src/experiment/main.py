import pyglet
import pyglet.gl as gl

window = pyglet.window.Window(width=800, height=600, caption="MTI835")
label1 = pyglet.text.Label(font_size=8, y=window.height-8)
label2 = pyglet.text.Label(font_size=8, y=window.height-18)
label3 = pyglet.text.Label(font_size=8, y=window.height-28)
label4 = pyglet.text.Label(font_size=8, y=window.height-38)

def output_text():
    return "This is a test"

@window.event
def on_draw():
    window.clear()
    label1.text = output_text()
    label1.draw()
    label2.draw()
    label3.draw()
    label4.draw()
        #/home/benoit/sm/Spider-Man.obj
@window.event
def on_key_press(symbol, modifiers):
    label2.text = "Key pressed: symbol={0}, modifiers={1}".format(symbol, modifiers)
        
@window.event
def on_mouse_press(x, y, button, modifiers):
    label3.text = "Mouse pressed: x={0}, y={1}, button={2}, modifiers={3}".format(x, y, button, modifiers) 
    
def setup_opengl():
    gl.glClearColor(0.5, 0.7, 1.0, 1)
    
if __name__ == '__main__':
    setup_opengl()
    pyglet.app.run()


