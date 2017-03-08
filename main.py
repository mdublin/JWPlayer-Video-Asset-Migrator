#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import datetime
from clint.textui import colored, puts
from JWPlayer_api import create

def parse_feed(feed_url):
    r = requests.get(feed_url)
    json_feed = json.loads(r.text)
    title, description, tags, date, sourceurl = "", "", "", "", ""

    sourcetype = "url"
    sourceformat = "mp4"

    # nested callback that send video assets to JWPlayer API if HD renditions are available
    def add_elements():
        nonlocal title, description, tags, date
        title = item["name"]
        description = item["shortDescription"]
        tags = str((", ").join(item["tags"]))
        # for converting to human readable, but API wants unicode timestamp
        #date = datetime.datetime.fromtimestamp(int(item["creationDate"][0:10])).strftime('%Y-%m-%d')
        # slicing because the Unix time stamp in Brightcove JSON feed is problematic, adding extra values
        date = int(item["creationDate"][0:10])
        # sending video asset to JWPlayer Management API
        create(title=title, description=description, tags=tags, sourceurl=sourceurl, sourcetype=sourcetype, sourceformat=sourceformat)


    for index, item in enumerate(json_feed['items']):
        if index < 5:
            # parse array of renditions to extract highest-res rendition
            for index, entry in enumerate(item["renditions"]):
                if entry["frameHeight"] == 1080:
                    sourceurl = entry["url"]
                    add_elements()
                    break
                elif entry["frameHeight"] == 720:
                    sourceurl = entry["url"]
                    add_elements()
                    break
                else:
                    if index == len(json_feed) - 1:
                        puts(colored.red("Skipping this asset, no HD rendition available..."))


if __name__ == '__main__':
    parse_feed(feed_url)
