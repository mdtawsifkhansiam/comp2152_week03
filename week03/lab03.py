import random

diceOptions = list(range(1, 7))

numLives = 10
mNumLives = 12
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

print("Available Weapons:")
for index, weapon in enumerate(weapons, start=1):
    print(f"{index}. {weapon}")

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Input must be an integer between {min_val} and {max_val}. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

combatStrength = get_valid_input("Enter your combat strength (1-6): ", 1, 6)
mCombatStrength = get_valid_input("Enter monster's combat strength (1-6): ", 1, 6)

print("\nStarting battle simulation...")
for round_num in range(1, 20, 2):
    hero_roll = random.choice(diceOptions)
    monster_roll = random.choice(diceOptions)
    hero_strength = combatStrength + hero_roll
    monster_strength = mCombatStrength + monster_roll
    hero_weapon = weapons[hero_roll - 1]
    monster_weapon = weapons[monster_roll - 1]

    print(f"\nRound {round_num}: Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {hero_strength}, Monster Total Strength: {monster_strength}.")

    if hero_strength > monster_strength:
        print("Hero wins the round!")
    elif hero_strength < monster_strength:
        print("Monster wins the round!")
    else:
        print("It's a tie!")
    if round_num == 11:
        print("\nBattle Truce declared in Round 11. Game Over!")
        break
