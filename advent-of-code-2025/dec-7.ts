import { assertEquals } from "jsr:@std/assert@1.0.16/equals";

type StartChar = "S";
type EmptySpaceChar = ".";
type SplitterChar = "^";
type GridChar = StartChar | EmptySpaceChar | SplitterChar;
type GridRow = Array<GridChar>;
type Grid = Array<GridRow>;
type Position = [x: number, y: number];

function isStartChar(char: GridChar): char is StartChar {
  return char === "S";
}

function isSplitterChar(char: GridChar): char is SplitterChar {
  return char === "^";
}

function isEMptySpaceChar(char: GridChar): char is EmptySpaceChar {
  return char === ".";
}

function indexOfStartPositionInStartingRow(row: GridRow): number | null {
  const index = row.indexOf("S");
  if (index === -1) return null;
  return index;
}

function parseInputStringIntoGrid(input: string): Grid {
  return input.split("\n").map((line) => line.split("") as GridRow);
}

function solveGridSplits(grid: Grid): number {
  if (grid.length < 1) throw new Error("Grid is too small");
  const startingY = 1;

  const startingX = indexOfStartPositionInStartingRow(grid[0]);
  if (!startingX) throw new Error("Did not find S in starting row");

  const history = new PositionCheckHistory();
  return countSplits(grid, [startingX, startingY], history);
}

function solveGridTimelines(grid: Grid): number {
  if (grid.length < 1) throw new Error("Grid is too small");
  const startingY = 1;

  const startingX = indexOfStartPositionInStartingRow(grid[0]);
  if (!startingX) throw new Error("Did not find S in starting row");

  const history = new PositionCheckHistory();
  return countTimelines(grid, [startingX, startingY], history);
}

function countSplits(
  grid: Grid,
  [x, y]: Position,
  history: PositionCheckHistory,
): number {
  //console.log(compactGridIntoString(grid, history, [x, y]), [x, y]);
  //waitForUserToPressKey("c", "continue");
  history.addPosition([x, y]);

  const nextYIndexOfSplitter = findYIndexOfNextSplitterInclStartingPosition(
    grid,
    [x, y],
    history,
  );
  if (nextYIndexOfSplitter === null) {
    return 0;
  }

  const leftPos: Position = [x - 1, nextYIndexOfSplitter];
  const rightPos: Position = [x + 1, nextYIndexOfSplitter];
  const [shouldCountLeft, shouldCountRight] = [
    canExploreSplitsFromPos(grid, leftPos, history),
    canExploreSplitsFromPos(grid, rightPos, history),
  ];
  //let splitMessage = "";
  //splitMessage += shouldCountLeft ? "✅ Left" : "❌ Left";
  //splitMessage += shouldCountRight ? " Right ✅" : " Right ❌";
  //console.log(splitMessage);

  const alreadHitThisSplitter = history.hasCheckedPosition(leftPos) &&
    history.hasCheckedPosition(rightPos);
  if (alreadHitThisSplitter) {
    return 0;
  }

  const splitsFromLeftSide = shouldCountLeft
    ? countSplits(grid, leftPos, history)
    : 0;
  const splitsFromRightSide = shouldCountRight
    ? countSplits(grid, rightPos, history)
    : 0;

  return 1 + splitsFromLeftSide + splitsFromRightSide;
}

function countTimelines(
  grid: Grid,
  [x, y]: Position,
  history: PositionCheckHistory,
): number {
  if (
    history.hasCheckedPosition([x, y]) &&
    history.getValueAtPosition([x, y]) !== undefined
  ) {
    return history.getValueAtPosition([x, y]) as number;
  }

  //console.log(compactGridIntoString(grid, history, [x, y]));

  const nextYIndexOfSplitter = findYIndexOfNextSplitterInclStartingPosition(
    grid,
    [x, y],
    history,
  );
  if (nextYIndexOfSplitter === null) {
    return 1;
  }

  const leftPos: Position = [x - 1, nextYIndexOfSplitter];
  const rightPos: Position = [x + 1, nextYIndexOfSplitter];
  const [shouldCountLeft, shouldCountRight] = [
    canExploreTimelinesFromPos(grid, leftPos),
    canExploreTimelinesFromPos(grid, rightPos),
  ];

  const splitsFromLeftSide = shouldCountLeft
    ? history.getValueAtPosition(leftPos) ??
      countTimelines(grid, leftPos, history)
    : 0;
  history.addPosition(leftPos, splitsFromLeftSide);
  const splitsFromRightSide = shouldCountRight
    ? history.getValueAtPosition(rightPos) ??
      countTimelines(grid, rightPos, history)
    : 0;
  history.addPosition(rightPos, splitsFromRightSide);

  return splitsFromLeftSide + splitsFromRightSide;
}

class PositionCheckHistory {
  private storedValues: Map<string, number | undefined>;

  constructor() {
    this.storedValues = new Map<string, number>();
  }

