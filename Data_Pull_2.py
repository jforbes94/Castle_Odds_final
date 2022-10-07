import requests
import json
import csv
import pandas as pd
from sqlalchemy import create_engine

url = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="CastleOdds",password="chrispaul",hostname="CastleOdds.mysql.pythonanywhere-services.com",databasename="CastleOdds$sports2")

my_conn = create_engine(url)


# An api key is emailed to you when you sign up to a plan
# Get a free API key at https://api.the-odds-api.com/
API_KEY = '47d66785c7acf3142c2338749b097426'

SPORT = 'baseball_mlb' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h,spreads,totals' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'decimal' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# First get a list of in-season sports
#   The sport 'key' from the response can be used to get odds in the next request
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

sports_response = requests.get(
    'https://api.the-odds-api.com/v4/sports',
    params={
        'api_key': API_KEY
    }
)


if sports_response.status_code != 200:
    print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')

   # print('List of in season sports:', sports_response.json())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Now get a list of live & upcoming games for the sport you want, along with odds for different bookmakers
# This will deduct from the usage quota
# The usage quota cost = [number of markets specified] x [number of regions specified]
# For examples of usage quota costs, see https://the-odds-api.com/liveapi/guides/v4/#usage-quota-costs
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

Sports_ls = ['baseball_mlb','basketball_nba','icehockey_nhl']

odds_json =[]

for sport in Sports_ls:
    SPORT = sport
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )

    if odds_response.status_code != 200:
        print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

    else:
        odds_json.append(odds_response.json())
        # print('Number of events:', len(odds_json))
        #print(odds_json)

        # Check the usage quota
        # print('Remaining requests', odds_response.headers['x-requests-remaining'])
        # print('Used requests', odds_response.headers['x-requests-used'])

games=  pd.DataFrame(columns=['game_id', 'away_team', 'home_team','start_time','sport_key','sport_title'])

odds = pd.DataFrame(columns=['game_id', 'away_team', 'home_team','start_time','sport_key','sport_title','sportsbook','last_update',
                             'H2H_home_price','H2H_away_price',
                             'home_spread','away_spread','spread_home_price','spread_away_price',
                             'over','under','over_price','under_price'])



for t in odds_json:
    for i in t:

        game_dict = {'game_id': i['id'], 'away_team': i['away_team'] , 'home_team': i['home_team'],
                'start_time':i['commence_time'],'sport_key': i['sport_key'],'sport_title': i['sport_title']}

        game_id = i['id']
        home= i['home_team']
        away = i['away_team']
        start_time = i['commence_time']
        sport_key = i['sport_key']
        sport_title = i['sport_title']

        games = games.append(game_dict, ignore_index = True)

        for k in i['bookmakers']:
            sportsbook = k['title']
            H2H_home_price=None
            H2H_away_price=None
            home_spread =None
            away_spread =None
            spread_home_price = None
            spread_away_price = None
            over = None
            under = None
            over_price =None
            under_price =None

            for j in k['markets']:
                market = j['key']
                if(market == 'h2h'):

                    for l in j['outcomes']:
                        if(l['name'] == home):
                            H2H_home_price = l['price']
                        else:
                            H2H_away_price = l['price']
                if(market == 'spreads'):
                    for l in j['outcomes']:
                        if(l['name'] == home):
                            spread_home_price = l['price']
                            home_spread = l['point']
                        else:
                            spread_away_price = l['price']
                            away_spread = l['point']
                if(market == 'totals'):
                    for l in j['outcomes']:
                        if(l['name'] == 'Over'):
                            over = l['point']
                            over_price = l['price']
                        else:
                            under = l['point']
                            under_price = l['price']
            odds_dict = {'game_id': i['id'], 'away_team': i['away_team'] , 'home_team': i['home_team'],'start_time':i['commence_time'],'sport_key': i['sport_key'],'sport_title': i['sport_title'],
                         'sportsbook':sportsbook,'last_update':k['last_update'],
                         'H2H_home_price':H2H_home_price,'H2H_away_price':H2H_away_price,
                         'home_spread':home_spread,'away_spread':away_spread,'spread_home_price':spread_home_price,'spread_away_price':spread_away_price,
                          'over':over,'under':under,'over_price':over_price,'under_price':under_price}
            output = pd.DataFrame([odds_dict])
            odds = pd.concat([odds,output],ignore_index=True)



