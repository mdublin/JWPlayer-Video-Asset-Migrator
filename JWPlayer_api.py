import jwplatform
import os
from clint.textui import colored, puts


def create(**kwargs):

    api_key = os.environ.get('api_key')
    api_secret = os.environ.get('api_secret')

    jwplatform_client = jwplatform.Client(api_key, api_secret)

    print("")
    puts(colored.yellow("Loading the following asset: "))
    puts(colored.blue(str(kwargs)))

    try:
        response = jwplatform_client.videos.create(
            title=str(
                kwargs["title"]),
            description=str(
                kwargs["description"]),
            tags=str(
                kwargs["tags"]),
            sourceurl=str(
                kwargs["sourceurl"]),
            sourcetype=kwargs["sourcetype"],
            sourceformat=kwargs["sourceformat"])
        # print(response)
        print("")
        puts(colored.magenta("JWPlayer Management API response: "))
        puts(colored.green(str(response)))

        return response
    except jwplatform.errors.JWPlatformNotFoundError as err:
        print("")
        puts(colored.magenta("JWPlayer Management API response: "))
        puts(colored.red(str(err.message)))
