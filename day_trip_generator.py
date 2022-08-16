from random import choice as ran_cho
# Day Trip Generator
# 1) Store the trip options for destinations, restaurants, transportation and entertainment, each in their own list
# 2) Get random element from each list. Recommended to declare variables with random_(thing)* (destination, restaurant, transportation, entertainment)
# 3) Display the initial Random Trip to your user
# 4) Prompt the user to see if they are satisfied
# 5) If not, find out which trip feature they want to change and randomly select a new feature
# 6) Keep doing this process until the user is satisfied with the trip
# 7) Display the completed trip to console.

destinations_list = ['NYC', 'Boston', 'Denver', 'Los Angeles', 'Chicago', 'Atlanta', 'Orlando']
restaurants_list = ['chili\'s', 'texas roadhouse', 'olive garden', 'dave and busters', 'the cheesecake factory', 'chipotle', 'buffalo wild wings']
transportation_list = ['train', 'airplane', 'personal vehicle', 'rental car', 'bus']
entertainment_list = ['museum', 'football game', 'baseball game', 'theatre', 'theme park', 'nature park']


def choosing_destination(destinations_list):
    random_destination = ran_cho(destinations_list)
    random_destination.title()
    return random_destination

def choosing_transportation(transportation_list):
    random_transportation = ran_cho(transportation_list)
    random_transportation.title()
    return random_transportation

def choosing_restaurant(restaurants_list):
    random_restaurant = ran_cho(restaurants_list)
    random_restaurant.title()
    return random_restaurant

def choosing_entertainment(entertainment_list):
    random_entertainment = ran_cho(entertainment_list)
    random_entertainment.title()
    return random_entertainment

def user_choice_destination(chosen_options):
    # Currently does not check to see if previous random element is same and new random element
    destination_randomly_chosen = choosing_destination(destinations_list)
    chosen_destination = input(f'Would you like to go to {destination_randomly_chosen}? y/n: ')
    if chosen_destination == 'y':
        chosen_options.append(destination_randomly_chosen)
    elif chosen_destination == 'n':
        user_choice_destination(chosen_options)
        # does not include invalid entry (if not y/n)

def user_choice_transportation(chosen_options):
    # Currently does not check to see if previous random element is same and new random element
    transportation_randomly_chosen = choosing_destination(transportation_list)
    chosen_destination = input(f'Would you like to travel by {transportation_randomly_chosen}? y/n: ')
    if chosen_destination == 'y':
        chosen_options.append(transportation_randomly_chosen)
    elif chosen_destination == 'n':
        user_choice_transportation(chosen_options)
        # does not include invalid entry (if not y/n)

def user_choice_restaurant(chosen_options):
    # Currently does not check to see if previous random element is same and new random element
    restaurant_randomly_chosen = choosing_destination(restaurants_list)
    chosen_restaurant = input(f'Would you like to dine at {restaurant_randomly_chosen} during your visit? y/n: ')
    if chosen_restaurant == 'y':
        chosen_options.append(restaurant_randomly_chosen)
    elif chosen_restaurant == 'n':
        user_choice_restaurant(chosen_options)
        # does not include invalid entry (if not y/n)

def user_choice_entertainment(chosen_options):
    # Currently does not check to see if previous random element is same and new random element
    entertainment_randomly_chosen = choosing_entertainment(entertainment_list)
    chosen_entertainment = input(f'Would you like to visit a {entertainment_randomly_chosen}? y/n: ')
    if chosen_entertainment == 'y':
        chosen_options.append(entertainment_randomly_chosen)
    elif chosen_entertainment == 'n':
        user_choice_entertainment(chosen_options)
        # does not include invalid entry (if not y/n)

def do_the_things():
    chosen_options = []
    print('\nWelcome to the random day trip generator. To get started, let\'s find out where you would like to go')
    
    user_choice_destination(chosen_options)
    print(f'Excellent! You have chosen to go to {chosen_options[0]}!')

    user_choice_transportation(chosen_options)
    print(f'Great, you have chosen to go to {chosen_options[0]} by way of {chosen_options[1]}!')

    user_choice_restaurant(chosen_options)
    print(f'Enjoy dining at {chosen_options[2]}!')

    user_choice_entertainment(chosen_options)
    print(f'Congradulations! You will go to {chosen_options[0]} by means of {chosen_options[1]}. While there, you will dine at {chosen_options[2]} and visit a {chosen_options[3]}!')

do_the_things()

