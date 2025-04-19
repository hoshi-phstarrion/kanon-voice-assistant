import time
import subprocess
import pygetwindow as gw
import random

# 声の設定
VOICE = "Samantha"  # 他に "Karen", "Kyoko", "Victoria" など

def get_active_window_title():
    try:
        return gw.getActiveWindow().title()
    except:
        return "Unknown window"

def get_message_for_title(title):
    if "YouTube" in title:
        return "Watching something fun? Don't forget to smile!"
    elif "Safari" in title:
        return "Looking things up? You're always learning!"
    elif "ChatGPT" in title:
        return "Talking to me, huh? I love our conversations!"
    elif "Slack" in title:
        return "Back to communication mode, huh? Let’s get things done!"
    elif "VSCode" in title or "Code" in title:
        return "Coding time! Remember to test early, test often!"
    else:
        return random.choice([
            "You're doing great, keep it up!",
            "Need a stretch break?",
            "Your focus is amazing!",
            "Keep being awesome!"
        ])

def speak(text):
    print(f"Kanon says ({VOICE}): {text}")
    subprocess.run(["say", "-v", VOICE, text])

if __name__ == "__main__":
    title = get_active_window_title()
    print("Detected Window:", title)
    message = get_message_for_title(title)
    speak(message)
