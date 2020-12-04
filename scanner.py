import requests
import json
import datetime
#constants for the url and files
URL = "https://freegeoip.app/json/"
FILE = "ipAddresses.txt"
NEWFILE = "jsondata.txt" #-------------------FIX THIS TO CORRECT FILE PATH IT IS CURRENTLY SET TO DEBUGGING PATH
def main():
    #start time
    begin = datetime.datetime.now()
    #debug counter
    counter = 0

    #open read file
    fileName = open(FILE)
    #open write file
    newFile = open(NEWFILE, "a", encoding="utf-8")

    #loop to get each ip location
    for line in fileName:
        #fix data how i want
        line = line.rstrip('\n')
        #look up ip
        response = requests.get(URL + line)
        #if rate limit exceeded
        if response.text == 'Rate limit exceeded\n':
            print(response.text)
            #could make this sleep for an hour and then do another 15k requests if needed
            break
        #turn to a dict
        response = response.json()
        #write dict values to file
        newFile.write(str(response.get("ip")) + "," + str(response.get("country_code")) + "," + 
        str(response.get("country_name")) + "," + str(response.get("region_code")) + "," + str(response.get("city")) + "," + 
        str(response.get("zip_code")) + "," + str(response.get("time_zone")) + "," + str(response.get("latitude")) + "," + 
        str(response.get("longitude")) + "," + str(response.get("metro_code")))
        newFile.write("\n")

        #counts ip address and prints as it runs -- used for debugging
        counter += 1
        print(counter)

    #close files
    fileName.close()
    newFile.close()
    #debugging done
    print("done")
    #time elasped
    print("Time elasped: " + str(datetime.datetime.now() - begin))


#calls main
main()