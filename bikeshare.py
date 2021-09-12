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

    while True:

     city = input("Please Select one of the city between Chicago, New York City or Washington: ").lower()

     if city in ['chicago', 'new york city', 'washington']: 

            break

    else:

        print('Not Valid')

    # TO DO: get user input for month (all, january, february, ... , june)  

    while True:

     month = input("Depending on wich month you want to filter the data? Choose one of these[all,January,"

                  "February ,"

                  "March, April,May, or June]").lower()

     if month in ['all', 'january', 'february','march','april','may','june']: 

            break

    else:

        print('Not Valid')

    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:

     day = input("Depending on wich month you want to filter the data? Choose one of these[all,Sunday, Monday ,"

                  "Tuesday, Wednesday ,Thersday,Friday, or Saturday]").lower()

     if day in ['all', 'sunday', 'monday','tuesday','wednesday','thersday','friday','saturday']: 

            break

    else:

        print('Not Valid')

    

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

     #load intended file into data frame

    df = pd.read_csv(CITY_DATA[city])



    #convert columns od Start Time and End Time into date format yyyy-mm-dd

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['End Time'] = pd.to_datetime(df['End Time'])



    #extract month from Start Time into new column called month

    df['month'] = df['Start Time'].dt.month



    #filter by month



    if month != 'all':

        # use the index of the months list to get the corresponding int

        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1



        # filter by month to create the new dataframe

        df = df[df['month'] == month]



    # extract day from Start Time into new column called month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by day of week if applicable

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]





    return df





def time_stats(df):

    """Displays statistics on the most frequent times of travel."""



    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()



    # TO DO: display the most common month

    print ("The most common month is: ", df['month'].value_counts().idxmax())



    # TO DO: display the most common day of week

    print ("The most common day is: ", df['day_of_week'].value_counts().idxmax())



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    print ("The most common hour is: ", df['hour'].value_counts().idxmax())



    print('-'*40)



def station_stats(df):

    """Displays statistics on the most popular stations and trip."""



    print ('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()



    # TO DO: display most commonly used start station

    print("The most common start station is: ", df ['Start Station'].value_counts().idxmax())





    # TO DO: display most commonly used end station

    print("The most common end station is: ", df['End Station'].value_counts().idxmax())





    # TO DO: display most frequent combination of start station and end station trip

    print('The most frequent combination of start station and end station trip')

    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)

    print(most_common_start_and_end_stations)





    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)





def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""



    print('\nCalculating Trip Duration...\n')

    start_time = time.time()



    # TO DO: display total travel time

    total_duration = df['Trip Duration'].sum() / 3600.0

    print("total travel time in hours is: ", total_duration)



    # display mean travel time

    mean_duration = df['Trip Duration'].mean() / 3600.0

    print("mean travel time in hours is: ", mean_duration)







    





    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)





def user_stats(df,city):

    """Displays statistics on bikeshare users."""



    print('\nCalculating User Stats...\n')

    start_time = time.time()



    # TO DO: Display counts of user types

    count_user = df['User Type'].value_counts()

    print('Total Counts of user type are {}.\n'.format(count_user))

    

    if city == 'chicago' or city=='new york city':



    # Display counts of gender

        df['Gender'].fillna('Not given',inplace=True)

        count_user_gender = df['Gender'].value_counts()

        print('\nTotal Counts of user Gender type are {}.\n'.format(count_user_gender))



   


    # Display earliest, most recent, and most common year of birth

        earliest_birth_year =df['Birth Year'].min()

        print('The earliest year of birth:{}.'.format(earliest_birth_year))

        most = df['Birth Year'].max()

        print('The most recent year of birth:{}.'.format(most))

        most_common= df['Birth Year'].value_counts().idxmax()

        print('The most common year of birth:{}.'.format(most_common))

    



    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)





def main():

    while True:

        city, month, day = get_filters()

        df = load_data(city, month, day)
        
        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)             

        user_stats(df,city)
        
        # Print five rows of data
        i=0
        while True:
             data = input('\nWould you like to restart? Enter yes or no.\n')
             if data.lower() =='yes':
                 print(df[i:i + 5])
                 i+= 5
             else:
                  break
 

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


   





if __name__ == "__main__":

	main()