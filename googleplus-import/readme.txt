This application uses tweepy, https://github.com/tweepy/tweepy to interface 
with Twitter.

Set up an application on Twitter, https://dev.twitter.com/apps

Register a new app, put in an Application Name, Description, Organization.

Application Type: Client
Default Access type: Read & Write

Upload an icon if desired.

You'll be presented with a screen that gives you a Consumer key and 
Consumer secret.  Put those values in googleplusconnect.py.

Run googleplusconnect.py

Cut and paste the URL that is generated into a browser, authorize the
application, and key the pin code generated into the output. The script
will output two lines of code with your ACCESS_KEY and ACCESS_SECRET.

Paste the Consumer Key, Consumer Secret and the two generated lines into
emailgp.py.

Generate a .forward file that calls your script*:

"|/usr/src/myenv/bin/python /usr/src/myenv/emailgp.py"

Messages that are > 137 characters are trimmed.

To enable this, go to https://plus.google.com/circles and Add a new person.
Add the email address that you're running the script from and give it a 
descriptive name like 'Google Plus Twitter'. Add that 'person' to each
of the circles you would like to rebroadcast to Twitter.

Now, when you post to a circle, make sure that it says:

Also email 1 Person not yet using Google+



* This assumes that you have set up a virtual environment for this script
which I strongly recommend. For the above example, you would do:

cd /usr/src
virtualenv --no-site-packages myenv
cd myenv
source bin/activate
easy_install tweepy
