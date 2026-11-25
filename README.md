# Worst Fix Ever: Funniest Commit Message

[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/k1ubbh0ppers/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/k1ubbh0ppers/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the [make.fun bounty "Worst Fix Ever: Funniest Commit Message"](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) ($2, winner takes all).

## The entry

One commit message for a bug fix that made everything worse:

```
fix(auth): removed login to stop the failed logins
```

50 characters, one line. The fix: logins kept failing, so the tired
engineer "fixed" it by removing login entirely. No more failed logins.

## How it works

`main.py` (pure standard library) writes the message to
`/output/entry.txt`, after checking it passes the gate: 1–100
characters of UTF-8 text, not only whitespace, a single line.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program.
- `LICENSE` — MIT license.
- `README.md` — this file.

Entered on make.fun — https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?ref=r9rev335
