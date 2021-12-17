import requests
from xml.dom.minidom import parse, parseString
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# set endpoint FQDN or IP address
ep_url = 'https://14arundel.pexappeal.com:20001/'
# URL for authentication
session_auth = ep_url+'xmlapi/session/begin'
# URL for making bookings
bookings_url = ep_url+'bookingsputxml'

# authentication
username = 'admin'
password = 'Cycl0p$$'

# xml payload = booking properties
example_xml = "<?xml version='1.0'?>\r\n\t<Bookings item=\"1\" status=\"OK\">\r\n\t\t<Booking item=\"1\">\r\n\t\t\t<Id item=\"1\">1</Id>\r\n\t\t\t<Title item=\"1\">OBTP Example</Title>\r\n\t\t\t<Agenda item=\"1\"></Agenda>\r\n\t\t\t<Privacy item=\"1\">Public</Privacy>\r\n\t\t\t<Organizer item=\"1\">\r\n\t\t\t\t<FirstName item=\"1\">Demo</FirstName>\r\n\t\t\t\t<LastName item=\"1\"></LastName>\r\n\t\t\t\t<Email item=\"1\"></Email>\r\n\t\t\t</Organizer>\r\n\t\t\t<Time item=\"1\">\r\n\t\t\t\t<StartTime item=\"1\">2021-12-17T00:50:00Z</StartTime>\r\n\t\t\t\t<StartTimeBuffer item=\"1\">600</StartTimeBuffer>\r\n\t\t\t\t<EndTime item=\"1\">2021-12-17T01:10:00Z</EndTime>\r\n\t\t\t\t<EndTimeBuffer item=\"1\">0</EndTimeBuffer>\r\n\t\t\t</Time>\r\n\t\t\t<MaximumMeetingExtension item=\"1\">10</MaximumMeetingExtension>\r\n\t\t\t<BookingStatus item=\"1\">OK</BookingStatus>\r\n\t\t\t<BookingStatusMessage item=\"1\"></BookingStatusMessage>\r\n\t\t\t<Webex item=\"1\">\r\n\t\t\t\t<Enabled item=\"1\">False</Enabled>\r\n\t\t\t\t<MeetingNumber item=\"1\"></MeetingNumber>\r\n\t\t\t\t<Password item=\"1\"></Password>\r\n\t\t\t</Webex>\r\n\t\t\t<Encryption item=\"1\">BestEffort</Encryption>\r\n\t\t\t<Role item=\"1\">Master</Role>\r\n\t\t\t<Recording item=\"1\">Disabled</Recording>\r\n\t\t\t<DialInfo item=\"1\">\r\n\t\t\t\t<Calls item=\"1\">\r\n\t\t\t\t\t<Call item=\"1\">\r\n\t\t\t\t\t\t<Number item=\"1\">test_call@pexappeal.com</Number>\r\n\t\t\t\t\t\t<Protocol item=\"1\">SIP</Protocol>\r\n\t\t\t\t\t\t<CallRate item=\"1\">6000</CallRate>\r\n\t\t\t\t\t\t<CallType item=\"1\">Video</CallType>\r\n\t\t\t\t\t</Call>\r\n\t\t\t\t</Calls>\r\n\t\t\t\t<ConnectMode item=\"1\">OBTP</ConnectMode>\r\n\t\t\t</DialInfo>\r\n\t\t</Booking>\r\n\t</Bookings>\r\n"

# Authenticating to get the sesison token
auth_response = requests.post(session_auth,auth=(username,password),verify=False)
  
# gather the secure ID from cookie
cookies_dict = auth_response.cookies.get_dict()
auth_token = cookies_dict['SecureSessionId']

# set the request headers including the session token (SecureSessionID)
req_headers = {
  'Cookie': 'SecureSessionId='+auth_token+'; Path=/; secure; HttpOnly; SameSite=Strict; SecureSessionId='+auth_token,
  'Content-Type': 'application/xml'
}

# make the booking
book_response = requests.request("POST",bookings_url,headers=req_headers,data=example_xml,verify=False)

# response code
print(f'\nResponse Code: {book_response.status_code}')

