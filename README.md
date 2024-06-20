# movie-spoiler

A script I made for someone as a practical joke to their friend. This allows you to use something like Tautulli Notification Agents to work with Plex to send a text notification. Currently the script looks up a string that exists on IMDB using an API, but you can customize it as you see fit.

## How to use

1. Clone the repository
2. Create a twilio account.
3. Edit the config.json file with your Twilio settings
4. Run the script with the following command:

```bash
python3 spoiler.py
```
## How to create a Twilio account
  * Go to Twilio's new account page
  * Sign up for an account
  * Enter your first name, last name, email address, and a password that meets Twilio's requirements
  * Verify your email address
  * Verify your phone number
  * Select your country and enter your phone number
  * Enter the verification code you received
  * Follow the prompts to get started

4. Follow the instructions on the screen

## How it works

The script will ask you for the name of the movie you want to spoil. It will then search for the movie on the [OMDb API](http://www.omdbapi.com/) and get the plot of the movie. It will then ask you how many words you want to reveal at a time. It will then reveal the plot of the movie word by word with a delay between each word.

## Disclaimer

This script was made for fun and should not be used to spoil movies for people who don't want to be spoiled. Use at your own risk.
