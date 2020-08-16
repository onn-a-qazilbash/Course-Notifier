# University Course Wait-list Notifier

A web interaction script written in Python and Selenium that will notify the user via text if a course has at least one seat available. 

A common frustration faced by students when enrolling in university courses is they can become full. This is especially true for important or popular courses. 

The university offers a "feature" to be emailed if there is a spot open. However, the university will send the email per 30 minutes. If a class has a spot open at 12:01, the university will send an email at 12:30. This delay is enough for other students to fill up the class before one can recieve the official notification. 

This script will refresh the wait list page once every 10 minutes. If classes exist with one or more seats available, a text will be immediately sent to the users cell phone to notify them. This implentation improves notification delivery speed up to 300% over the universitys notification system. 

## Notifier in Practice
![](https://i.imgur.com/4nOpJ1W.jpg)




## Important Notes
- This script does not auto-enroll in courses. This was a purposeful decision as to not break the Code of Student Behaviour and Conditions of Use.
- This script refreshes once every ten minutes. This timer was chosen as to not burden the university servers.
- All element IDs, attributes, and credentials are saved in a local file. This is to deter and prevent unauthorized users from abusing the program. 
