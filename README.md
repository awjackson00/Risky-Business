# Risky Business

**Portfolio Resilience: Backtesting Asset Allocation Strategies During Financial Crises**

**Authors:** Dane Herrin and Alexander Jackson  
**Willamette University · DATA 510 · Summer 2026**  
**Maintained and hosted by:** Alexander Jackson

This is Alexander Jackson's separately hosted copy of the jointly authored **Risky Business** capstone website. The historical analysis, visualizations, methods, figures, and authorship attribution remain intact.

- **Target public site:** https://awjackson00.github.io/Risky-Business/
- **Results and figures:** https://awjackson00.github.io/Risky-Business/results.html
- **Original team-hosted site:** https://daneherrin.github.io/data510--Quant-Back-Testing-/
- **Analysis repository (including source notebooks):** https://github.com/awjackson00/data510--Quant-Back-Testing-
- **My portfolio:** https://awjackson00.github.io/projects/risky-business.html

## Contents

The complete public-facing website lives in `docs/` and includes:

- `index.html`: study overview and team credits
- `results.html`: performance table and supporting figures
- `writeup.html`: full capstone write-up
- `reproducibility.html`: instructions to reproduce the analysis
- `assets/css/style.css`: original site styling
- `assets/figures/`: three original analytical figures
- `assets/poster.pdf`: capstone poster
- `LICENSE`: MIT license crediting both authors

## Hosting

The workflow in `.github/workflows/publish.yml` imports the original `docs/` website from **my own analysis repository** on the first run. It copies the actual image and PDF files, validates local HTML references, commits the copy into this repository, and attempts to publish through GitHub Pages.

**One-time setup:** In this repository, open **Settings → Pages → Build and deployment**, set **Source: GitHub Actions**. Then open **Actions → Publish Risky Business → Run workflow** if the initial run failed before Pages was enabled.

Future ordinary pushes to `main` publish this repository's own `docs/` content, without resetting local edits. To intentionally refresh the copy from the analytical source, open **Actions → Publish Risky Business → Run workflow** and select **Refresh website copy from analysis repository**.

Because the site uses relative links, it works at the project path `/Risky-Business/` without changing the analysis data or the original project's live site.

## Authorship and responsible use

This is a jointly developed capstone, not a claim of sole authorship. The included MIT license credits **Dane Herrin and Alexander Jackson**. Financial information is historical, educational, and **not investment advice**. Yahoo Finance market data are not redistributed.

The original collaborator's site remains independent and unchanged.
