**Python3.6**

Statement of Purpose:

Simple Python3 solution for migrating CMS-scale amounts of video assets and their associated metadata from a legacy OVP solution or CMS via JSON feed into JWPlayer via JWPlayer's Management API.

While the [JWPlayer API documentation](https://developer.jwplayer.com/jw-platform/docs/developer-guide/management-api/batch-migration/) does recommend a batch upload process that involves creating and parsing a CSV file, this method skips over the need for a CSV and just uses a video asset JSON feed (although it could easily be altered to parse MRSS) typical of the type that can be created from OVPs like Brightcove, Kaltura, Ooyala, etc, to directly pass video assets and their associated metadata to the JWPlayer Management API directly.

This is meant to be run as a command line tool.

To start, simple activate a virtualenv, install the dependencies with ```$ pip install -r requirements.txt``` and run the ```run.py``` file.
