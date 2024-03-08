import visualization as visual
import handle_api as api

OPTIONS = '''"1": Visualize the amount of agents per role.
"2": Visualize the amount of weapons per type.
"3": Visualize the amount of skins per weapon.
Enter an option: 
'''

def main():
    '''
    The interface of the program,.

    It collects the user input and runs a function based on what the user inputted.
    '''
    print('Welcome to the VALORANT API Visualizer!\n\nTo start, enter one of the options:')
    while True:
        user_input = input(OPTIONS)
        if user_input == '1':
            data = api.get_roles('https://valorant-api.com/v1/agents/')
            visual.create_visual(data, 'agents')
            break
        elif user_input == '2':
            data = api.get_weapon_types('https://valorant-api.com/v1/weapons/')
            visual.create_visual(data, 'weapontype')
            break
        elif user_input == '3':
            data = api.skin_per_gun('https://valorant-api.com/v1/weapons/')
            visual.create_visual(data, 'weaponskins')
            break
        else:
            print('Not a valid option!')

if __name__ =="__main__":
    main()
