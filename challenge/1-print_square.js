#!/usr/bin/node
/*
    Print a square using the character #

    The size of the square should be provided as the first argument
    of the program.
*/

if (process.argv.length <= 2) {
  console.error("Missing argument\n");
  console.error("Usage: ./1-print_square.js <size>\n");
  console.error("Example: ./1-print_square.js 8\n");
  process.exit(1);
}

const size = parseInt(process.argv[2], 10);

for (let i = 0 ; i < size ; i ++) {
  for (let j = 0 ; j < size ; j ++) {
      process.stdout.write("#");
  }
  process.stdout.write("\n");
}