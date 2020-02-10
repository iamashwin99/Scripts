from __future__ import print_function
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime, time, os
import pytz
from random import seed
from random import random

seed(1)



source = "Raw" # put all the audi and transcript files in the raw folder MAKE SURE RAW FOLDER HAS ANOTHER BACKUP
tzone = pytz.timezone("Asia/Kolkata")
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
calid = 'ifrsnk1f0851jhllqm3pbsat78@group.calendar.google.com'  # Time table calender ID,(made public)


def lecTime(fname):
    # print("Getting date and time of file: "+ fname)
    timestamp = os.stat(fname).st_mtime
    value = datetime.datetime.fromtimestamp(timestamp)

    value = value + datetime.timedelta(minutes = -20)
    print("Time of end of file: " + fname + " = " + value.strftime('%Y-%m-%d %H:%M:%S'))
    return value


def time2event(time):
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    print('Getting the event for time = ' + time )
    events_result = service.events().list(calendarId=calid, timeMin=time,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        # start = event['start'].get('dateTime', event['start'])
        # print(start,event['summary'])
        print(event['summary'])
        return event['summary']


def main():
    i = 0

    for filename in os.listdir(source):
        fname = source + "/" + filename

        t = lecTime(str(fname))
        #t.tzinfo()
        time = tzone.localize(t)
        timeiso = time.isoformat()
        #time = t.astimezone(tzone).isoformat() # + 'Z'  # 'Z' indicates UTC time
        event = time2event(timeiso)
        day = t.strftime('-%d-%m-%Y')
        newname = source + "/" + event + day

        if(os.path.exists(newname)==True):
            num=random()
            newname=newname+str(num)
        os.rename(fname,newname)



if __name__ == "__main__":
    #time2event("2020-01-09T09:59:38+05:30")

    main()
