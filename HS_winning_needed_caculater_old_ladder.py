import random
import numpy as np
import matplotlib.pyplot as plt
test_time = 3000


def simulate_play(winning_rate, total_winning_needed):
    total_count = 0
    winning_count = 0
    consist_winning_count = 0
    while(winning_count < total_winning_needed and total_count <= 999):
        r = random.randint(1, 100)
        total_count += 1
        if(r <= 100 * winning_rate):
            consist_winning_count += 1

            if(consist_winning_count >= 3):
                winning_count += 2
            else:
                winning_count += 1
        else:
            consist_winning_count = 0
            winning_count -= 1

    return total_count


def show_figure(all_total_counts, total_winning_needed):

    x = all_total_counts

    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(5, 8))

    ax0.hist(x[0], 40, density=1, histtype='stepfilled',
             facecolor='yellow', alpha=0.5)

    ax0.hist(x[1], 40, density=1, histtype='stepfilled',
             facecolor='yellowgreen', alpha=0.5)

    ax0.hist(x[2], 40, density=1, histtype='stepfilled',
             facecolor='green', alpha=0.5)

    ax1.hist(x[0], 100, density=1, histtype='stepfilled',
             facecolor='yellow', alpha=0.5, cumulative=True, rwidth=0.8)
    ax1.hist(x[1], 100, density=1, histtype='stepfilled',
             facecolor='yellowgreen', alpha=0.5, cumulative=True, rwidth=0.8)
    ax1.hist(x[2], 100, density=1, histtype='stepfilled',
             facecolor='green', alpha=0.5, cumulative=True, rwidth=0.8)

    ax0.set_title('PDF of total game play for winning \n' + str(total_winning_needed) +
                  " stars in HS")
    ax1.set_title('CDF of total game play for winning \n' + str(total_winning_needed) +
                  " stars in HS")
    fig.subplots_adjust(hspace=0.4)
    plt.show()


def main():
    all_total_counts = [[], [], []]
    compare_num = 3
    total_winning_needed = int(input("Enter your expected stars to win: "))
    for jj in range(0, compare_num):
        winning_rate = float(
            input("Enter your expected winning rate for figure %i: " % (jj+1)))

        for ii in range(test_time):
            ii = ii
            total_count = simulate_play(winning_rate, total_winning_needed)
            all_total_counts[jj].append(total_count)

    show_figure(all_total_counts, total_winning_needed)


if __name__ == "__main__":
    main()
