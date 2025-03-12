function binarySearch(arr, target) {
	let low = 0;
	let high = arr.length - 1;
	let mid = 0;
	while (high >= low) {
		mid = Math.floor((low + high) / 2);
		if (arr[mid] === target) return mid;
		if (arr[mid] >= target) high = mid - 1;
		if (arr[mid] <= target) low = mid + 1;
	}
	return -1;
}

// Testing code
const assert = (condition, message) => {
	if (!condition) {
		console.error(`Test failed: ${message}`);
	} else {
		console.log("Test passed");
	}
};

// Test cases
const arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];

assert(binarySearch(arr, 1) === 0, "Test Case 1");
assert(binarySearch(arr, 5) === 2, "Test Case 2");
assert(binarySearch(arr, 9) === 4, "Test Case 3");
assert(binarySearch(arr, 15) === 7, "Test Case 4");
assert(binarySearch(arr, 19) === 9, "Test Case 5");
assert(binarySearch(arr, 21) === -1, "Test Case 6");
assert(binarySearch(arr, 0) === -1, "Test Case 7");
