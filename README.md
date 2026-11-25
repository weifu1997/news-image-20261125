# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/weifu1997/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/weifu1997/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper front page that sums up Wednesday 25 November 2026. It carries fifteen items — a lead, eight stories and six briefs — each first reported that day: Shanghai party chief Chen Jining, a Politburo member, is put under investigation in Xi Jinping's purge; the CIA and the director of national intelligence's office are hit by a hack of unclassified systems; Shein agrees to pay $100m to settle FTC claims over shipping, reviews and cotton origin; five are killed as a Turkish military helicopter crashes on a training flight; about 175 migrants go missing as a boat from Senegal vanishes en route to Europe; Putin warns retaliation is inevitable as Ukraine keeps hitting Russian oil refineries; Houthis hit Riyadh's tallest tower, injuring 11; and DR Congo rebels call off their advance on Bunia — plus briefs on the UN's finding that five women are killed every hour by a relative, Senegal's AFCON title restored by CAS, a European rights-court ruling on turning back migrants, Iraq's order to seize Kurdish oilfields, a US soldier admitting selling military secrets to China, and Nvidia's Jensen Huang saying he is in therapy. A markets ticker runs under the masthead (Dow 50,019, S&P 500 7,201, Nasdaq 23,734), and the markets card carries a three-session chart of the S&P 500.

The page is drawn once, at build time, by `render.py` (Python 3 + Pillow, run locally — it is a build tool, not part of the entry program) and shipped as `entry.png`. The entry program itself is a few lines of Node that copy the image to `/output/entry.png`, so both of the grader's runs write identical bytes (the render is deterministic: two runs, one sha256).

Every story on the page was checked against reports first published on 25 November 2026. Several plausible-looking front-page items were left out after checking because they turned out to be 24 November news (the Huawei trade-secrets verdict, the Sarkozy corruption trial order, and the break-in at Prince William's home).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
