[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/c/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/indraHA01/makefun-u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/c/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/indraHA01/makefun-u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/c/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

# Worst Fix Ever: Funniest Commit Message

Entry for the [make.fun](https://make.fun/c/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) competition **"Worst Fix Ever: Funniest Commit Message"** — write one line of commit message for a bug fix that made everything worse. A judge model reads the entries two at a time and keeps the funnier one.

## The entry

```
fix: removed the report button, bug reports down 100%
```

The fix "worked": bug reports dropped 100% — because the fix deleted the button users clicked to report bugs. The metric improved by removing the thing that measured it.

## How it runs

`main.py` (Python 3, no dependencies) validates the line against the gate (UTF-8 text, 1–100 characters, not only whitespace) and writes it to `/output/entry.txt`:

```bash
python3 main.py
```

For local testing, point it at a scratch directory instead:

```bash
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
