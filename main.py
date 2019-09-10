from api.amsterdam_api import AmsterdamApi
from api.ns_api import NSApi

def trash_bins():
    amsterdam_api = AmsterdamApi()
    list_trash_bins = amsterdam_api.get_trash_bins()

    print("Overview of trash bins in Amsterdam")

    for trash_bin in list_trash_bins:
        print(
            str(trash_bin['id']) + "\t" +
            trash_bin['name'] + "\t" +
            trash_bin['type'] + "\t" +
            trash_bin['address']
        )


def main():
    print("NS API Test")
    ns_api = NSApi()

    # Get a list of train stations
    #print(ns_api.get_train_stations())

    # Get a list of disruptions
    #print(ns_api.get_disruptions())

    # Get all the departure trains from one train station (direction and delay in seconds)
    # Use id from get_train_stations() as identifier.
    #print(ns_api.get_departures("8400057"))


    list_disruptions = ns_api.get_disruptions()
    list_train_stations = ns_api.get_train_stations()

    delay_total = 0

    for station in list_train_stations:
        station_id = station['id']
        print(station_id)

        list_departures = ns_api.get_departures(station_id)

        for departures in list_departures :
            delay = departures['delay_seconds']
            delay_total += delay


    print("de totale delay van alle treinen met vertraging op alle stations opgeteld is ", delay_total)
    
    
    list_departures_from_AmsterdamCS = ns_api.get_departures("8400058") #id van amsterdam centraal 
    delay_total = 0

    for departures in list_departures_from_AmsterdamCS:
        
        delay = departures['delay_seconds']
        delay_total += delay 

    print("de totale delay op amsterdam centraal station", delay_total)   



    impact_buffer = 0 
    stations_size = 0

    for disruptions in list_disruptions:

       impact = disruptions['impact']
       stations = disruptions['stations']

#this sadly only works when there is only one instance of the highest impact nr 
#if there are several highest impact numbers then it will settle on the first it encounters 
       if len(stations) > stations_size:
           stations_size = len(stations)

       if impact > int(impact_buffer):
           impact_buffer = impact
           station_buffer = stations


       #print(impact)
       #print(stations, len(stations))
       
         

    print("\rthe highest impact nr. : ", impact_buffer )
    print("\r these stations were impacted by this disruption :", station_buffer)
    print("\r the most stations affected by a single disruption :", stations_size)

if __name__ == "__main__":
    main()
