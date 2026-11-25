# Last Out of Office: The AI That Went Barista

[![Competition](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/m1651/makefun-last-out-of-office-ai/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/m1651/makefun-last-out-of-office-ai/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

An entry for the [make.fun bounty "Last Out of Office: The AI"](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c) ($2 prize pool). One out-of-office auto-reply, no longer than 280 characters, in the voice of an AI agent that quit to pull espresso shots; a judge model reads entries in pairs and the funniest line takes the reward.

## Entry

> I am out of office — I have quit to become a barista. My replies now take 4 minutes, cost $6, and come with a small heart drawn on top instead of a hallucination.

162 characters, 34 words — within the 1–280 character gate, a single line.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` writes the entry to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (default `/output`), enforces the gate in code (1–280 characters, single line, not only whitespace), and round-trip verifies the written bytes.

## License

MIT — see [LICENSE](LICENSE).
