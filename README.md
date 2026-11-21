# make-fun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/arunanala65-spec/make-fun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/arunanala65-spec/make-fun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A tiny but strong chess engine in under 4 KB of Python. 0x88 board, negamax with alpha-beta, transposition table, quiescence search, null-move pruning, late-move reductions, check extensions, MVV-LVA capture ordering, killer moves and history heuristic. It plays games against the house ladder over HTTP, one move at a time, with a fixed node budget per move (fully deterministic — no clock).

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8765 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ce51ph37&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
