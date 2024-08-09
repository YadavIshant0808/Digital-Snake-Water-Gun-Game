import random as r

# Initialize score counters
player_score = 0
bot_score = 0

def play_game():
    global player_score, bot_score
    
    print("Snake, Water & Gun game")
    l1 = ["Snake", "Water", "Gun"]
    c = r.randint(1, 3)
    print(f"1. {l1[0]} 2. {l1[1]} 3. {l1[2]}")
    user = int(input("Choose any one option. 1, 2 or 3\n"))
    
    try:
        if 0 < user < 4:
            if c == user:
                print(f"Bot and You Both Choose {l1[c-1]}\nTie")
            elif c == 1 and user == 2:
                print(f"Bot Choose {l1[c-1]} , Bot Wins ")
                bot_score += 1
            elif c == 1 and user == 3:
                print(f"Bot Choose {l1[c-1]} , You Win ")
                player_score += 1
            elif c == 2 and user == 1:
                print(f"Bot Choose {l1[c-1]} , You Win ")
                player_score += 1
            elif c == 2 and user == 3:
                print(f"Bot Choose {l1[c-1]} , Bot Wins ")
                bot_score += 1
            elif c == 3 and user == 1:
                print(f"Bot Choose {l1[c-1]} , Bot Wins ")
                bot_score += 1
            elif c == 3 and user == 2:
                print(f"Bot Choose {l1[c-1]} , You Win ")
                player_score += 1
    except Exception as e:
        print(e)

for i in range(5):
    play_game()

# After 5 rounds, display the total score and the winner
print("\nFinal Scores:")
print(f"You: {player_score}")
print(f"Bot: {bot_score}")

if player_score > bot_score:
    print("Congratulations! You are the Winner! 🏆")
elif player_score < bot_score:
    print("Bot Wins! Better luck next time!")
else:
    print("It's a Tie!\n")

#Author:-
print("Made by **Ishant Yadav** with ❤️ in India.")