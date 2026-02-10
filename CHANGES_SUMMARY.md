# Document Changes Summary

## Overview
This document summarizes the changes made to the author information and document metadata as requested.

## Changes Made

### 1. Author Affiliation Update (Muntasir Al Mamun)

**Previous affiliation:**
- School of Computer Science, Nanjing University of Posts and Telecommunications

**Updated affiliation:**
- College of Overseas Education, Nanjing University of Posts and Telecommunications

### 2. Journal Reference Removal

**Previous:** `\journal{Nuclear Physics B}`
**Updated:** `%% \journal{Nuclear Physics B}` (commented out)

This change removes the "Preprint submitted to Nuclear Physics B" text from the documents.

## Files Modified

### LaTeX Source Files
1. **elsarticle-template-num.tex** (Main Paper)
   - Updated Muntasir Al Mamun's affiliation label from `label1` to `label3`
   - Added new affiliation definition for `label3`: College of Overseas Education
   - Commented out the `\journal{Nuclear Physics B}` line

2. **manuscript-without-author-details.tex** (Manuscript)
   - Commented out the `\journal{Nuclear Physics B}` line

3. **title-page-with-author-details.tex** (Title Page)
   - Added "College of Overseas Education" to Author 2's information

### Generated Files

#### PDF Files (Compiled from LaTeX)
- elsarticle-template-num.pdf
- manuscript-without-author-details.pdf
- title-page-with-author-details.pdf

#### Word Files (Converted from LaTeX using Pandoc)
- elsarticle-template-num.docx
- manuscript-without-author-details.docx
- title-page-with-author-details.docx

## Verification

The changes have been verified in the generated PDFs:
- Author 2 (Muntasir Al Mamun) now shows "College of Overseas Education, Nanjing University of Posts and Telecommunications"
- The university location remains "Nanjing, China"
- The Nuclear Physics B journal reference has been removed from the document header

## How to Use

All documents are available in three formats:
1. **LaTeX Source** (.tex) - For editing and recompiling
2. **PDF** (.pdf) - For reading and printing
3. **Word** (.docx) - For editing in Microsoft Word or compatible applications

To recompile the LaTeX files if needed:
```bash
pdflatex elsarticle-template-num.tex
pdflatex manuscript-without-author-details.tex
pdflatex title-page-with-author-details.tex
```

To regenerate Word files:
```bash
pandoc -s elsarticle-template-num.tex -o elsarticle-template-num.docx
pandoc -s manuscript-without-author-details.tex -o manuscript-without-author-details.docx
pandoc -s title-page-with-author-details.tex -o title-page-with-author-details.docx
```
