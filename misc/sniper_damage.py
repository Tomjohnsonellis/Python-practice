"""
I'm currently part of a gaming group for "Dark Heresy"
The character I'm playing is a sniper and I wanted to know what kind of damage he'd do.
"""


import matplotlib.pyplot as plt
import random

def calculate_damage(degrees_of_success:int) -> int:
    if degrees_of_success == 0:
        return 0

    damage = 0
    if degrees_of_success == 2 or degrees_of_success == 3:
        damage += random.randint(1, 10)
    elif degrees_of_success >= 4:
        damage += random.randint(1, 10)
        damage += random.randint(1, 10)

    damage += random.randint(1, 10) + 4
    return damage


def calculate_degrees_of_success(ballistic_skill:int, roll_result:int) -> int:
    if roll_result > ballistic_skill:
        return 0

    degrees = 1 + ((ballistic_skill - roll_result) // 10)
    return degrees


def simulate_attack(simulations:int=1000, ballistic_skill:int=85) -> list:
    attack_results = []
    for attack in range(0,simulations):
        dice_roll = random.randint(1,100)
        if dice_roll != 100:
            attack_results.append(calculate_damage(calculate_degrees_of_success(ballistic_skill, dice_roll)))
        else:
            attack_results.append(0)

    return attack_results

def plot_results(attack_data:list, ballistic_skill) -> None:
    plt.hist(attack_data, density=False, bins=len(set(results)))
    # plt.hist(attack_data, bins=len(set(attack_data)))
    plt.title("Sniper Rifle Damage")
    plt.xlabel("Damage Dealt")
    plt.ylabel("Occurrences")
    summary_info = get_attack_summary(attack_data)
    # text_lines = []
    # for x in summary_info:
    #     text_lines.append(x +"\n")

    # plt.text(0.99,0.01, text_lines)


    textstr = '\n'.join((
        "Ballistic Skill: {}".format(ballistic_skill),
        summary_info[0],
        summary_info[1],
        summary_info[2],
        summary_info[3],
        summary_info[4],
    ))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.text(x=max(attack_data)*0.5, y=attack_data.count(0)*0.75, s=textstr, bbox=props)

    plt.savefig("sniper_stats.png")
    plt.show()
    return


def calculate_miss_rate(attack_data:list) -> str:
    misses = attack_data.count(0)
    accuracy =  misses/len(attack_data)
    accuracy = round(accuracy * 100, 2)
    return "{}%".format(accuracy)



def get_attack_summary(attack_data:list, printout:bool=False) -> list:
    attack_stats = []
    attack_stats.append("Shots Fired: {}".format(len(attack_data)))
    attack_stats.append("Minimum Damage: {}".format(min(attack_data)))
    attack_stats.append("Maximum Damage: {}".format(max(attack_data)))
    average_damage = round((sum(attack_data) / len(attack_data)),2)
    attack_stats.append("Average Damage Dealt: {}".format(average_damage))
    attack_stats.append("Miss Rate: {}".format(calculate_miss_rate(attack_data)))

    if printout:
        print("----- Sniper Rifle Damage Summary -----")
        for x in attack_stats:
            print(x)
        print("-----")
    return attack_stats



if __name__ == '__main__':

    print("===== Sniper Damage Calculator =====")
    user_simulations = input("How many simulations? > ")
    if str(user_simulations) == "":
        user_simulations = 10000

    user_ballistic_skill = input("What is your ballistic skill? > ")
    if str(user_ballistic_skill) == "":
        user_ballistic_skill = 50

    results = simulate_attack(int(user_simulations), int(user_ballistic_skill))
    get_attack_summary(results, printout=True)
    plot_results(results, user_ballistic_skill)
