# Project 4 - PDF Merger

A tiny `pypdf` script that joins several PDF files into one.

## Setup

```bash
pip install pypdf
```

## Files

| File | What it does |
| --- | --- |
| `pdf-merger.py` | Merges `sample1.pdf` and `sample2.pdf` into `sample-1-and-2.pdf`. |
| `sample1.pdf`, `sample2.pdf` | Sample PDFs to merge. |
| `sample-1-and-2.pdf` | The merged result. |

## Run it

```bash
python pdf-merger.py
```

## How it works

```python
from pypdf import PdfWriter

merger = PdfWriter()

merger.append("sample1.pdf")   # add a file
merger.append("sample2.pdf")   # add another - order matters
merger.write("sample-1-and-2.pdf")
```

`PdfWriter` collects pages in the order you append them, then `write()` saves them all as one new PDF.

To merge your own files, swap the names in `append()` - add as many lines as you need.

## Notes

- Appending only reads the source files; the originals are never changed.
- Want just part of a file? `append()` takes a page range: `merger.append("sample1.pdf", pages=(0, 3))` adds the first 3 pages (counting from 0).
- Calling `merger.close()` at the end frees the open files - good habit once you start merging a lot of PDFs.
- `pypdf` is the maintained package; older tutorials use `PyPDF2`, which is the same project under its old name.

## Learn more

- [pypdf docs](https://pypdf.readthedocs.io/en/stable/)
- [Merging PDFs guide](https://pypdf.readthedocs.io/en/stable/user/merging-pdfs.html)
- [Extracting text from a PDF](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)
