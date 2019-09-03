from api.amsterdam_api import AmsterdamApi


def main():
    
    count = 0
    rest = 0
    paper = 0
    id_number = 0
    
    amsterdam_api = AmsterdamApi()
    list_trash_bins = amsterdam_api.get_trash_bins()

    print("Overview of trash bins in Amsterdam")

    for trash_bin in list_trash_bins:  
        count += 1
        
        if trash_bin['type'] == "Rest":
            rest += 1
        if trash_bin['type'] == "Papier":
            paper += 1
            
        id_number = id_number + trash_bin['id']
        
        print(
            str(trash_bin['id']) + "\t" +
            trash_bin['name'] + "\t" +
            trash_bin['type'] + "\t" +
            trash_bin['address']        
            
        )
        
    percentage_paper = (paper/count) * 100 
    percentage_rest = (rest/count) * 100 
    average_id_number = (id_number/count) 
    
    print("\n total amount Bins   :", count)
    print(" total amount Rest   :", rest)
    print(" total amount Paper : ", paper)
    
    print("\n out of all bins", percentage_paper, "% is paper")
    print(" out of all bins", percentage_rest, "% is rest")
    
    print(" \n and now for some totally useless information, \n the average id number of the bins is", average_id_number)
    
if __name__ == "__main__":
    main()
