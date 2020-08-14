# University Course Wait-list Notifier

A web interaction script written in Python using Selenium script that will immediately text you if a university course has at least one seat available. 

A common issue I face when enrolling in university classes is they're usually full. This is especially true for important or popular courses. 

The university offers a "feature" to be emailed if there is a spot open. However, my frustration with this system is the university sends emails per half hour. If a class has a spot open at 12:01, the university will send an email at 12:30. This delay is enough for other people to enroll before I can get the email. 

This script will refresh the refresh the wait list page once every 10 minutes. If classes exist with one or more seats available, a text will be immediately sent to the users cell phone notifying them. 




## Important Notes
- This script does not auto-enroll in courses. This was a purposeful decision as to not break the Student Code of Conduct and Terms of Use.
- This script refreshes once every ten minutes. This timer was chosen as to not burden the university servers.
- All element IDs, attributes, and credentials are saved in a local file. This is to deter and prevent unauthorized users from abusing the program. 
