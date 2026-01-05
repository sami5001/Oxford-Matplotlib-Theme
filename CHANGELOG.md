# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-05

### Added
- 56 official Oxford University brand colors (35 brand + 21 thesis colors)
- 13 curated color palettes:
  - General purpose: PRIMARY, PROFESSIONAL, VIBRANT, PASTEL
  - Data-specific: DIVERGING, SEQUENTIAL_BLUE
  - Themed: HEALTH, TRADITIONAL, CONTEMPORARY, CELEBRATORY, CORPORATE, INNOVATIVE
  - Academic: PHC_THESIS (27 colors for thesis work)
- 7 theme presets: default, presentation, poster, colorblind, minimal, notebook, print
- 5 journal export presets: Nature, Nature double, PLOS, BMJ, Lancet
- Journal-ready export functions supporting SVG, PNG, PDF, TIFF, EPS formats
- Oxford branding/watermark support via `add_oxford_branding()`
- Convenience function `oxford_figure()` for quick figure creation
- Publication constants: `PUBLICATION_DPI`, `PUBLICATION_DPI_HIGH`, `SUPPORTED_FORMATS`
- Comprehensive API documentation
- Migration guide from oxford-plotly-theme
- Input validation for all public functions
- Case-insensitive color and palette lookups

### Technical Details
- No browser or kaleido dependencies (unlike Plotly)
- Uses matplotlib's native savefig for direct export
- PEP 561 compliant with py.typed marker
- Supports Python 3.8+
