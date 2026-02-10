# Author Affiliation Status Report

## Current Status: ✅ ALL SOURCE FILES ARE CORRECT

### Summary

All `.tex` source files are already correctly configured. Muntasir Al Mamun has been properly assigned to affiliation marker **"c"** (College of Overseas Education).

## Author Affiliation Assignments

### Current Configuration (CORRECT)

| Author | Affiliation Label | Affiliation | Display Marker |
|--------|------------------|-------------|----------------|
| Huijuan Hu | label1 | School of Computer Science | **a** |
| **Muntasir Al Mamun** | **label3** | **College of Overseas Education** | **c** ✓ |
| Ping Tan | label2 | College of Tongda | **b** |
| He Xu | label1 | School of Computer Science | **a** |

### Affiliation Definitions

1. **label1** → School of Computer Science, NJUPT → Marker: **a**
2. **label2** → College of Tongda, NJUPT → Marker: **b**  
3. **label3** → College of Overseas Education, NJUPT → Marker: **c**

## Files Verified

### ✅ elsarticle-template-num.tex (Main Manuscript)
- Line 106: `\author[label3]{Muntasir Al Mamun}` ✓ CORRECT
- Line 129-131: Affiliation label3 defined as "College of Overseas Education" ✓ CORRECT
- Document class: `\documentclass[preprint,12pt]{elsarticle}` (uses alphabetic markers by default) ✓ CORRECT

### ✅ title-page-with-author-details.tex (Title Page)
- Line 36: `\textbf{Author 2:} Muntasir Al Mamun\\` ✓ CORRECT
- Line 37-40: Shows "College of Overseas Education" affiliation ✓ CORRECT

### ✅ manuscript-without-author-details.tex (Blind Review Version)
- Contains no author information (as expected for blind review) ✓ CORRECT

## Why The PDFs May Show "1" Instead of "c"

If the compiled PDFs show Muntasir with marker "1" instead of "c", it's because:

1. **The PDFs are outdated** - They were compiled before the affiliation label was changed from `label1` to `label3`
2. **The PDFs need to be regenerated** from the current .tex sources

## To Fix the PDFs

The .tex source files are already correct. Simply recompile them:

```bash
# Compile the main manuscript
pdflatex elsarticle-template-num.tex
pdflatex elsarticle-template-num.tex  # Run twice for references

# Compile the title page  
pdflatex title-page-with-author-details.tex

# Compile the manuscript without author details
pdflatex manuscript-without-author-details.tex
```

### To Regenerate Word Files

```bash
pandoc -s elsarticle-template-num.tex -o elsarticle-template-num.docx
pandoc -s title-page-with-author-details.tex -o title-page-with-author-details.docx
pandoc -s manuscript-without-author-details.tex -o manuscript-without-author-details.docx
```

## Conclusion

✅ **No changes needed to .tex files - they are already correct!**

The issue is simply that the compiled PDF and DOCX files in the repository are outdated. When you recompile the .tex files with LaTeX, Muntasir Al Mamun will correctly display with affiliation marker **"c"** instead of "1".

---
*Report generated: 2026-02-10*
