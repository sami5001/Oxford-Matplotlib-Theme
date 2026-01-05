# API Reference

Complete API documentation for `oxford-matplotlib-theme`.

---

## Table of Contents

- [Module Overview](#module-overview)
- [Colors Module](#colors-module)
- [Styles Module](#styles-module)
- [Presets Module](#presets-module)
- [Utils Module](#utils-module)
- [Usage Patterns](#usage-patterns)

---

## Module Overview

The package is organized into four main modules:

- **`colors`**: Color definitions and palettes
- **`styles`**: Theme application and figure creation
- **`presets`**: Pre-configured theme variants
- **`utils`**: Branding and export utilities

All functions can be imported from the top level:

```python
from oxford_matplotlib_theme import (
    # Styles
    apply_oxford_theme,
    oxford_figure,
    reset_theme,

    # Colors
    OXFORD_COLORS,
    OXFORD_PALETTE,
    get_palette,

    # Presets
    apply_preset,
    list_presets,

    # Utils
    save_oxford_figure,
    get_journal_preset,
)
```

---

## Colors Module

### OxfordColors Class

Static class containing all 56 official Oxford University brand colors as class attributes (35 brand + 21 thesis colors).

**Attributes:**

#### Primary Color
- `OXFORD_BLUE` - `#002147` (Pantone 282C) - Primary signature color

#### PHC Accent
- `OXFORD_PHC` - `#8A1751` - PHC Department accent

#### Secondary Colors (23 colors)
- `MAUVE` - `#776885` (Pantone 667C)
- `PEACH` - `#E08D79` (Pantone 4051C)
- `POTTERS_PINK` - `#ED9390` (Pantone 2339C)
- `DUSK` - `#C4A29E` (Pantone 6030C)
- `LILAC` - `#D1BDD5` (Pantone 524C)
- `SIENNA` - `#994636` (Pantone 4036C)
- `RED` - `#BE0F34` (Pantone 187C)
- `PLUM` - `#7F055F` (Pantone 2425C)
- `CORAL` - `#FE615A` (Pantone 178C)
- `LAVENDER` - `#D4CDF4` (Pantone 2635C)
- `ORANGE` - `#FB5607` (Pantone 1655C)
- `PINK` - `#E6007E` (Pantone 2385C)
- `GREEN` - `#426A5A` (Pantone 5545C)
- `OCEAN_GREY` - `#789E9E` (Pantone 2211C)
- `YELLOW_OCHRE` - `#E2C044` (Pantone 4016C)
- `COOL_GREY` - `#E4F0EF` (Pantone 7541C)
- `SKY_BLUE` - `#B9D6F2` (Pantone 277C)
- `SAGE_GREEN` - `#A0AF84` (Pantone 7494C)
- `VIRIDIAN` - `#15616D` (Pantone 5473C)
- `ROYAL_BLUE` - `#1D42A6` (Pantone 2126C)
- `AQUA` - `#00AAB4` (Pantone 7710C)
- `VIVID_GREEN` - `#65E5AE` (Pantone 3385C)
- `LIME_GREEN` - `#95C11F` (Pantone 2292C)
- `CERULEAN_BLUE` - `#49B6FF` (Pantone 292C)
- `LEMON_YELLOW` - `#F7EF66` (Pantone 3935C)

#### Neutral Colors (6 colors)
- `CHARCOAL` - `#211D1C` (Pantone 419C)
- `ASH_GREY` - `#61615F` (Pantone 6215C)
- `UMBER` - `#89827A` (Pantone 403C)
- `STONE_GREY` - `#D9D8D6` (Pantone Cool Gray 1C)
- `SHELL_GREY` - `#F1EEE9` (Pantone Warm Gray 1C)
- `OFF_WHITE` - `#F2F0F0` (Pantone 663C)

#### Metallic Colors (2 colors)
- `GOLD` - `#FFD700` (Pantone 10122C)
- `SILVER` - `#C0C0C0` (Pantone 10103C)

**Example:**
```python
from oxford_matplotlib_theme.colors import OxfordColors

# Access colors directly
oxford_blue = OxfordColors.OXFORD_BLUE  # '#002147'
coral = OxfordColors.CORAL  # '#FE615A'
```

---

### OXFORD_COLORS Dictionary

Dictionary providing lowercase snake_case access to all 56 colors.

**Type:** `Dict[str, str]`

**Keys:** 56 color names in lowercase with underscores

**Example:**
```python
from oxford_matplotlib_theme import OXFORD_COLORS

# Access by name (case-sensitive, lowercase)
oxford_blue = OXFORD_COLORS['oxford_blue']  # '#002147'
coral = OXFORD_COLORS['coral']  # '#FE615A'

# List all colors
for name, hex_code in OXFORD_COLORS.items():
    print(f"{name}: {hex_code}")
```

---

### OXFORD_PALETTE List

Default 8-color cycle used by the Oxford theme.

**Type:** `List[str]`

**Colors:** `['#002147', '#1D42A6', '#00AAB4', '#FE615A', '#65E5AE', '#FB5607', '#776885', '#49B6FF']`

Corresponds to: Oxford Blue, Royal Blue, Aqua, Coral, Vivid Green, Orange, Mauve, Cerulean Blue

**Rationale:**
- Starts with Oxford Blue (primary)
- Alternates cool and warm colors
- Maximizes distinction between adjacent colors
- Good contrast for colorblind users

**Example:**
```python
from oxford_matplotlib_theme import OXFORD_PALETTE

# Use in custom color cycle
apply_oxford_theme(color_cycle=OXFORD_PALETTE)

# Or access directly
first_color = OXFORD_PALETTE[0]  # '#002147'
```

---

### ColorPalettes Class

Static class containing 13 pre-defined color palettes for different visualization needs.

**Attributes:**

- **`PRIMARY`** (10 colors) - General purpose, most versatile
- **`PROFESSIONAL`** (6 colors) - Business/academic presentations
- **`VIBRANT`** (7 colors) - Eye-catching visualizations
- **`PASTEL`** (7 colors) - Softer, subtle visualizations
- **`DIVERGING`** (5 colors) - Data with meaningful center point
- **`SEQUENTIAL_BLUE`** (5 colors) - Continuous/ordered data
- **`HEALTH`** (5 colors) - Medical/PHC department specific
- **`TRADITIONAL`** (6 colors) - Heritage and stability
- **`CONTEMPORARY`** (6 colors) - Modern and clean
- **`CELEBRATORY`** (6 colors) - Festive and bright
- **`CORPORATE`** (6 colors) - Professional and formal
- **`INNOVATIVE`** (6 colors) - Tech-focused
- **`PHC_THESIS`** (27 colors) - Comprehensive thesis palette for academic work

**Example:**
```python
from oxford_matplotlib_theme.colors import ColorPalettes

# Access palette directly
vibrant_colors = ColorPalettes.VIBRANT
print(len(vibrant_colors))  # 7

# Use in plotting
for i, color in enumerate(ColorPalettes.PRIMARY):
    ax.plot(x, data[i], color=color)
```

---

### get_color()

Get a color hex code by name.

**Signature:**
```python
def get_color(name: str) -> str
```

**Parameters:**
- `name` (str): Color name (case-sensitive, lowercase with underscores)

**Returns:**
- `str`: Hex color code (e.g., '#002147')

**Raises:**
- `ValueError`: If color name is not found

**Example:**
```python
from oxford_matplotlib_theme import get_color

# Get specific colors
oxford_blue = get_color('oxford_blue')  # '#002147'
coral = get_color('coral')  # '#FE615A'

# Use in plotting
ax.plot(x, y, color=get_color('aqua'))
```

---

### get_palette()

Get a color palette by name.

**Signature:**
```python
def get_palette(palette_name: str = 'primary', n_colors: Optional[int] = None) -> List[str]
```

**Parameters:**
- `palette_name` (str, default='primary'): Palette name (case-insensitive)
  - Options: 'primary', 'professional', 'vibrant', 'pastel', 'diverging', 'sequential_blue', 'health', 'traditional', 'contemporary', 'celebratory', 'corporate', 'innovative', 'phc_thesis'
- `n_colors` (int, optional): Number of colors to return
  - If `None`, returns all colors in palette
  - If greater than palette length, cycles through palette

**Returns:**
- `List[str]`: List of hex color codes

**Example:**
```python
from oxford_matplotlib_theme import get_palette

# Get full palette
vibrant = get_palette('vibrant')  # 7 colors

# Get specific number of colors
colors = get_palette('professional', n_colors=3)  # First 3 colors

# Cycle if requesting more than available
colors = get_palette('diverging', n_colors=10)  # DIVERGING has 5, returns 10 by cycling

# Use with plots
colors = get_palette('health', n_colors=4)
for i, color in enumerate(colors):
    ax.plot(x, data[i], color=color, label=f'Series {i+1}')
```

**Note:** Returns a copy of the palette to prevent mutation.

---

### get_color_palette()

Alias for `get_palette()` for compatibility with oxford-plotly-theme.

**Signature:**
```python
def get_color_palette(palette_name: str = 'primary', n_colors: Optional[int] = None) -> List[str]
```

Identical to `get_palette()`. Use whichever name you prefer.

---

## Styles Module

### apply_oxford_theme()

Apply Oxford University theme to all matplotlib figures globally.

**Signature:**
```python
def apply_oxford_theme(
    style_base: str = 'seaborn-v0_8-paper',
    color_cycle: Optional[List[str]] = None,
    font_scale: float = 1.0
) -> None
```

**Parameters:**
- `style_base` (str, default='seaborn-v0_8-paper'): Base matplotlib style
  - Options: 'seaborn-v0_8-paper', 'seaborn-v0_8-notebook', 'seaborn-v0_8-whitegrid', etc.
- `color_cycle` (List[str], optional): Custom color cycle
  - Can be color names (e.g., 'oxford_blue') or hex codes (e.g., '#002147')
  - If `None`, uses `OXFORD_PALETTE`
- `font_scale` (float, default=1.0): Multiplier for all font sizes
  - Use >1.0 for larger fonts (e.g., 1.4 for presentations)
  - Use <1.0 for smaller fonts

**Returns:**
- `None`: Modifies matplotlib rcParams in place

**rcParams Modified:**
- `axes.prop_cycle`: Oxford color cycle
- `axes.labelcolor`: Oxford Blue
- `axes.edgecolor`: Oxford Blue
- `text.color`: Oxford Blue
- `xtick.color`: Oxford Blue
- `ytick.color`: Oxford Blue
- `font.sans-serif`: ['Arial', 'Helvetica', 'DejaVu Sans', 'sans-serif']
- `legend.edgecolor`: Oxford Blue
- `figure.facecolor`: 'white'
- `axes.facecolor`: 'white'
- Font sizes (if `font_scale != 1.0`)

**Example:**
```python
from oxford_matplotlib_theme import apply_oxford_theme

# Basic usage
apply_oxford_theme()

# With larger fonts for presentation
apply_oxford_theme(font_scale=1.4)

# With custom color cycle
apply_oxford_theme(color_cycle=['coral', 'aqua', 'oxford_blue'])

# With different base style
apply_oxford_theme(style_base='seaborn-v0_8-whitegrid')
```

---

### oxford_figure()

Create a matplotlib figure with Oxford styling applied.

**Signature:**
```python
def oxford_figure(
    figsize: Tuple[float, float] = (10, 6),
    style_base: str = 'seaborn-v0_8-paper',
    color_cycle: Optional[List[str]] = None,
    font_scale: float = 1.0,
    **kwargs
) -> Tuple[Figure, Axes]
```

**Parameters:**
- `figsize` (tuple, default=(10, 6)): Figure size in inches (width, height)
- `style_base` (str, default='seaborn-v0_8-paper'): Base style
- `color_cycle` (List[str], optional): Custom color cycle
- `font_scale` (float, default=1.0): Font size multiplier
- `**kwargs`: Additional arguments passed to `plt.subplots()`

**Returns:**
- `tuple`: (Figure, Axes) - Matplotlib Figure and Axes objects

**Example:**
```python
from oxford_matplotlib_theme import oxford_figure

# Basic usage
fig, ax = oxford_figure()
ax.plot([1, 2, 3], [1, 4, 9])
plt.show()

# Custom size for journal
fig, ax = oxford_figure(figsize=(3.5, 2.5))

# With presentation fonts
fig, ax = oxford_figure(font_scale=1.4)

# Pass additional kwargs
fig, ax = oxford_figure(dpi=150)
```

---

### reset_theme()

Reset matplotlib to default settings, removing Oxford theme.

**Signature:**
```python
def reset_theme() -> None
```

**Parameters:** None

**Returns:** None

**Example:**
```python
from oxford_matplotlib_theme import apply_oxford_theme, reset_theme

apply_oxford_theme()
# ... create plots ...

reset_theme()  # Back to matplotlib defaults
```

---

### get_oxford_rcparams()

Get Oxford theme rcParams as a dictionary without applying them.

**Signature:**
```python
def get_oxford_rcparams(
    style_base: str = 'seaborn-v0_8-paper',
    color_cycle: Optional[List[str]] = None,
    font_scale: float = 1.0
) -> dict
```

**Parameters:**
Same as `apply_oxford_theme()`

**Returns:**
- `dict`: Dictionary of rcParams with Oxford theme settings

**Example:**
```python
from oxford_matplotlib_theme import get_oxford_rcparams

# Inspect theme settings
params = get_oxford_rcparams()
print(params['axes.labelcolor'])  # '#002147'

# Check scaled font sizes
params_scaled = get_oxford_rcparams(font_scale=1.5)
print(params_scaled['font.size'])
```

---

## Presets Module

### PRESETS Dictionary

Dictionary of pre-configured theme variants.

**Type:** `Dict[str, Dict[str, Any]]`

**Available Presets:**

| Preset | Description | Font Scale | Base Style |
|--------|-------------|------------|------------|
| `default` | Standard for academic papers | 1.0 | seaborn-v0_8-paper |
| `presentation` | Larger fonts for slides | 1.4 | seaborn-v0_8-paper |
| `poster` | Extra large for posters | 1.8 | seaborn-v0_8-paper |
| `colorblind` | Accessible palette | 1.0 | seaborn-v0_8-paper |
| `minimal` | Clean with grid | 1.0 | seaborn-v0_8-whitegrid |
| `notebook` | Optimized for Jupyter | 1.1 | seaborn-v0_8-notebook |
| `print` | High contrast for printing | 1.0 | seaborn-v0_8-paper |

**Example:**
```python
from oxford_matplotlib_theme.presets import PRESETS

# Inspect preset configuration
print(PRESETS['presentation'])
# {'description': '...', 'style_base': '...', 'color_cycle': None, 'font_scale': 1.4}
```

---

### apply_preset()

Apply a pre-configured Oxford theme preset.

**Signature:**
```python
def apply_preset(preset_name: str) -> None
```

**Parameters:**
- `preset_name` (str): Preset name (case-insensitive)
  - Options: 'default', 'presentation', 'poster', 'colorblind', 'minimal', 'notebook', 'print'

**Returns:** None

**Raises:**
- `ValueError`: If preset name is not found

**Example:**
```python
from oxford_matplotlib_theme import apply_preset

# For presentations
apply_preset('presentation')  # 1.4x larger fonts

# For posters
apply_preset('poster')  # 1.8x larger fonts

# Accessible colors
apply_preset('colorblind')

# Case-insensitive
apply_preset('PRESENTATION')  # Works
```

---

### list_presets()

Print a formatted table of all available presets.

**Signature:**
```python
def list_presets() -> None
```

**Parameters:** None

**Returns:** None (prints to stdout)

**Example:**
```python
from oxford_matplotlib_theme import list_presets

list_presets()
# Outputs:
# Available Oxford Theme Presets:
# ==================================================
# Name            Description
# --------------------------------------------------
# default         Standard Oxford theme for academic papers
# presentation    Larger fonts and elements for slides
# ...
```

---

### get_preset_config()

Get the configuration dictionary for a preset.

**Signature:**
```python
def get_preset_config(preset_name: str) -> Dict[str, Any]
```

**Parameters:**
- `preset_name` (str): Preset name (case-insensitive)

**Returns:**
- `dict`: Configuration with keys: 'description', 'style_base', 'color_cycle', 'font_scale'

**Raises:**
- `ValueError`: If preset name is not found

**Example:**
```python
from oxford_matplotlib_theme import get_preset_config

config = get_preset_config('presentation')
print(config['font_scale'])  # 1.4

# Use for custom modification
config = get_preset_config('default')
config['font_scale'] = 1.3
apply_oxford_theme(**{k: v for k, v in config.items() if k != 'description'})
```

---

## Utils Module

### JOURNAL_PRESETS Dictionary

Pre-configured settings for major academic journals.

**Type:** `Dict[str, Dict[str, Any]]`

**Available Journals:**

| Journal | Figure Size (in) | DPI | Format |
|---------|-----------------|-----|--------|
| `nature` | (3.5, 2.5) | 300 | svg |
| `nature_double` | (7.0, 5.0) | 300 | svg |
| `plos` | (6.83, 5.0) | 300 | tiff |
| `bmj` | (3.27, 2.5) | 300 | eps |
| `lancet` | (3.27, 2.5) | 300 | tiff |

**Example:**
```python
from oxford_matplotlib_theme.utils import JOURNAL_PRESETS

print(JOURNAL_PRESETS['nature'])
# {'figsize': (3.5, 2.5), 'dpi': 300, 'format': 'svg'}
```

---

### add_oxford_branding()

Add Oxford University branding watermark to a figure.

**Signature:**
```python
def add_oxford_branding(
    fig: Figure,
    add_watermark: bool = False,
    watermark_text: str = "University of Oxford",
    position: Literal['bottom_right', 'bottom_left', 'top_right', 'top_left'] = 'bottom_right',
    opacity: float = 0.5,
    fontsize: int = 10,
) -> Figure
```

**Parameters:**
- `fig` (Figure): Matplotlib Figure object
- `add_watermark` (bool, default=False): Whether to add watermark
- `watermark_text` (str, default="University of Oxford"): Watermark text
- `position` (str, default='bottom_right'): Corner position
  - Options: 'bottom_right', 'bottom_left', 'top_right', 'top_left'
- `opacity` (float, default=0.5): Transparency (0=invisible, 1=opaque)
- `fontsize` (int, default=10): Font size

**Returns:**
- `Figure`: The same figure object (modified in place)

**Example:**
```python
from oxford_matplotlib_theme import oxford_figure, add_oxford_branding

fig, ax = oxford_figure()
ax.plot([1, 2, 3], [1, 4, 9])

# Add watermark
add_oxford_branding(fig, add_watermark=True)

# Custom watermark
add_oxford_branding(
    fig,
    add_watermark=True,
    watermark_text='Oxford PHC - DRAFT',
    position='top_left',
    opacity=0.3,
    fontsize=12
)
plt.show()
```

---

### save_oxford_figure()

Save matplotlib figure with high-quality publication settings.

**Signature:**
```python
def save_oxford_figure(
    fig: Figure,
    filename: str,
    format: str = 'png',
    dpi: int = 300,
    bbox_inches: str = 'tight',
    **kwargs
) -> None
```

**Parameters:**
- `fig` (Figure): Matplotlib Figure object
- `filename` (str): Output filename (extension added if missing)
- `format` (str, default='png'): Output format
  - Options: 'png', 'svg', 'pdf', 'eps', 'tiff', etc.
- `dpi` (int, default=300): Resolution (dots per inch)
  - 300 for standard publications
  - 600 for high-quality print
- `bbox_inches` (str, default='tight'): Bounding box setting
  - 'tight' removes excess whitespace
- `**kwargs`: Additional arguments passed to `fig.savefig()`

**Returns:** None

**Example:**
```python
from oxford_matplotlib_theme import oxford_figure, save_oxford_figure

fig, ax = oxford_figure()
ax.plot([1, 2, 3], [1, 4, 9])

# Save as PNG
save_oxford_figure(fig, 'plot.png')

# Save as SVG (vector format)
save_oxford_figure(fig, 'plot.svg')

# High-resolution TIFF for journal
save_oxford_figure(fig, 'figure1', format='tiff', dpi=600)

# PDF with custom padding
save_oxford_figure(fig, 'plot.pdf', pad_inches=0.1)
```

**Note:** No browser or kaleido dependency required!

---

### get_journal_preset()

Get figure size and export settings for specific journals.

**Signature:**
```python
def get_journal_preset(journal_name: str) -> Dict[str, Any]
```

**Parameters:**
- `journal_name` (str): Journal name (case-insensitive)
  - Options: 'nature', 'nature_double', 'plos', 'bmj', 'lancet'

**Returns:**
- `dict`: Configuration with keys: 'figsize', 'dpi', 'format'

**Raises:**
- `ValueError`: If journal name is not found

**Example:**
```python
from oxford_matplotlib_theme import get_journal_preset, oxford_figure, save_oxford_figure

# Get Nature preset
preset = get_journal_preset('nature')
# Returns: {'figsize': (3.5, 2.5), 'dpi': 300, 'format': 'svg'}

# Create figure with journal size
fig, ax = oxford_figure(figsize=preset['figsize'])
ax.plot(x, y)
ax.set_title('My Research')

# Save with journal settings
save_oxford_figure(fig, 'figure1', format=preset['format'], dpi=preset['dpi'])
```

---

## Usage Patterns

### Basic Workflow

```python
from oxford_matplotlib_theme import apply_oxford_theme
import matplotlib.pyplot as plt

# 1. Apply theme
apply_oxford_theme()

# 2. Create plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title('My Plot')

# 3. Show or save
plt.show()
# or
fig.savefig('plot.png', dpi=300, bbox_inches='tight')
```

### Using Convenience Function

```python
from oxford_matplotlib_theme import oxford_figure

# Creates pre-styled figure
fig, ax = oxford_figure()
ax.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

### Custom Colors

```python
from oxford_matplotlib_theme import apply_oxford_theme, get_palette

apply_oxford_theme()

# Use palette
colors = get_palette('vibrant', n_colors=3)
for i, color in enumerate(colors):
    ax.plot(x, data[i], color=color, label=f'Series {i}')
```

### For Presentations

```python
from oxford_matplotlib_theme import apply_preset

apply_preset('presentation')  # 1.4x fonts

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

### Journal Submission

```python
from oxford_matplotlib_theme import get_journal_preset, oxford_figure, save_oxford_figure

preset = get_journal_preset('nature')
fig, ax = oxford_figure(figsize=preset['figsize'])
ax.plot(x, y)
save_oxford_figure(fig, 'figure1', format=preset['format'], dpi=preset['dpi'])
```

### Multi-Panel Figures

```python
from oxford_matplotlib_theme import apply_oxford_theme

apply_oxford_theme()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y1)
axes[0, 1].bar(categories, values)
axes[1, 0].scatter(x, y2)
axes[1, 1].boxplot(data)

plt.tight_layout()
plt.show()
```

---

## Advanced Customization

### Custom Color Cycle

```python
# Use specific colors in custom order
custom_colors = ['coral', 'aqua', 'vivid_green', 'oxford_blue', 'mauve']
apply_oxford_theme(color_cycle=custom_colors)

# Now plotting automatically uses these colors
for i in range(5):
    ax.plot(x, data[i], label=f'Series {i}')
```

### Font Scaling

```python
# Fine-tune font sizes
apply_oxford_theme(font_scale=1.25)  # 25% larger

# Or use presets
apply_preset('presentation')  # 1.4x
apply_preset('poster')  # 1.8x
```

### Combining Features

```python
from oxford_matplotlib_theme import (
    oxford_figure,
    add_oxford_branding,
    save_oxford_figure,
    get_journal_preset
)

# Get journal settings
preset = get_journal_preset('nature')

# Create figure
fig, ax = oxford_figure(figsize=preset['figsize'])
ax.plot(x, y)
ax.set_title('Clinical Outcome Prediction')

# Add branding
add_oxford_branding(fig, add_watermark=True, opacity=0.3)

# Save
save_oxford_figure(fig, 'figure1', format=preset['format'], dpi=preset['dpi'])
```

---

For more examples, see:
- `examples/basic_usage.py`
- `examples/clinical_ml.py`
- `examples/publication_figures.py`
- `docs/MIGRATION_GUIDE.md`