games.to_sql(con=my_conn,name='games',if_exists='replace',index=False)

met_ls = ["H2H_home_price",'H2H_away_price','spread_home_price','spread_away_price','over_price','under_price']
metdict = {
  "spread_home_price": "home_spread",
  "spread_away_price": "away_spread",
  "over_price": "over",
  "under_price": "under"
}


for met in met_ls:
    if(met in ['H2H_home_price','H2H_away_price']):
        temp = odds
        #temp = odds.loc[:,["game_id","sportsbook","last_update",met]]
        temp = temp.sort_values(['game_id',met], axis=0, ascending=[0,0], inplace=False, kind='quicksort', na_position='last')
        temp.reset_index(inplace=True,drop=True)

#        temp[met] = temp.to_numeric(temp.met, downcast="float")
#        avg_price = temp.groupby('game_id')[met].mean()
#        avg_price.reset_index()
        temp['num_in_group'] = temp.groupby('game_id').cumcount()
        temp = temp[temp['num_in_group']<3]

        for i in range(3):
            line_temp = temp[temp['num_in_group'] == i]
            games = games.merge(line_temp[['game_id','sportsbook',met]],how='left',on ='game_id')
            games.rename(columns={"sportsbook": "Sportsbook" + met + str(i+1), met: met + str(i+1)},inplace=True)
    if(met in ['spread_away_price','spread_home_price','over_price','under_price']):
        line = metdict[met]
        temp = odds
        temp = temp.sort_values(['game_id',met], axis=0, ascending=[0,0], inplace=False, kind='quicksort', na_position='last')
        a = temp.groupby('game_id')[line].max()
        a= a.reset_index()
        a.rename(columns={line:"Best_line"},inplace=True)
        temp = temp.merge(a,how='left',left_on='game_id',right_on='game_id')

        #temp = temp[temp[line] = temp['Best_line']]

        temp = temp.query(str(line) + '>= Best_line')

        temp['num_in_group'] = temp.groupby('game_id').cumcount()
        temp = temp[temp['num_in_group']<3]
        for i in range(3):
            line_temp = temp[temp['num_in_group'] == i]


            games = games.merge(line_temp[['game_id','sportsbook',met,line]],how='left',on ='game_id')
            games.rename(columns={"sportsbook":  "Sportsbook_" + met + str(i+1), met: met + str(i+1),line:line + str(i+1)},inplace=True)

price_ls = ['H2H_home_price1',
'H2H_home_price2',
'H2H_home_price3',
'H2H_away_price1',
'H2H_away_price2',
'H2H_away_price3',
'spread_home_price1',
'spread_home_price2',
'spread_home_price3',
'spread_away_price1',
'spread_away_price2',
'spread_away_price3',
'over_price1',
'over_price2',
'over_price3',
'under_price1',
'under_price2',
'under_price3']

def mapping(odds):
    if odds >= 2:
        return '+' + str(round((odds - 1) * 100,-1))
    elif odds == 1:
        return str('Betting Suspended')
    else:
        return str(round(-100 / (odds-1),-1))


for price in price_ls:
    met = str(price) + '_ST'
    #print(met)
    games[met] =  games[price].apply(mapping)

nba = games[games['sport_key'] == 'basketball_nba']
mlb = games[games['sport_key'] == 'baseball_mlb']
nhl = games[games['sport_key'] == 'icehockey_nhl']


nba.to_sql(con=my_conn,name='sports_nba',if_exists='replace',index=False)
mlb.to_sql(con=my_conn,name='sports_mlb',if_exists='replace',index=False)
nhl.to_sql(con=my_conn,name='sports_nhl',if_exists='replace',index=False)

