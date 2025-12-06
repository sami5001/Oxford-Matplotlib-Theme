"""
Oxford Matplotlib Theme - Publication-Ready Figures
===================================================
Demonstrates creating multi-panel journal-ready figures with proper sizing
and formatting for academic publications.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from oxford_matplotlib_theme import (
    apply_oxford_theme,
    get_palette,
    get_journal_preset,
    save_oxford_figure,
    add_oxford_branding
)

# Apply Oxford theme
apply_oxford_theme()


def example_1_2x2_panel():
    """Example 1: 2x2 multi-panel figure for publications."""
    print("Creating Example 1: 2x2 multi-panel figure...")

    fig = plt.figure(figsize=(12, 10))
    gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)

    colors = get_palette('primary', n_colors=4)

    # Panel A: Line plot
    ax1 = fig.add_subplot(gs[0, 0])
    x = np.linspace(0, 10, 100)
    ax1.plot(x, np.sin(x), color=colors[0], linewidth=2, label='sin(x)')
    ax1.plot(x, np.cos(x), color=colors[1], linewidth=2, label='cos(x)')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('(A) Temporal Pattern', fontweight='bold', loc='left')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)

    # Panel B: Bar chart
    ax2 = fig.add_subplot(gs[0, 1])
    categories = ['Control', 'Treatment A', 'Treatment B', 'Treatment C']
    values = [45, 68, 72, 85]
    errors = [5, 7, 6, 8]
    ax2.bar(categories, values, color=colors[0], alpha=0.8, edgecolor='white', linewidth=0.5)
    ax2.errorbar(categories, values, yerr=errors, fmt='none', color='black', capsize=5, linewidth=1.5)
    ax2.set_ylabel('Response Rate (%)')
    ax2.set_title('(B) Treatment Efficacy', fontweight='bold', loc='left')
    ax2.grid(True, axis='y', alpha=0.3)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')

    # Panel C: Scatter plot with regression
    ax3 = fig.add_subplot(gs[1, 0])
    np.random.seed(42)
    x_data = np.random.uniform(0, 100, 50)
    y_data = 2 * x_data + 10 + np.random.normal(0, 15, 50)
    ax3.scatter(x_data, y_data, s=80, color=colors[2], alpha=0.6,
                edgecolors='white', linewidth=0.5)

    # Add regression line
    z = np.polyfit(x_data, y_data, 1)
    p = np.poly1d(z)
    x_line = np.linspace(0, 100, 100)
    ax3.plot(x_line, p(x_line), color=colors[3], linewidth=2.5, linestyle='--',
             label=f'y = {z[0]:.2f}x + {z[1]:.1f}')

    ax3.set_xlabel('Predictor Variable')
    ax3.set_ylabel('Outcome Variable')
    ax3.set_title('(C) Correlation Analysis', fontweight='bold', loc='left')
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)

    # Panel D: Box plot
    ax4 = fig.add_subplot(gs[1, 1])
    data = [np.random.normal(100, 15, 100) for _ in range(4)]
    bp = ax4.boxplot(data, labels=categories, patch_artist=True, widths=0.6)

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    for median in bp['medians']:
        median.set(color='#002147', linewidth=2)

    ax4.set_ylabel('Measurement Value')
    ax4.set_title('(D) Distribution Comparison', fontweight='bold', loc='left')
    ax4.grid(True, axis='y', alpha=0.3)
    plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right')

    # Overall title
    fig.suptitle('Comprehensive Analysis of Treatment Effects',
                 fontsize=16, fontweight='bold', y=0.98)

    return fig


def example_2_3panel_horizontal():
    """Example 2: 3-panel horizontal figure."""
    print("Creating Example 2: 3-panel horizontal figure...")

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    colors = get_palette('vibrant', n_colors=3)

    # Generate sample data
    np.random.seed(42)

    # Panel A: Time series
    ax = axes[0]
    time = np.arange(0, 100)
    signal = np.cumsum(np.random.randn(100))
    ax.plot(time, signal, color=colors[0], linewidth=2)
    ax.fill_between(time, signal - 5, signal + 5, color=colors[0], alpha=0.2)
    ax.set_xlabel('Time Point')
    ax.set_ylabel('Signal Intensity')
    ax.set_title('(A) Time Series', fontweight='bold', loc='left')
    ax.grid(True, alpha=0.3)

    # Panel B: Heatmap
    ax = axes[1]
    data_2d = np.random.randn(10, 10)
    im = ax.imshow(data_2d, cmap='RdBu_r', aspect='auto', vmin=-2, vmax=2)
    ax.set_xlabel('Feature Index')
    ax.set_ylabel('Sample Index')
    ax.set_title('(B) Feature Matrix', fontweight='bold', loc='left')
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Value', rotation=270, labelpad=15)

    # Panel C: Violin plot
    ax = axes[2]
    data_violin = [np.random.normal(0, std, 100) for std in range(1, 5)]
    parts = ax.violinplot(data_violin, positions=range(1, 5),
                           showmeans=True, showmedians=True)

    # Color the violins
    for pc, color in zip(parts['bodies'], colors):
        pc.set_facecolor(color)
        pc.set_alpha(0.7)

    ax.set_xlabel('Group')
    ax.set_ylabel('Distribution')
    ax.set_title('(C) Group Variability', fontweight='bold', loc='left')
    ax.set_xticks(range(1, 5))
    ax.set_xticklabels([f'G{i}' for i in range(1, 5)])
    ax.grid(True, axis='y', alpha=0.3)

    plt.tight_layout()

    return fig


def example_3_journal_nature():
    """Example 3: Nature journal single-column figure."""
    print("Creating Example 3: Nature single-column figure...")

    # Get Nature preset
    preset = get_journal_preset('nature')

    fig, ax = plt.subplots(figsize=preset['figsize'])

    # Create publication-quality plot
    colors = get_palette('professional', n_colors=2)
    np.random.seed(42)

    x = np.linspace(0, 5, 100)
    y1 = np.exp(-x) * np.cos(2 * np.pi * x)
    y2 = np.exp(-x) * np.sin(2 * np.pi * x)

    ax.plot(x, y1, color=colors[0], linewidth=1.5, label='Component A')
    ax.plot(x, y2, color=colors[1], linewidth=1.5, label='Component B')

    ax.set_xlabel('Time (arbitrary units)', fontsize=8)
    ax.set_ylabel('Signal (arbitrary units)', fontsize=8)
    ax.legend(fontsize=7, framealpha=0.9)
    ax.grid(True, alpha=0.3)

    # Adjust tick label size for journal
    ax.tick_params(labelsize=7)

    plt.tight_layout()

    print(f"  Figure size: {preset['figsize']} inches")
    print(f"  Recommended DPI: {preset['dpi']}")
    print(f"  Recommended format: {preset['format']}")

    return fig


def example_4_journal_plos():
    """Example 4: PLOS journal double-column figure."""
    print("Creating Example 4: PLOS double-column figure...")

    # Get PLOS preset
    preset = get_journal_preset('plos')

    fig, axes = plt.subplots(1, 2, figsize=preset['figsize'])

    colors = get_palette('health', n_colors=3)

    # Left panel: Box plot comparison
    ax = axes[0]
    data = [np.random.normal(loc, 10, 100) for loc in [100, 110, 95]]
    bp = ax.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3'],
                     patch_artist=True, widths=0.6)

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.8)

    for median in bp['medians']:
        median.set(color='#002147', linewidth=2)

    ax.set_ylabel('Measurement (units)', fontsize=10)
    ax.set_title('A', fontweight='bold', loc='left', fontsize=12)
    ax.grid(True, axis='y', alpha=0.3)

    # Right panel: Scatter with error bars
    ax = axes[1]
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [20, 35, 30, 45, 50]
    y_err = [3, 4, 5, 4, 6]

    ax.errorbar(x_vals, y_vals, yerr=y_err, fmt='o', color=colors[0],
               markersize=8, capsize=5, capthick=2, linewidth=2, markeredgecolor='white')

    ax.set_xlabel('Treatment Duration (weeks)', fontsize=10)
    ax.set_ylabel('Response (%)', fontsize=10)
    ax.set_title('B', fontweight='bold', loc='left', fontsize=12)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    print(f"  Figure size: {preset['figsize']} inches")
    print(f"  Recommended DPI: {preset['dpi']}")
    print(f"  Recommended format: {preset['format']}")

    return fig


def main():
    """Run all examples."""
    print("=" * 70)
    print("Oxford Matplotlib Theme - Publication Figure Examples")
    print("=" * 70)
    print()

    # Create examples
    examples = [
        example_1_2x2_panel(),
        example_2_3panel_horizontal(),
        example_3_journal_nature(),
        example_4_journal_plos(),
    ]

    print()
    print("=" * 70)
    print(f"Created {len(examples)} publication-ready figures")
    print()
    print("To save for journal submission:")
    print("  save_oxford_figure(fig, 'figure1', format='svg', dpi=300)")
    print()
    print("Close the figure windows to exit")
    print("=" * 70)

    # Show all figures
    plt.show()


if __name__ == '__main__':
    main()
