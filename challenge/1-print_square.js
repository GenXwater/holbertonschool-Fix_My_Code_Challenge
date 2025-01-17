#!/usr/bin/node
/*
    Print a square using the character #

    The size of the square should be provided as the first argument
    of the program.
*/

if (process.argv.length <= 2) {
  console.error("Error: Missing size argument"); // Clearer error message
  console.error("Usage: ./1-print_square.js <size>");
  console.error("Example: ./1-print_square.js 5");
  process.exit(1);
}

// Parse the size argument as an integer
const size = parseInt(process.argv[2], 10);

// Validate the size argument
if (isNaN(size) || size <= 0) {
  console.error("Error: Size must be a positive integer");
  process.exit(1);
}

// Generate the square
for (let row = 0; row < size; row++) {
  console.log("#".repeat(size)); // Print a full row of '#' using .repeat()
}
