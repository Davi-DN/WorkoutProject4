import matplotlib.pyplot as plt

def create_visual(dict, type):
    '''
    Creates a visualization of the data given by the handle_api.py functions.
    It graphs all of the data and correctly labels the X and Y axis.

    Parameter(s)----------------------
    dict: The dictionary that the handle_api.py functions created
    type: This tells the function how to label the X and Y axis since there are different types of data that require different X and Y axis.

    It creates a .jpg file of the visualization.
    '''
    if type == 'weaponskins':
        fig, ax = plt.subplots(figsize=(16,8))
    else:
        fig, ax = plt.subplots(figsize=(10,4))

    x = ax.bar(dict.keys(), dict.values(), 0.5, edgecolor='black', linewidth=1)
    ax.bar_label(x, labels=dict.values(), label_type='edge')

    if type == 'agents':
        ax.set_xlabel('Types of Agents')
        ax.set_ylabel('Amount of Agents')

    elif type == 'weapontype':
        ax.set_xlabel('Type of weapon')
        ax.set_ylabel('Number of weapons')

    elif type == 'weaponskins':

        ax.set_xlabel('Type of weapon')
        ax.set_ylabel('Number of weapons skins')

    plt.savefig('WorkoutProject4-ddngo3.jpg')
    plt.show()