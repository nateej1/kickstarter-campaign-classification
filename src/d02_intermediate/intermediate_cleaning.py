import pandas as pd
import numpy as np
import functools

def kickstarter_deduped_to_intermediate(kick_deduped):
    """
    TEST
    """
    kick_deduped.drop(columns='index', inplace=True)

    # Let's break up the category variables
    category = kick_deduped['category'].str.partition("name\":\"")[2]
    kick_deduped['sub_category'] = category.str.partition("\"")[0]

    sub_category = kick_deduped['category'].str.partition("slug\":\"")[2]
    kick_deduped['overall_category'] = sub_category.str.partition("\"")[0]

    # let's drop the old category variable
    kick_deduped.drop(columns='category', inplace=True)

    # break up the location variable
    city = kick_deduped['location'].str.partition("localized_name\":\"")[2]
    kick_deduped['city'] = city.str.partition("\"")[0]

    country = kick_deduped['location'].str.partition("country\":\"")[2]
    kick_deduped['country_loc'] = country.str.partition("\"")[0]

    state_location = kick_deduped['location'].str.partition("state\":\"")[2]
    kick_deduped['state_loc'] = state_location.str.partition("\"")[0]
    # drop the old location variable
    kick_deduped.drop(columns='location', inplace=True)

    # let's break up the creator variable
    creator_name = kick_deduped['creator'].str.partition("name\":\"")[2]
    kick_deduped['creator_name'] = creator_name.str.partition("\"")[0]

    creator_slug = kick_deduped['creator'].str.partition("slug\":\"")[2]
    kick_deduped['creator_slug'] = creator_slug.str.partition("\"")[0]
    # drop the old creator variable
    kick_deduped.drop(columns='creator', inplace=True)

    # convert unixtime to datetime
    kick_deduped['created_at'] = pd.to_datetime(kick_deduped['created_at'],unit='s')
    kick_deduped['deadline'] = pd.to_datetime(kick_deduped['deadline'],unit='s')
    kick_deduped['launched_at'] = pd.to_datetime(kick_deduped['launched_at'],unit='s')
    kick_deduped['state_changed_at'] = pd.to_datetime(kick_deduped['state_changed_at'],unit='s')

    return kick_deduped
