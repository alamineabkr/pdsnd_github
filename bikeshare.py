import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Which city do you want explore (chicago, new york city, washington) ? ").lower()
    while city not in ['chicago', 'new york city','washington']:
        print ("Invalid input. Please try again.")
        city = input("Which city do you want explore (chicago, new york city, washington) ?")
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter a given month (e.g: all, january, february, ... , june)").lower()
    while month not in ['all', 'january','february','march','april','may','june']:
        print ("Invalid input. Please try again.")
        month = input("Enter a given month (e.g: all, january, february, ... , june)")
        month = month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day of week (all, monday, tuesday, ... sunday)").lower()
    while day not in ['all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        print ("Invalid input. Please try again.")
        day = input("Enter the day of week (all, monday, tuesday, ... sunday)")
        day = day.lower()

    #print('-'*40)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # extract month and day of week from Start Time to create new columns
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # use the index of the months list to get the corresponding int
        days = ['sunday', 'monday','tuesday','wednesday','thursday','friday','saturday']
        day = days.index(day)

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # find the most common month (from 1 to 12)
    popular_month = df['month'].mode()[0]
    # list of months get to fullname of the month
    months = ['January', 'February', 'March', 'April', 'May', 'June','July','August','September','October','November','December']
    # TO DO: display the most common month
    print('Most Frequent Start month:', months[popular_month-1],'(',popular_month,')')

    # find the most common month (from 1 to 12)
    popular_day_of_week = df['day_of_week'].mode()[0]
    # list of day of week in order to have the fullname
    week = ['Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    # TO DO: display the most common day of week
    print('Most Frequent Start day_of_week:', week[popular_day_of_week])

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    # TO DO: display the most common start hour
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))


    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # find the most common Start Station name
    popular_startstation = df['Start Station'].mode()[0]
    # TO DO: display most commonly used start station
    print('Most Frequent Start Station:', popular_startstation)

    # find the most common End Station name
    popular_endstation = df['End Station'].mode()[0]
    # TO DO: display most commonly used end station
    print('Most Frequent End Station:', popular_endstation)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End'] = df['Start Station']+ ' -> ' + df['End Station']
    popular_startend = df['Start-End'].mode()[0]
    print('Most Frequent Start and End Station:', popular_startend)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # find the total travel time
    total_travel_time = df['Trip Duration'].sum()
    # TO DO: display total travel time
    print('The total travel time (in seconds):', total_travel_time)


    # find the mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    # TO DO: display mean travel time
    print('The mean travel time (in seconds):', mean_travel_time)

    # find the shortest travel time
    min_travel_time = df['Trip Duration'].min()
    # TO DO: display mean travel time
    print('The shortest travel time (in seconds):', min_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # find the counts of user types
    user_types = df['User Type'].value_counts()
    # create a list with each user type
    user_type = df['User Type'].value_counts().index.tolist()
    # TO DO: Display counts of user types
    print('The counts of user types:')

    for user in range(len(user_type)):
        print(user_type[user],'=',user_types[user])

    # handle Washington missing gender column
    try:
        # find the counts of gender
        genders = df['Gender'].value_counts()
        # create a list with each user type
        gender = df['Gender'].value_counts().index.tolist()
        # TO DO: Display counts of gender
        print('\n\nThe counts of gender:')
        for x in range(len(gender)):
            print(gender[x],'=',genders[x])

    except KeyError:
    #error log
        #print ('Washington missing gender column') #bebug
        pass


    # handle Washington missing birth year column
    try:

        # find the earliest, most recent, and most common year of birth
        earliest_dob = df['Birth Year'].min()
        recent_dob = df['Birth Year'].max()
        common_dob = df['Birth Year'].mode()[0]
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nThe earliest, most recent, and most common year of birth :')
        print('Earliest: ',int(earliest_dob))
        print('Most recent: ',int(recent_dob))
        print('Most common: ',int(common_dob))
    except KeyError:
    #error log
        #print ('Washington missing birth year column') #bebug
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        while (view_data.lower()=='yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            if view_display != 'yes':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
