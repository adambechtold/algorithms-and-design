function isAnagram(s: string, t: string): boolean {
    return isAnagramFast(s, t);
}

function isAnagramFast(s: string, t: string): boolean {
    const [sCount, tCount] = [s, t].map(countCharsFast);
    return areCountsEqual(sCount, tCount);
}

function isAnagramCounting(s: string, t: string): boolean {
    const [sCount, tCount] = [countChars(s), countChars(t)];
    return areCharCountsEqual(sCount, tCount);
}

function areCharCountsEqual(mapA: Map<string, number>, mapB: Map<string, number>) {
    if (mapA.size !== mapB.size) return false;

    for (const [key, aVal] of mapA) {
        if (!mapB.has(key)) return false;
        if (mapB.get(key) !== aVal) return false;
    }
    return true;
}

function countChars(s: string) {
    return Array.from(s).reduce((acc: Map<string, number>, c: string) => {
        if (acc.has(c)) {
            acc.set(c, acc.get(c) + 1);
        } else {
            acc.set(c, 1);
        }
        return acc;
    }, new Map<string, number>())
}

function isAnagramSorting(s: string, t: string): boolean {
    const sSorted = Array.from(s).sort().join('');
    const tSorted = Array.from(t).sort().join('');
    return sSorted === tSorted;
}

function countCharsFast(s: string): Record<string, number> {
  const result: Record<string, number> = {};
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    result[c] = (result[c] || 0) + 1;
  }
  return result;
}

function areCountsEqual(a: Record<string, number>, b: Record<string, number>): boolean {
  const aKeys = Object.keys(a);
  if (aKeys.length !== Object.keys(b).length) return false;

  for (const key of aKeys) {
    if (a[key] !== b[key]) return false;
  }

  return true;
}