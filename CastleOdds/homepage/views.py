from django.shortcuts import render
#from homepage.models import Games
from homepage.models import MLB
from homepage.models import NBA
from homepage.models import NHL


#from django.http import HttpResponse

#games = [
#{
#    'away_team': 'Golden State Warriors',
#    'home_team': 'Memphis Grizzlies',
#    'h2h_away_price': '+220',
#    'h2h_home_price': '-410',
#    'over_price': '+150',
#    'under_price': '-120',
#    'away_spread': '-110',
#    'home_spread': '-110'
#    },
#    {
#    'away_team': 'Milwaukee Bucks',
#    'home_team': 'Boston Celtics',
#    'h2h_away_price': '+320',
#    'h2h_home_price': '-510',
#    'over_price': '+250',
#    'under_price': '-220',
#    'away_spread': '-110',
#    'home_spread': '-110'
#    }
#]

def homepage(request):
    return render(request,'homepage/homepage.html')
##, context)

def sports(request):
    resultsdisplay = MLB.objects.all()
    nba = NBA.objects.all()
    nhl = NHL.objects.all()
    return render(request,'homepage/sports.html',{'MLB':resultsdisplay,'NBA':nba,'NHL':nhl})






