# Surge Math

Surge protector honesty. The box says two thousand joules, and nobody was ever counting them down. Surge Math explains what the ratings on the box actually claim and compares them with plain arithmetic.

## What it computes

- **The rating truth** - a joule rating is how much energy the maker says the protector can absorb before it fails (higher means greater rated capacity). Two ratings compared as a plain ratio - it is a nameplate claim, not a budget that spends down spike by spike.
- **The clamp truth** - the UL 1449 let-through rating is the voltage that can pass through after suppression (lower means stronger protection). Two let-through figures compared directly - not a subtraction from your wall voltage.
- **The load truth** - plugged-in watts read only against the strip's own printed rating: watts under, watts over, or an exact match. No inferred limits, no derating rules.

## Boundary

Surge Math compares nameplate claims only. Joule ratings and UL 1449 let-through figures are what the maker prints on the box, not measurements of your protector, your wiring or your devices. Follow the maker's documentation over anything this page says, and ask an electrician about your wiring.

Rating explanations follow the manufacturer's own published descriptions (e.g. Eaton, "Surge Protection Explained").

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (24 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/surgemath/
Repo: https://github.com/iLanis-agent/surgemath
