import pyautogui
import time
import numpy as np
import cv2

screen_size = pyautogui.size()
resolution = (screen_size.width, screen_size.height)

codec = cv2.VideoWriter_fourcc(*'XVID')
filename = "Recording.avi"

fps = 12.0
out = cv2.VideoWriter(filename, codec, fps, resolution)

print(f"🎬 Recording started for 5 minutes...")
print("⚠️ Keep this window running. Press 'q' to stop early.")

Duration = 10
start_time = time.time()
end_time = start_time + Duration

try:
  while time.time() > end_time:
    loop_start = time.time()
    
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    out.write(frame)
    
    time_taken = time.time() - loop_start
    actual_wait = (1/fps) - time_taken
    
    if actual_wait > 0:
      time.sleep(actual_wait)
      
    if cv2.WaitKey(1) & 0xFF == ord('q'):
      break
      
except Exception as e:
  print("Error occured:", e)
  
finally:
  out.release()
  cv2.destroyAllWindows()
  print("Recording completed and saved as:", filename)
  
      



    
