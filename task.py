print(r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⠿⢋⣡⣴⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⡟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠆⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⠏⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣾⣿⠟⠋⣀⣤⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⡟⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⣴⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⣉⠛⠃⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡆⢠⣤⠀⣉⠙⠛⠿⢿⣿⣿⠀⣾⣿⣿⠃⣼⣿⣿⣿⣿⠿⠛⢉⣡⣤⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡇⢸⣿⠀⣿⠿⠷⣶⠀⣈⡁⠀⠻⠿⡟⠀⠿⠟⠋⣁⣠⣴⣾⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡇⢸⣿⠀⣿⡄⢠⣿⠀⣿⡇⠀⣶⣦⡄⠀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡇⢸⣿⠀⠿⢧⣾⣿⠀⣿⡇⠀⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡇⢸⣿⣷⣶⣤⣄⣉⠀⣿⡇⠀⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠛⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣿⣿⣿⡇⠀⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠻⢿⡇⠀⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
print("Welcome to the Mysterious Treasure Island!")
print("Find the hidden treasure 💎")
left_or_right = input("Left or Right?\n").lower()

if left_or_right == "left":
    print("You enter a path covered in vines, leading you deeper into the island")
elif left_or_right == "right":
    print("You fell into a hole 💀 Game Over.")
    exit()
else:
    print("You got lost... Game Over.")
    exit()

swim_or_wait = input("You reach a wide river with strange ripples. Do you swim across or wait for something to happen?\n").lower()

if swim_or_wait == "swim":
    print("The water hides sharp-toothed fish! 🐟 You are attacked! Game Over")
    exit()
elif swim_or_wait == "wait":
    print("After a while, a wooden raft appears mysteriously. You cross safely.”")
else:
    print("You stand still, confused... Game Over.")
    exit()

door = input("You arrive at an ancient stone temple with three glowing doors — one Red 🔥, one Blue 🌊, one Yellow 🌟. Which do you open?\n").lower()

if door == "yellow":
    print("A chest of gold shines before you! 💎 You Win")
elif door == "blue":
    print("Wild beasts rush at you from the shadows! 🐯 Game Over")
    exit()
elif door == "red":
    print("Flames burst out — you’re burned alive! 🔥 Game Over")
    exit()
else:
    print("You picked a door that doesn’t exist! The temple collapses around you. 💀 Game Over.")
    exit()