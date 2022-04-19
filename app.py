from eye_detection import EyeDetection
from mouse_listener import MouseListener
from multiprocessing import Pool


class App:
    
    def run(self):
        pool = Pool()
        #threadMouseListener =  MouseListener(1,'mouse-listener-thread',1)
        threadEyeDetection = EyeDetection(2,'eye-detection-thread',2)
        pool.apply_async(threadEyeDetection.run())
        #pool.apply_async(threadMouseListener.run())

        
    
App().run()