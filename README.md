# Surge Math

Surge protector honesty. The box says two thousand joules, and every little spike was always going to spend some. Surge Math turns the rated budget, the clamping voltage and the plugged-in load into honest arithmetic on labeled norms.

## What it computes

- **The joule truth** - a joule rating is a budget that spends itself: spikes absorbed times average joules each, against the rating on the box, as joules left, joules past the rating, or exactly spent.
- **The clamp truth** - clamping voltage is where the protector starts fighting, not where it wins: how many volts a clamp lets past the line first, or how far under the line a too-low clamp sits.
- **The load truth** - plugged-in watts against the strip's honest continuous figure (amps times volts, derated to 80% as a labeled norm), as watts over, headroom left, or exactly at the honest limit.

## Boundary

Surge Math keeps labeled-norm arithmetic only. Joule budgets, clamp figures and load math are labeled norms, not measurements of your protector, your wiring or your devices. A surge protector is sacrificial: replace it on the maker's schedule, follow the maker's rating over anything this page says, and ask an electrician about your wiring.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (28 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/surgemath/
Repo: https://github.com/iLanis-agent/surgemath
