import time

game = input("What game do you want to play? ")

if game == "Fortnite":
   print("Connecting to Epic Games...")
   time.sleep(1)
   
   for percent in range(100, -1, -1):
      print(f"Downloading update: {percent}%", end="\r")
      time.sleep(0.05)

   print("\nLaunching Fortnite!")

elif game == "Minecraft":
   print("Generating World...")
   time.sleep(1.5)
   print("Launching Minecraft!")
else:
   print("Fetching Roblox player data...")
   time.sleep(2)
   print("Launching Roblox!")
