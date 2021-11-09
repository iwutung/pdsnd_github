import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data.')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please select a city to explore.\n Chicago\n New York\n Washington\n -> ').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Oops... looks like an error occured! \nPlease enter a valid option! example: chicago')

    print('Great! Now let\'s apply some filters!')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to explore?\n -> ').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Oops... looks like an error occured! \n Please enter one of the following months:\n all, january, february, march, april, may, june')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day of the week would you like to explore?\n -> ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Oops... looks like an error occured! \n Please enter one of the followings:\n all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data for specified city
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create month and day columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    # filter by month if applicabe
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day if applicable
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month: ', df['month'].mode()[0])

    # display the most common day of week
    print('Most common day of the week: ', df['day'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most common start hour: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most commonly used end station: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['station_combination'] = df['Start Station'] + ', and ' + df['End Station']
    print('Most frequent combination of start and end station: ', df['station_combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['travel_time'] = df['End Time'] - df['Start Time']
    print('Total travel time: ', df['travel_time'].sum())

    # display mean travel time
    print('Mean travel time: ', df['travel_time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    while True:
        try:
            # Display counts of gender
            print(df['Gender'].value_counts())

            # Display earliest, most recent, and most common year of birth
            print('Earliest year of birth: ', df['Birth Year'].min())
            print('Most recent year of birth: ', df['Birth Year'].max())
            print('Most common year of birth: ', df['Birth Year'].mode()[0])
            break
        except:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    """Displays data upon request by the user"""
    n = 0
    while True:
        # Prompt the user if they want to see 5 lines of row data
        view_data = input('\nWould you like to view more data in detail? Enter yes or no.\n -> ')
        # Display that data if the answer is 'yes'
        # Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration
        if view_data.lower() == 'yes':
            print(df.iloc[n:n+5])
            n += 5
        #  Stop the program when the user says 'no' or there is no more raw data to display
        elif view_data.lower() == 'no':
            break
        else:
            print('Sorry, I didnt quite get that.\nPlease enter yes or no')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n -> ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
