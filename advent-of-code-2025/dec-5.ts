import { assertEquals } from "jsr:@std/assert@1.0.16/equals";

type FreshIdRangeTuple = [number, number];

class FreshSet {
  private idRanges: FreshIdRangeTuple[];

  constructor(freshIdRanges: FreshIdRangeTuple[]) {
    this.idRanges = freshIdRanges;
  }

  isFresh(id: number): boolean {
    return this.idRanges.some(([startIncl, endIncl]) =>
      isWithinRange(id, startIncl, endIncl)
    );
  }

  countFreshIds() {
    return consolidateIdRanges(this.idRanges).reduce((acc: number, range) => {
      console.log("count", range, rangeSize(range));
      return acc + rangeSize(range);
    }, 0);
  }
}

function isWithinRange(num: number, startIncl: number, endIncl: number) {
  return num >= startIncl && num <= endIncl;
}

function rangeSize(range: FreshIdRangeTuple) {
  return 1 + range[1] - range[0];
}

assertEquals(rangeSize([0, 1]), 2);
assertEquals(rangeSize([0, 2]), 3);
assertEquals(rangeSize([1, 2]), 2);
assertEquals(rangeSize([5, 9]), 5);

function areRangesOverlapping(a: FreshIdRangeTuple, b: FreshIdRangeTuple) {
  return a[0] <= b[1] && b[0] <= a[1];
}

assertEquals(areRangesOverlapping([3, 5], [10, 14]), false);
assertEquals(areRangesOverlapping([12, 18], [10, 14]), true);
assertEquals(areRangesOverlapping([1, 10], [3, 5]), true);
assertEquals(areRangesOverlapping([3, 5], [1, 10]), true);
assertEquals(areRangesOverlapping([1, 5], [6, 10]), false);
assertEquals(areRangesOverlapping([1, 5], [5, 10]), true);

function consolidateIdRanges(ranges: FreshIdRangeTuple[]) {
  const rangesSortedByStartAsc = ranges.sort((a, b) => a[0] - b[0]);

  const consolidatedRanges: FreshIdRangeTuple[] = [rangesSortedByStartAsc[0]];

  for (const range of rangesSortedByStartAsc.slice(1)) {
    const currentRange = consolidatedRanges[consolidatedRanges.length - 1];
    if (areRangesOverlapping(currentRange, range)) {
      currentRange[1] = Math.max(currentRange[1], range[1]);
    } else {
      consolidatedRanges.push(range);
    }
  }

  return consolidatedRanges;
}

assertEquals(consolidateIdRanges([[1, 2]]), [[1, 2]]);
assertEquals(consolidateIdRanges([[1, 2], [2, 3]]), [[1, 3]]);
assertEquals(consolidateIdRanges([[1, 1], [2, 3]]), [[1, 1], [2, 3]]);

const exampleRanges: FreshIdRangeTuple[] = [[3, 5], [10, 14], [16, 20], [
  12,
  18,
]];
const exampleFreshSet = new FreshSet(exampleRanges);
assertEquals(exampleFreshSet.isFresh(1), false);
assertEquals(exampleFreshSet.isFresh(5), true);
assertEquals(exampleFreshSet.isFresh(8), false);
assertEquals(exampleFreshSet.isFresh(11), true);
assertEquals(exampleFreshSet.isFresh(17), true);
assertEquals(exampleFreshSet.isFresh(32), false);

function parseInput(s: string) {
  const freshIdRanges: FreshIdRangeTuple[] = [];
  const ids: number[] = [];

  const isRange = (str: string) => str.includes("-");

  s.split("\n").forEach((row) => {
    if (row.length === 0) {
      // do nothing
    } else if (isRange(row)) {
      freshIdRanges.push(row.split("-").map(Number) as [number, number]);
    } else {
      ids.push(Number(row));
    }
  });

  return { freshIdRanges, ids };
}

const exampleString = `3-5
10-14
16-20
12-18

1
5
8
11
17
32`;
const exampleIds = [1, 5, 8, 11, 17, 32];
assertEquals(parseInput(exampleString).ids, exampleIds);
assertEquals(parseInput(exampleString).freshIdRanges, exampleRanges);

function countFreshItems(s: string) {
  const { freshIdRanges, ids } = parseInput(s);
  const freshIdSet = new FreshSet(freshIdRanges);

  return ids.reduce((acc: number, id: number) => {
    if (freshIdSet.isFresh(id)) acc++;
    return acc;
  }, 0);
}
assertEquals(countFreshItems(exampleString), 3);
//console.log(countFreshIds(Deno.readTextFileSync("dec-5.txt")));

function countFreshIds(s: string) {
  const { freshIdRanges } = parseInput(s);
  const freshIdSet = new FreshSet(freshIdRanges);

  return freshIdSet.countFreshIds();
}
assertEquals(countFreshIds(exampleString), 14);

console.log(countFreshIds(Deno.readTextFileSync("dec-5.txt")));
