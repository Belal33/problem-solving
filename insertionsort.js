const { runSortTest } = require("./runTest");

function insertionSort(arr) {
	for (let i = 1; i < arr.length; i++) {
		let el = arr[i];
		for (j = i - 1; j >= 0; j--) {
			if (arr[j] > el) {
				arr[j + 1] = arr[j];
				arr[j] = el;
			} else {
				break;
			}
		}
	}
	return arr;
}

runSortTest(insertionSort);