  public addPosition(pos: Position, value?: number) {
    const key = PositionCheckHistory.buildKeyFromPosition(pos);
    this.storedValues.set(key, value);
  }

  public hasCheckedPosition(pos: Position) {
    const key = PositionCheckHistory.buildKeyFromPosition(pos);
    return this.storedValues.has(key);
  }

  public getValueAtPosition(pos: Position) {
    const key = PositionCheckHistory.buildKeyFromPosition(pos);
    return this.storedValues.get(key);
  }

  private static buildKeyFromPosition(position: Position): string {
    return `${position[0]},${position[1]}`;
  }
}

function isPositionWithinBounds(
  grid: Grid,
  [x, y]: Position,
): boolean {
  const maxYIndex = grid.length - 1;
  const maxXIndex = grid[0].length;

  if (x < 0 || x > maxXIndex) {
    console.log(`${x} would be out of bounds`);
    return false;
  }

  if (y < 0 || y > maxYIndex) {
    console.log(`${y} would be out of bounds`);
    return false;
  }

  return true;
}

function canExploreSplitsFromPos(
  grid: Grid,
  pos: Position,
  history: PositionCheckHistory,
) {
  return isPositionWithinBounds(grid, pos) &&
    !history.hasCheckedPosition(pos);
}

function canExploreTimelinesFromPos(
  grid: Grid,
  pos: Position,
) {
  return isPositionWithinBounds(grid, pos);
}

function findYIndexOfNextSplitterInclStartingPosition(
  grid: Grid,
  [x, startingY]: Position,
  history?: PositionCheckHistory,
): number | null {
  let y = startingY;
  const maxYIndex = grid.length - 1;

  while (y <= maxYIndex && !isSplitterChar(grid[y][x])) {
    history?.addPosition([x, y]);
    y++;
  }

  if (y > maxYIndex) return null;
  return y;
}

assertEquals(
  findYIndexOfNextSplitterInclStartingPosition([["."]], [0, 0]),
  null,
);
assertEquals(findYIndexOfNextSplitterInclStartingPosition([["^"]], [0, 0]), 0);
assertEquals(
  findYIndexOfNextSplitterInclStartingPosition([["."], ["^"]], [0, 0]),
  1,
);
assertEquals(
  findYIndexOfNextSplitterInclStartingPosition([[".", "^"], ["^", "."]], [
    0,
    0,
  ]),
  1,
);

const exampleString = `.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............`;

function compactGridIntoString(
  grid: Grid,
  history: PositionCheckHistory,
  pos?: Position,
) {
  let gridStr = "";
  for (let y = 0; y < grid.length; y++) {
    let rowStr = "";
    for (let x = 0; x < grid[0].length; x++) {
      if (pos && x === pos[0] && y === pos[1]) {
        rowStr += "👨‍🚀";
        continue;
      }
      const cellStr = history.hasCheckedPosition([x, y]) ? "|" : grid[y][x];
      rowStr += cellStr;
    }
    rowStr += "\n";
    gridStr += rowStr;
  }

  return gridStr;
}
assertEquals(
  compactGridIntoString(
    parseInputStringIntoGrid(exampleString),
    new PositionCheckHistory(),
  ),
  exampleString + "\n",
);

const simpleGrid = `.S.
...
.^.
...`;
//assertEquals(solveGridSplits(parseInputStringIntoGrid(simpleGrid)), 2);
//assertEquals(solveGridTimelines(parseInputStringIntoGrid(simpleGrid)), 2);

const simpleGrid2 = `..S..
.....
.^...`;
//assertEquals(solveGridSplits(parseInputStringIntoGrid(simpleGrid2)), 0);
assertEquals(solveGridTimelines(parseInputStringIntoGrid(simpleGrid2)), 1);

const simpleGrid3 = `..S..
.....
..^..
.....
.^.^.`;
assertEquals(solveGridSplits(parseInputStringIntoGrid(simpleGrid3)), 3);
assertEquals(solveGridTimelines(parseInputStringIntoGrid(simpleGrid3)), 4);

const simpleGrid4 = `...S...
.......
...^...
.......
..^.^..
.......
.^.^...
.......
..^....`;
assertEquals(solveGridSplits(parseInputStringIntoGrid(simpleGrid4)), 6);

assertEquals(solveGridSplits(parseInputStringIntoGrid(exampleString)), 21);
assertEquals(
  solveGridTimelines(parseInputStringIntoGrid(exampleString)),
  40,
);
console.log(
  solveGridTimelines(
    parseInputStringIntoGrid(Deno.readTextFileSync("dec-7.txt")),
  ),
);

function waitForUserToPressKey(actionKey: string, actionLabel: string) {
  const response = prompt(
    `Press ${actionKey} to ${actionLabel} (or Ctrl+C to exit):`,
  );

  if (response === actionKey) {
    return;
  }

  console.log("\nInterrupted.\n");
  Deno.exit(1);
}
