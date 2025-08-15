#!/usr/bin/env python3
import random
import matplotlib.pyplot as plt


# list of possible entries
entries = ["one", 
           "two two", 
           "three", "rrr", "rgmsd", "msfsd", "fnfsndfns", 'dsaa', 'wqwfsdss', 'fafsafsafasfasfas', 'fdsfds']

# generate grid and fill with entries
def generate_card(entries, size=3, free_space='free', output_file='bingo_card.png'):
    n_cells = size * size - (1 if free_space else 0) # FREE goes in the middle space of the grid
    # check if there are enough entries to fill up all spaces without repetitions
    # TODO break if fewer entries than size else continue

    selected = random.sample(entries, n_cells)

    # Insert FREE space in the center if free_space wanted, else leave string empty in def above
    # works only for size > 2
    if free_space:
        # TODO only insert if size odd
        mid = size // 2
        selected.insert(mid * size + mid, free_space)

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(size, size))
    ax.set_axis_off()

    # Draw grid and fill with text
    for i in range(size):
        for j in range(size):
            idx = i * size + j
            text = selected[idx]
            ax.text(j + 0.5, size - i - 0.5, text, ha='center', va='center', wrap=True, fontsize=10)
            ax.add_patch(plt.Rectangle((j, size - i - 1), 1, 1, fill=False, edgecolor='red'))

    ax.set_xlim(0, size)
    ax.set_ylim(0, size)

    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

generate_card(entries, output_file='custom_bingo.png')