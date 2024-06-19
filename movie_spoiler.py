import sys
from imdb import IMDb
import re
from twilio.rest import Client
import json

# Get settings from config.json
with open('config.json') as f:
    config = json.load(f)

# Your Twilio account SID and auth token
account_sid = config['account_sid']
auth_token = config['auth_token']

recipient_number = config['recipient_number']
twilio_number = config['twilio_number']
last_message_length = config['last_message_length']

# Check if a command line argument is provided
if len(sys.argv) < 2:
    print("Usage: python fun.py <IMDb ID>")
    sys.exit(1)  # Exit the script if no argument is provided

ia = IMDb()  # Create an instance of the IMDb class
movie_id = sys.argv[1]  # Use the first command line argument as the movie ID
movie_id = int(movie_id[2:]) if movie_id.startswith(
    'tt') else int(movie_id)  # Convert the movie ID to an integer
movie = ia.get_movie(movie_id)  # Get the movie object

if movie is not None:  # Check if the movie object is None
    # Retrieve the synopsis (plot) of the movie
    synopsis = movie.get('synopsis', [''])[0]  # type: ignore
    # Split the synopsis into sentences
    sentences = re.split('(?<=[.!?]) +', synopsis)
    # Get the last sentences of the synopsis
    last_sentences = ' '.join(
        sentences[-last_message_length:]) if sentences else ''

    if movie is not None:
        print(f"Last {last_message_length} sentences of the synopsis of '{
              movie['title']}':")
        # Create a Twilio client
        client = Client(account_sid, auth_token)

        # Define the message
        message = last_sentences

        # Send the SMS
        message = client.messages.create(
            body=message,
            from_=twilio_number,
            to=recipient_number
        )

        # Print the message SID
        print(f"SMS sent with SID: {message.sid}")
    else:
        print("Movie not found.")
else:
    print("Movie not found.")
