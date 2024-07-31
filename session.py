import os
from termcolor import colored, cprint
import keyboard as k
import time



def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def loading():
    clear()
    print("loading   ", end="", flush=True)
    for i in range(5):
        print("\b" * 3, end="", flush=True)
        for j in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\b" * 3 + "   ", end="", flush=True)


def edit_scene():
    clear()
    print("\nChoose a scene:")
    senses = [
        "sea",
        "forest",
        "forested lake",
        "forest river",
        "aroura",
        "desert hills",
        "oceanic island",
        "beach sunset",
        "sunset",
        "mountain sunset"]
    ids = []
    for i, s in enumerate(senses):
        print(f"{i + 1}. {s}")
        ids.append(f"{i + 1}")

    time.sleep(0.2)

    while True:
        i = input("Enter your choice: ").strip()
        if i in ids:
            print(f"you chose {senses[int(i) - 1]}")
            time.sleep(3)
            return senses[int(i) - 1]
        else:
            print("Invalid choice. Please try again.")


def edit_background_noise():
    noises = [
        {"name": "sea", "description": "A calm and serene background noise.", "sound": "sea.wav"},
        {"name": "forest", "description": "A calm and serene background noise.", "sound": "forest.wav"},
        {"name": "forest lake", "description": "A calm and serene background noise.", "sound": "forest lake.wav"},
        {"name": "forest river", "description": "A calm and serene background noise.", "sound": "forest river.wav"},
        {"name": "aroura", "description": "A calm and serene background noise.", "sound": "aroura.wav"},
        {"name": "desert hills", "description": "A calm and serene background noise.", "sound": "desert hills.wav"},
        {"name": "oceanic island", "description": "A calm and serene background noise.", "sound": "oceanic island.wav"},
        {"name": "beach sunset", "description": "A calm and serene background noise.", "sound": "beach sunset.wav"},
        {"name": "sunset", "description": "A calm and serene background noise.", "sound": "sunset.wav"},
        {"name": "mountain sunset", "description": "A calm and serene background noise.", "sound": "mountain sunset.wav"},
        {"name": "caffe", "description": "A calm and serene background noise.", "sound": "caffe.wav"},
        {"name": "Wind Noise", "description": "A calm and serene background noise.", "sound": "Wind Noise.wav"},
        {"name": "Ocean Waves", "description": "A calm and serene background noise.", "sound": "Ocean Waves.wav"},
    ]

    clear()

    print("\nChoose background noise:")
    ids = []
    for i, n in enumerate(noises):
        print(f"{i + 1}. {n["name"]}")
        ids.append(f"{i}")

    time.sleep(0.2)

    while True:
        i = input("Enter your choice: ").strip()
        if i in ids:
            print(f"you chose {(noises[int(i) - 1])["name"]}")
            time.sleep(3)
            return noises[int(i) - 1]
        else:
            print("Invalid choice. Please try again.")


def edit_music():
    clear()
    music_list = [{"name": "Sun and His Daughter",
                   "description": "A serene background noise.",
                   "sound": "Sun and His Daughter.wav"},
                  {"name": "Hazy After Hours",
                   "description": "A serene background noise.",
                   "sound": "Hazy After Hours.wav"},
                  {"name": "Deep Urban",
                   "description": "A serene background noise.",
                   "sound": "Deep Urban.wav"},
                  {"name": "Island Beat",
                   "description": "A serene background noise.",
                   "sound": "Island Beat.wav"},
                  {"name": "Games Worldbeat",
                   "description": "A serene background noise.",
                   "sound": "Games Worldbeat.wav"},
                  ]

    ids = []
    for i, m in enumerate(music_list):
        print(f"{i + 1}. {m["name"]}")
        ids.append(f"{i}")

    time.sleep(0.2)

    while True:
        i = input("Enter your choice: ").strip()
        if i in ids:
            print(f"you chose {music_list[int(i) - 1]["name"]}")
            time.sleep(3)
            return music_list[int(i) - 1]
        else:
            print("Invalid choice. Please try again.")


