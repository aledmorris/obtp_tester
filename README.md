# OBTP Tester

A basic CLI based Python app to easily push an example booking (non-Webex) to a Cisco CE endpoint (tested as working on CE 9.15.3).

The intention is to quickly demonstrate or test what a booking entry looks and behaves like on the endpoint, delivered using OBTP. The menu allows you to add multiple bookings but each new booking will overwrite any previous booking (the menu option is there to avoid having to run the app again and authenticate in order to overwrite any existing booking).


**IMPORTANT: Disclaimer**

* This is an example only for educational and/or testing purposes and is intended for personal and non-commercial use only.
* The API used in the code is protected by Cisco and *should not be used commercially* as per the Permitted Commercial Use for Scheduled Meeting Join statement in the published API guide, see Page 23, https://www.cisco.com/c/dam/en/us/td/docs/telepresence/endpoint/ce915/collaboration-endpoint-software-api-reference-guide-ce915.pdf.

