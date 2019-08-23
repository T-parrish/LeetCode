// A palindrome is a sequence of characters which reads the same backwards and forwards
// a subsequence is a group of characters chosen from a list while maintaining their order. For instance, the subsequences of abc are [a, b, c, ab, ac, bc, abc]
// the score of string s is the maximum product between two non-overlapping palindromic subsequences of s that we'll refer to as b
// score(s) = max(length(a) * length(b))
// there may be multiple ways to choose a and b, but there can't be any overlap between the two subsequences.
// concretely: 
// attract -> [a, t, r, c, t, aa, tt, ata, ara, ttt, tat, tct, atta]
// the maximum score is atta (4) and c or r (1) = 4

let test = 'acdapmpomp'

function getScore(s) {
  const isPalindrome = (inputStr) => {
    // returns true if the array is same backwards and forwards
    // spread a copy of the string into an array, 
    // reverse, and join it back together 
    return inputStr == [...inputStr].reverse().join('') // o(n)
  }

  const palindromeSet = new Set()
  const palindromes = []

  // keeps a set of all unique substrings to match against and improve efficiency
  // since each individual letter is likely to be a palindrome, we can 
  // add the individual letters to the palindrome array if they don't exist in the set
  const updateBuckets = (str) => {
    if(palindromeSet.has(str)) {
      return
    } else if (isPalindrome(str)) {
      palindromeSet.add(str)
      palindromes.push(str)
    }
  }

  const pruneSet = new Set()

  const updatePruneCache = (val) => {
    pruneSet.add(val)
  }

  // o(n!) time
  const parsePalindromes = (prefix, target, updater, cache, cacheHandler) => {
    for (let i = 0; i < target.length; i++) {
      let outputString = prefix + target[i]
      
      // run the subsequence through the updater
      // updater checks against palindrome set and only 
      // sends unique palindromes to the palindrome array
      // this will make downstream events more efficient
      updater(outputString)

      // recurse over the string to generate all possible 
      // permutations and update the palindrome set / array 
      if (!cache.has(outputString)) {
        cacheHandler(outputString)
        parsePalindromes(prefix + target[i], target.slice(i + 1), updater, cache, cacheHandler);
      }
    }
  }

  try {
    // start recursion with empty string
    parsePalindromes('', s, updateBuckets, pruneSet, updatePruneCache)
  } catch (e) {
    console.log('something went wrong: ', e)
  }

  // Helper function to calculate the intersection between two strings.  
  const intersectionHelper = (palOne, palTwo, cache) => {
    const tempA = new Set(palOne)
    const tempB = new Set(palTwo)

    const filteredA = [...tempA].filter((char) => { 
      return tempB.has(char)
    })

    let noIntersection = [...filteredA].length === 0

    // cache intersecting pairs to improve performance
    !noIntersection && cache.add([palOne, palTwo])
    return noIntersection
  }

  // find two largest palindromes with no overlap
  // o(nlogn + n^2)
  const getLargest = (palindromeArray, helper) => {
    const intersectionSet = new Set()
    // sort the array => o(nlogn)
    let sortedPalindromes = palindromeArray.sort((a, b) => {
      return a.length > b.length ? -1 : a.length < b.length ? 1 : 0
    })

    let container = []

    // Worst case time complexity: o(n^2) for two passes over the data
    // Best case we can return a much earlier value since we sorted the data
    // this means that the earlier match will likely be the max
    for(let i=0; i<sortedPalindromes.length; i++) {
      // returns first match since it will be the 
      // highest score after sorting the array
      if (container.length > 0) {
        return container
      } 

      for(let j=1+i; j<sortedPalindromes.length; j++){
        // helper returns true if there is no overlap between the two
        // palindrome strings. if true, we want to add the product
        // to our holding container.

        if(intersectionSet.has([palindromeArray[i], sortedPalindromes[j]])) {
          continue
        } else if(helper(palindromeArray[i], sortedPalindromes[j], intersectionSet) === true) {
          // aggregates the scores of max intersecting pair at each step
          container.push(palindromeArray[i].length * sortedPalindromes[j].length)
          break
        } 
      }
    }

    return container
  } 

  let output = getLargest(palindromes, intersectionHelper)
  console.log(output[0])
  return output[0]

}

getScore(test)