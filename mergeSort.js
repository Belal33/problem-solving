const { runSortTest } = require("./runTest");

function sliceIncloudEnd(arr, start, end) {
	return arr.slice(start, end + 1);
}
function mergeSort(arr = [], start = 0, end = arr.length - 1) {
	if (start >= end) return arr;
	let mid = Math.floor((end + start) / 2);

	// left side
	mergeSort(arr, start, mid);
	// right side
	mergeSort(arr, mid + 1, end);
	// merge
	merge(arr, start, mid, end);
	return arr;
}

function merge(arr, start, mid, end) {
	let left = sliceIncloudEnd(arr, start, mid);
	let right = sliceIncloudEnd(arr, mid + 1, end);
	let iLeft = 0,
		iRight = 0,
		k = start;

	while (iLeft < left.length && iRight < right.length) {
		if (left[iLeft] <= right[iRight]) {
			// if left element is smaller
			arr[k++] = left[iLeft++];
		} else {
			// if left element is greater
			arr[k++] = right[iRight++];
		}
	}
	// if right array is not empty
	while (iLeft < left.length) {
		arr[k++] = left[iLeft++];
	}
	while (iRight < right.length) {
		arr[k++] = right[iRight++];
	}
}

let testArr = [3, 4, 2, 1, 5];
runSortTest(mergeSort);
// mergeSort(testArr);
// console.log(mergeSort(testArr));
