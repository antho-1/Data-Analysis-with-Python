import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult_data.csv")
    
    # Count occurrences by race
    race_count = df['race'].value_counts()

    # Get the average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Calculate the percentage of people who have a Bachelor's degree
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = round((bachelors_count/total_count)*100, 1)

    # Calculate the percentage of people with advanced education
    # (`Bachelors`, `Masters`, or `Doctorate`) that make more than 50K per year
    # Also calculate the percentage of those without advanced education that make >50K per yer

    degrees = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(degrees)].shape[0]
    lower_education = total_count - higher_education

    # percentage with salary >50K:
    # with higher education
    higher_education_rich = round((df[(df['education'].isin(degrees)) 
                                    & (df['salary'] == '>50K')].shape[0]/higher_education)*100, 1)
    # without higher education
    lower_education_rich = round((df[(~df['education'].isin(degrees))
                                     & (df['salary'] == '>50K')].shape[0]/lower_education)*100, 1)
    
    # Get the minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Find the percentage of people who work the minimum number of hours and have a salary >50K
    num_min_workers = df[df['hours-per-week']==min_work_hours].shape[0]
    rich_percentage = round((df[(df['hours-per-week'] == min_work_hours)
                         & (df['salary'] == '>50K')].shape[0]/num_min_workers)*100, 1)

    # Find the country with the highest % of salaries >50K
    countries = df['native-country'].unique()
    # Calculate percentage directly within the loop
    country_percentages = {
        country: ((df[(df['native-country'] == country)
                        & (df['salary'] == '>50K')].shape[0])
                    / df[df['native-country'] == country].shape[0])*100
        for country in countries
    }

    highest_earning_country = max(country_percentages, key=country_percentages.get)
    highest_earning_country_percentage = round(
        country_percentages[highest_earning_country], 1)

    # Identify the most popular occupation for those who earn >50K in India
    IN_df = df[df['native-country'] == 'India']
    high_earners_IN = IN_df[IN_df['salary'] == '>50K']
    top_IN_occupation = high_earners_IN['occupation'].mode()[0]

    # Display the results

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
