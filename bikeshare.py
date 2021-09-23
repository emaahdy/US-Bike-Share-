import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no 
        day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_list = ["chicago", "new york city", "washington"]

    user_message = "Would you like to see the statistics of Chicago, New York City, or Washington?\n"
    city = get_and_check_user_input(user_message, city_list).lower() 


    # TO DO: get user input for month (all, january, february, ... , june)

    month_list = ["january", "february", "march", "april", "may", "june"]
    y_or_n = ["y", "n"]

    user_message = "Would you like to filter the data by month? Please type Y or N.\n"
    month_question = get_and_check_user_input(user_message, y_or_n).upper()

    if month_question == "Y":
        user_message = "Which month January, February, March, April, May, or June?\n"
        month = get_and_check_user_input(user_message, month_list).lower()   
    else:
        month = "all"


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    user_message = "Would you like to filter the data by day? Please type Y or N.\n"
    day_question = get_and_check_user_input(user_message, y_or_n).upper()


    if day_question == "Y":
        user_message = "Which day monday, tuesday, ... sunday?\n"
        day = get_and_check_user_input(user_message, day_list).lower()

    else:
        day = "all"



    print('-'*40)
    return city, month, day



def get_and_check_user_input(user_message, ans_list):
    while True:
        try:
            user_ans = input(user_message).lower().strip()
            if user_ans in ans_list:
                break
            else:
                print("That is not a valid selection.")
        except:
            print("That is not a valid selection.")

    return user_ans




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

    # convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and week day from Start Time to create separate columns for each
    df['month'] = df['Start Time'].dt.month_name()   # month_name is a method that needs to be called, and not an attribute so hence the brackets ()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #filter by month 
    if month != "all":
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month.title()]   # .title() to make day into uppercase
        

        

    #filter by week day
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]  # .title() to make day into uppercase
        

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day of the Week:', popular_day)

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_comb_station = (df['Start Station'] + ' ' + df['End Station']).mode()[0]
    print('Most Frequent Combination of Start and End Stations:', popular_comb_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print("Total Trip Duration: ", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Average Trip Duration: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts() 

    print("User Types:", user_types, '\n', sep='\n')

    # TO DO: Display counts of gender
    if city == "washington":
        gender_counts = "Not Available"
    else:
        gender_counts =df['Gender'].value_counts() 

    print("Gender Counts:", gender_counts, '\n', sep='\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == "washington":
        earliest_year = "Not Available"
        recent_year = "Not Available"
        popular_year = "Not Available"
    else: 
        earliest_year =df['Birth Year'].min() 
        recent_year = df['Birth Year'].max() 
        popular_year = df['Birth Year'].mode()[0]

    print("the Earliest Year of Birth:", earliest_year)
    print("the Most Recent Year of Birth:", recent_year)
    print("the Most Frequent Year of Birth:", popular_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def raw_data(df_raw):
    """Displays 5 rows of raw data upon user request"""

    y_or_n = ["y", "n"]


    user_message = "Would you like to see five lines of the raw data? Please type Y or N.\n"
    raw_d_question = get_and_check_user_input(user_message, y_or_n).upper()

    if raw_d_question == "Y":
        print(df_raw.head(5), "\n")
        print('-'*40)
    

        data_count = 4
        while data_count <= len(df_raw)-1:
            user_message = "Would you like to see five more lines of the raw data? Please type Y or N.\n"
            raw_d_question_more = get_and_check_user_input(user_message, y_or_n).upper()

            if raw_d_question_more == "Y":
                if data_count + 5 <= len(df_raw)-1:
                    print(df_raw.iloc[data_count+1:data_count+5+1], "\n")
                    print('-'*40) 
                    data_count += 5
                elif (data_count+1) < (len(df_raw)-1): 
                    print(df_raw.iloc[data_count+1:], "\n")
                    print("you have reached the end of the data set")
                    print('-'*40)
                    break
                else:
                    print("you have reached the end of the data set")
                    print('-'*40)
                    break
                    

            else:
                print('-'*40)
                break
        
         




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df_raw = load_data(city, "all", "all")

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df_raw)

        restart = input('\nWould you like to restart? Enter Y or N.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
