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

def choose_random_element(category_list):
    # Purpose: takes in one of four above lists, randomly chooses (ran_cho) an element from list, returns element
    return ran_cho(category_list)

def string_updating_list(options):
    # Purpose: Creates a string with updated values for day trip; takes in options_list, updates values, prints
    destination = options[0]
    transportation = options[1]
    restaurant = options[2]
    entertainment = options[3]
    print(f'\tDestination: {destination.title()}\n\tMode of Transportation: {transportation.title()}\n\tRestaurant: {restaurant.title()}\n\tEntertainment: {entertainment.title()}')
    
def making_changes(user_input, chosen_options, category_list):
    # Purpose: Takes what user wants to change, makes the changes
    chosen_options[user_input - 1] = choose_random_element(category_list)
    string_updating_list(chosen_options)
    selecting_changes(chosen_options)

def selecting_changes(chosen_options):
    # Purpose: Checks if user wants to make changes to their options in day trip; makes changes if user wants
    user_input = int(input("\nWhat would you like to change?\n\t1 for Destination\n\t2 for Mode of Transportation\n\t3 for Restaurant\n\t4 for Entertainment\n\t0 to stop making changes\n"))
    # Purpose: Check first if user inputs 0; exits function without wasting computing time
    if user_input == 0:
        print(f'\nEnjoy your {chosen_options[1].title()} ride to {chosen_options[0].title()} where you will be visiting a {chosen_options[3].title()} and dining at {chosen_options[2].title()}!\n')
        return
    # Purpose: If not 0, checks user selection, completes task
    if user_input == 1:
        making_changes(user_input, chosen_options, destinations_list)
    elif user_input == 2:
        making_changes(user_input, chosen_options, transportation_list)
    elif user_input == 3:
        making_changes(user_input, chosen_options, restaurants_list)
    elif user_input == 4:
        making_changes(user_input, chosen_options, entertainment_list)
    else:
        print("Invalid entry. Please enter 1, 2, 3, 4, or 0.")
        selecting_changes(chosen_options)

def main():
    # Purpose: Runs entire program; generates initial randomized lists; asks user if they are satisfied with their options
    chosen_destination = choose_random_element(destinations_list)
    chosen_transpotation = choose_random_element(transportation_list)
    chosen_restaurant = choose_random_element(restaurants_list)
    chosen_entertainment = choose_random_element(entertainment_list)
    chosen_options = [chosen_destination, chosen_transpotation, chosen_restaurant, chosen_entertainment]

    print('\nRandomly Generated Trip:')
    print(f'\tDestination: {chosen_options[0].title()}\n\tMode of Transportation: {chosen_options[1].title()}\n\tRestaurant: {chosen_options[2].title()}\n\tEntertainment: {chosen_options[3].title()}')
    user_input = input("Would you like to make any changes? y/n: ")
    if user_input == 'y':
        selecting_changes(chosen_options)
    else:
        print(f'\nEnjoy your {chosen_options[1].title()} ride to {chosen_options[0].title()} where you will be visiting a {chosen_options[3].title()} and dining at {chosen_options[2].title()}!\n')

main()