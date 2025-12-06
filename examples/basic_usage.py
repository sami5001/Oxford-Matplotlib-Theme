"""
Oxford Matplotlib Theme - Basic Usage Examples
==============================================
Demonstrates basic plotting with Oxford University styling.

Run this script to see 6 fundamental plot types with Oxford branding.
"""

import numpy as np
import matplotlib.pyplot as plt
from oxford_matplotlib_theme import apply_oxford_theme, get_palette


# Apply Oxford theme globally
apply_oxford_theme()


def example_1_line_plot():
    """Example 1: Line plot with multiple series."""
    print("Creating Example 1: Line plot with multiple series...")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Generate data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.exp(-x/10)
    y4 = np.cos(x) * np.exp(-x/10)

    # Plot multiple series (will use Oxford color cycle)
    ax.plot(x, y1, label='sin(x)', linewidth=2)
    ax.plot(x, y2, label='cos(x)', linewidth=2)
    ax.plot(x, y3, label='sin(x)·exp(-x/10)', linewidth=2, linestyle='--')
    ax.plot(x, y4, label='cos(x)·exp(-x/10)', linewidth=2, linestyle='--')

    # Styling
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title('Trigonometric Functions with Decay')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def example_2_bar_chart():
    """Example 2: Bar chart with grouped bars."""
    print("Creating Example 2: Grouped bar chart...")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Data
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    group1 = [23, 45, 56, 78]
    group2 = [35, 52, 48, 65]
    group3 = [42, 38, 61, 55]

    # Bar positions
    x = np.arange(len(categories))
    width = 0.25

    # Create bars with Oxford colors
    colors = get_palette('primary', n_colors=3)
    ax.bar(x - width, group1, width, label='Group 1', color=colors[0])
    ax.bar(x, group2, width, label='Group 2', color=colors[1])
    ax.bar(x + width, group3, width, label='Group 3', color=colors[2])

    # Styling
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_title('Grouped Bar Chart Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    ax.grid(True, axis='y', alpha=0.3)

    plt.tight_layout()
    return fig


def example_3_scatter_plot():
    """Example 3: Scatter plot with color-coded groups."""
    print("Creating Example 3: Scatter plot with groups...")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Generate random data for three groups
    np.random.seed(42)
    n_points = 50

    # Group 1
    x1 = np.random.normal(2, 0.8, n_points)
    y1 = np.random.normal(2, 0.8, n_points)

    # Group 2
    x2 = np.random.normal(5, 0.8, n_points)
    y2 = np.random.normal(5, 0.8, n_points)

    # Group 3
    x3 = np.random.normal(8, 0.8, n_points)
    y3 = np.random.normal(3, 0.8, n_points)

    # Get colors from Oxford palette
    colors = get_palette('vibrant', n_colors=3)

    # Plot with different markers
    ax.scatter(x1, y1, s=100, alpha=0.6, color=colors[0], label='Group A', edgecolors='white', linewidth=0.5)
    ax.scatter(x2, y2, s=100, alpha=0.6, color=colors[1], label='Group B', edgecolors='white', linewidth=0.5)
    ax.scatter(x3, y3, s=100, alpha=0.6, color=colors[2], label='Group C', edgecolors='white', linewidth=0.5)

    # Styling
    ax.set_xlabel('Feature X')
    ax.set_ylabel('Feature Y')
    ax.set_title('Scatter Plot with Grouped Data')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def example_4_histogram():
    """Example 4: Histogram with distribution."""
    print("Creating Example 4: Histogram...")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Generate random data
    np.random.seed(42)
    data = np.random.normal(100, 15, 1000)

    # Create histogram with Oxford color
    colors = get_palette('primary')
    ax.hist(data, bins=30, color=colors[0], alpha=0.7, edgecolor='white', linewidth=0.5)

    # Add mean line
    mean_value = np.mean(data)
    ax.axvline(mean_value, color=colors[1], linestyle='--', linewidth=2, label=f'Mean = {mean_value:.1f}')

    # Styling
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Sample Data')
    ax.legend()
    ax.grid(True, axis='y', alpha=0.3)

    plt.tight_layout()
    return fig


def example_5_pie_chart():
    """Example 5: Pie chart with Oxford colors."""
    print("Creating Example 5: Pie chart...")

    fig, ax = plt.subplots(figsize=(10, 8))

    # Data
    sizes = [30, 25, 20, 15, 10]
    labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']

    # Get colors from celebratory palette
    colors = get_palette('celebratory', n_colors=5)

    # Create pie chart
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.85
    )

    # Style the text
    for text in texts:
        text.set_fontsize(11)

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)

    ax.set_title('Distribution by Category')

    plt.tight_layout()
    return fig


def example_6_box_plot():
    """Example 6: Box plot comparing distributions."""
    print("Creating Example 6: Box plot...")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Generate data for different groups
    np.random.seed(42)
    data1 = np.random.normal(100, 10, 100)
    data2 = np.random.normal(110, 15, 100)
    data3 = np.random.normal(95, 8, 100)
    data4 = np.random.normal(105, 12, 100)

    data = [data1, data2, data3, data4]
    labels = ['Treatment A', 'Treatment B', 'Treatment C', 'Treatment D']

    # Create box plot
    colors = get_palette('professional', n_colors=4)

    bp = ax.boxplot(data, labels=labels, patch_artist=True, widths=0.6)

    # Color the boxes
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    # Style whiskers, caps, and medians
    for whisker in bp['whiskers']:
        whisker.set(linewidth=1.5)

    for cap in bp['caps']:
        cap.set(linewidth=1.5)

    for median in bp['medians']:
        median.set(color='#002147', linewidth=2)  # Oxford Blue

    # Styling
    ax.set_ylabel('Measurement Value')
    ax.set_title('Comparison of Treatment Effects')
    ax.grid(True, axis='y', alpha=0.3)

    plt.tight_layout()
    return fig


def main():
    """Run all examples and display them."""
    print("=" * 70)
    print("Oxford Matplotlib Theme - Basic Usage Examples")
    print("=" * 70)
    print()

    # Create all examples
    examples = [
        example_1_line_plot(),
        example_2_bar_chart(),
        example_3_scatter_plot(),
        example_4_histogram(),
        example_5_pie_chart(),
        example_6_box_plot(),
    ]

    print()
    print("=" * 70)
    print(f"Created {len(examples)} example figures")
    print("Close the figure windows to exit")
    print("=" * 70)

    # Show all figures
    plt.show()


if __name__ == '__main__':
    main()
