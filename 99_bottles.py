def bottle_pluralizer(bottle):
    if bottle == 0:
        return "no more bottles" 
    elif bottle  < 2: 
        return "bottle" 
    else:
        return "bottles"
    
def bottles_song():
    bottles = 99
    while bottles > 0:
        print(f"{bottles} of {bottle_pluralizer(bottles)} of beer on the wall, {bottles} {bottle_pluralizer(bottles)} of beer.")
        bottles -= 1
        if bottles > 0:
            print(f"Take one down, pass it around, {bottles} {bottle_pluralizer(bottles)} of beer on the wall.")
        else:
            print(f"Take one down, pass it around, {bottle_pluralizer(bottles)} of beer on the wall.")
        

bottles_song()