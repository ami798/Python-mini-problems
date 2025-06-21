t = int(input())  

for _ in range(t):
    n, x = map(int, input().split())  
    a = list(map(int, input().split()))  

    a.sort(reverse=True)  
    teams = 0
    team_size = 0

    for skill in a:
        team_size += 1  
        if team_size * skill >= x:  
            teams += 1  # Form the team
            team_size = 0  # Reset for the next team

    print(teams)
