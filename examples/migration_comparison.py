"""
Oxford Matplotlib Theme - Migration from Plotly Guide
====================================================
Side-by-side comparison of Plotly and Matplotlib code for common plots.

This demonstrates how to migrate from oxford-plotly-theme to
oxford-matplotlib-theme with equivalent functionality.
"""

import numpy as np


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def example_1_basic_line_plot():
    """Example 1: Basic line plot comparison."""
    print_header("Example 1: Basic Line Plot")

    print("\n--- PLOTLY VERSION (oxford-plotly-theme) ---")
    plotly_code = """
import plotly.graph_objects as go
from oxford_plotly_theme import apply_oxford_theme, create_oxford_figure

apply_oxford_theme()

fig = create_oxford_figure(title='My Plot')
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 9], mode='lines', name='Data'))
fig.show()
"""
    print(plotly_code)

    print("\n--- MATPLOTLIB VERSION (oxford-matplotlib-theme) ---")
    matplotlib_code = """
import matplotlib.pyplot as plt
from oxford_matplotlib_theme import apply_oxford_theme

apply_oxford_theme()

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9], label='Data')
ax.set_title('My Plot')
ax.legend()
plt.show()
"""
    print(matplotlib_code)

    print("\nKEY DIFFERENCES:")
    print("  • Matplotlib returns (fig, ax) tuple instead of single fig object")
    print("  • Use ax.plot() instead of fig.add_trace(go.Scatter())")
    print("  • Use ax.set_title() instead of title parameter in create_oxford_figure()")


def example_2_multi_series_plot():
    """Example 2: Multiple series plot."""
    print_header("Example 2: Multiple Series")

    print("\n--- PLOTLY VERSION ---")
    plotly_code = """
fig = create_oxford_figure()
fig.add_trace(go.Scatter(x=x, y=y1, name='Series 1'))
fig.add_trace(go.Scatter(x=x, y=y2, name='Series 2'))
fig.add_trace(go.Scatter(x=x, y=y3, name='Series 3'))
fig.show()
"""
    print(plotly_code)

    print("\n--- MATPLOTLIB VERSION ---")
    matplotlib_code = """
fig, ax = plt.subplots()
ax.plot(x, y1, label='Series 1')
ax.plot(x, y2, label='Series 2')
ax.plot(x, y3, label='Series 3')
ax.legend()
plt.show()
"""
    print(matplotlib_code)

    print("\nKEY DIFFERENCES:")
    print("  • Matplotlib automatically cycles through Oxford color palette")
    print("  • No need for separate add_trace calls - just multiple plot() calls")
    print("  • Legend must be called explicitly with ax.legend()")


def example_3_custom_colors():
    """Example 3: Using custom colors."""
    print_header("Example 3: Custom Colors")

    print("\n--- PLOTLY VERSION ---")
    plotly_code = """
from oxford_plotly_theme import OXFORD_COLORS, get_color_palette

# Single color
fig.add_trace(go.Scatter(..., marker=dict(color=OXFORD_COLORS['coral'])))

# Multiple colors from palette
colors = get_color_palette('vibrant', n_colors=3)
"""
    print(plotly_code)

    print("\n--- MATPLOTLIB VERSION ---")
    matplotlib_code = """
from oxford_matplotlib_theme import OXFORD_COLORS, get_palette

# Single color
ax.plot(x, y, color=OXFORD_COLORS['coral'])

# Multiple colors from palette
colors = get_palette('vibrant', n_colors=3)
for i, (data, color) in enumerate(zip(datasets, colors)):
    ax.plot(x, data, color=color, label=f'Series {i+1}')
"""
    print(matplotlib_code)

    print("\nKEY DIFFERENCES:")
    print("  • Function name: get_color_palette() → get_palette()")
    print("  • OXFORD_COLORS dictionary is identical in both")
    print("  • Color specification: marker=dict(color=...) → color=...")


def example_4_export_figures():
    """Example 4: Exporting figures."""
    print_header("Example 4: Exporting Figures")

    print("\n--- PLOTLY VERSION ---")
    plotly_code = """
from oxford_plotly_theme import save_oxford_figure

# Requires kaleido library (and Chrome browser in background)
save_oxford_figure(fig, 'plot.png', width=800, height=600, scale=2)
save_oxford_figure(fig, 'plot.svg')
"""
    print(plotly_code)

    print("\n--- MATPLOTLIB VERSION ---")
    matplotlib_code = """
from oxford_matplotlib_theme import save_oxford_figure

# No browser dependency - direct export
save_oxford_figure(fig, 'plot.png', dpi=300)
save_oxford_figure(fig, 'plot.svg')

# Or use matplotlib's native savefig:
fig.savefig('plot.pdf', dpi=300, bbox_inches='tight')
"""
    print(matplotlib_code)

    print("\nKEY DIFFERENCES:")
    print("  • Matplotlib: NO browser/kaleido dependency!")
    print("  • Size control: width/height in pixels → figsize in inches + DPI")
    print("  • Matplotlib supports more formats natively: PNG, SVG, PDF, EPS, TIFF")


