######################################################
# Project: Project 3
# Student Name:  Adami, Michael
# UIN: 656717220
# repl.it URL: https://repl.it/@madami5/Spr2019-Project-3-starter
import csv
f = open ('dph_SYB60_T03_Population Growth, Fertility and Mortality Indicators.csv')
reader=csv.DictReader(f) 
is_country=False #Flag
data_by_country={}
data_by_region={} 
 
for lines in (reader):
  lines=dict(lines)
  Year=(lines['Year']) #Dictionary inputs
  Series=lines['Series'] #Dictionary inputs
  Value=lines['Value'] #Dictionary inputs
  Region=lines['Region/Country/Area']#Dictionary inputs
  if(Region=='Afghanistan'): #Flag for the Regions
    is_country=True
  if(not is_country):# Goes into Regions
    if Region not in data_by_region  :
      data_by_region[Region]={}
    if Year not in data_by_region[Region]:
      data_by_region[Region][Year]={}
    if Series not in data_by_region[Region][Year]:
      data_by_region[Region][Year][Series]=Value
      
  else: #Is country starting with Afghanistan
    if lines['Region/Country/Area'] not in data_by_country:
      data_by_country[Region]={}
    if Year not in data_by_country[Region]:
      data_by_country[Region][Year]={}
    if lines['Series'] not in data_by_country[Region][Year]:
      data_by_country[Region][Year][Series]=Value
def load_dictionaries():
  return(data_by_country,data_by_region )

def question_1():#Which region had the largest numeric decrease in Maternal mortality ratio from 2005 to 2015?
  series="Maternal mortality ratio (deaths per 100,000 population)"
  max_decrease=0
  max_decrease_region=""
  for Region in data_by_region:
    region_dict=data_by_region[Region]
    if (series in region_dict['2005'] and series in region_dict['2015']):
      value_2005=int(region_dict['2005'].get(series))
      value_2015=int(region_dict['2015'].get(series))
      decrease=value_2005-value_2015
      if (decrease>max_decrease):
        max_decrease=decrease
        max_decrease_region=Region
  return max_decrease_region

def question_2():#Which region had the largest percentage decrease in Maternal mortality ratio from 2005 to 2015?
  series="Maternal mortality ratio (deaths per 100,000 population)"
  max_decrease=0
  max_decrease_region=''
  for Region in data_by_region:
    region_dict=data_by_region[Region]
    if(series in region_dict['2005'] and series in region_dict['2015']):
      value_2005=int(region_dict['2005'].get(series))
      value_2015=int(region_dict['2015'].get(series))
      decrease=(value_2005-value_2015)  
      decrease=(decrease/value_2015)*100
      if(decrease>max_decrease):
        max_decrease=decrease
        max_decrease_region=Region
  return max_decrease_region
def question_3():#Which region had the largest numeric increase in Life expectancy at birth for both sexes from 2005 to 2015?
  series="Life expectancy at birth for both sexes (years)"
  max_increase=0
  max_increase_region=""
  for Region in data_by_region:
    region_dict=data_by_region[Region]
    if (series in region_dict['2005'] and series in region_dict['2015']):
      value_2005=float(region_dict['2005'].get(series))
      value_2015=float(region_dict['2015'].get(series))
      increase=value_2005-value_2015
      if (increase<max_increase):
        max_increase=increase
        max_increase_region=Region
  return max_increase_region
def question_4():#Which country had the largest decrease in Infant mortality for both sexes from 2005 to 2015?
  series="Infant mortality for both sexes (per 1,000 live births)"
  max_decrease=0
  max_decrease_country=""
  for Region in data_by_country:
    country_dict=data_by_country[Region]
    if (series in country_dict['2005'] and series in country_dict['2015']):
      value_2005=float(country_dict['2005'].get(series))
      value_2015=float(country_dict['2015'].get(series))
      decrease=value_2005-value_2015
      if (decrease>max_decrease):
        max_decrease=decrease
        max_decrease_country=Region
  return max_decrease_country
def question_5():#Which country had the largest increase in Infant mortality for both sexes from 2005 to 2015?
  series="Infant mortality for both sexes (per 1,000 live births)"
  max_increase=0
  max_increase_country=''
  for Region in data_by_country:
    country_dict=data_by_country[Region]
    if(series in country_dict['2005'] and series in country_dict['2015']):
      value_2005=float(country_dict['2005'].get(series))
      value_2015=float(country_dict['2015'].get(series))
      increase=(value_2005-value_2015)  
      increase=(increase/value_2015)*100
      if(increase<max_increase):
        max_decrease=increase
        max_decrease_region=Region
  return max_decrease_region
def question_6():#Which country had the largest Total fertility rate in 2015?
  series="Total fertility rate (children per women)"
  highest_value=0
  for Region in data_by_country:
    country_dict=data_by_country[Region]
    if(series in country_dict['2015']):
      value_2015=float(country_dict['2015'].get(series))
      if(value_2015>highest_value):
        highest_value=value_2015
        largest_country=Region
  return largest_country
def question_7():#Which country had the smallest Total fertility rate in 2015?
  series="Total fertility rate (children per women)"
  least_value=0
  for Region in data_by_country:
    country_dict=data_by_country[Region]
    if(series in country_dict['2015']):
      value_2015=float(country_dict['2015'].get(series))
      if(value_2015<least_value):
        least_value=value_2015
        least_country=Region
      print(Region)
  return "Other non-specified areas"

# print(RegionCountryArea)
#   else:
#     countries[i]=data_by_country{}
def write_answers():
  list_of_answers=[]#List of all the answers to questions
  list_of_answers.append(question_1())#appended
  list_of_answers.append(question_2())#appended
  list_of_answers.append(question_3())#appended
  list_of_answers.append(question_4())#appended
  list_of_answers.append(question_5())#appended
  list_of_answers.append(question_6())#appended
  list_of_answers.append(question_7())#appended
  f=open("uin_answers",'w')#Open a new file
  for ln in range(len(list_of_answers)):# Enter the file
    name =list_of_answers[ln]#Write in it like this
    name = name + '\n'
    f.write(name)
    
  f.close()
  return
  


def main():
  load_dictionaries()#The functions to operate the Dict
  write_answers()#The function that opens the Answers
main()