def recommendations():
    clear()
    recommendations_list = [
        {
            "name": "Tropical Beach",
            "description": "Relax with the sound of waves on a tropical beach.",
            "noise": "Ocean Waves",
            "music": "Island Beat",
            "scene": "oceanic island"
        },
        {
            "name": "Mountain Retreat",
            "description": "Enjoy the serene ambiance of a mountain retreat.",
            "noise": "Wind Noise",
            "music": "Deep Urban",
            "scene": "mountain sunset"
        },
        {
            "name": "Forest Haven",
            "description": "Immerse yourself in the tranquility of a dense forest.",
            "noise": "forest",
            "music": "Games Worldbeat",
            "scene": "forest"
        },
        {
            "name": "Sunset Paradise",
            "description": "Watch the sun set over the horizon with calm music.",
            "noise": "beach sunset",
            "music": "Hazy After Hours",
            "scene": "beach sunset"
        },
        {
            "name": "Desert Calm",
            "description": "Feel the tranquility of desert hills with soothing sounds.",
            "noise": "desert hills",
            "music": "Sun and His Daughter",
            "scene": "desert hills"
        },
        {
            "name": "Aurora Bliss",
            "description": "Experience the magical aurora with calm background noise.",
            "noise": "aurora",
            "music": "Deep Urban",
            "scene": "aurora"
        },
        {
            "name": "Lakeside Serenity",
            "description": "Relax by the forest lake with gentle music.",
            "noise": "forest lake",
            "music": "Hazy After Hours",
            "scene": "forested lake"
        },
        {
            "name": "River Escape",
            "description": "Unwind by the forest river with peaceful tunes.",
            "noise": "forest river",
            "music": "Games Worldbeat",
            "scene": "forest river"
        },
    ]


    ids = []
    for i, m in enumerate(recommendations_list):
        print(f"{i + 1}. {m["name"]}")
        ids.append(f"{i}")

    time.sleep(0.2)

    while True:
        i = input("Enter your choice: ").strip()
        if i in ids:
            print(f"you chose {recommendations_list[int(i) - 1]["name"]}")
            time.sleep(3)
            return recommendations_list[int(i) - 1]
        else:
            print("Invalid choice. Please try again.")

def session():
    scene = None
    noise = None
    music = None
    z = True
    while z:
        clear()
        print("\nMenu:")
        print(f"1. Edit Scene {"(" + colored(scene, "green") + ")" if scene else ""}")
        print(f"2. Edit Background Noise {"(" + colored(noise, "green") + ")" if noise else ""}")
        print(f"3. Edit Music {"(" + colored(music, "green") + ")" if music else ""}")
        print("4. Recommendations")
        print("Press " + colored("Enter", "red") + " if you are done editing.")
        time.sleep(0.2)
        while True:
            if k.is_pressed("enter"):
                if scene and noise and music:
                    z = False
                    break
                else: 
                    print("Please fill all options")
                    time.sleep(0.2)
            if k.is_pressed("1"):
                scene = edit_scene()
                break
            if k.is_pressed("2"):
                noise = edit_background_noise()["name"]
                break
            if k.is_pressed("3"):
                music = edit_music()["name"]
                break
            if k.is_pressed("4"):
                recommendation = recommendations()
                scene = recommendation["scene"]
                noise = recommendation["noise"]
                music = recommendation["music"]
                break
        
    loading()
    clear()

    cprint("░██████╗████████╗░█████╗░██████╗░████████╗███████╗██████╗░  ░██████╗███████╗░██████╗░██████╗██╗░█████╗░███╗░░██╗", "yellow")
    cprint("██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ██╔════╝██╔════╝██╔════╝██╔════╝██║██╔══██╗████╗░██║", "yellow")
    cprint("╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░█████╗░░██║░░██║  ╚█████╗░█████╗░░╚█████╗░╚█████╗░██║██║░░██║██╔██╗██║", "yellow")
    cprint("░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██║░░██║  ░╚═══██╗██╔══╝░░░╚═══██╗░╚═══██╗██║██║░░██║██║╚████║", "yellow")
    cprint("██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗██████╔╝  ██████╔╝███████╗██████╔╝██████╔╝██║╚█████╔╝██║░╚███║", "yellow")
    cprint("╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  ╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝", "yellow")

    print("Started session with: ")
    
    print("Scene: " + colored(scene, "green"))
    print("Noise: " + colored(noise, "green"))
    print("Music: " + colored(music, "green"))