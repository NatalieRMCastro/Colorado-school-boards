#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from cdp_backend.pipeline.ingestion_models import EventIngestionModel
from cdp_scrapers.youtube_utils import YoutubeIngestionScraper

###############################################################################

# dictionary syntax: "Channel Name" : {"School District Name":"Body Searc"}

# This dictionary is ordered by size of the school district
SCHOOL_BOARDS_AND_BODY_NAMES = {
    "DougCoSchools": {
        "Douglas County School District": "BOE Meeting",
    },
    "adams12fivestarschools-esc86": {
        "Adams 12 Five Star Schools": "Board of Education Meeting",
    },
    "psdondemand3088": {
        "Poudre School District R-1": "Board of Education Meeting",
    },
    "bouldervalleyschooldistric5781": {
        "Boulder Valley School District RE-2": "Board of Education Meeting",
    },
}

###############################################################################

def get_events(
    from_dt: datetime,
    to_dt: datetime,
    **kwargs,
) -> List[EventIngestionModel]:
    """
    Get all events for the provided timespan.

    Parameters
    ----------
    from_dt: datetime
        Datetime to start event gather from.
    to_dt: datetime
        Datetime to end event gather at.

    Returns
    -------
    events: List[EventIngestionModel]
        All events gathered that occured in the provided time range.

    Notes
    -----
    As the implimenter of the get_events function, you can choose to ignore the from_dt
    and to_dt parameters. However, they are useful for manually kicking off pipelines
    from GitHub Actions UI.
    """
    # storing all of the events in a list
    events = []
    
    # iterating over the list above
    for channels_name, body_search_terms in SCHOOL_BOARDS_AND_BODY_NAMES.items():
        scraper = YoutubeIngestionScraper(
            channel_name=channels_name,
            body_search_terms=body_search_terms,
            timezone="MST",
        )
        
        curr_channel_events = scraper.get_events(begin=from_dt, end=to_dt)
        print(f"Finished {channels_name}\n")
        
        # combine all new and existing events together
        events = [
            *events,
            *curr_channel_events
        ]

    print ("\nLIST OF EVENTS SCRAPED\n")    
    return events