def example_5_subplots():
    """Example 5: Multi-panel figures."""
    print_header("Example 5: Multi-Panel Figures (Subplots)")

    print("\n--- PLOTLY VERSION ---")
    plotly_code = """
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=2, subplot_titles=('A', 'B', 'C', 'D'))
fig.add_trace(go.Scatter(...), row=1, col=1)
fig.add_trace(go.Bar(...), row=1, col=2)
fig.add_trace(go.Scatter(...), row=2, col=1)
fig.add_trace(go.Box(...), row=2, col=2)
fig.update_layout(template='oxford')
"""
    print(plotly_code)

    print("\n--- MATPLOTLIB VERSION ---")
    matplotlib_code = """
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

axes[0, 0].plot(x, y)
axes[0, 0].set_title('A')

axes[0, 1].bar(categories, values)
axes[0, 1].set_title('B')

axes[1, 0].scatter(x, y)
axes[1, 0].set_title('C')

axes[1, 1].boxplot(data)
axes[1, 1].set_title('D')

plt.tight_layout()
"""
    print(matplotlib_code)

    print("\nKEY DIFFERENCES:")
    print("  • Matplotlib: axes is a 2D array → access with axes[row, col]")
    print("  • No need to specify row/col when adding traces - work directly on axes")
    print("  • Use plt.tight_layout() to automatically adjust spacing")


def example_6_presets():
    """Example 6: Using theme presets."""
    print_header("Example 6: Theme Presets")

    print("\n--- PLOTLY VERSION ---")
    plotly_code = """
# Plotly version doesn't have preset system
# Manual customization required
apply_oxford_theme()
fig = create_oxford_figure(width=1000, height=600)  # Larger for presentation
"""
    print(plotly_code)

    print("\n--- MATPLOTLIB VERSION ---")
    matplotlib_code = """
from oxford_matplotlib_theme import apply_preset

# Quick presets for different use cases
apply_preset('presentation')  # Larger fonts (1.4x)
apply_preset('poster')        # Extra large fonts (1.8x)
apply_preset('colorblind')    # Accessible palette
apply_preset('minimal')       # Clean with grid

fig, ax = plt.subplots()
# ... plotting code ...
"""
    print(matplotlib_code)

    print("\nNEW FEATURE:")
    print("  • Matplotlib version includes 7 pre-configured presets")
    print("  • Presets: default, presentation, print, colorblind, minimal, notebook, poster")
    print("  • Automatically adjusts fonts, colors, and styling for specific use cases")


def example_7_journal_export():
    """Example 7: Journal-specific export."""
    print_header("Example 7: Journal-Ready Export")

    print("\n--- PLOTLY VERSION ---")
    plotly_code = """
# Manual sizing for journals
fig = create_oxford_figure(width=350, height=250)  # Nature single-column
save_oxford_figure(fig, 'figure1.svg', scale=2)
"""
    print(plotly_code)

    print("\n--- MATPLOTLIB VERSION ---")
    matplotlib_code = """
from oxford_matplotlib_theme import get_journal_preset, save_oxford_figure

# Get preset for specific journal
preset = get_journal_preset('nature')
# Returns: {'figsize': (3.5, 2.5), 'dpi': 300, 'format': 'svg'}

fig, ax = plt.subplots(figsize=preset['figsize'])
# ... plotting code ...
save_oxford_figure(fig, 'figure1', format=preset['format'], dpi=preset['dpi'])
"""
    print(matplotlib_code)

    print("\nNEW FEATURE:")
    print("  • Built-in presets for Nature, PLOS, BMJ, Lancet")
    print("  • Automatically uses correct figure size, DPI, and format")
    print("  • Ensures compliance with journal requirements")


def example_8_branding():
    """Example 8: Adding Oxford branding."""
    print_header("Example 8: Oxford Branding/Watermark")

    print("\n--- PLOTLY VERSION ---")
    plotly_code = """
from oxford_plotly_theme import add_oxford_branding

add_oxford_branding(fig, watermark_text='Oxford University', position='bottom_right')
"""
    print(plotly_code)

    print("\n--- MATPLOTLIB VERSION ---")
    matplotlib_code = """
from oxford_matplotlib_theme import add_oxford_branding

add_oxford_branding(
    fig,
    add_watermark=True,
    watermark_text='University of Oxford',  # Note: correct Oxford wording
    position='bottom_right',
    opacity=0.5
)
"""
    print(matplotlib_code)

    print("\nKEY DIFFERENCES:")
    print("  • Matplotlib version uses 'University of Oxford' (official wording)")
    print("  • Must set add_watermark=True explicitly")
    print("  • Same position options: bottom_right, bottom_left, top_right, top_left")


def main():
    """Run all migration examples."""
    print("\n" + "=" * 70)
    print("OXFORD THEME: PLOTLY → MATPLOTLIB MIGRATION GUIDE")
    print("=" * 70)
    print("\nThis guide shows code comparisons for migrating from oxford-plotly-theme")
    print("to oxford-matplotlib-theme. Both themes maintain identical Oxford branding,")
    print("but matplotlib offers better performance and no browser dependencies.")
    print()

    # Run all examples
    example_1_basic_line_plot()
    example_2_multi_series_plot()
    example_3_custom_colors()
    example_4_export_figures()
    example_5_subplots()
    example_6_presets()
    example_7_journal_export()
    example_8_branding()

    print("\n" + "=" * 70)
    print("SUMMARY OF BENEFITS")
    print("=" * 70)
    print("\nMatplotlib version advantages:")
    print("  - No browser/kaleido dependency for image export")
    print("  - Faster rendering and export")
    print("  - Native support for more formats (PDF, EPS, TIFF)")
    print("  - Built-in theme presets (presentation, poster, colorblind, etc.)")
    print("  - Journal-specific export presets")
    print("  - Better integration with scientific Python ecosystem")
    print("  - Smaller file sizes for vector formats")
    print()
    print("Maintained features:")
    print("  • All 36 official Oxford colors")
    print("  • All 12 color palettes")
    print("  • Oxford Blue styling for axes and labels")
    print("  • Arial/Helvetica fonts")
    print("  • Watermark/branding support")
    print("=" * 70)


if __name__ == '__main__':
    main()
