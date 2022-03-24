from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Country:
    def __init__(self, country_input, option_input):
        self.country_input = country_input
        self.option_input = option_input
    def option(self):
        pop_2020 = pd.read_csv('data/2020_pop.csv')
        array_2020 = np.array(pop_2020)
        list_option = ('median age','fertility rate','density','urban population percentage','urban population',"country'share",'word population','global rank','land area')
        for i in range(len(array_2020)):
            if self.country_input == str(array_2020[i][0]):
                answer = array_2020[i][self.option_input+4]
                if self.option_input == 4 or self.option_input == 6:
                    print(f'The most updated {list_option[self.option_input-1]} of {self.country_input}: {answer}%')
                elif self.option_input == 7:
                    print(f'The most updated {list_option[self.option_input-1]} of the world: {answer}')
                else:
                    print(f'The most updated {list_option[self.option_input-1]} of {self.country_input}: {answer}')

def option(country_input):
    print('\nMenu options:')
    print('q-To quit')
    print('c-change the country')
    print(f'1-To see the updated median age of {country_input}')
    print(f'2-To see the updated fertility rate of {country_input}')
    print(f'3-To see the updated density of {country_input}')
    print(f'4-To see the updated urban population percentage of {country_input}')
    print(f'5-To see the updated urban population of {country_input}')
    print(f'6-To see the updated world population of the world')
    print(f"7-To see the updated country's share of {country_input}")
    print(f'8-To see the updated global rank of {country_input}')
    print(f'9-To see the updated land area of {country_input}')
def modify(value):
    value = value.split(',')
    value = ''.join(value)
    value = int(value)
    return value
def population(country_input,array_2020,array_2019,array_2018):
    font = {'size':15,                                                                             
            'color':'blue'
    }
    for i in range(len(array_2020)):
        if country_input == str(array_2020[i][0]):
            y1 = np.array([modify(array_2018[i][1]),modify(array_2019[i][1]),modify(array_2020[i][1])])
            y2 = np.array([array_2018[i][2],array_2019[i][2],array_2020[i][2]])
            mean_pop = np.mean(y1)
            mean_change = np.mean(y2)
            min_change = np.min(y2)
            max_change = np.max(y2)
            print(f'The mean population of {country_input} from 2018-2020: {int(mean_pop)}')
            print(f'The mean percentage of population change of {country_input} from 2018-2020: {mean_change:.3f}%')
            print(f'The minimum percentage of population change of {country_input} from 2018-2020: {min_change:.3f}%')
            print(f'The maximum percentage of population change of {country_input} from 2018-2020: {max_change:.3f}%')
            x = ('2018','2019','2020')
            plt.title(f'The population of {country_input} from 2018-2020', fontdict=font)
            plt.xlabel('The year')
            plt.ylabel('The population')
            plt.ticklabel_format(axis='y',useMathText=True)
            lower = min(y1)-100000
            if lower < 0:
                lower = 100000
            plt.ylim(lower,max(y1)+1000000)
            plt.bar(x,y1,label = 'The population')
            plt.legend(shadow = True, loc ='best') 
            plt.show()
            plt.title(f'The percentage of population change of {country_input} from 2018-2020', fontdict=font)
            plt.xlabel('The year')
            plt.ylabel('The percentage of population change')
            plt.plot(x,y2,'om',label = 'The percentage')
            plt.legend(shadow = True, loc ='best') 
            plt.tight_layout()
            plt.show()
def print_region(countries):
    for i in range(len(countries)):
            if i==(len(countries)-1):
                print(countries[i], end='.')
            else:
                print(countries[i], end=', ')
def print_countries(countries):
    for i in range(1,len(countries)):
        print(countries[i])            
def list_countries(input_region):
    region = pd.read_csv('data/continents.csv')
    region = np.array(region)
    country = []
    for i in range(len(region)):
        if input_region == str(region[i][0]):
            for j in range(len(region[i])):
                if str(region[i][j]) != 'nan':
                    country.append(region[i][j])
            return (country)
def check_continent(user_input,list):
    while user_input not in list:
        print('')
        print_region(list)
        user_input = input('\nPlease re-enter the continent: ',)
    return user_input  
def check_countries(user_input,list):
    while user_input not in list:
        print('-'*40)
        print_countries(list)
        print('-'*40)
        user_input = input('\nPlease re-enter the country name: ',)
    return user_input
def input_process(region,array_2020,array_2019,array_2018):
    print('Continents list: ')
    print_region(region)
    region_input = input('\n\nPlease enter the continent: ')
    region_input =check_continent(region_input,region)
    countries = list_countries(region_input)
    print('-'*40)
    print_countries(countries)
    print('-'*40)
    country_input = input('\nPlease enter a country name listed above: ')
    country_input = check_countries(country_input,countries)
    population(country_input,array_2020,array_2019,array_2018)
    print('-'*40)
    option(country_input)
    print('-'*40)
    return country_input
    

def main():
    option_list=['q','c','1','2','3','4','5','6','7','8','9']
    pop_2020 = pd.read_csv('data/2020_pop.csv')
    array_2020 = np.array(pop_2020)
    pop_2019 = pd.read_csv('data/2019_pop.csv')
    array_2019 = np.array(pop_2019)
    pop_2018 = pd.read_csv('data/2018_pop.csv')
    array_2018 = np.array(pop_2018)
    region = pd.read_csv('data/continents.csv')
    region = region['Continent'].to_list()
    country_input = input_process(region,array_2020,array_2019,array_2018)
    menu_options = input('\nEnter an option above: ')
    while menu_options not in option_list:
        option(country_input)
        print('-'*40)   
        menu_options=input("\nPlease re-enter an valid option: ")
    while menu_options != 'q':
        while menu_options == 'c':
            print('\n\n')
            country_input = input_process(region,array_2020,array_2019,array_2018)
            menu_options = input('\nEnter an option above: ')
            while menu_options not in option_list:
                option(country_input)
                print('-'*40)
                menu_options=input("\nPlease re-enter an valid option: ")
                if menu_options == 'q':
                    break
        if menu_options =='q':
            break
        execute = Country(country_input, int(menu_options))
        option(country_input)
        print('-'*40)
        execute.option()
        menu_options = input('\nEnter an option above: ')
        while menu_options not in option_list:
            option(country_input)
            print('-'*40)
            menu_options=input('\nPlease re-enter an valid option: ',)
    print('\n_______Thank you for using the program_______')

if __name__ == '__main__':
    main()