#!/usr/bin/env python3
import random
import matplotlib.pyplot as plt
import textwrap
import os

# CONFIG
NUM_CARDS = 10
GRID_SIZE = 3
FREE_SPACE = 'free: Verspätung' # e.g. "free: Verspätung" or "" if grid size even
TITLE = "Verspätungs-Bingo"
SAVE_FOLDER = "3x3_bingo_cards"

os.makedirs(SAVE_FOLDER, exist_ok=True)

# list of possible entries
entries = ["Signalstörung",
           "Arbeiten an der Strecke",
           "Personen auf Gleisen",
           "Halt durch belegten Bahnhof",
           "Halt durch überholenden Zug",
           "WC außer Betrieb",
           "Reservierungsanzeigen defekt",
           "Ersatzzug",
           "Warten auf Fahrgäste eines anderen Zuges",
           "Zugausfall",
           "Anschlusszug wartet",
           "Anschlusszug wartet nicht",
           "Laute Menschen im Ruhebereich",
           "Stark riechendes Essen",
           "Witzige Lautsprecheransagen",
           "Verspätung weil nur ein Gleis verfügbar ist",
           "Komfort Check-In nicht verfügbar",
           "Oberleitungstörung",
           "Wagen fehlt",
           "Geänderte Wagenreihung",
           "Klima defekt",
           "Kein Bordrestaurant",
           "Keine Fahrradmitnahme möglich",
           "Warten auf Zugpersonal",
           "Zugpersonalausfall",
           "Weichenstörung",
           "Warten auf Gegenzug",
           "Außerplanmäßiger Halt",
           "Schreiende Kinder",
           "Ersatzvekehr mit Bussen",
           "Bombenentschärfung",
           "Polizeikontrolle",
           "Notarzteinsatz",
           "Brand auf der Strecke",
           "Sturmschäden",
           "kein WLAN"
]

def wrap_text(text, width=15):
    return "\n".join(textwrap.wrap(text, width=width))


# generate grid and fill with entries
def generate_card(entries, size, free_space, output_file, title):
    n_cells = size * size - (1 if free_space else 0)

    if len(entries) < n_cells:
        raise ValueError("Not enough entries to fill the bingo card.")

    if free_space and size % 2 == 0:
        raise ValueError("FREE space can only be used in odd-sized grids.")
    
    selected = random.sample(entries, n_cells)

    if free_space:
        mid = size // 2
        selected.insert(mid * size + mid, free_space)

    fig, ax = plt.subplots(figsize=(size, size))
    ax.set_axis_off()

    if title:
        fig.text(0.5, 1.02, title, ha='center', va='bottom', fontsize=16)

    # Draw grid and fill with text
    for i in range(size):
        for j in range(size):
            idx = i * size + j
            wrapped = wrap_text(selected[idx], width=15) # keep in bounds of grid
            ax.text(j + 0.5, size - i - 0.5, wrapped, ha='center', va='center', wrap=True, fontsize=5)
            ax.add_patch(plt.Rectangle((j, size - i - 1), 1, 1, fill=False, edgecolor='black'))

    ax.set_xlim(0, size)
    ax.set_ylim(0, size)

    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

for i in range(1, NUM_CARDS + 1):
    #filename = f"bingo_{i:02}.png"
    filename = os.path.join(SAVE_FOLDER, f"bingo_{i:02}.png")
    generate_card(entries, size=GRID_SIZE, free_space=FREE_SPACE, output_file=filename, title=TITLE)
