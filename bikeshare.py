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
    city = input('Would you like to see data for Chicago, New York city or Washington? ').lower()
    while True:
        if city == 'chicago':
            break
        elif city == 'new york city':
            break
        elif city == 'washington':
            break
        else:
            city = input('please re-enter the city name, you can choose Chicago, New York city or Washington: ').lower()
        


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Choose a month from January to June or all: ').lower()
    while True:
        if month == 'january':
            break
        elif month == 'february':
            break
        elif month == 'march':
            break
        elif month == 'april':
            break
        elif month == 'may':
            break
        elif month == 'june':
            break
        elif month == 'all':
            break
        else:
            month = input('please re-enter the name of the month, you can choose any month from January to June or all: ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Choose a day of the week or all: ').lower()
    while True:
        if day == 'monday':
            break
        elif day == 'tuesday':
            break
        elif day == 'wednesday':
            break
        elif day == 'thursday':
            break
        elif day == 'friday':
            break
        elif day == 'saturday':
            break
        elif day == 'sunday':
            break
        elif day == 'all':
            break
        else:
            day = input('please re-enter the day of the week, you can choose any day from Monday to Sunday or all: ').lower()


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().to_frame()
    print('most common month is: ', most_common_month.index[0])
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().to_frame()
    print('most common day of the week is: ', most_common_day.index[0])
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('most common hour is: ', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().to_frame()
    print('most common start station is: ', most_common_start_station.index[0])
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().to_frame()
    print('most common end station is: ', most_common_end_station.index[0])
    # TO DO: display most frequent combination of start station and end station trip
    station_combination = df['Start Station'] +' AND '+ df['End Station']
    print('most common start and end stations combinations are: ', station_combination.value_counts().to_frame().index[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is: ', df['Trip Duration'].sum(), 'seconds')
    # TO DO: display mean travel time
    print('mean travel time is: ', df['Trip Duration'].mean(), 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('user counts: \n', df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('user gender counts: \n', df['Gender'].value_counts())
    else:
        print('Gender stats cannot be calculated because it does not appear in the dataframe')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('earliest birth year: ', df['Birth Year'].min())
        print('most recent birth year: ', df['Birth Year'].max())
        print('most common birth year: ', df['Birth Year'].mean())
    else:
        print('Birth year stats cannot be calculated because it does not appear in the dataframe')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df.head()

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        i = 0
        while True:
            user_input = input('Do you want to see raw data?\n yes/no ')
            if user_input == 'yes':
                print(df[i:i+5])
                i += 5
            elif user_input == 'no':
                break
            else:
                print('\nincorrect input!!!\n')
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
