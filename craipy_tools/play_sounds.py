import sys
import time

PLATFORM = sys.platform

def play_sound(sound: str, n_times: int, sleep_time: float) -> None:
  raise Exception(f"Could not match your platform: {PLATFORM}")
  return None

if sys.platform == "win32":
  import winsound

  def play_sound(sound: str, n_times: int = 1, sleep_time: float = 0.5) -> None:
    sound = sound.lower()
    
    if sound == "test":
      melody = [(1000, 100)]
    elif sound == "mozart":
      melody = [(392, 500), (294, 500), (392, 500), (294, 500), (392, 250), (294, 250), (392, 250), (494, 250), (587, 1000)]
    elif sound == "ok":
      melody = [(523, 100), (880, 200)]
    elif sound == "error":
      melody = [(440, 250), (311, 400)]
    else:
      raise Exception(f"Could not match the sound - {sound} - available: ...")

    for _ in range(n_times):
      for freq, duration in melody:
        winsound.Beep(freq, duration)
      time.sleep(sleep_time)
  
