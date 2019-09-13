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


    list_train_stations = ns_api.get_train_stations()

    delay_total = 0
    delay_current_station = 0

    for station in list_train_stations:
        station_id = station['id']
        station_name = station['name']

        list_departures = ns_api.get_departures(station_id)

        for departures in list_departures :
            delay = departures['delay_seconds']
            delay_current_station += delay
            delay_total += delay
            
        print('delay at', station_name, 'is',delay_current_station)            
        delay_current_station = 0 

    print("\n\r de totale delay van alle treinen met vertraging op alle stations opgeteld is ", delay_total)
    print('dat is', delay_total/3600, 'uur')
    print('het minimumloon in Nederland is 14,40 per uur  (in 2016), dus dat is', (delay_total/3600)*14.4 ,'Euro verspild aan wachten op de trein') 

if __name__ == "__main__":
    main()
