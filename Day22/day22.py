

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
    
    while len(players[1])>0 and len(players[2])>0:
        nums = (players[1].pop(0),players[2].pop(0))
        winner = 1+(nums[1]>nums[0])
        players[winner].append(max(nums))
        players[winner].append(min(nums))

    winning_deck = [deck for deck in players.values() if len(deck)>0][0]
    print('Winning score is {0}'.format(sum(ix*winning_deck[-ix] for ix in range(1,len(winning_deck)+1))))