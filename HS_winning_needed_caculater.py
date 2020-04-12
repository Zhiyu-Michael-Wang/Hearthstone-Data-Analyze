import random
import numpy as np
import matplotlib.pyplot as plt
test_time = 3000


def simulate_play(winning_rate, total_winning_needed, winning_streak):
    total_count = 0
    star_count = 0
    consist_winning_count = 0
    while(star_count < total_winning_needed and total_count <= 350):
        r = random.randint(1, 100)
        total_count += 1
        if(r <= 100 * winning_rate):
            consist_winning_count += 1
            star_bounce = (winning_streak - int(star_count / 15)) if (winning_streak - int(star_count / 15)) >= 1 else 1

            if(consist_winning_count >= 3):
                star_count += 2 * star_bounce
            else:
                star_count += star_bounce
        else:
            consist_winning_count = 0
            if not star_count % 15 == 0:
                star_count -= 1

    return total_count


def show_figure(all_total_counts, total_winning_needed, winning_streak, winning_rate):

    x = all_total_counts

    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(5, 8))

    ax0.hist(x[0], 40, density=1, histtype='stepfilled',
             facecolor='green', alpha=0.3)
    ax0.hist(x[1], 40, density=1, histtype='stepfilled',
             facecolor='yellow', alpha=0.3)
    ax0.hist(x[2], 40, density=1, histtype='stepfilled',
             facecolor='red', alpha=0.3)

    ax1.hist(x[0], 100, density=1, histtype='stepfilled',
             facecolor='green', alpha=0.3, cumulative=True, rwidth=0.8)
    ax1.hist(x[1], 100, density=1, histtype='stepfilled',
             facecolor='yellow', alpha=0.3, cumulative=True, rwidth=0.8)
    ax1.hist(x[2], 100, density=1, histtype='stepfilled',
             facecolor='red', alpha=0.3, cumulative=True, rwidth=0.8)

    ax0.set_title('--PDF-- \nStar needed: ' + str(total_winning_needed) +
                  '\nWinning streak bounce: ' + str(winning_streak) +
                  '\nExpected winning rate:  ' + str(winning_rate) + '±0.03')
    ax1.set_title('--CDF-- \nStar needed: ' + str(total_winning_needed) +
                  '\nWinning streak bounce: ' + str(winning_streak) +
                  '\nExpected winning rate:  ' + str(winning_rate) + '±0.03')
    fig.subplots_adjust(hspace=0.4)
    plt.show()


def main():
    all_total_counts = [[], [], []]
    COMPARE_NUM = 3
    UNCERTAINITY = 0.03
    total_winning_needed = int(input("Enter your expected stars to win: "))
    winning_streak = int(input("Enter your present winning streak: "))

    winning_rate = float(
        input("Enter your expected winning rate: "))

    winning_rates = [winning_rate + UNCERTAINITY, winning_rate, winning_rate - UNCERTAINITY]

    for ii in range(test_time):        
        for jj in range(COMPARE_NUM):
            total_count = simulate_play(winning_rates[jj], total_winning_needed, winning_streak)
            all_total_counts[jj].append(total_count)

    show_figure(all_total_counts, total_winning_needed, winning_streak, winning_rate)


if __name__ == "__main__":
    main()
