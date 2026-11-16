# Data: what to drop here and in what shape

## Ad results (`data/meta-exports/`)
Export weekly from Dolphin or Meta Ads Manager at **ad level**, one row per ad, for the reporting week
(Monday–Sunday). Name the file `YYYY-MM-DD_to_YYYY-MM-DD.csv`. Real exports are git-ignored (private);
`_TEMPLATE.csv` and `SAMPLE_*.csv` are kept.

Columns (header names can vary; `tools/weekly_report.py` recognises the common Meta/Dolphin names):
| Column | Meta Ads Manager name (typical) |
|---|---|
| ad_name | Ad name |
| spend | Amount spent |
| impressions | Impressions |
| reach | Reach (optional, for frequency) |
| video_3s_views | 3-second video plays |
| thruplays | ThruPlays |
| link_clicks | Link clicks (or Outbound clicks) |
| purchases | Purchases (or Results) |
| revenue | Purchases conversion value |

Ad names must follow `playbook/naming-convention.md`, so each ad maps to an angle, persona and format.

## Reviews (`data/reviews/`)
Any CSV with at least: `text`, `rating`, `date`, `source`. Optional: `product`, `name`.
