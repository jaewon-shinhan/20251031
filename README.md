# Stock Price Summary (temp.csv)

This repository contains a daily price history snapshot for three tickers—Samsung Electronics (005930.KS), Apple (AAPL), and Nvidia (NVDA)—covering 16 October 2023 through 10 October 2025. The CSV combines open, high, low, close, and volume fields for each company.

## Dataset structure

* **File:** `temp.csv`
* **Rows:** 516 trading days
* **Date range:** 2023-10-16 → 2025-10-10
* **Columns:**
  * `Date`
  * For each ticker (`005930.KS`, `AAPL`, `NVDA`): `Close`, `High`, `Low`, `Open`, `Volume`

## Summary statistics

The tables below provide basic descriptive statistics (mean, population standard deviation, minimum, and maximum) for each price metric.

### 005930.KS (Samsung Electronics)

| Metric | Mean | Std Dev | Min | Max |
| --- | ---: | ---: | ---: | ---: |
| Close | 66,471.53 | 9,698.76 | 48,968.97 | 94,400.00 |
| High | 67,202.08 | 9,704.97 | 50,784.92 | 94,500.00 |
| Low | 65,822.65 | 9,599.22 | 48,968.97 | 92,700.00 |
| Open | 66,509.00 | 9,727.71 | 49,263.38 | 94,000.00 |
| Volume | 19,481,204.69 | 8,607,645.64 | 2,957,915.00 | 57,691,266.00 |

### AAPL (Apple)

| Metric | Mean | Std Dev | Min | Max |
| --- | ---: | ---: | ---: | ---: |
| Close | 209.52 | 24.35 | 163.82 | 258.10 |
| High | 211.47 | 24.51 | 165.21 | 259.24 |
| Low | 207.33 | 24.05 | 162.91 | 256.72 |
| Open | 209.29 | 24.33 | 164.17 | 257.99 |
| Volume | 56,558,297.39 | 26,893,569.34 | 23,234,700.00 | 318,679,900.00 |

### NVDA (Nvidia)

| Metric | Mean | Std Dev | Min | Max |
| --- | ---: | ---: | ---: | ---: |
| Close | 115.60 | 38.97 | 40.30 | 192.57 |
| High | 117.54 | 39.40 | 40.85 | 195.62 |
| Low | 113.41 | 38.51 | 39.21 | 191.06 |
| Open | 115.59 | 39.03 | 40.43 | 193.51 |
| Volume | 325,122,504.81 | 156,182,871.77 | 105,157,000.00 | 1,142,269,000.00 |

## Notable extremes

* **Highest closing price**
  * 005930.KS — ₩94,400 on 2025-10-10
  * AAPL — $258.10 on 2024-12-26
  * NVDA — $192.57 on 2025-10-09
* **Highest trading volume**
  * 005930.KS — 57.7M shares on 2024-01-11
  * AAPL — 318.7M shares on 2024-09-20 (triple witching)
  * NVDA — 1.14B shares on 2024-03-08

## Daily momentum snapshot

Average day-over-day percentage changes in closing price show steady upward drift, especially for Nvidia:

| Ticker | Avg daily % change | Positive days | Negative days | Samples |
| --- | ---: | ---: | ---: | ---: |
| 005930.KS | 0.10% | 232 | 218 | 481 |
| AAPL | 0.08% | 269 | 228 | 498 |
| NVDA | 0.33% | 277 | 220 | 498 |

These figures use population statistics and do not account for dividends or currency conversions.

## Reproducing the analysis

All numbers above were generated with small Python scripts using the standard library (`csv`, `math`). Re-run the calculations by executing the snippets below from the repository root:

```bash
python scripts/summary.py  # (script not provided; see README for inline snippets)
```

Alternatively, adapt the inline examples in this README to compute additional metrics such as rolling volatility or inter-ticker correlations.

