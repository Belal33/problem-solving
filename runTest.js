function assertEqual(actual, expected, message) {
	if (JSON.stringify(actual) === JSON.stringify(expected)) {
		console.log(`✔ ${message}`);
	} else {
		console.error(`✘ ${message}`);
		console.error(`  Expected: ${JSON.stringify(expected)}`);
		console.error(`  Actual: ${JSON.stringify(actual)}`);
	}
}

function runSortTest(sortingFunction) {
	assertEqual(
		sortingFunction([5, 3, 8, 4, 2]),
		[2, 3, 4, 5, 8],
		"Test Case 1: Sorts an array of numbers"
	);
	assertEqual(
		sortingFunction([1, 2, 3, 4, 5]),
		[1, 2, 3, 4, 5],
		"Test Case 2: Returns an already sorted array"
	);
	assertEqual(sortingFunction([]), [], "Test Case 3: Handles an empty array");
	assertEqual(
		sortingFunction([1]),
		[1],
		"Test Case 4: Handles an array with one element"
	);
	assertEqual(
		sortingFunction([4, 2, 2, 8, 5, 3]),
		[2, 2, 3, 4, 5, 8],
		"Test Case 5: Sorts an array with duplicate elements"
	);
}

module.exports = { runSortTest, assertEqual };
