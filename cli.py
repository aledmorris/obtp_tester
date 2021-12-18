import requests
from xml.dom.minidom import parse, parseString
import urllib3
from getpass import getpass


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# set endpoint FQDN or IP address
ep_url = 'https://14arundel.pexappeal.com:20001/'
# URL for authentication
session_auth = ep_url+'xmlapi/session/begin'
# URL for making bookings
bookings_url = ep_url+'bookingsputxml'

timezone_offset = 10 # hrs

# Default booking values
firstname = 'Aled'
lastname = 'Morris'
email = 'aled@pexappeal.com'
start_buffer = '300' # secs
end_buffer = '0' # secs
proto = 'SIP'
call_rate = '4096'
call_type = 'Video'
uri = 'test_call@pexappeal.com'


# function
def display_menu():
    
    print("""
    *********************************************
     MENU: Choose an option:
     
     [1] Add booking to endpoint
     [2] Exit
    
    *********************************************          
    """)

def make_booking(booking_title,start_time,duration):
    
    #calculat the start time, end time, using the duration and timezone
    utc_start = ''
    utc_end = ''
    
    # xml payload = booking properties
    example_xml = "<?xml version='1.0'?>\r\n\t<Bookings item=\"1\" status=\"OK\">\r\n\t\t<Booking item=\"1\">\r\n\t\t\t<Id item=\"1\">1</Id>\r\n\t\t\t<Title item=\"1\">"+booking_title+"</Title>\r\n\t\t\t<Agenda item=\"1\"></Agenda>\r\n\t\t\t<Privacy item=\"1\">Public</Privacy>\r\n\t\t\t<Organizer item=\"1\">\r\n\t\t\t\t<FirstName item=\"1\">"+firstname+"</FirstName>\r\n\t\t\t\t<LastName item=\"1\">"+lastname+"</LastName>\r\n\t\t\t\t<Email item=\"1\">"+email+"</Email>\r\n\t\t\t</Organizer>\r\n\t\t\t<Time item=\"1\">\r\n\t\t\t\t<StartTime item=\"1\">"+utc_start+"</StartTime>\r\n\t\t\t\t<StartTimeBuffer item=\"1\">"+start_buffer+"</StartTimeBuffer>\r\n\t\t\t\t<EndTime item=\"1\">"+utc_end+"</EndTime>\r\n\t\t\t\t<EndTimeBuffer item=\"1\">"+end_buffer+"</EndTimeBuffer>\r\n\t\t\t</Time>\r\n\t\t\t<MaximumMeetingExtension item=\"1\">10</MaximumMeetingExtension>\r\n\t\t\t<BookingStatus item=\"1\">OK</BookingStatus>\r\n\t\t\t<BookingStatusMessage item=\"1\"></BookingStatusMessage>\r\n\t\t\t<Webex item=\"1\">\r\n\t\t\t\t<Enabled item=\"1\">False</Enabled>\r\n\t\t\t\t<MeetingNumber item=\"1\"></MeetingNumber>\r\n\t\t\t\t<Password item=\"1\"></Password>\r\n\t\t\t</Webex>\r\n\t\t\t<Encryption item=\"1\">BestEffort</Encryption>\r\n\t\t\t<Role item=\"1\">Master</Role>\r\n\t\t\t<Recording item=\"1\">Disabled</Recording>\r\n\t\t\t<DialInfo item=\"1\">\r\n\t\t\t\t<Calls item=\"1\">\r\n\t\t\t\t\t<Call item=\"1\">\r\n\t\t\t\t\t\t<Number item=\"1\">"+uri+"</Number>\r\n\t\t\t\t\t\t<Protocol item=\"1\">"+proto+"</Protocol>\r\n\t\t\t\t\t\t<CallRate item=\"1\">"+call_rate+"</CallRate>\r\n\t\t\t\t\t\t<CallType item=\"1\">"+call_type+"</CallType>\r\n\t\t\t\t\t</Call>\r\n\t\t\t\t</Calls>\r\n\t\t\t\t<ConnectMode item=\"1\">OBTP</ConnectMode>\r\n\t\t\t</DialInfo>\r\n\t\t</Booking>\r\n\t</Bookings>\r\n"

    # set the request headers including the session token (SecureSessionID)
    req_headers = {
    'Cookie': 'SecureSessionId='+auth_token+'; Path=/; secure; HttpOnly; SameSite=Strict; SecureSessionId='+auth_token,
    'Content-Type': 'application/xml'
    }

    # make the booking
    book_response = requests.request("POST",bookings_url,headers=req_headers,data=example_xml,verify=False)

    # response code
    print(f'\nResponse Code: {book_response.status_code}')
    
    


# Banner
print('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("""
████████╗███████╗░██████╗████████╗  ░█████╗░██████╗░████████╗██████╗░
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
░░░██║░░░█████╗░░╚█████╗░░░░██║░░░  ██║░░██║██████╦╝░░░██║░░░██████╔╝
░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░  ██║░░██║██╔══██╗░░░██║░░░██╔═══╝░
░░░██║░░░███████╗██████╔╝░░░██║░░░  ╚█████╔╝██████╦╝░░░██║░░░██║░░░░░
░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░  ░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░░░
""")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Welcome to CLI OBTP Tester')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('\nTo begin, enter your endpoint credentials...\n')

# authentication
print('Authentication...')
username = input('> Enter Username: ')
while username == '':
    print('!!! Cannot have a blank username...')
    username = input('> Enter Username: ')
password = getpass('> Enter Password: ')




# Authenticating to get the sesison token
auth_response = requests.post(session_auth,auth=(username,password),verify=False)

if auth_response is '204' or '200':
    
    # gather the secure ID from cookie
    cookies_dict = auth_response.cookies.get_dict()
    auth_token = cookies_dict['SecureSessionId']
    
    print('Authenticated ok...')

        
    looping = True   
    
    
    # loop when user not exit
    while looping:
        
        # display the menu
        display_menu()
        
        choice = input('> Your selection: ')
        
        if choice == 1:
            # do stuff to add a booking to the endpoint
            print('\nLet\'s add a booking...')
                                   
            # Booking Title
            booking_title = input('> Booking title: ')
            # start time
            start_time = input('> Start time HH:MM 24 hrs (assumes today\'s date): ')
            # end time (calculated)
            duration = input('> Duration (mins): ')                 
            
            make_booking(booking_title,start_time,duration)
            
            
            
        elif choice == 2:
            # exit the loop
            looping=False
            print('\n>>...Exiting the app....')
            
        else:
            # any other selection
            print(f'\nError! -\'{choice}\' is not a valid option.')
            
      
   
        
    
    
    
    
    



