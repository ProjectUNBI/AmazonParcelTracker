from Objects.AlertManager import AlertMananager

READ_FILE_DELAY = 5 * 60 * 60 #order detail json will read for every 5 hour
LOAD_TRACK_DELAY = 1 * 60 * 60 # will retract every 1 hour
RETRY_TRACK_DELAY = 120  #2 minute
DELAY_PER_ORDER_CHECK = 30 #delay per rquestof order is 30 seconds



# READ_FILE_DELAY = 5 * 60 * 60 #order detail json will read for every 5 hour
# LOAD_TRACK_DELAY = 60 # will retract every 1 minute
# RETRY_TRACK_DELAY = 10 # 10 seconds
# DELAY_PER_ORDER_CHECK = 1 #delay per rquestof order is 1 seconds


TRACK_PORT = 63666

ALERT_MANAGER = AlertMananager()


