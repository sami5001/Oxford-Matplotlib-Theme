# Migration Guide: Plotly → Matplotlib

Complete guide for migrating from `oxford-plotly-theme` to `oxford-matplotlib-theme`.

---

## Table of Contents

1. [Why Migrate?](#why-migrate)
2. [Installation](#installation)
3. [Quick Comparison](#quick-comparison)
4. [Import Changes](#import-changes)
5. [Function Mapping](#function-mapping)
6. [Code Translation Examples](#code-translation-examples)
7. [Common Gotchas](#common-gotchas)
8. [FAQ](#faq)

---

## Why Migrate?

### Benefits of Matplotlib Version

**No Browser Dependencies**
- Plotly requires kaleido library (which uses Chromium browser)
- Matplotlib exports natively - no hidden browser processes
- Faster and more reliable export

**Better Performance**
- Direct rendering without browser overhead
- Faster figure generation for large datasets
- Smaller file sizes for vector formats

**Native Format Support**
- Built-in support for PDF, EPS, TIFF
- Better LaTeX integration
- No quality loss in conversion

**New Features**
- 7 pre-configured presets (presentation, poster, colorblind, etc.)
- Journal-specific export presets (Nature, PLOS, BMJ, Lancet)
- Font scaling system
- Better integration with scientific Python ecosystem

**Easier Deployment**
- No system dependencies
- Works in headless environments
- Smaller installation footprint

### What Stays the Same

- All 36 official Oxford colors
- All 12 color palettes
- Oxford Blue styling
- Arial/Helvetica fonts
- Watermark/branding support

---

## Installation

### Uninstall Plotly Version (optional)

```bash
pip uninstall oxford-plotly-theme
```

### Install Matplotlib Version

```bash
# Clone repository
git clone https://github.com/sami5001/oxford-matplotlib-theme.git
cd oxford-matplotlib-theme

# Install
pip install -e .

# Or with all optional dependencies
pip install -e ".[all]"
```

---

## Quick Comparison

| Feature | Plotly | Matplotlib |
|---------|--------|------------|
| **Theme application** | `apply_oxford_theme()` | `apply_oxford_theme()` |
| **Figure creation** | `create_oxford_figure()` | `oxford_figure()` → returns `(fig, ax)` |
| **Color access** | `OXFORD_COLORS['coral']` | `OXFORD_COLORS['coral']` |
| **Palette function** | `get_color_palette()` | `get_palette()` or `get_color_palette()` |
| **Plotting** | `fig.add_trace(go.Scatter(...))` | `ax.plot(...)` |
| **Export** | `fig.write_image()` (needs kaleido) | `fig.savefig()` (native) |
| **Presets** | Not available | `apply_preset('presentation')` |
| **Journal sizes** | Manual | `get_journal_preset('nature')` |

---

## Import Changes

### Basic Imports

**Before (Plotly):**
```python
import plotly.graph_objects as go
from oxford_plotly_theme import (
    apply_oxford_theme,
    create_oxford_figure,
    OXFORD_COLORS,
    get_color_palette
)
```

**After (Matplotlib):**
```python
import matplotlib.pyplot as plt
from oxford_matplotlib_theme import (
    apply_oxford_theme,
    oxford_figure,  # Note: different name
    OXFORD_COLORS,
    get_palette     # Note: shorter name (or use get_color_palette)
)
```

### Additional Matplotlib Imports

```python
# For subplots
from matplotlib.gridspec import GridSpec  # Multi-panel figures

# For advanced styling
import matplotlib as mpl
```

---

## Function Mapping

### Theme Functions

| Plotly Function | Matplotlib Equivalent | Notes |
|----------------|----------------------|-------|
| `apply_oxford_theme()` | `apply_oxford_theme()` | Same API |
| `create_oxford_figure(title='...')` | `oxford_figure()` then `ax.set_title('...')` | Returns `(fig, ax)` |
| N/A | `apply_preset('presentation')` | New feature! |
| N/A | `reset_theme()` | Restore defaults |

### Color Functions

| Plotly Function | Matplotlib Equivalent | Notes |
|----------------|----------------------|-------|
| `OXFORD_COLORS['coral']` | `OXFORD_COLORS['coral']` | Identical |
| `get_color_palette('vibrant')` | `get_palette('vibrant')` | Shorter name |
| `OxfordColors.CORAL` | `OxfordColors.CORAL` | Identical |
| `ColorPalettes.PRIMARY` | `ColorPalettes.PRIMARY` | Identical |

### Export Functions

| Plotly Function | Matplotlib Equivalent | Notes |
|----------------|----------------------|-------|
| `fig.write_image('plot.png')` | `fig.savefig('plot.png', dpi=300, bbox_inches='tight')` | Native |
| `save_oxford_figure(fig, 'plot')` | `save_oxford_figure(fig, 'plot')` | Same API |
| N/A | `get_journal_preset('nature')` | New feature! |

### Branding Functions

| Plotly Function | Matplotlib Equivalent | Notes |
|----------------|----------------------|-------|
| `add_oxford_branding(fig, ...)` | `add_oxford_branding(fig, add_watermark=True, ...)` | Must set `add_watermark=True` |

---

## Code Translation Examples

### Example 1: Basic Line Plot

**Plotly:**
```python
import plotly.graph_objects as go
from oxford_plotly_theme import apply_oxford_theme, create_oxford_figure

apply_oxford_theme()

fig = create_oxford_figure(title='My Plot')
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 9], mode='lines', name='Data'))
fig.update_xaxes(title_text='X-axis')
fig.update_yaxes(title_text='Y-axis')
fig.show()
```

**Matplotlib:**
```python
import matplotlib.pyplot as plt
from oxford_matplotlib_theme import apply_oxford_theme

apply_oxford_theme()

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9], label='Data')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('My Plot')
ax.legend()
plt.show()
```

**Key Differences:**
- Matplotlib returns `(fig, ax)` tuple
- Use `ax.plot()` instead of `fig.add_trace()`
- Set labels/title on axes object

---

### Example 2: Multiple Series with Colors

**Plotly:**
```python
colors = get_color_palette('vibrant', n_colors=3)

fig = create_oxford_figure()
fig.add_trace(go.Scatter(x=x, y=y1, name='Series 1', line=dict(color=colors[0])))
fig.add_trace(go.Scatter(x=x, y=y2, name='Series 2', line=dict(color=colors[1])))
fig.add_trace(go.Scatter(x=x, y=y3, name='Series 3', line=dict(color=colors[2])))
fig.show()
```

**Matplotlib:**
```python
colors = get_palette('vibrant', n_colors=3)

fig, ax = plt.subplots()
ax.plot(x, y1, color=colors[0], label='Series 1')
ax.plot(x, y2, color=colors[1], label='Series 2')
ax.plot(x, y3, color=colors[2], label='Series 3')
ax.legend()
plt.show()
```

**Key Differences:**
- `get_color_palette()` → `get_palette()`
- `line=dict(color=...)` → `color=...`
- Simpler syntax overall

---

### Example 3: Bar Chart

**Plotly:**
```python
fig = go.Figure()
fig.add_trace(go.Bar(
    x=['A', 'B', 'C'],
    y=[1, 3, 2],
    marker=dict(color=OXFORD_COLORS['coral'])
))
fig.update_layout(template='oxford')
fig.show()
```

**Matplotlib:**
```python
apply_oxford_theme()

fig, ax = plt.subplots()
ax.bar(['A', 'B', 'C'], [1, 3, 2], color=OXFORD_COLORS['coral'])
plt.show()
```

**Key Differences:**
- Much simpler matplotlib syntax
- No need to update layout - theme already applied

---

### Example 4: Scatter Plot

**Plotly:**
```python
fig = create_oxford_figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(
        size=10,
        color=OXFORD_COLORS['aqua'],
        opacity=0.6
    ),
    name='Data Points'
))
fig.show()
```

**Matplotlib:**
```python
fig, ax = oxford_figure()
ax.scatter(x, y,
          s=100,  # Size in points^2 (10^2 = 100)
          color=OXFORD_COLORS['aqua'],
          alpha=0.6,
          label='Data Points')
ax.legend()
plt.show()
```

**Key Differences:**
- `mode='markers'` → use `ax.scatter()`
- `marker=dict(size=...)` → `s=...`
- `opacity` → `alpha`
- Size scale is different (Matplotlib uses points^2)

---

### Example 5: Subplots / Multi-Panel

**Plotly:**
```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=2, subplot_titles=('A', 'B', 'C', 'D'))

fig.add_trace(go.Scatter(x=x1, y=y1), row=1, col=1)
fig.add_trace(go.Bar(x=x2, y=y2), row=1, col=2)
fig.add_trace(go.Scatter(x=x3, y=y3), row=2, col=1)
fig.add_trace(go.Box(y=y4), row=2, col=2)

fig.update_layout(template='oxford')
fig.show()
```

**Matplotlib:**
```python
apply_oxford_theme()

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

axes[0, 0].plot(x1, y1)
axes[0, 0].set_title('A')

axes[0, 1].bar(x2, y2)
axes[0, 1].set_title('B')

axes[1, 0].scatter(x3, y3)
axes[1, 0].set_title('C')

axes[1, 1].boxplot(y4)
axes[1, 1].set_title('D')

plt.tight_layout()
plt.show()
```

**Key Differences:**
- `axes` is a 2D NumPy array → access with `axes[row, col]`
- Work directly on each axes object
- Use `plt.tight_layout()` for spacing
- No need to specify `row=, col=` when adding traces

---

### Example 6: Export to File

**Plotly:**
```python
# Requires kaleido library
import plotly.io as pio

fig = create_oxford_figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 9]))

# Export PNG
fig.write_image('plot.png', width=800, height=600, scale=2)

# Export SVG
fig.write_image('plot.svg')

# Or using save_oxford_figure
save_oxford_figure(fig, 'plot.png', width=800, height=600)
```

**Matplotlib:**
```python
# No kaleido needed!
fig, ax = oxford_figure(figsize=(8, 6))
ax.plot([1, 2, 3], [1, 4, 9])

# Export PNG
fig.savefig('plot.png', dpi=300, bbox_inches='tight')

# Export SVG
fig.savefig('plot.svg', bbox_inches='tight')

# Or using save_oxford_figure
save_oxford_figure(fig, 'plot', format='png', dpi=300)
```

**Key Differences:**
- NO browser/kaleido dependency!
- Figure size in inches + DPI (not pixels)
- `bbox_inches='tight'` removes whitespace
- Faster export

**Size Conversion:**
- Plotly: `width=800, height=600` pixels
- Matplotlib: `figsize=(8, 6)` inches at `dpi=100` = 800×600 pixels

---

### Example 7: ROC Curve (Clinical ML)

**Plotly:**
```python
from sklearn.metrics import roc_curve, auc

fpr, tpr, _ = roc_curve(y_true, y_pred)
roc_auc = auc(fpr, tpr)

fig = create_oxford_figure()
fig.add_trace(go.Scatter(
    x=fpr,
    y=tpr,
    mode='lines',
    name=f'AUC = {roc_auc:.3f}',
    line=dict(color=OXFORD_COLORS['oxford_blue'], width=3)
))
fig.add_trace(go.Scatter(
    x=[0, 1],
    y=[0, 1],
    mode='lines',
    name='Random',
    line=dict(color='black', dash='dash')
))
fig.update_xaxes(title='FPR')
fig.update_yaxes(title='TPR')
fig.show()
```

**Matplotlib:**
```python
from sklearn.metrics import roc_curve, auc

fpr, tpr, _ = roc_curve(y_true, y_pred)
roc_auc = auc(fpr, tpr)

fig, ax = oxford_figure(figsize=(8, 8))
ax.plot(fpr, tpr, color=OXFORD_COLORS['oxford_blue'],
       linewidth=3, label=f'AUC = {roc_auc:.3f}')
ax.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random')

ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_title('ROC Curve')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)
plt.show()
```

**Key Differences:**
- Simpler matplotlib syntax
- Built-in grid support with `ax.grid()`
- Easier to add reference lines

---

## Common Gotchas

### 1. Figure Creation Returns Different Types

**Wrong:**
```python
fig = oxford_figure()  # This is wrong!
fig.plot([1, 2, 3], [1, 4, 9])  # Error: Figure has no plot method
```

**Correct:**
```python
fig, ax = oxford_figure()  # Returns tuple
ax.plot([1, 2, 3], [1, 4, 9])  # Use ax, not fig
```

### 2. Legend Must Be Called Explicitly

**Wrong:**
```python
ax.plot(x, y, label='Data')  # Label set but legend not shown
```

**Correct:**
```python
ax.plot(x, y, label='Data')
ax.legend()  # Must call legend() to show it
```

### 3. Grid is Not Automatic

**Wrong:**
```python
ax.plot(x, y)  # No grid shown by default
```

**Correct:**
```python
ax.plot(x, y)
ax.grid(True, alpha=0.3)  # Add grid explicitly
```

### 4. Marker Size Scale is Different

Plotly uses pixels, Matplotlib uses points squared:

```python
# Plotly
marker=dict(size=10)  # 10 pixels

# Matplotlib
s=100  # Area in points^2 (roughly 10-point diameter)
```

### 5. Color Specification Syntax

```python
# Plotly
line=dict(color='#FF0000', width=2)
marker=dict(color='#FF0000', size=10)

# Matplotlib
color='#FF0000', linewidth=2
color='#FF0000', s=100
```

### 6. Export File Extensions

Matplotlib is stricter about file extensions:

```python
# Plotly - infers format
fig.write_image('plot.png')
fig.write_image('plot.svg')

# Matplotlib - can specify format OR use extension
fig.savefig('plot.png')  # Infers PNG from extension
fig.savefig('plot', format='svg')  # Must specify format if no extension
```

### 7. Figure Size Units

```python
# Plotly - pixels
create_oxford_figure(width=800, height=600)

# Matplotlib - inches
oxford_figure(figsize=(8, 6))  # At default 100 DPI = 800×600 pixels
```

**Conversion:** `pixels = inches × DPI`

### 8. Subplot Indexing

```python
# Plotly
fig.add_trace(..., row=1, col=1)  # 1-indexed

# Matplotlib
axes[0, 0].plot(...)  # 0-indexed
```

---

## New Features in Matplotlib Version

### 1. Theme Presets

Not available in Plotly version!

```python
from oxford_matplotlib_theme import apply_preset

# Larger fonts for presentations
apply_preset('presentation')  # 1.4x font scale

# Extra large for posters
apply_preset('poster')  # 1.8x font scale

# Accessible colors
apply_preset('colorblind')
```

### 2. Journal Export Presets

Not available in Plotly version!

```python
from oxford_matplotlib_theme import get_journal_preset

# Get Nature journal settings
preset = get_journal_preset('nature')
# Returns: {'figsize': (3.5, 2.5), 'dpi': 300, 'format': 'svg'}

# Create journal-sized figure
fig, ax = oxford_figure(figsize=preset['figsize'])
ax.plot(x, y)
save_oxford_figure(fig, 'figure1', format=preset['format'], dpi=preset['dpi'])
```

Available presets: `'nature'`, `'nature_double'`, `'plos'`, `'bmj'`, `'lancet'`

### 3. Font Scaling

```python
# Scale all fonts by 1.5x
apply_oxford_theme(font_scale=1.5)

# Or use presets
apply_preset('presentation')  # font_scale=1.4
apply_preset('poster')  # font_scale=1.8
```

### 4. Custom Color Cycles

```python
# Set custom color order
custom_colors = ['coral', 'aqua', 'vivid_green', 'oxford_blue']
apply_oxford_theme(color_cycle=custom_colors)

# Now plots automatically use these colors in order
ax.plot(x, y1)  # Uses coral
ax.plot(x, y2)  # Uses aqua
ax.plot(x, y3)  # Uses vivid_green
```

---

## FAQ

**Q: Do I need to uninstall oxford-plotly-theme?**

A: No, they can coexist. They have different package names.

**Q: Will my Plotly code break?**

A: No, the Plotly theme continues to work independently.

**Q: Can I use both themes in the same script?**

A: Yes, but not simultaneously on the same figure. Use one or the other.

**Q: How long does migration typically take?**

A: Simple plots: 5-10 minutes. Complex multi-panel figures: 20-30 minutes.

**Q: What about interactive features?**

A: Matplotlib is primarily for static figures. For interactivity, stick with Plotly.

**Q: Can I export to the same formats?**

A: Yes! Matplotlib supports SVG, PNG, PDF, TIFF, EPS natively.

**Q: Is the color accuracy identical?**

A: Yes! All hex codes are identical between versions.

**Q: What about 3D plots?**

A: Both support 3D via `go.Scatter3d` (Plotly) and `ax = fig.add_subplot(111, projection='3d')` (Matplotlib).

**Q: Will matplotlib figures look exactly like Plotly ones?**

A: Very similar! Minor differences in default spacings and fonts, but all Oxford branding is identical.

**Q: Can I convert existing Plotly code automatically?**

A: No automatic converter, but the patterns are consistent. Most conversions are straightforward replacements.

---

## Migration Checklist

- [ ] Install `oxford-matplotlib-theme`
- [ ] Update imports (`plotly` → `matplotlib.pyplot`)
- [ ] Change `create_oxford_figure()` → `oxford_figure()`
- [ ] Update `fig.add_trace(go.Scatter(...))` → `ax.plot(...)`
- [ ] Change `get_color_palette()` → `get_palette()`
- [ ] Update subplot creation (`make_subplots` → `plt.subplots`)
- [ ] Change export (`fig.write_image()` → `fig.savefig()`)
- [ ] Add `ax.legend()` calls where needed
- [ ] Add `ax.grid()` calls where appropriate
- [ ] Update figure sizes (pixels → inches)
- [ ] Test all exports (SVG, PNG, PDF)
- [ ] Verify colors and styling match expectations

---

## Getting Help

- See `examples/migration_comparison.py` for side-by-side code examples
- Check `docs/API_REFERENCE.md` for complete function documentation
- Review `examples/basic_usage.py` and `examples/clinical_ml.py` for patterns
- Report issues on GitHub

---

**Happy migrating!** The matplotlib version offers better performance, no browser dependencies, and new features while maintaining all the Oxford branding you know.
