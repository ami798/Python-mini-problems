
n = int(input())
cards = list(map(int, input().split()))


nahom_score = 0
mikeyas_score = 0
left = 0
right = n - 1
turn = 0  
while left <= right:
    if cards[left] >= cards[right]:
        chosen_card = cards[left]
        left += 1
    else:
        chosen_card = cards[right]
        right -= 1

    if turn == 0:
        nahom_score += chosen_card
    else:
        mikeyas_score += chosen_card

    
    turn = 1 - turn

print(nahom_score, mikeyas_score)
