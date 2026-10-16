import math, json

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def article(n):
    s = str(n)
    return "An" if (s.startswith("8") or s.startswith("11") or s.startswith("18")) else "A"

def rating_truth(a, b):
    if not (a > 0):
        raise ValueError("the first joule rating must be above zero")
    if not (b > 0):
        raise ValueError("the second joule rating must be above zero")
    if a == b:
        return f"{article(a)} {a}-joule rating and a {b}-joule rating carry the same rated capacity honestly."
    return f"{article(a)} {a}-joule rating is rated to absorb {fixed1(a / b)} times the energy of a {b}-joule rating honestly."

def clamp_truth(a, b):
    if not (a > 0):
        raise ValueError("the first let-through must be above zero")
    if not (b > 0):
        raise ValueError("the second let-through must be above zero")
    if a == b:
        return f"{article(a)} {a}-volt let-through and a {b}-volt let-through pass the same voltage honestly."
    diff = tenths(abs(a - b))
    dir = "fewer" if a < b else "more"
    return f"{article(a)} {a}-volt let-through lets {fixed1(diff)} {dir} volts through than a {b}-volt rating honestly."

def load_truth(watts, rating):
    if not (watts > 0):
        raise ValueError("the plugged-in watts must be above zero")
    if not (rating > 0):
        raise ValueError("the strip's rating must be above zero")
    diff = tenths(watts - rating)
    if diff == 0:
        return f"{watts} watts plugged in matches the strip's own {rating}-watt rating exactly honestly."
    dir = "under" if diff < 0 else "over"
    return f"{watts} watts plugged in against the strip's own {rating}-watt rating reads {fixed1(abs(diff))} watts {dir} the rating honestly."

FNS = {"ratingTruth": rating_truth, "clampTruth": clamp_truth, "loadTruth": load_truth}

CASES = [
    ("ratingTruth", [2000, 1000]),
    ("ratingTruth", [1000, 2000]),
    ("ratingTruth", [1500, 1500]),
    ("ratingTruth", [3000, 400]),
    ("ratingTruth", [300, 600]),
    ("ratingTruth", [600, 400]),
    ("ratingTruth", [800, 400]),
    ("ratingTruth", [0, 1000]),
    ("ratingTruth", [2000, 0]),
    ("clampTruth", [330, 500]),
    ("clampTruth", [500, 330]),
    ("clampTruth", [400, 400]),
    ("clampTruth", [330, 400]),
    ("clampTruth", [330, 331]),
    ("clampTruth", [0, 500]),
    ("clampTruth", [330, 0]),
    ("loadTruth", [1700, 1800]),
    ("loadTruth", [2000, 1800]),
    ("loadTruth", [1800, 1800]),
    ("loadTruth", [450, 1800]),
    ("loadTruth", [10, 1800]),
    ("loadTruth", [1850, 1800]),
    ("loadTruth", [0, 1800]),
    ("loadTruth", [1700, 0]),
]

out = []
for fn, args in CASES:
    rec = {"fn": fn, "args": args}
    try:
        rec["out"] = FNS[fn](*args)
    except ValueError as e:
        rec["err"] = str(e)
    out.append(rec)
    print(fn, args, "->", rec.get("out") or ("ERR: " + rec["err"]))

with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(f"{len(out)} cases written")
