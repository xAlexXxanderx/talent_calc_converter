wowhead_wotlk_link = print('Enter full wowhead.com/wotlk/talent-calc link OR only talent string: ', end='')
wowhead_wotlk_link = input()

def check_string(s):
    # Returns True if string is empty or contains only digits and hyphens
    return all(char.isdigit() or char == '-' for char in s)

def add_zeroes(t,max_talent_count):
    t_count = len(t)
    if max_talent_count == t_count:
        return(t)
    else:
        zeroes_count = max_talent_count - t_count
        for i in range(0,zeroes_count):
            t = t + "0"
        return(t)

max_talents = {
    "deathknight": [28,29,31],
    "druid": [28,30,27],
    "hunter": [26,27,28],
    "mage": [30,28,28],
    "paladin": [26,26,26],
    "priest": [28,27,27],
    "rogue": [27,28,28],
    "shaman": [25,29,26],
    "warlock": [28,27,26],
    "warrior": [31,27,27],
    }

if check_string(wowhead_wotlk_link):
    player_class = print('Enter player_class: ', end='')
    player_class = input()
    talent_list = wowhead_wotlk_link.split("-")
else:
    player_class = wowhead_wotlk_link.split("talent-calc/")[1].split("/")[0]
    talent_list = wowhead_wotlk_link.split("talent-calc/")[1].split("/")[1].split("-")

player_class = player_class.replace("-","")
talent_string = ""
for i in range(0,3):
    try:
        talent_string = talent_string + add_zeroes(talent_list[int(i)],max_talents[player_class][int(i)])
    except IndexError:
        talent_string = talent_string + "0"*max_talents[player_class][int(i)]

old_talented = "http://talent.mmo-champion.com/?"+player_class+"="+talent_string
new_talented = "http://rpgworld.altervista.org/335/"+player_class+".php?"+talent_string

print("Old Talented")
print(old_talented+"\n")
print("New Talented")
print(new_talented)
