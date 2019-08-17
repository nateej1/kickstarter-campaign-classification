import numpy as np
import pandas as pd

def kickstarter_feature_engineering(kick_intermediate):
    """

    TEST
    """
    kick_inter = kick_intermediate

    # sources
    # average exchange rate over a decade - https://www.ofx.com/en-us/forex-news/historical-exchange-rates/yearly-average-rates/
    # world regions - https://unstats.un.org/unsd/methodology/m49/
    # country codes - https://laendercode.net/en/2-letter-list.html

    # restrict to successful & failed
    kick_inter = kick_inter.loc[(kick_inter['state'] == 'successful')|(kick_inter['state'] == 'failed')]

    # drop unneeded columns
    kick_inter.drop(columns=['backers_count', 'converted_pledged_amount', 'country',
                             'currency_symbol', 'currency_trailing_code', 'current_currency',
                             'friends', 'is_backing', 'is_starrable', 'is_starred',
                             'last_update_published_at', 'permissions', 'pledged',
                             'slug', 'source_url', 'spotlight', 'staff_pick', 'static_usd_rate',
                             'unread_messages_count','unseen_activity_count', 'urls', 'usd_pledged',
                             'usd_type', 'overall_category', 'creator_name', 'creator_slug', 'disable_communication'],
                    inplace=True)

    # create feature with blurb word count
    kick_inter['blurb_word_count'] = kick_inter.blurb.str.split().str.len()
    # drop original blurb column
    kick_inter.drop('blurb', axis=1, inplace=True)

    # create length of campaign feature
    kick_inter['campaign_length'] = (kick_inter['deadline'] - kick_inter['launched_at']).dt.days

    # create delta between created and launched date
    kick_inter['delta_created_launched'] = (kick_inter['launched_at'] - kick_inter['created_at']).dt.days

    # CONVERT GOAL TO GOAL_USD
    # boolean series that are missing the exchange rate
    bool_series = pd.isnull(kick_inter["fx_rate"])
    kick_inter[bool_series].currency.value_counts()

    # let's fill in the null fx columnn
    avg_fx_rate_10yr = {
        'EUR': 1.231885,
        'MXN': 0.068639,
        'USD': 1.000000,
        'GBP': 1.473741,
        'CAD': 0.869234,
        'SEK': 0.131576,
        'DKK': 0.165301,
        'HKD': 0.128529,
        'NOK': 0.14488,
        'AUD': 0.857369,
        'SGD': 0.757244,
        'CHF': 1.043232,
        'NZD': 0.744532
    }
    currency = ['EUR', 'MXN', 'USD', 'GBP', 'CAD',
                'SEK', 'DKK', 'HKD', 'NOK', 'AUD',
                'SGD', 'CHF', 'NZD']

    for cur in currency:
        null_exRatesEUR = ((kick_inter.fx_rate.isnull()) & (kick_inter.currency==cur))
        kick_inter.loc[null_exRatesEUR, 'fx_rate']=avg_fx_rate_10yr[cur]

    # create goal USD
    kick_inter['goal_usd'] = kick_inter.goal * kick_inter.fx_rate

    # drop unneeded columns
    kick_inter.drop(columns=['created_at', 'deadline', 'fx_rate', 'launched_at',
                             'state_changed_at', 'city', 'state_loc', 'name'],
                    inplace=True)

    # rename columns
    kick_inter.rename({'goal':'goal_original', 'state':'target',
                       'sub_category': 'category', 'country_loc':'country'},
                      axis=1, inplace=True)

    # drop duplicated ids
    kick_inter.drop_duplicates(subset=['id'], keep='first', inplace=True)

    kick_inter['successful_dummy'] = pd.get_dummies(kick_inter['target'], drop_first=True)

    # we no longer need our target column anymore
    kick_inter.drop(columns=['target'], inplace=True)

    # let's drop our remaining null columns
    kick_inter.dropna(inplace=True)

    # LET'S COMBINE OUR COUNTRIES INTO WORLD REGIONS
    # build a world regions dictionary
    world_regions = {
        'Northern America': ['US', 'CA', 'MX', 'GL', 'BM'],
        'Northern Africa':['MA', 'TN', 'EG', 'LY', 'DZ', 'SD'],
        'Eastern Africa':['KE', 'MG', 'MW', 'ET', 'UG', 'TZ', 'RW', 'MU', 'ZW', 'SO', 'SC', 'MZ', 'ZM', 'DJ',
                          'SS'],
        'Middle Africa':['CM', 'TD', 'CG', 'CD', 'GA', 'GQ', 'CF'],
        'Southern Africa':['ZA', 'BW', 'SZ', 'LS'],
        'Western Africa':['GH', 'NG', 'LR', 'SN', 'ML', 'SL', 'NE', 'BF', 'GN', 'GM', 'CI', 'CV', 'MR', 'BJ'],
        'Caribbean':['HT', 'TT', 'PR', 'DO', 'JM', 'BS', 'CU', 'KY', 'CW', 'GP', 'SX', 'VI', 'BB',
                     'AG', 'DM', 'LC', 'VC', 'TC', 'KN', 'GD'],
        'Central America':['GT', 'SV','BZ', 'PA', 'HN', 'CR', 'NI'],
        'South America':['CO', 'PE', 'VE', 'EC', 'AR', 'BR', 'CL', 'BO', 'SR', 'UY', 'PY', 'GY'],
        'Central Asia':['KG', 'KZ', 'TJ'],
        'Eastern Asia':['HK', 'JP', 'CN', 'MN', 'KR', 'MQ', 'TW', 'KP', 'MO'],
        'South-eastern Asia':['ID', 'SG', 'VN', 'MY', 'TH', 'KH', 'PH', 'MM', 'LA', 'TL'],
        'Southern Asia':['BD', 'IN', 'LK', 'NP', 'AF', 'PK', 'BT', 'IR', 'MV'],
        'Western Asia':['IL', 'JO', 'AM', 'LB', 'AE', 'CY', 'PS', 'GE', 'YE', 'IQ', 'KW', 'AZ', 'SA',
                        'SY', 'QA', 'BH', 'TR'],
        'Eastern Europe':['PL', 'RO', 'UA', 'MD', 'HU', 'CZ', 'RU', 'BG', 'SK', 'BY', 'FO'],
        'Northern Europe':['SE', 'GB', 'NO', 'IE', 'DK', 'FI', 'LT', 'IS', 'EE', 'SJ', 'LV', 'AX'],
        'Southern Europe': ['ES', 'IT', 'HR', 'RS', 'PT', 'SI', 'GR', 'MT', 'BA', 'MK', 'XK', 'GI',
                            'VA', 'MC', 'AL', 'ME'],
        'Western Europe':['FR', 'CH', 'DE', 'BE', 'NL', 'LU', 'AT', 'MC'],
        'Australia and New Zealand':['AU', 'NZ'],
        'Melanesia':['VU', 'PG', 'FJ', 'NC'],
        'Micronesia':['FM', 'GU', 'KI'],
        'Polynesia':['WS', 'TO', 'CK', 'PF', 'PN'],
        'Antarctica': ['AQ']
    }

    # flip the dictionary to make each individual value in the value list a new key.
    countries_regions = {}
    for key, val in world_regions.items():
        for i in range(len(val)):
            countries_regions[val[i]] = key


    # let's make a for loop to assign the correct region to the correct country in our dataframe.
    countries = ['US', 'ES', 'FR', 'AU', 'SE', 'CH', 'CA', 'GB', 'IT', 'NO', 'HK',
           'KE', 'MX', 'IE', 'JP', 'DE', 'BE', 'NZ', 'NL', 'CN', 'CO', 'GT',
           'HR', 'PL', 'DK', 'MN', 'ID', 'LU', 'FI', 'KR', 'SG', 'GH', 'HT',
           'BD', 'RS', 'AT', 'TT', 'NG', 'PE', 'SV', 'PT', 'ZA', 'MG', 'VN',
           'MQ', 'IL', 'PR', 'RO', 'TW', 'UA', 'MD', 'JO', 'TR', 'CM', 'SI',
           'IN', 'VE', 'AM', 'EC', 'HU', 'AR', 'LK', 'MA', 'LB', 'BR', 'CL',
           'CZ', 'BO', 'GL', 'MY', 'TH', 'GR', 'MW', 'BZ', 'RU', 'AE', 'KH',
           'DO', 'CY', 'ET', 'UG', 'MT', 'PA', 'HN', 'BG', 'PH', 'LR', 'CR',
           'LT', 'TZ', 'SK', 'TN', 'WS', 'BA', 'IS', 'PS', 'BY', 'SN', 'MK',
           'KG', 'ML', 'SR', 'VU', 'PG', 'EE', 'NP', 'UY', 'GE', 'TD', 'AQ',
           'RW', 'CG', 'FM', 'SL', 'SJ', 'BW', 'TO', 'GU', 'YE', 'MM', 'AF',
           'CK', 'JM', 'CD', 'KZ', 'EG', 'MU', 'ZW', 'FJ', 'XK', 'PY', 'BS',
           'PK', 'CU', 'NI', 'KY', 'LV', 'CW', 'NE', 'GI', 'BF', 'SO', 'LY',
           'GP', 'SC', 'TJ', 'GN', 'GM', 'SX', 'MZ', 'VA', 'IQ', 'BT', 'VI',
           'KW', 'SZ', 'MC', 'CI', 'LA', 'AL', 'GY', 'BB', 'ZM', 'AG', 'DJ',
           'IR', 'DM', 'CV', 'NC', 'DZ', 'KP', 'FO', 'LS', 'TL', 'KI', 'PF',
           'MR', 'LC', 'VC', 'AX', 'MO', 'AZ', 'SA', 'SY', 'PN', 'GA', 'GQ',
           'TC', 'KN', 'QA', 'BJ', 'MV', 'SS', 'SD', 'ME', 'BH', 'GD', 'CF',
           'BM']

    for country in countries:
        kick_inter.loc[kick_inter['country']==country, 'world_regions']=countries_regions[country]

    # let's reset the index.
    kick_inter.reset_index(inplace=True, drop=True)

    # let's merge the new cluster feature with this.
    # kick_inter = kick_inter.merge(cluster_features_df,
    #                 how='left', on='id')

    return kick_inter
