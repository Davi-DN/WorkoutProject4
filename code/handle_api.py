import urllib.request
import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}

def get_roles(url_name):
    '''
    This function looks through all of the VALORANT agents and makes a dictionary that tracks the amount of agents per agent type.

    Parameter(s)----------------------
    url_name: The URL of the API to get all of the VALORANT agents.

    This function returns the dictionary with the information.
    '''
    roles = {}
    request = urllib.request.Request(url_name, data=None, headers=headers)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response_data = response_data.decode(encoding = 'utf-8')
    response_data = json.loads(response_data)
    response.close()
    
    for agent in response_data['data']:
        if agent['isPlayableCharacter']:
            role = agent["role"]["displayName"]
            if role not in roles.keys():
                roles[role] = 1
            else:
                roles[role] += 1

    return roles


def get_weapon_types(url_name):
    '''
    This function looks through all of the VALORANT weapons and makes a dictionary that tracks the amount of weapons per weapon type.

    url_name: The URL of the API to get all of the VALORANT weapons.

    This function returns the dictionary with the information.
    '''
    weapon_types = {}
    request = urllib.request.Request(url_name, data=None, headers=headers)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response_data = response_data.decode(encoding = 'utf-8')
    response_data = json.loads(response_data)
    response.close()
    
    for weapon in response_data['data']:
        try:
            weapon_name = weapon["displayName"]
            types = weapon['shopData']['categoryText']
            if types not in weapon_types.keys():
                weapon_types[types] = 1
            else:
                weapon_types[types] += 1
        except:
            weapon_types[weapon["displayName"]] = 1

    return weapon_types


def skin_per_gun(url_name):
    '''
    This function looks through all of the VALORANT weapons and makes a dictionary that tracks the amount of skins each weapon has.

    Parameters:
    url_name: The URL of the API to get all of the VALORANT weapons.

    This function returns the dictionary with the information.
    '''
    weapon_skins = {}
    request = urllib.request.Request(url_name, data=None, headers=headers)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response_data = response_data.decode(encoding = 'utf-8')
    response_data = json.loads(response_data)
    response.close()
    
    for weapon in response_data['data']:
        weapon_name = weapon["displayName"]
        amt = len(weapon['skins'])
        if weapon_name not in weapon_skins.keys():
            weapon_skins[weapon_name] = amt     

    return weapon_skins