import os
import threading
import time

def deletefile(filepath, delay=10800):#3h 
    def delete():
        time.sleep(delay)
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
        except Exception:
            pass
    threading.Thread(target=delete, daemon=True).start()
