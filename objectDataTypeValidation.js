const isSupporedType = (type) => {
	// if not valid raise error
	let supporedTypes = ["string", "number", "boolean", "array", "undefined"];
	return supporedTypes.includes(type);
};

const validateObject = (obj, schema) => {
	for (let key in schema) {
		//  if schema is not direct type (number ,string ,bolean,undefined)
		if (typeof obj[key] !== schema[key]) {
			if (typeof schema[key] === "object") {
				if (!validateObject(obj[key], schema[key])) {
					console.log(`${key} is not valid object`);
					return false;
				} else {
					console.log(`${key} is valid [${key}:{}]`);
				}
			} else if (schema[key] === "array") {
				if (Array.isArray(obj[key]))
					console.log(`${key} is valid type. ${"array"} == ${schema[key]}`);
				else {
					console.log(`${key} is not valid array`);
					return false;
				}
			} else {
				console.log(`${key} is not valid array or object]`);
				return false;
			}
		} else if (!isSupporedType(schema[key])) {
			throw new Error(`${key} is not supported type  [${schema[key]}]`);
		} else {
			console.log(`${key} is valid type. ${typeof obj[key]} == ${schema[key]}`);
		}
	}
	return true;
};

// Test Cases

console.log("###########################################################");
console.log("###################### start testing ######################");
console.log("###########################################################");
// Helper function to run tests and log results
const runTest = (testName, obj, schema, expected) => {
	console.log(`\nRunning test: ${testName}`);
	const result = validateObject(obj, schema);
	if (result === expected) {
		console.log(`Test ${testName} passed.`);
	} else {
		console.error(
			`
			 *******************************************************************
			 * Test ${testName} failed. Expected ${expected}, but got ${result}*
			 *******************************************************************
			 ${JSON.stringify(obj, null, 2)}
			 ${JSON.stringify(schema, null, 2)}
			`
		);
	}
};

// Test Case 1: Valid Object
const schema1 = {
	name: "string",
	age: "number",
	hobbies: "array",
	isMarried: "boolean",
	address: {
		city: "string",
		zip: "number",
	},
};
const obj1 = {
	name: "John Doe",
	age: 30,
	hobbies: ["reading", "hiking"],
	isMarried: true,
	address: {
		city: "New York",
		zip: 10001,
	},
};
runTest("Valid Object", obj1, schema1, true);

// Test Case 2: Invalid Object - Wrong Type
const obj2 = {
	name: "Jane Doe",
	age: "30", // Should be a number
	hobbies: ["reading"],
	isMarried: false,
	address: {
		city: "London",
		zip: 2000,
	},
};
runTest("Invalid Object - Wrong Type", obj2, schema1, false);

// Test Case 3: Invalid Object - Missing Key
const obj3 = {
	name: "Peter Pan",
	age: 25,
	hobbies: ["flying"],
	// isMarried is missing
	address: {
		city: "Neverland",
		zip: 0,
	},
};
runTest("Invalid Object - Missing Key", obj3, schema1, false); // it will pass because the function only check if the key is exist in the object not the opposite

// Test Case 4: Invalid Object - Nested Wrong Type
const obj4 = {
	name: "Alice",
	age: 22,
	hobbies: ["wondering"],
	isMarried: false,
	address: {
		city: 123, // Should be a string
		zip: 90210,
	},
};
runTest("Invalid Object - Nested Wrong Type", obj4, schema1, false);

// Test Case 5: Invalid Object - Nested Missing Key
const obj5 = {
	name: "Bob",
	age: 40,
	hobbies: ["coding"],
	isMarried: true,
	address: {
		// city is missing
		zip: 12345,
	},
};
runTest("Invalid Object - Nested Missing Key", obj5, schema1, false); // it will pass because the function only check if the key is exist in the object not the opposite

// Test Case 6: Valid Object - Empty Object
const schema6 = {};
const obj6 = {};
runTest("Valid Object - Empty Object", obj6, schema6, true);

// Test Case 7: Invalid Object - Array instead of object
const schema7 = {
	name: "string",
	address: {
		city: "string",
	},
};
const obj7 = {
	name: "test",
	address: ["test"],
};
runTest("Invalid Object - Array instead of object", obj7, schema7, false);

// Test Case 8: Valid Object - undefined value
const schema8 = {
	name: "string",
	value: "undefined",
};
const obj8 = {
	name: "test",
	value: undefined,
};
runTest("Valid Object - undefined value", obj8, schema8, true);

// Test Case 9: Invalid Object - wrong undefined value
const schema9 = {
	name: "string",
	value: "undefined",
};
const obj9 = {
	name: "test",
	value: "test",
};
runTest("Invalid Object - wrong undefined value", obj9, schema9, false);

// Test Case 10: Valid Object - array value
const schema10 = {
	name: "string",
	value: "array",
};
const obj10 = {
	name: "test",
	value: ["test"],
};
runTest("Valid Object - array value", obj10, schema10, true);

// Test Case 11: Invalid Object - wrong array value
const schema11 = {
	name: "string",
	value: "array",
};
const obj11 = {
	name: "test",
	value: "test",
};
runTest("Invalid Object - wrong array value", obj11, schema11, false);

// Test Case 12: Invalid schema - unsupported type
const schema12 = {
	name: "string",
	value: "date",
};
const obj12 = {
	name: "test",
	value: "test",
};
try {
	runTest("Invalid schema - unsupported type", obj12, schema12, false);
} catch (error) {
	console.error(
		`Test Invalid schema - unsupported type passed with error: ${error.message}`
	);
}
console.log("###########################################################");
console.log("###################### end testing ######################");
console.log("###########################################################");
