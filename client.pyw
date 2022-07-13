from datetime import datetime
from subprocess import check_output
import time, qbittorrentapi, logging, yaml

##################################################################~CONFIGURATION~##################################################################
with open("config.txt") as file: # Open the file as read
    config_file = yaml.load(file, Loader=yaml.FullLoader) # Set the contents to = tmp_current_dictionary

for key, value in config_file.items():
    if key == "Logging":
        if value == None:
            qlogging = False
        else:
            qlogging = value
    if key == "Qbittorrent_IP_Address":
        if value == None:
            qbit_ip = 'localhost'
        else:
            qbit_ip = value
    if key == "Qbittorrent_Port": 
        if value == None:
            qbit_port = 8080
        else:
            qbit_port = value
    if key == "Qbittorrent_Username":
        if value == None:
            qbit_username = "admin"
        else:
            qbit_username = value
    if key == "Qbittorrent_Password":
        if value == None:
            qbit_password = "adminadmin"
        else:
            qbit_password = value
    if key == "Active_Hours":
        if value == None:
            Active_Hours = ["03","04","05","06","07","08"]
        else:
            Active_Hours = value


##################################################################




##################################################################~MAIN~##################################################################
# instantiate a Client using the appropriate WebUI configuration
qbt_client = qbittorrentapi.Client(host=qbit_ip, port=qbit_port, username=qbit_username, password=qbit_password,)

logging.basicConfig(filename='qbit_disable.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')



while True:
    times = datetime.now().strftime("%H")

    #We try to login and catch the error
    try:
        qbt_client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        logging.error(e)


    if times in Active_Hours:
        #check_output("docker start qb", shell=True)
        qbt_client.torrents.resume.all()
        if qlogging == True:
            logging.info("QB - Resume")
        pass


    else:
        #check_output("docker stop qb", shell=True)
        qbt_client.torrents.pause.all()
        if qlogging == True:
            logging.info("QB - Pause")        
        pass


    time.sleep(1)
    #We then try to logout 
    try:
        qbt_client.auth_log_out()
    except all as e:
         logging.error(e)
    time.sleep(59)

##################################################################