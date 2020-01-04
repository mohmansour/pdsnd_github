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
    cty=['chicago','new york city','washington']
    tmp=""
    while tmp not in cty:
            tmp = input('\nWould you like to see data for Chicago, New York City, or Washington?\n')
            tmp = tmp.lower()
    city=tmp
    
    # TO DO: get user input for month (all, january, february, ... , june)
    mnth=['all','january','february','march','april','june']
    while tmp not in mnth:
        tmp = input('\nWould you like to see data for (all, january, february, ... , june)?\n')
        tmp = tmp.lower()
    month=tmp
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dy=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while tmp not in dy:
        tmp = input('\nWould you like to see data for (all, monday, tuesday, ... sunday)?\n')
        tmp = tmp.lower()
    day=tmp

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    # extract hour from the Start Time column to create an hour column
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('\nMost Popular Month:', popular_month)

    # TO DO: display the most common day of week
    # extract hour from the Start Time column to create an hour column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('\nMost Popular Weekday:', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_sstation = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station:', popular_sstation)


    # TO DO: display most commonly used end station
    popular_estation = df['End Station'].mode()[0]
    print('\nMost Popular End Station:', popular_estation)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+'__'+df['End Station']
    popular_trip = df['combination'].mode()[0]
    print('\nMost Popular Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal Travel Time:',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('\nAverage Travel Time:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCount of each User Type :',user_types)

    # Check if we use Washington file
    if 'Birth Year' in df:
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print('\nCount of each Gender :',gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nThe earliest recent Year :',df['Birth Year'].min())
        print('\nThe most recent Year :',df['Birth Year'].max())
        print('\nThe most common year :',df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df,strt,en):
    """Displays raw data on bikeshare users."""

    print('\nDisplaying 5 raw data...\n')
    start_time = time.time()
    
    #five row data to show
    print(df.iloc[strt:en,:])
    
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
        strt=0
        en=5
        while True:
            raw = input('\nWould you like to see raw data? Enter yes or no.\n')
            if raw.lower() != 'yes':
                break
            else:
                raw_data(df,strt,en)
                strt=en
                en=en+5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
