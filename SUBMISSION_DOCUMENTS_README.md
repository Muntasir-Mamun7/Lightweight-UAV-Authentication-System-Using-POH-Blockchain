# Submission Documents

This directory contains the required submission documents for journal/conference submission.

## Files Created

### 1. Manuscript Without Author Details (`manuscript-without-author-details.pdf`)
This is the **blind review version** of the manuscript. It contains:
- Complete title
- Abstract
- Graphical abstract
- Research highlights
- Keywords
- All sections (Introduction, Related Work, System Architecture, Implementation, Performance Evaluation, Discussion, Future Work, Conclusion)
- References

**What's removed for blind review:**
- Author names
- Author affiliations
- Author email addresses
- Corresponding author information

### 2. Title Page With Author Details (`title-page-with-author-details.pdf`)
This is a **separate title page** containing author information. It includes:
- Paper title
- All author names with their roles/positions
- Author affiliations
- Author email addresses
- Corresponding author designation and contact information

## Purpose

These two documents are typically required for double-blind peer review submissions where:
1. The main manuscript is reviewed anonymously (without knowing who the authors are)
2. The title page with author details is kept separate and only revealed after review acceptance

## Source Files

- `manuscript-without-author-details.tex` - LaTeX source for the blind review manuscript
- `title-page-with-author-details.tex` - LaTeX source for the title page

## How to Regenerate

If you need to regenerate these PDFs after making changes:

```bash
# Compile the manuscript without author details
pdflatex manuscript-without-author-details.tex

# Compile the title page with author details
pdflatex title-page-with-author-details.tex
```

## Notes

- Both documents are based on the main paper: "A Lightweight and Practical UAV Authentication System Implementation based on Proof-of-History Blockchain"
- The manuscript uses the Elsevier article class (`elsarticle.cls`)
- The title page uses a simple article format for clarity
