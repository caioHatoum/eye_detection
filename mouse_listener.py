from pynput.mouse import Listener
import threading

class MouseListener:
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    def run(self):
        
        def on_move(x, y):
            print('Pointer moved to {0}'.format(
            (x, y)))
            

        def on_click(x, y, button, pressed):
            print('{0} at {1}'.format(
                'Pressed' if pressed else 'Released',
                (x, y)))
            if not pressed:
                # Stop listener
                return True

        def on_scroll(x, y, dx, dy):
            print('Scrolled {0}'.format(
                (x, y)))

        # Collect events until released
        with Listener(
                on_move=on_move,
                on_click=on_click,
                on_scroll=on_scroll) as listener:
            listener.join()
