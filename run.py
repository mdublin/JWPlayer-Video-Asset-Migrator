from clint.textui import colored, puts, prompt, indent
from main import parse_feed
import validators
import os

# credentials setup
api_key = prompt.query("Please enter your JWPlayer API Key: ")
os.environ['api_key'] = api_key

api_secret = prompt.query("Please enter your JWPlayer API Secret: ")
os.environ['api_secret'] = api_secret

# feed setup
feed_ok = False
while feed_ok is False:
    feed_prompt = prompt.query("Please enter the JSON video asset feed you wish to parse: ")
    if validators.url(feed_prompt) is True:
        puts(colored.green("URL has been validated!"))
        feed_ok = True
    else:
        puts(colored.red("There's a problem with this URL, please try submitting a different url."))
        feed_ok = False

start_ingest_prompt = ""
while start_ingest_prompt == "":
    start_ingest_prompt = prompt.query("Would you like to start the ingest process? [Y/N]")
    if start_ingest_prompt.upper() == ("Y" or "YES"):
        puts(colored.green("Starting ingest process..."))
        # sending feed url and creds to parser
        parse_feed(feed_prompt)
        break
    elif start_ingest_prompt.upper() == ("N" or "NO"):
        puts(colored.red("Exiting asset migrator...."))
        break
    else:
        puts(colored.yellow("Please enter either 'Y' or 'N' "))
