import { assertEquals } from "jsr:@std/assert";

// Diagram: https://www.tldraw.com/f/SCuT_cSxjvfIQaZoTQVhW?d=v2765.4390.1840.1074.SLsar4eMDHcnZCw3QuU06

type RotationDirection = "R" | "L";
type RotationInstructionString = `${RotationDirection}${number}`;
type RotationInstrution = { direction: RotationDirection; distance: number };

// === Counting Strategies ===
type CountContext = {
  before: number;
  after: number;
  instruction: RotationInstructionString;
};
type CountDecisionFn = (arg: CountContext) => number;

// -- Landed on Zero ---
const traveledToZero: CountDecisionFn = (ctx: CountContext) => {
  if (ctx.before === 0) return 0;
  return ctx.after === 0 ? 1 : 0;
};

assertEquals(traveledToZero({ before: 0, after: 0, instruction: "R0" }), 0);
assertEquals(traveledToZero({ before: 0, after: 1, instruction: "R1" }), 0);
assertEquals(traveledToZero({ before: 0, after: -1, instruction: "L1" }), 0);
assertEquals(traveledToZero({ before: -1, after: 1, instruction: "R2" }), 0);
assertEquals(traveledToZero({ before: 1, after: -1, instruction: "L2" }), 0);
assertEquals(traveledToZero({ before: -1, after: 0, instruction: "R1" }), 1);
assertEquals(traveledToZero({ before: 1, after: 0, instruction: "L1" }), 1);

// --- Times Past Zero or Landed on Zero ---
const timesPastZeroOrLandedOnZero: CountDecisionFn = (ctx: CountContext) => {
  const { after, before, instruction } = ctx;

  const { distance, direction } = parseInstructionIntoNumber(instruction);
  const roundTrips = Math.floor(Math.abs(distance) / 100);

  let count = roundTrips;

  if (before !== after && before !== 0) {
    // we traveled somewhere new
    const remainder = distance % 100;
    const afterRemainder = remainder + before;

    if (direction === "L" && afterRemainder <= 0) {
      count++;
    }
    if (direction === "R" && afterRemainder >= 100) {
      count++;
    }
  }

  return count;
};

assertEquals(
  timesPastZeroOrLandedOnZero({ before: 50, after: 51, instruction: "R1" }),
  0,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 1, after: 0, instruction: "L1" }),
  1,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 99, after: 0, instruction: "R1" }),
  1,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 0, after: 0, instruction: "R0" }),
  0,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 0, after: 1, instruction: "R1" }),
  0,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 0, after: 99, instruction: "L1" }),
  0,
);

assertEquals(
  timesPastZeroOrLandedOnZero({ before: 1, after: 99, instruction: "L2" }),
  1,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 99, after: 1, instruction: "R2" }),
  1,
);

assertEquals(
  timesPastZeroOrLandedOnZero({ before: 99, after: 99, instruction: "R100" }),
  1,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 10, after: 10, instruction: "L100" }),
  1,
);

assertEquals(
  timesPastZeroOrLandedOnZero({ before: 99, after: 0, instruction: "R101" }),
  2,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 99, after: 1, instruction: "R102" }),
  2,
);

assertEquals(
  timesPastZeroOrLandedOnZero({ before: 1, after: 0, instruction: "L101" }),
  2,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 1, after: 99, instruction: "L102" }),
  2,
);

// Examples
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 52, after: 0, instruction: "R48" }),
  1,
);
assertEquals(
  timesPastZeroOrLandedOnZero({ before: 95, after: 50, instruction: "R60" }),
  1,
);

assertEquals(
  timesPastZeroOrLandedOnZero({ before: 50, after: 50, instruction: "R1000" }),
  10,
);

// === Solve Puzzle ===
function solveFromString(s: string, fn: CountDecisionFn): number {
  const instructions = parseInput(s);
  return getPassword(50, instructions, fn);
}

// Part 1
assertEquals(
  solveFromString(
    `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82`,
    traveledToZero,
  ),
  3,
);

// Part 2
assertEquals(
  solveFromString(
    `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82`,
    timesPastZeroOrLandedOnZero,
  ),
  6,
);

function getPassword(
  initialPosition: number,
  instructions: RotationInstructionString[],
  countIncrementFn: CountDecisionFn,
) {
  let currentPosition = initialPosition;

  let count = 0;
  for (const instruction of instructions) {
    const before = currentPosition;
    const after = rotateDial(before, instruction);
    count += countIncrementFn({ before, after, instruction });
    currentPosition = after;
  }

  return count;
}

// --- Rotate Dial --
function rotateDial(
  position: number,
  instruction: RotationInstructionString,
  numberOfSafePositions: number = 100,
): number {
  const { distance } = parseInstructionIntoNumber(instruction);
  const newPositionUnbounded = position + distance;
  const clampedPosition =
    ((newPositionUnbounded % numberOfSafePositions) + numberOfSafePositions) %
    numberOfSafePositions;
  return clampedPosition;
}

assertEquals(rotateDial(0, "R5"), 5);
assertEquals(rotateDial(0, "R10"), 10);
assertEquals(rotateDial(5, "R10"), 15);
assertEquals(rotateDial(99, "R1"), 0);
assertEquals(rotateDial(99, "R2"), 1);

assertEquals(rotateDial(99, "R2"), 1);

assertEquals(rotateDial(0, "L5"), 95);
assertEquals(rotateDial(0, "L10"), 90);
assertEquals(rotateDial(5, "L10"), 95);
assertEquals(rotateDial(10, "L5"), 5);
assertEquals(rotateDial(10, "L10"), 0);

// === Parsers ===
function parseInstructionIntoNumber(
  instruction: RotationInstructionString,
): { direction: RotationDirection; distance: number } {
  const value = Number(instruction.slice(1));
  const isPositive = instruction.startsWith("R");

  return {
    direction: isPositive ? "R" : "L",
    distance: isPositive ? value : -1 * value,
  } as RotationInstrution;
}

assertEquals(parseInstructionIntoNumber("L0"), { direction: "L", distance: 0 });
assertEquals(parseInstructionIntoNumber("R0"), { direction: "R", distance: 0 });
assertEquals(parseInstructionIntoNumber("R1"), { direction: "R", distance: 1 });
assertEquals(parseInstructionIntoNumber("L1"), {
  direction: "L",
  distance: -1,
});
assertEquals(parseInstructionIntoNumber("L10"), {
  direction: "L",
  distance: -10,
});
assertEquals(parseInstructionIntoNumber("R10"), {
  direction: "R",
  distance: 10,
});

function parseInput(s: string): RotationInstructionString[] {
  const strings = s.split("\n");

  const instructions = strings.filter(isValidInstruction);
  if (strings.length !== instructions.length) {
    console.log(
      "The following are not instricitons",
      instructions.filter((i) => !isValidInstruction(i)),
    );
    throw new Error("Some are not instructions");
  }

  return instructions;
}

function isValidInstruction(s: string): s is RotationInstructionString {
  if (s.length < 2) return false;

  const firstLetter = s[0];
  if (firstLetter !== "R" && firstLetter !== "L") return false;

  const value = parseInstructionIntoNumber(s as RotationInstructionString);
  if (Number.isNaN(value)) return false;

  return true;
}

console.log(
  solveFromString(
    Deno.readTextFileSync("dec-1.txt"),
    timesPastZeroOrLandedOnZero,
  ),
);
