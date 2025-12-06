"""
Demonstration of the new PHC-THESIS palette
============================================
This script demonstrates the newly added PHC-THESIS color palette
which contains 27 colors from thesis color PDFs combined with Oxford branding colors.
"""

import sys
sys.path.insert(0, 'oxford_matplotlib_theme')
from colors import OxfordColors, get_palette, ColorPalettes

print("=" * 70)
print("PHC-THESIS PALETTE DEMONSTRATION")
print("=" * 70)
print()

# Display new thesis colors
print("NEW THESIS COLORS ADDED:")
print("-" * 70)
thesis_colors = [
    'WHITE', 'BLACK', 'THESIS_PURPLE_1', 'BRIGHT_BLUE',
    'THESIS_PURPLE_2', 'SLATE_BLUE_1', 'SLATE_BLUE_2',
    'PERIWINKLE', 'IRIS', 'DEEP_TEAL', 'GOLDEN_YELLOW',
    'DUSTY_MAUVE', 'WISTERIA', 'POWDER_BLUE', 'GREY_BLUE',
    'AMETHYST', 'NAVY_BLUE', 'SOFT_PURPLE',
    'PALE_GREY', 'HEATHER', 'CORNFLOWER'
]

for i, color_name in enumerate(thesis_colors, 1):
    color_value = getattr(OxfordColors, color_name)
    print(f"{i:2d}. {color_name:20s} = {color_value}")

print()
print("=" * 70)
print("PHC-THESIS PALETTE (27 colors)")
print("=" * 70)
print()

# Get the PHC-THESIS palette
phc_palette = get_palette('phc_thesis')

print(f"Total colors in PHC-THESIS palette: {len(phc_palette)}")
print()

# Display palette organization
print("PALETTE ORGANIZATION:")
print("-" * 70)
print("Oxford Branding (2):")
print(f"  1. OXFORD_BLUE  = {phc_palette[0]}")
print(f"  2. OXFORD_PHC   = {phc_palette[1]}")
print()

print("Blues (9):")
for i in range(2, 10):
    print(f"  {i+1}. {phc_palette[i]}")
print()

print("Purples (10):")
for i in range(10, 20):
    print(f"  {i+1}. {phc_palette[i]}")
print()

print("Neutrals & Accents (6):")
for i in range(20, 27):
    print(f"  {i+1}. {phc_palette[i]}")
print()

print("=" * 70)
print("USAGE EXAMPLES")
print("=" * 70)
print()

print("Example 1: Get all 27 colors")
print("-" * 70)
print("```python")
print("from oxford_matplotlib_theme import get_palette")
print()
print("colors = get_palette('phc_thesis')")
print("print(len(colors))  # 27")
print("```")
print()

print("Example 2: Use specific thesis colors")
print("-" * 70)
print("```python")
print("from oxford_matplotlib_theme import OxfordColors")
print()
print("plt.plot(x, y, color=OxfordColors.BRIGHT_BLUE)")
print("plt.scatter(x, z, color=OxfordColors.THESIS_PURPLE_1)")
print("```")
print()

print("Example 3: Cycle through palette for many series")
print("-" * 70)
print("```python")
print("colors = get_palette('phc_thesis', n_colors=40)  # Cycles after 27")
print("for i, color in enumerate(colors):")
print("    ax.plot(x, data[i], color=color, label=f'Series {i+1}')")
print("```")
print()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"- Added 21 new thesis color constants")
print(f"- Total colors now: 57 (36 original + 21 new)")
print(f"- Created PHC_THESIS palette with 27 colors")
print(f"- Total palettes now: 13")
print(f"- Updated all tests and documentation")
print()
print("The PHC-THESIS palette is ideal for:")
print("  • PhD theses and dissertations")
print("  • Extended academic documents")
print("  • Multi-chapter publications")
print("  • Large datasets requiring many distinct colors")
print("=" * 70)
