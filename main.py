import os
import requests
from nbt import nbt

minecraft_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft")

def doesSavesExist():
    path =   os.path.join(minecraft_path, "saves")
    return os.path.exists(path)

def doesWorldExist(world_name:str):
    path = os.path.join(minecraft_path, "saves", world_name)
    return os.path.exists(path)

def getUUID(player_name:str):
    request = requests.get("https://api.mojang.com/users/profiles/minecraft/" + player_name)

    if (request.status_code == 200):
        return request.json()["id"]
    else:
        return None

def findPlayerFile(uuid:str, world_name:str):
    path = os.path.join(minecraft_path, "saves", world_name, "playerdata")
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            found_uuid = os.path.splitext(file_name)[0].replace("-", "")
            if uuid == found_uuid:
                return file_name

    return None

def getDeathLocation(file_name:str, world_name:str):
    nbt_file = nbt.NBTFile(os.path.join(minecraft_path, "saves", world_name, "playerdata", file_name),'rb')

    return nbt_file["LastDeathLocation"]["dimension"], nbt_file["LastDeathLocation"]["pos"]

if __name__ == "__main__":
    if not doesSavesExist():
        print("Could not access minecraft saves folder")
        exit(1)

    world_name = input("Enter your world name: ")
    if not doesWorldExist(world_name):
        print("World does not exist")
        exit(1)

    player_name = input("Enter your player name: ")

    uuid = getUUID(player_name)
    if uuid == None:
        print("Could not get player's UUID")
        exit(1)

    file_name = findPlayerFile(uuid, world_name)
    if file_name == None:
        print("Could not find player data")
        exit(1)

    dimension, pos = getDeathLocation(file_name, world_name)

    print("\n--------------------")
    print(f"{dimension}\nx={pos[0]} y={pos[1]} z={pos[2]}")
    print("--------------------\n")



