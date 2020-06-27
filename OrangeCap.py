'''
We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:
Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed (here they are 'match1', 'match2', 'match3'), nor are the names of the players. A player need not have a score recorded in all matches.
Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total score of playername.
{'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}
ans=('player3',100)
'''

def OrangeCap(a):
    matches=list(sorted(a.keys()))
    players=[]
    for n in matches:
        players.append(list(a[n].keys()))
    flattened_players = set([y for x in players for y in x])
    total={}
    for n in flattened_players:
        total[n]=0
        for match in matches:
            if n in a[match].keys():
                total[n]=total[n]+a[match][n]
    b=max(total.values())
    for n in total.keys():
        if total[n]==b:
            c=(n,b)
    return c
a={'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}
print(OrangeCap(a))