import { assertEquals } from "jsr:@std/assert@1.0.16/equals";

type FreshIdRangeTuple = [number, number];
type FreshIdRange = {
  startIncl: number;
  endIncl: number;
};

class FreshSet {
  private idRanges: FreshIdRange[];

  constructor(freshIdRanges: FreshIdRangeTuple[]) {
    this.idRanges = freshIdRanges.map(([startIncl, endIncl]) => ({
      startIncl,
      endIncl,
    }));
  }

  isFresh(id: number): boolean {
    return this.idRanges.some(({ startIncl, endIncl }) =>
      isWithinRange(id, startIncl, endIncl)
    );
  }
}

function isWithinRange(num: number, startIncl: number, endIncl: number) {
  return num >= startIncl && num <= endIncl;
}

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

function solve(s: string) {
  const { freshIdRanges, ids } = parseInput(s);
  const freshIdSet = new FreshSet(freshIdRanges);

  return ids.reduce((acc: number, id: number) => {
    if (freshIdSet.isFresh(id)) acc++;
    return acc;
  }, 0);
}

assertEquals(solve(exampleString), 3);

console.log(solve(Deno.readTextFileSync("dec-5.txt")));
