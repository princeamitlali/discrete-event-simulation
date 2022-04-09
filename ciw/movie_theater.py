"""
    imagine a movie theater simulation where we have to find out with the existing system how many customer can be controlled in a span of 1 hour.
    few assumptions:-
    1. ticket can be booked online and offline
    2. ticket window open prior one hour only
    3. in online booking the time taken to complete the process is 2 min
    4. in offline booking process of booking is 1 min
    5. there is only one online and one offline booking available
    6. once booked user need to verify the ticket at theater door
    7. 30% people prefer online booking
    8. 70% people prefer offline booking
    9. at checking 20% false people arrives
    10. at online 40 people book ticket per hour
    11. at offline 120 people book ticket per hour
    12. at checking 140 people arrives in one hour
    
"""
# variables

arrival_rate_online_customer = 40/60
arrival_rate_offline_customer = 200/60
arrival_rate_at_checking = 140/60

service_rate_at_online = 1/2
service_rate_at_offline = 1/1
service_rate_at_checking = 1/0.5

percentage_arrival_online = 70/100
percentage_arrival_offline = 30/100
percentage_arrival_checking = 20/100

number_of_online_counter = 1
number_of_offline_counter = 1
number_of_checking_counter = 1

import ciw
N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=arrival_rate_online_customer),
                           ciw.dists.Exponential(rate=arrival_rate_offline_customer),
                           ciw.dists.Exponential(rate=arrival_rate_at_checking)],
    service_distributions=[ciw.dists.Exponential(rate=service_rate_at_online),
                           ciw.dists.Exponential(rate=service_rate_at_offline),
                           ciw.dists.Exponential(rate=service_rate_at_checking)],
    routing=[[0.0, 0.0,percentage_arrival_online],
             [0.0, 0.0, percentage_arrival_offline],
             [0.0, 0.0, percentage_arrival_checking]],
    number_of_servers=[number_of_online_counter, number_of_offline_counter, number_of_checking_counter]
)

completed_custs = []
for trial in range(10):
    ciw.seed(trial)
    Q = ciw.Simulation(N)
    Q.simulate_until_max_time(70)
    recs = Q.get_all_records()
    num_completed = len([r for r in recs if r.node==3 and r.arrival_date < 60])
    completed_custs.append(num_completed)
    
    print(sum(completed_custs) / len(completed_custs))