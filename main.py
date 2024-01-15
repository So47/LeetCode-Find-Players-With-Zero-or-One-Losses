class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Using defaultdict to simplify the incrementation process
        from collections import defaultdict

        #using defaultdict so we don't have to check if key existed or not
        winners = defaultdict(int) 
        losers = defaultdict(int)
        answer = [[],[]]
        
        ## Since 'key1' doesn't exist, it is automatically created with the default value 0, then incremented
        for winner, loser in matches:
            winners[winner] +=1 
            losers[loser] +=1
        
        # List of players who won at least one match and never lost
        answer[0] = sorted([player for player in winners if player not in losers])

        # List of players who lost exactly one match
        answer[1] = sorted([player for player in losers if losers[player] == 1])       

        return answer
