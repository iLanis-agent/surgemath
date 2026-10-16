// Surge Math engine - plain arithmetic on the ratings printed on the box.
// A joule rating is how much energy the maker says the protector can absorb
// before it fails. A UL 1449 let-through rating is the voltage that can pass
// through after suppression; lower means stronger protection. These are
// nameplate claims to compare, not budgets to count down.

function tenths(x) { return Math.floor(x * 10 + 0.5) / 10; }
function fixed1(x) { return tenths(x).toFixed(1); }
function article(n) { const s = String(n); return (s.startsWith("8") || s.startsWith("11") || s.startsWith("18")) ? "An" : "A"; }

function ratingTruth(a, b) {
  if (!(a > 0)) throw new Error("the first joule rating must be above zero");
  if (!(b > 0)) throw new Error("the second joule rating must be above zero");
  if (a === b) return `${article(a)} ${a}-joule rating and a ${b}-joule rating carry the same rated capacity honestly.`;
  return `${article(a)} ${a}-joule rating is rated to absorb ${fixed1(a / b)} times the energy of a ${b}-joule rating honestly.`;
}

function clampTruth(a, b) {
  if (!(a > 0)) throw new Error("the first let-through must be above zero");
  if (!(b > 0)) throw new Error("the second let-through must be above zero");
  if (a === b) return `${article(a)} ${a}-volt let-through and a ${b}-volt let-through pass the same voltage honestly.`;
  const diff = tenths(Math.abs(a - b));
  const dir = a < b ? "fewer" : "more";
  return `${article(a)} ${a}-volt let-through lets ${fixed1(diff)} ${dir} volts through than a ${b}-volt rating honestly.`;
}

function loadTruth(watts, rating) {
  if (!(watts > 0)) throw new Error("the plugged-in watts must be above zero");
  if (!(rating > 0)) throw new Error("the strip's rating must be above zero");
  const diff = tenths(watts - rating);
  if (diff === 0) return `${watts} watts plugged in matches the strip's own ${rating}-watt rating exactly honestly.`;
  const dir = diff < 0 ? "under" : "over";
  return `${watts} watts plugged in against the strip's own ${rating}-watt rating reads ${fixed1(Math.abs(diff))} watts ${dir} the rating honestly.`;
}

if (typeof module !== "undefined") {
  module.exports = { ratingTruth, clampTruth, loadTruth };
}
