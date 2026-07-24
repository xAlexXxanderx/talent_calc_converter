import argparse

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

def add_hyphens(s,max_talent_count_list):
    new_s = ""
    i = 0
    for i in range(len(s)):
        if (i == max_talent_count_list[0]-1):
            new_s = new_s + s[i] + "-"
        elif (i == max_talent_count_list[0] + max_talent_count_list[1]-1):
            new_s = new_s + s[i] + "-"
        else:
            new_s = new_s + s[i]
        i = i+1
    return(new_s)

def del_zeroes(s):
    new_s = ""
    s_list = s.split("-")
    new_s = s_list[0].rstrip("0") +"-"+ s_list[1].rstrip("0") +"-"+ s_list[2].rstrip("0")
    return(new_s)

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

def from_wowhead_to_talented():
    wowhead_wotlk_link = print('Enter full wowhead.com/wotlk/talent-calc link OR only talent string: ', end='')
    wowhead_wotlk_link = input()

    wowhead_wotlk_link =  wowhead_wotlk_link.split("_")[0] #remove glyphs
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

def from_talented_to_wowhead():
    talented_wotlk_link = print('Enter full Talented link OR only talent string (MMO Champion or Altervista format): ', end='')
    talented_wotlk_link = input()

    if check_string(talented_wotlk_link):
        player_class = print('Enter player_class: ', end='')
        player_class = input()
        talent_string = talented_wotlk_link
    else:
        talented_wotlk_link = talented_wotlk_link.replace("http://talent.mmo-champion.com/?","").replace("http://rpgworld.altervista.org/335/","")
        talented_wotlk_link = talented_wotlk_link.replace("=","|").replace(".php?","|")
        player_class = talented_wotlk_link.split("|")[0]
        talent_string = talented_wotlk_link.split("|")[1]
    
    talent_string_new = del_zeroes(add_hyphens(talent_string,max_talents[player_class])).rstrip("-")

    print("Wowhead:")
    print("https://www.wowhead.com/wotlk/talent-calc/"+player_class+"/"+talent_string_new)

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--standart", action="store_true", help="convert from wowhead to talented")
parser.add_argument("-r", "--reverse", action="store_true", help="convert from talented to wowhead")

args = parser.parse_args()

if args.standart:
    from_wowhead_to_talented()
elif args.reverse:
    from_talented_to_wowhead()
else:
    from_wowhead_to_talented()
