// a string(x,y) is considered valid if the following criteria are met:
// the string starts with a (, has a comma after X and ends with a )
// there is no space between the opening parenthesis and the first character of X
// there is no space between the comma and the last character of x
// there is one space between the comma and the first character of y
// there is no space between y and the closing parenthesis
// x and y are decimal numbers and may be preceded by a sign
// there are no leading zeros
// no other characters are allowed in X or Y

let test = [
  "(-77.11112223331, +130.0100)",
  "(+75, -180)",
  "(+90.0, -147.45)",
  "(+90, +180)",
  "(90, 180)",
  "(-90.00000, -180.0000)",
  "(75, 280)",
  "(+190.0, -147.45)",
  "(+90, +180.2)",
  "(90., 180.)",
  "(-090.00000, -180.0000)"
];

function isValid(coordinates) {
  // o(1) time
  const pCheck = coordinate => {
    // the string starts with a (, has a comma after X and ends with a )
    let a = coordinate[0] === "(" && coordinate[coordinate.length - 1] === ")";

    // there is no space between y and the closing parenthesis
    let temp = coordinate.split(")")[0];
    let b = temp[temp.length - 1] !== " ";

    return a && b;
  };

  // o(1) time
  const spaceCheck = coordinate => {
    // there is no space between the opening parenthesis and the first character of X
    return coordinate[1] !== " ";
  };

  // o(n) time from split built-in
  const xFormatCheck = coordinate => {
    let temp = coordinate.split(",");
    let xFormat = temp[0];

    // there is no space between the comma and the last character of x
    return xFormat[xFormat.length - 1] != " ";
  };

  // o(n) for split built-in
  const yFormatCheck = coordinate => {
    let temp = coordinate.split(",");
    let yFormat = temp[temp.length - 1];
    // there is one space between the comma and the first character of y
    return yFormat[0] === " ";
  };

  // returns true if there are no signs in the string
  // otherwise returns the indices of the signs from the target string
  const signParse = coordinate => {
    let signIndices = [];
    // create a set from the coordinate string for better lookup time o(1)
    const coordinateSet = new Set(coordinate);
    const acceptableSigns = ["+", "-"];

    // if the coordinate includes these signs, we find the indices
    // worst-case time: o(n), best-case time: o(1)
    // o(n) from includes() then iterating to find the indices
    // o(1) from includes() then returning true if signs aren't there
    if (coordinateSet.has(acceptableSigns[0] || acceptableSigns[1])) {
      // iterate over coordinate string to grab the indices of signs
      for (let i = 0; i < coordinate.length; i++) {
        if (
          coordinate[i] === acceptableSigns[0] ||
          coordinate[i] === acceptableSigns[1]
        ) {
          signIndices.push(i);
        }
      }
      return signIndices;
    } else {
      // if the signs aren't there, we can return true
      return true;
    }
  };

  // returns an array formatted like so:
  // [X, Y] -> [75.4283, 134.1234]
  const numParse = coordinate => {
    // characters we don't want to include in the full string output
    // that we will use to test ane make sure that there are no
    // alphanumerics or other characters in the coordinate
    const filteredChars = new Set(["+", "-", " ", ",", "(", ")"]);
    const acceptableNumbers = new Set([
      "0",
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "."
    ]);

    // gets the indices of the + or - symbols: eg [1, 8]
    const signIndices = signParse(coordinate) // o(n)

    // since signIndices returns true in the absense of the symbols,
    // run some tests if the return value is not true
    if (signIndices !== true) { // o(a)
      let check = new Set()
      for(let i=0; i< signIndices.length; i++) {
        // if the element following the sign index is not
        // in the list of acceptable characters, we can return false
        if (!acceptableNumbers.has(coordinate[signIndices[i]+1])) {
          check.add(false)
        } else {
          check.add(true)
        }
      }
      // break the function and return false if false is in the check set
      if (check.has(false)) {
        return false
      }
    }

    // final output arrays
    const numOutput = [];
    const allCharOutput = [];

    // values that will be reassigned
    let numberBucket = [];
    let allCharBucket = [];

    // o(n) time where n is the length of the coordinate string
    for (let i = 0; i < coordinate.length; i++) {
      // if the coordinate at position i does not exist
      // in the filtered char set, add it to the string bucket
      if (!filteredChars.has(coordinate[i])) {
        allCharBucket.push(coordinate[i]);
      }
      if (acceptableNumbers.has(coordinate[i])) {
        numberBucket.push(coordinate[i]);
      // if we hit a comma or an ending parenthesis...
      } else if (coordinate[i] === "," || coordinate[i] === ")") {
        // join all numbers together, add to numOutput array
        // then clear temp so we can have a numOutput array
        // in the following format: [90.284912, 230.37472]

        // make a copy of the array for joining to
        // avoid directly mutating the temp array
        let joined = [...numberBucket].join("");
        let joinedAllChars = [...allCharBucket].join("");
        numOutput.push(joined);
        allCharOutput.push(joinedAllChars);

        // clear temp buckets for next pass
        numberBucket = [];
        allCharBucket = [];
      }
    }

    // test to make sure that no extra characters are in the
    // coordinate string by measuring the length of the number
    // string against the length of the total char string
    // returns false if numoutput length is less than total char output
    if (
      numOutput[0].length < allCharOutput[0].length ||
      numOutput[1].length < allCharOutput[1].length
    ) {
      
      return false;
    // otherwise, return the number array for further testing
    } else {
      return numOutput;
    }
  };

  const testNums = numArray => {
    let truthContainer = new Set();

    // checks to see if first element in input string is a 0
    // if it is, add false to the container
    const handlePrecedingZero = inputString => {
      inputString[0] === '0'
        ? truthContainer.add(false)
        : truthContainer.add(true);
    };

    const handleTrailingDecimal = (inputString) => {
      // if last element in the input string is 
      // a decimal, add false to the truth container
      inputString[inputString.length - 1] === '.'
        ? truthContainer.add(false)
        : truthContainer.add(true);
    }

    // break function and return false if 
    // the first or second condition fails
    if (truthContainer.has(false)){
      return false
    }

    const handleMagnitude = (inputString, index) => {
      const magCheck = parseFloat(inputString);
      // checking magnitude of X (first array element)
      if (index === 0) {
        0 <= magCheck && magCheck <= 90
          ? truthContainer.add(true)
          : truthContainer.add(false);
        // checking magnitude of Y (2nd array element)
      } else if (index === 1) {
        0 <= magCheck && magCheck <= 180
          ? truthContainer.add(true)
          : truthContainer.add(false);
      }
    };

    numArray.forEach((numString, idx) => {
      handlePrecedingZero(numString);
      handleTrailingDecimal(numString)
      handleMagnitude(numString, idx);
    });

    // return false if false exists in the truth container
    return !truthContainer.has(false);
  };

  const output = [];
  let temp = new Set();

  for (let i = 0; i < coordinates.length; i++) {
    // if these tests pass, we can assume the
    // coordinates are formatted like so: (X, Y)
    // with proper spacing between the parentheses
    // and commas with respect to X and Y coords
    temp.add(pCheck(coordinates[i])); // o(1)
    temp.add(spaceCheck(coordinates[i])); // o(1)
    temp.add(xFormatCheck(coordinates[i])); // o(n)
    temp.add(yFormatCheck(coordinates[i])); // o(n)

    // returns false if the num parser discovers a condition
    // that would make the coordinate invalid
    // o(n) + o(a) + o(n)
    // where n is the length of the coordinate string
    // a is the length of the operator indices
    // reduces to o(2n) + o(a) -> o(n) + o(a)
    let numArray = numParse(coordinates[i]); 

    // if the numArray is not false, run the 2nd round of tests
    // otherwise push false to the temp array
    // o(b) where b is the number of elements in the number array (2)
    numArray !== false ? temp.add(testNums(numArray)) : temp.add(false)
    
    // switch based on false values being found in the temp array
    // evaluates in o(1) time since we're querying a set
    switch (temp.has(false)) {
      // if false values are found in temp, send 'Invalid' to output array
      case true:
        output.push("Invalid");
        break;
      // if there are no false values in temp, send 'Valid' to output array
      case false:
        output.push("Valid");
        break;
    }

    temp = new Set();
  }

  // final time complexity: o(y) * (o(3n) + o(a) + o(b))
  // y is the length of the coordinate array
  // n is the length of each individual coordinate string
  // a is the length of the operator index array (2)
  // b is the length of the number array (2)
  // this reduces to: o(y) * (o(n) + o(2a)) -> o(y) * (o(n) + o(a))
  // since a is a constant number, this gives us a final
  // worst case time complexity of o(y)*o(n)
  output.forEach((validity) => {
    console.log(validity)
  })
}

isValid(test);

