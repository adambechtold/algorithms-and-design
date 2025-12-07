import { assertEquals } from "jsr:@std/assert@1.0.16/equals";

type FloorTile = "@" | ".";
type Grid<T> = Array<Array<T>>;
type CafeteriaFloor = Grid<FloorTile>;

type PositionZeroIndexed = {
  x: number;
  y: number;
};

const OutOfBounds = Symbol("OutOfBounds");

function getAtGridPosition<T>(
  floor: Grid<T>,
  position: PositionZeroIndexed,
) {
  if (!floor.length) {
    throw new Error(
      `Must provide floor with tiles. Not empty. Position: ${position}, floor: ${floor}`,
    );
  }
  const maxYPosition = floor.length - 1;
  const maxXPosition = floor[0].length - 1;

  const { x, y } = position;

  if (x > maxXPosition || x < 0) return OutOfBounds;
  if (y > maxYPosition || y < 0) return OutOfBounds;

  return floor[y][x];
}

assertEquals(getAtGridPosition([["a", "b"]], { x: 1, y: 0 }), "b");
assertEquals(getAtGridPosition([["a", "b"]], { x: 0, y: 0 }), "a");
assertEquals(getAtGridPosition([["a", "b"]], { x: 0, y: 1 }), OutOfBounds);
assertEquals(getAtGridPosition([["a", "b"]], { x: 2, y: 0 }), OutOfBounds);
assertEquals(getAtGridPosition([["a", "b"]], { x: -1, y: 0 }), OutOfBounds);
assertEquals(getAtGridPosition([["a", "b"]], { x: 0, y: -1 }), OutOfBounds);
assertEquals(
  getAtGridPosition([["a", "b"], ["c", "d"]], { x: 0, y: 1 }),
  "c",
);
assertEquals(
  getAtGridPosition([["a", "b"], ["c", "d"]], { x: 1, y: 1 }),
  "d",
);

function getNeighborIndexesInclOutOfBounds(position: PositionZeroIndexed) {
  const { x: xPos, y: yPos } = position;

  const neighbors: PositionZeroIndexed[] = [];

  for (let y = yPos - 1; y <= yPos + 1; y++) {
    for (let x = xPos - 1; x <= xPos + 1; x++) {
      if (x === xPos && y === yPos) continue;
      neighbors.push({ x, y });
    }
  }

  return neighbors;
}

function numberOfSurroundingTowels(
  floor: CafeteriaFloor,
  position: PositionZeroIndexed,
): number {
  const neighbors = getNeighborIndexesInclOutOfBounds(position);
  const contentsOfNeighbors = neighbors.map((n) => getAtGridPosition(floor, n));
  const numberOfPaperTowls =
    contentsOfNeighbors.filter((c) => c === "@").length;
  return numberOfPaperTowls;
}

function countPickablePaperTowels(floor: CafeteriaFloor) {
  let count = 0;
  for (let y = 0; y < floor.length; y++) {
    for (let x = 0; x < floor[0].length; x++) {
      const contentsAtPosition = getAtGridPosition(floor, { x, y });
      if (contentsAtPosition !== "@") continue;
      const towelCount = numberOfSurroundingTowels(floor, { x, y });
      if (towelCount < 4) {
        count++;
      }
    }
  }

  return count;
}

function pickUpAllPaperTowels(floor: CafeteriaFloor) {
  let totalNumTowelsRemoved = 0;
  let towelsRemovedThisIteration = 0;
  let currentFloorState = copyFloor(floor);
  do {
    towelsRemovedThisIteration = 0;
    currentFloorState = copyFloor(currentFloorState);

    for (let y = 0; y < currentFloorState.length; y++) {
      for (let x = 0; x < currentFloorState[0].length; x++) {
        const contentsAtPosition = getAtGridPosition(currentFloorState, {
          x,
          y,
        });
        if (contentsAtPosition !== "@") continue;
        const towelCount = numberOfSurroundingTowels(currentFloorState, {
          x,
          y,
        });
        if (towelCount < 4) {
          towelsRemovedThisIteration++;
          totalNumTowelsRemoved++;
          currentFloorState[y][x] = ".";
        }
      }
    }
  } while (towelsRemovedThisIteration > 0);

  return totalNumTowelsRemoved;
}

function copyFloor(floor: CafeteriaFloor) {
  const newFloor: CafeteriaFloor = [];
  for (const row of floor) {
    const newRow: CafeteriaFloor[number] = [];
    for (const tile of row) {
      newRow.push(tile);
    }
    newFloor.push(newRow);
  }
  return newFloor;
}

function _printFloor(floor: CafeteriaFloor) {
  console.log(
    floor.map((row) => row.join("")).join("\n"),
  );
}

const exampleInput = `..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.`;

function parseStringIntoCafeteriaFloor(s: string): CafeteriaFloor {
  const rows = s.split("\n");
  return rows.map((r) => r.split("")) as Array<FloorTile[]>;
}

assertEquals(
  countPickablePaperTowels(parseStringIntoCafeteriaFloor(exampleInput)),
  13,
);
assertEquals(
  pickUpAllPaperTowels(parseStringIntoCafeteriaFloor(exampleInput)),
  43,
);

console.log(
  pickUpAllPaperTowels(
    parseStringIntoCafeteriaFloor(Deno.readTextFileSync("dec-4.txt")),
  ),
);
