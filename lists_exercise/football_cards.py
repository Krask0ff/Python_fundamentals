text = input().split()

team_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
team_A_count = 11
team_B_count = 11

for i in text:
    if i in team_A:
        idx = team_A.index(i)
        if i in team_A:
            team_A.pop(idx)
            team_A_count -= 1
    if i in team_B:
        idx = team_B.index(i)
        if i in team_B:
            team_B.pop(idx)
            team_B_count -= 1
if team_A_count < 7 or team_B_count < 7:
    print(f"Team A - {team_A_count}; Team B - {team_B_count}")
    print("Game was terminated")
else:
    print(f"Team A - {team_A_count}; Team B - {team_B_count}")
