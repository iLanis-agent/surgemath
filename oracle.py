import math, json

def plural(n, one, many):
    return one if n == 1 else many

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def joule_truth(rating, count, avg):
    if not (rating > 0):
        raise ValueError("the joule rating must be above zero")
    if not (count >= 0):
        raise ValueError("the spikes must be zero or more")
    if not (avg > 0):
        raise ValueError("the average spike must be above zero")
    left = rating - count * avg
    if left > 0:
        verdict = f"leaves {fixed1(left)} joules honestly"
    elif left < 0:
        verdict = f"runs {fixed1(-left)} joules past the rating honestly"
    else:
        verdict = "spends the rating exactly honestly"
    return f"{rating} joules on the box against {count} absorbed {plural(count, 'spike', 'spikes')} of {avg} joules each {verdict}."

def clamp_truth(clamp, line):
    if not (clamp > 0):
        raise ValueError("the clamp rating must be above zero")
    if not (line > 0):
        raise ValueError("the line voltage must be above zero")
    diff = clamp - line
    if diff > 0:
        return f"A {clamp}-volt clamp on a {line}-volt line lets {fixed1(diff)} volts past before it starts fighting honestly."
    return f"A {clamp}-volt clamp on a {line}-volt line sits {fixed1(-diff)} volts under the line - it never stops fighting honestly."

def load_truth(watts, amps, volts):
    if not (watts > 0):
        raise ValueError("the plugged-in watts must be above zero")
    if not (amps > 0):
        raise ValueError("the strip amps must be above zero")
    if not (volts > 0):
        raise ValueError("the line voltage must be above zero")
    honest = amps * volts * 0.8
    over = watts - honest
    if over > 0:
        verdict = f"runs {fixed1(over)} watts over honestly"
    elif over < 0:
        verdict = f"leaves {fixed1(-over)} watts of headroom honestly"
    else:
        verdict = "sits exactly at the honest limit honestly"
    return f"{watts} watts plugged into a {amps}-amp, {volts}-volt strip with an honest {fixed1(honest)} watts {verdict}."

FNS = {"jouleTruth": joule_truth, "clampTruth": clamp_truth, "loadTruth": load_truth}

CASES = [
    ("jouleTruth", [2000, 30, 50]),
    ("jouleTruth", [1000, 25, 50]),
    ("jouleTruth", [1500, 30, 50]),
    ("jouleTruth", [2000, 0, 50]),
    ("jouleTruth", [3000, 40, 60]),
    ("jouleTruth", [500, 12, 50]),
    ("jouleTruth", [2000, 1, 50]),
    ("jouleTruth", [0, 30, 50]),
    ("jouleTruth", [2000, -1, 50]),
    ("jouleTruth", [2000, 30, 0]),
    ("clampTruth", [330, 120]),
    ("clampTruth", [400, 230]),
    ("clampTruth", [500, 120]),
    ("clampTruth", [330, 230]),
    ("clampTruth", [600, 120]),
    ("clampTruth", [110, 230]),
    ("clampTruth", [0, 120]),
    ("clampTruth", [330, 0]),
    ("loadTruth", [1700, 15, 120]),
    ("loadTruth", [1000, 15, 120]),
    ("loadTruth", [1440, 15, 120]),
    ("loadTruth", [300, 15, 230]),
    ("loadTruth", [2000, 10, 120]),
    ("loadTruth", [720, 15, 120]),
    ("loadTruth", [1800, 15, 120]),
    ("loadTruth", [0, 15, 120]),
    ("loadTruth", [1700, 0, 120]),
    ("loadTruth", [1700, 15, -5]),
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
print(f"{len(out)} cases written to expected.json")
