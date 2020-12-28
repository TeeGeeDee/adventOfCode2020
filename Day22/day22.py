
from copy import deepcopy

def combat(players_in):
    players = deepcopy(players_in)
    while len(players[1])>0 and len(players[2])>0:
        nums = (players[1].pop(0),players[2].pop(0))
        winner = 1+(nums[1]>nums[0])
        players[winner].append(max(nums))
        players[winner].append(min(nums))
    return players


def recursive_combat(players_in,game_num):
    players = deepcopy(players_in)
    ever_seen = set()
    while len(players[1])>0 and len(players[2])>0:
        game_state = (tuple(players[1]),tuple(players[2])) 
        if game_state in ever_seen:
            winner = 1
            return winner, players
        else:
            ever_seen.add(game_state)
            nums = (players[1].pop(0),players[2].pop(0))
            if len(players[1])>=nums[0] and len(players[2])>=nums[1]:
                subgame = {1:players[1][0:nums[0]],2:players[2][0:nums[1]]}
                winner,_ =  recursive_combat(subgame,game_num+1)
            else:
                winner = 1+(nums[1]>nums[0])
            players[winner].append(nums[winner-1])
            players[winner].append(nums[2-winner])
    winner = 1+(len(players[1])==0)
    return winner, players

if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        data = [c.rstrip('\n') for c in f.readlines()]
    
    players = {1:[],2:[]}
    player = 1
    for d in data[1:]:
        if d == 'Player 2:':
            player = 2
        elif d != '':
            players[player].append(int(d))
    
    players_combat_out = combat(players)

    winning_deck = [deck for deck in players_combat_out.values() if len(deck)>0][0]
    print('Winning score of combat is {0}'.format(sum(ix*winning_deck[-ix] for ix in range(1,len(winning_deck)+1))))

    winner,decks = recursive_combat(players,1)
    winning_deck = decks[winner]
    print('Winning score of recursive combat is {0}'.format(sum(ix*winning_deck[-ix] for ix in range(1,len(winning_deck)+1))))
    
    