# Risky Business: Quantitative Portfolio Management for Optimized Risk

**Portfolio Resilience: Backtesting Asset Allocation Strategies During Financial Crises**

Dane Herrin & Alexander Jackson · DATA 510 Data Science Capstone · Willamette University · Summer 2026

**Project site (live):** https://daneherrin.github.io/data510--Quant-Back-Testing-/

**Analysis repository:** https://github.com/awjackson00/data510--Quant-Back-Testing-

---

## What this is

A reproducible backtesting workflow comparing five portfolio constructions (Barbell,
Mega-Cap Technology, Energy, Real Estate, FMCG) across nine historical market regimes from
the Dot-com crash through the post-2023 period, evaluated on Sharpe ratio, Sortino ratio,
annualized return, and cumulative return — not return alone.

This folder (`/docs` in the analysis repo, or the root of a dedicated `-site` repo) is the
**public-facing project site**: landing page, full write-up, results and figures, a
reproducibility guide, an ethics and data notice, and team information. It is the Milestone 5
deliverable ("Project Website and Dissemination") for DATA 510.

## Site contents

| Page | Covers |
|---|---|
| `index.html` | Landing page: summary, key results snapshot, portfolio definitions, ethics notice, team |
| `results.html` | Full Table 1 (Sharpe/Sortino/return by portfolio × regime) and Figures 1–3 |
| `writeup.html` | Complete write-up: abstract through references |
| `reproducibility.html` | Step-by-step clone/install/reproduce guide |
| `assets/poster.pdf` | One-page project poster |
| `assets/figures/` | Figures 1–3, exported from the analysis notebooks |

## Publishing this site (GitHub Pages)

This is already live at https://daneherrin.github.io/data510--Quant-Back-Testing-/, served from the
`docs/` folder of the `main` branch of this repo. To redeploy after updating any file:

1. Copy the updated file(s) into `docs/` in your local clone.
2. `git add docs && git commit -m "Update site" && git pull origin main --rebase && git push origin main`
3. GitHub rebuilds the Pages deployment automatically, usually within a minute or two.

If you ever need to re-create the Pages setup from scratch: **Settings → Pages → Build and deployment
→ Source: "Deploy from a branch" → Branch: `main` / `docs`.**

### If a file 404s after deploying

Binary files (PDFs, images) are the most common thing to go missing on push. Before committing, run
`git status` and confirm the new/changed file shows up as staged — and check this repo's `.gitignore`
for a stray `*.pdf` or `assets/` rule that could be silently excluding it.

## Reproducing the analysis

See [`reproducibility.html`](reproducibility.html) for the full guide, or the short version:

```bash
git clone https://github.com/awjackson00/data510--Quant-Back-Testing-.git
cd data510--Quant-Back-Testing-
python3 -m venv .venv && source .venv/bin/activate
pip install numpy pandas yfinance matplotlib seaborn statsmodels scikit-learn jupyterlab
jupyter lab notebooks/
```

Run the notebooks in order: `EDA Capstone.ipynb` → `portfolioConstruction.ipynb` →
`SharpeRatioSheet.ipynb` (source of Table 1) → `ARIMA Time-Series Modeling.ipynb` (optional).

## Data & ethics

All data are public market data pulled live from Yahoo Finance via `yfinance`; no raw market
data is redistributed in this repository. The project contains no personally identifiable
information. All results are historical and educational — **not investment advice**. See
`index.html#ethics` for the full notice, including backtesting limitations (hindsight bias,
survivorship bias, staggered asset inception dates, and excluded transaction costs).

## License

Site and analysis code: MIT License (see `LICENSE`). Market data is used under Yahoo
Finance's terms via the open-source `yfinance` package.
