
 # Feature Flags to enable features incrementally
 # Note: Please enable these flags only when the task asks you to do

flag_homepage = True
flag_show_schedule_link = True
flag_ticketclass_in_search = True
flag_search_filters = True

## Database configurations
## Note: Please do not modify these

db_path = "trains.db"
db_uri = f"sqlite:///{db_path}"
db_init_url = "https://rajdhani.pipal.in/static/trains.db"

base_status_page_url = "https://rajdhani.pipal.in"
