// Surge Math engine - hypothetical arithmetic on labeled norms only.
// Joule budgets, clamp figures and load math are labeled norms, not
// measurements of your protector, your wiring or your devices.

function plural(n, one, many) { return n === 1 ? one : many; }
function tenths(x) { return Math.floor(x * 10 + 0.5) / 10; }
function fixed1(x) { return tenths(x).toFixed(1); }

function jouleTruth(rating, count, avg) {
  if (!(rating > 0)) throw new Error("the joule rating must be above zero");
  if (!(count >= 0)) throw new Error("the spikes must be zero or more");
  if (!(avg > 0)) throw new Error("the average spike must be above zero");
  const left = rating - count * avg;
  let verdict;
  if (left > 0) verdict = `leaves ${fixed1(left)} joules honestly`;
  else if (left < 0) verdict = `runs ${fixed1(-left)} joules past the rating honestly`;
  else verdict = "spends the rating exactly honestly";
  return `${rating} joules on the box against ${count} absorbed ${plural(count, "spike", "spikes")} of ${avg} joules each ${verdict}.`;
}

function clampTruth(clamp, line) {
  if (!(clamp > 0)) throw new Error("the clamp rating must be above zero");
  if (!(line > 0)) throw new Error("the line voltage must be above zero");
  const diff = clamp - line;
  if (diff > 0) return `A ${clamp}-volt clamp on a ${line}-volt line lets ${fixed1(diff)} volts past before it starts fighting honestly.`;
  return `A ${clamp}-volt clamp on a ${line}-volt line sits ${fixed1(-diff)} volts under the line - it never stops fighting honestly.`;
}

function loadTruth(watts, amps, volts) {
  if (!(watts > 0)) throw new Error("the plugged-in watts must be above zero");
  if (!(amps > 0)) throw new Error("the strip amps must be above zero");
  if (!(volts > 0)) throw new Error("the line voltage must be above zero");
  const honest = amps * volts * 0.8; // labeled norm: 80% continuous derate
  const over = watts - honest;
  let verdict;
  if (over > 0) verdict = `runs ${fixed1(over)} watts over honestly`;
  else if (over < 0) verdict = `leaves ${fixed1(-over)} watts of headroom honestly`;
  else verdict = "sits exactly at the honest limit honestly";
  return `${watts} watts plugged into a ${amps}-amp, ${volts}-volt strip with an honest ${fixed1(honest)} watts ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { jouleTruth, clampTruth, loadTruth };
}
