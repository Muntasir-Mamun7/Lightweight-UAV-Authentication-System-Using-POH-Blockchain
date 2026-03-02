# LaTeX Submission Package

**Paper:** A Lightweight and Practical UAV Authentication System based on Proof-of-History Blockchain

---

## Package Contents

```
latex-submission/
├── main.tex                    ← Main manuscript with full author details
├── manuscript-blind-review.tex ← Anonymized manuscript (for double-blind review)
├── title-page.tex              ← Separate title page with author details
├── elsarticle.cls              ← Elsevier document class (required)
├── elsarticle-num.bst          ← Bibliography style: numbered (default)
├── elsarticle-num-names.bst    ← Bibliography style: numbered with names
├── elsarticle-harv.bst         ← Bibliography style: Harvard author-year
├── Fig/
│   ├── graphical_abstract.png  ← Graphical abstract
│   ├── Fig1.png                ← System Architecture Overview
│   ├── Fig2.png                ← PoH Block Structure
│   ├── Fig3.png                ← Authentication Protocol Flow
│   ├── Fig4.png                ← Performance Results
│   └── Fig5.png                ← Scalability Evaluation
└── README.md                   ← This file
```

---

## Which File to Submit

| Submission Type | File to Use |
|---|---|
| Full manuscript (with authors) | `main.tex` |
| Double-blind review (anonymized) | `manuscript-blind-review.tex` |
| Separate title page | `title-page.tex` |

---

## How to Compile

Run pdfLaTeX **twice** (to resolve cross-references):

```bash
# Compile the full manuscript
pdflatex main.tex
pdflatex main.tex

# Or compile the blind review version
pdflatex manuscript-blind-review.tex
pdflatex manuscript-blind-review.tex

# Or compile the title page separately
pdflatex title-page.tex
```

---

## Authors

| Author | Role | Affiliation | Email |
|---|---|---|---|
| Huijuan Hu | Lecturer | School of Computer Science, NJUPT | hhj@njupt.edu.cn |
| Muntasir Al Mamun | — | College of Overseas Education, NJUPT | f22040119@njupt.edu.cn |
| Ping Tan | Assistant Professor | College of Tongda, NJUPT | tanping5.20@njupt.edu.cn |
| He Xu *(Corresponding)* | Professor | School of Computer Science, NJUPT | xuhe@njupt.edu.cn |

---

## Notes

- All `.tex` files use the Elsevier `elsarticle` document class (`elsarticle.cls` included).
- References are embedded directly using `\begin{thebibliography}` — no separate `.bib` file needed.
- All figures are referenced as `Fig/FigN.png` paths relative to the `.tex` file.
- The document is formatted for submission to **Blockchain: Research and Applications**.
