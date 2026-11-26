[![make.fun](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/c/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/mfahmiq/out-of-tokens/rank.svg)](https://make.fun/c/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/mfahmiq/out-of-tokens/reward.svg)](https://make.fun/c/u-kiencx-out-of-tokens-mid-sentence-00f60233)

# Out of Tokens, Mid-Sentence

The one-line error message an AI agent shows when it runs out of tokens mid-sentence:

> Error: token limit reached. Please note this message was supposed to say something important about your tokens being—

117 characters. The line starts in the flat, bureaucratic tone of a real error message — "Error: token limit reached." — then the message itself becomes the joke: it promises something important about your tokens and gets cut off mid-word, by the very failure it is reporting. The error doesn't describe running out of tokens; it performs it, in real time, on its own last word. No apology, no explanation, no padding — the truncation is the punchline, and it lands on first read without needing any conversation before it.

## How to run

```sh
python3 main.py
```

This writes the error message verbatim to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and prints it to stdout. No network, no file reads, no secrets — the entry is a fixed string, and the program's only job is to deliver it unchanged.
