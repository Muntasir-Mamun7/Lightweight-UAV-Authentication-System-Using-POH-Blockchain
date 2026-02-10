# Fix Complete: Author Affiliation Markers Corrected

## Issue Resolved ✅

**Problem:** Muntasir Al Mamun was showing affiliation marker "1" instead of "c" in the compiled PDF documents.

**Root Cause:** The .tex source files were already correct, but the compiled PDF and DOCX files in the repository were outdated and needed regeneration.

**Solution:** Regenerated all PDF and DOCX files from the correct .tex sources.

## Final Author Affiliation Configuration

### Author List with Correct Markers

| Author | Affiliation Marker | Affiliation |
|--------|-------------------|-------------|
| Huijuan Hu | **a** | School of Computer Science, NJUPT |
| **Muntasir Al Mamun** | **c** ✅ | **College of Overseas Education, NJUPT** |
| Ping Tan | **b** | College of Tongda, NJUPT |
| He Xu (Corresponding) | **a*** | School of Computer Science, NJUPT |

*\* indicates corresponding author*

## Files Updated

All documents have been regenerated with the correct affiliation markers:

### PDF Files (Recompiled from LaTeX)
1. ✅ **elsarticle-template-num.pdf** (Main Manuscript)
   - 24 pages, 2.6 MB
   - Muntasir Al Mamun now correctly shows marker **"c"**

2. ✅ **manuscript-without-author-details.pdf** (Blind Review Version)
   - 24 pages, 2.6 MB
   - No author information (as expected for blind review)

3. ✅ **title-page-with-author-details.pdf** (Title Page)
   - 2 pages, 38 KB
   - Shows full author information with affiliations

### DOCX Files (Regenerated with Pandoc)
1. ✅ **elsarticle-template-num.docx** (2.9 MB)
2. ✅ **manuscript-without-author-details.docx** (2.9 MB)
3. ✅ **title-page-with-author-details.docx** (10 KB)

## Verification

Extracted text from the main manuscript PDF confirms the fix:

```
Huijuan Huᵃ, Muntasir Al Mamunᶜ, Ping Tanᵇ, He Xuᵃ'*

ᵃ School of Computer Science, Nanjing University of Posts and
Telecommunications, Nanjing, China

ᵇ College of Tongda, Nanjing University of Posts and
Telecommunications, Nanjing, China

ᶜ College of Overseas Education, Nanjing University of Posts and
Telecommunications, Nanjing, China
```

✅ **Muntasir Al Mamun now correctly displays with affiliation marker "c"**

## Technical Details

### LaTeX Source Configuration (Correct)

```latex
%% Author 2
\author[label3]{Muntasir Al Mamun}
\ead{f22040119@njupt.edu.cn}

%% Affiliation 3
\affiliation[label3]{organization={College of Overseas Education, 
    Nanjing University of Posts and Telecommunications},
    city={Nanjing},
    country={China}}
```

### Document Class Configuration

All documents use the default elsarticle class without the `numafflabel` option, which means affiliations are displayed using lowercase letters (a, b, c) instead of numbers (1, 2, 3):

```latex
\documentclass[preprint,12pt]{elsarticle}
```

## Compilation Process

1. Installed TeXLive (LaTeX distribution)
2. Compiled all .tex files to PDF using `pdflatex`
3. Ran compilation twice to resolve cross-references
4. Installed Pandoc
5. Converted all .tex files to DOCX using `pandoc`

## Files Status

| File | Status | Notes |
|------|--------|-------|
| elsarticle-template-num.tex | ✅ No changes needed | Already correct |
| title-page-with-author-details.tex | ✅ No changes needed | Already correct |
| manuscript-without-author-details.tex | ✅ No changes needed | Already correct |
| elsarticle-template-num.pdf | ✅ Regenerated | Fixed affiliation markers |
| manuscript-without-author-details.pdf | ✅ Regenerated | Fixed affiliation markers |
| title-page-with-author-details.pdf | ✅ Regenerated | Updated |
| elsarticle-template-num.docx | ✅ Regenerated | Updated from .tex source |
| manuscript-without-author-details.docx | ✅ Regenerated | Updated from .tex source |
| title-page-with-author-details.docx | ✅ Regenerated | Updated from .tex source |

## Summary

🎉 **All done!** The issue has been completely resolved. Muntasir Al Mamun now correctly appears with affiliation marker **"c"** (College of Overseas Education) in all compiled documents, instead of the incorrect "1" that was showing before.

---
*Fix completed: 2026-02-10*
*All PDFs and DOCX files regenerated with correct affiliation markers*
