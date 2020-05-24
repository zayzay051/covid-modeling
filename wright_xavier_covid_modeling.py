# Simple COVID-19 Exponential Growth Simulator Template -- wright.x -- 5/24/20 -- Time -- Version 0.6

import time

num_infected_ppl = 0
current_day = 0
days_sim = 0
num_death_ppl = 0


print("this program will model potential covid-19 infection and deaths in the u.s. Right now the number of infections will double every six days.\n")
time.sleep(4)      
num_infected_ppl = int(input("how many people are currently infected? please enter an integer number with no commas. then press enter.  "))
days_sim = int(input("how many days of infection growth do you wnat to simulate? please enter and INTEGER with no commas. then press enter.  "))

print(f"the current number of infected with covid-19 is (num_infected_ppl:,) and you will simulate (days_sim) days worth of infection growth.\n")


while current_day <= days_sim:

    num_infected_ppl += num_infected_ppl
    (num_death_ppl)= round(num_infected_ppl * 0.023)
    print(f"on day (current_day) there will be (num_infected_ppl:,) and approximely  {num_deaths_ppl:,) poeple will die from covid-19.\n"
    current_day += 6
    time.sleep(3)
        
   # Write a print() statement that shows the total number of infections and the number of deaths after running your simulation.  

    
    
    
