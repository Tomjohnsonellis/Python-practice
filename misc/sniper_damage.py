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


def simulate_attack(simulations=1000, ballistic_skill=85) -> list:
    attack_results = []
    for attack in range(1,simulations):
        dice_roll = random.randint(1,100)
        attack_results.append(calculate_damage(calculate_degrees_of_success(ballistic_skill, dice_roll)))

    return attack_results

def plot_results(attack_data:list):
    plt.hist(attack_data, bins=len(set(attack_data)))
    plt.title("Funny Sniper Damage")
    plt.show()
    return


def calculate_miss_rate(attack_data):
    misses = attack_data.count(0)
    accuracy =  misses/len(attack_data)
    accuracy = round(accuracy * 100, 2)
    return "{}% Miss Rate".format(accuracy)



def print_attack_summary(attack_data):
    print("----- Sniper Rifle Damage Summary -----")
    print("Shots Fired: {}".format(len(attack_data)))
    print("Minimum Damage: {}".format(min(attack_data)))
    print("Maximum Damage: {}".format(max(attack_data)))
    average_damage = round((sum(attack_data) / len(attack_data)),2)
    print("Average Damage Dealt: {}".format(average_damage))
    print("Miss Rate: {}".format(calculate_miss_rate(attack_data)))
    print("-----")
    return



if __name__ == '__main__':

    results = simulate_attack(1000001, 85)
    print_attack_summary(results)
    plot_results(results)
