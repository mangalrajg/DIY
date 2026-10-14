# Shoe Rack Build Guide

A 60 in wide × 48 in tall × 12 in deep open plywood shoe rack.

- **Design**: Two side panels, bottom shelf raised 1.5 in on cleats, center divider, top board, six adjustable middle shelves on pins.
- **Joinery**: Wooden cleats throughout — no screws through outside faces, no blind screws.

## Files

| File | What it is |
|------|-----------|
| `shoe-rack-build-guide.pdf` | The generated build guide (17 pages, 27 figures) |
| `build_pdf.py` | Python script that generates the PDF — edit this to change text, dimensions, or figure order |
| `pdf_img/` | All figure images (JPG). Engineering drawings are generated with PIL; some are AI-generated base images patched with PIL |

## How to rebuild the PDF

```bash
pip install fpdf2 pymupdf pillow
python3 build_pdf.py
```

This regenerates `shoe-rack-build-guide.pdf` from `build_pdf.py` + `pdf_img/`.

## Making changes

- **Text/dimensions**: edit `build_pdf.py`, then rebuild.
- **A figure image**: replace the JPG in `pdf_img/` (keep the same filename), then rebuild.
- **Figure order**: figure numbers are assigned in code order via `fig=N` — keep them sequential in reading order.

## Key dimensions (in)

- Overall: 60 W × 48 H × 12 D
- Side panels: 47-1/4 × 12 (×2)
- Top board: 60 × 12
- Bottom shelf: 58.5 × 12 (on 1×2 cleats, raised 1.5 in)
- Divider: 45 × 12
- Middle shelves: 28.75 × 12 (×8 — 6 in use + 2 spare)
- Backstops: 28.5 × 2 (×8) · Front lips: 28.5 in 1×2 (×8)
- Cleats: 4× 12 in + 2× 8 in (1×2 pine)
