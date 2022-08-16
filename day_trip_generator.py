from random import choice as ran_cho
# Day Trip Generator
# 1) Store the trip options for destinations, restaurants, transportation and entertainment, each in their own list
# 2) Get random element from each list. Recommended to declare variables with random_(thing)* (destination, restaurant, transportation, entertainment)
# 3) Display the initial Random Trip to your user
# 4) Prompt the user to see if they are satisfied
# 5) If not, find out which trip feature they want to change and randomly select a new feature
# 6) Keep doing this process until the user is satisfied with the trip
# 7) Display the completed trip to console.

destinations_list = ['new york city', 'boston', 'denver', 'los angeles', 'chicago', 'atlanta', 'orlando']
restaurants_list = ['chilis', 'texas roadhouse', 'olive garden', 'dave and busters', 'the cheesecake factory', 'chipotle', 'buffalo wild wings']
transportation_list = ['train', 'airplane', 'personal vehicle', 'rental car', 'bus']
entertainment_list = ['museum', 'football game', 'baseball game', 'theatre', 'theme park', 'nature park']


def choosing_destination(destinations_list):
    random_destination = ran_cho(destinations_list)
    return random_destination

def choosing_transportation(transportation_list):
    random_transportation = ran_cho(transportation_list)
    return random_transportation

def choosing_restaurant(restaurants_list):
    random_restaurant = ran_cho(restaurants_list)
    return random_restaurant

def choosing_entertainment(entertainment_list):
    random_entertainment = ran_cho(entertainment_list)
    return random_entertainment

def make_changes(chosen_options):
    user_input = input("What would you like to change?\n\t1 for Destination\n\t2 for Mode of Transportation\n\t3 for Restaurant\n\t4 for Entertainment\n\t0 to stop making changes\n")
    if user_input == '1':
        new_destination = choosing_destination(destinations_list)
        chosen_options[0] = new_destination
        print(f'\t**New Destination: {chosen_options[0].title()}\n\tMode of Transportation: {chosen_options[1].title()}\n\tRestaurant: {chosen_options[2].title()}\n\tEntertainment: {chosen_options[3].title()}')
        make_changes(chosen_options)
    elif user_input == '2':
        new_transportation = choosing_transportation(transportation_list)
        chosen_options[1] = new_transportation
        print(f'\tDestination: {chosen_options[0].title()}\n\t**New Mode of Transportation: {chosen_options[1].title()}\n\tRestaurant: {chosen_options[2].title()}\n\tEntertainment: {chosen_options[3].title()}')
        make_changes(chosen_options)
    elif user_input == '3':
        new_restaurant = choosing_restaurant(restaurants_list)
        chosen_options[2] = new_restaurant
        print(f'\tDestination: {chosen_options[0].title()}\n\tMode of Transportation: {chosen_options[1].title()}\n\t**New Restaurant: {chosen_options[2].title()}\n\tEntertainment: {chosen_options[3].title()}')
        make_changes(chosen_options)
    elif user_input == '4':
        new_entertainment = choosing_entertainment(entertainment_list)
        chosen_options[3] = new_entertainment
        print(f'\tDestination: {chosen_options[0].title()}\n\tMode of Transportation: {chosen_options[1].title()}\n\tRestaurant: {chosen_options[2].title()}\n\t**New Entertainment: {chosen_options[3].title()}')
        make_changes(chosen_options)
    elif user_input == '0':
        print(f'\nEnjoy your {chosen_options[1].title()} ride to {chosen_options[0].title()} where you will be visiting a {chosen_options[3].title()} and dining at {chosen_options[2].title()}!\n')
    else:
        print("Invalid entry. Please enter 1, 2, 3, 4, or 0.")
        make_changes(chosen_options)


def main():
    chosen_destination = choosing_destination(destinations_list)
    chosen_transpotation = choosing_transportation(transportation_list)
    chosen_restaurant = choosing_restaurant(restaurants_list)
    chosen_entertainment = choosing_entertainment(entertainment_list)
    chosen_options = [chosen_destination, chosen_transpotation, chosen_restaurant, chosen_entertainment]

    print('\nRandomly Generated Trip:')
    print(f'\tDestination: {chosen_options[0].title()}\n\tMode of Transportation: {chosen_options[1].title()}\n\tRestaurant: {chosen_options[2].title()}\n\tEntertainment: {chosen_options[3].title()}')
    user_input = input("Would you like to make any changes? y/n: ")
    if user_input == 'y':
        make_changes(chosen_options)
    else:
        print(f'\nEnjoy your {chosen_options[1].title()} ride to {chosen_options[0].title()} where you will be visiting a {chosen_options[3].title()} and dining at {chosen_options[2].title()}!\n')


main()