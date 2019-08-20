class Node {
  constructor(data, left = null, right = null, count = 1) {
    this.data = data;
    this.left = left;
    this.right = right;
    this.count = count;
    this.smaller = 0;
    this.larger = 0;
  }
}

class AugBST {
  constructor() {
    this.root = null;
    this.counter = 0;
  }

  add(data) {
    const node = this.root;

    if (node === null) {
      this.root = new Node(data);
      return;
    } else {
      const searchTree = node => {
        if (data < node.data) {
          if (node.left === null) {
            node.left = new Node(data);
            return;
          } else if (node.left !== null) {
            return searchTree(node.left);
          }
        } else if (data > node.data) {
          if (node.right === null) {
            node.right = new Node(data);
            return;
          } else if (node.right !== null) {
            return searchTree(node.right);
          }
          // handles duplicate scores
        } else if (data === node.data) {
          node.count += 1;
          return;
        } else {
          return null;
        }
      };
      return searchTree(node);
    }
  }

  findMaxHeight(node = this.root) {
    if (node == null) {
      return -1;
    }
    let left = this.findMaxHeight(node.left);
    let right = this.findMaxHeight(node.right);
    if (left > right) {
      return left + 1;
    } else {
      return right + 1;
    }
  }

  leftSubHeight(node = this.root) {
    return this.findMaxHeight(node.left);
  }

  rightSubHeight(node = this.root) {
    return this.findMaxHeight(node.right);
  }

  balanceFactor() {
    return this.leftSubHeight() - this.rightSubHeight();
  }

  sumNodes(node = this.root, target) {
    while (node) {
      const { left, right } = node;

      if (node.data <= target) {
        this.counter += node.count;
        let a = this.sumNodes(left, target);
        let b = this.sumNodes(right, target);
        return a, b;
      } else if (node.data > target) {
        let a = this.sumNodes(left, target);
        return a;
      }
    }
    return this.counter;
  }

  augmentTree(node = this.root, parent = null, smaller=0, larger=0) {
    while (node) {
      const { left, right } = node;

      if (parent !== null) {
        parent.data >= node.data ? (node.smaller += 1) : node.smaller += 1;
        parent.data <= node.data ? (node.larger += 1) : node.larger += 1

        let a = this.augmentTree(left, node, node.smaller, node.larger);
        let b = this.augmentTree(right, node, node.smaller, node.larger);

        return a, b
      } else {
        let a = this.augmentTree(left, node, node.smaller + 1, node.larger);
        let b = this.augmentTree(right, node, node.smaller, node.larger + 1);

        return a, b
      }
    }
  }

  clearCounter() {
    this.counter = 0;
  }
}

function counts(teamA, teamB) {
  // Create new instance of AugBST class
  const tree = new AugBST();

  // if there are no entries for teamA,
  // all teamB entries are > teamA entries
  // so we can return the length of the teamB array
  if (teamA.length === 0) {
    return teamB.length;
  }

  // if there are no teamB entries, return 0
  if (teamB.length === 0) {
    return 0;
  }

  // Callback to add new values to the AugBST
  const updateBtree = val => {
    tree.add(val);
  };

  // Generates Augmented BST (not necessarily balanced)
  // Creates the tree in o(N) time where
  // N is the length of the teamA array
  teamA.forEach(score => updateBtree(score));

  tree.augmentTree();
  console.log(tree);

  const cache = {};

  // Callback to calculate the number of teamA scores that are < teamB scores
  // querying the augmented BST for nodes with scores < teamB scores should
  // take worst case o(logN) time in a balanced BST
  const calculateSolution = target => {
    // sums the scores that are < target
    let result;
    tree.clearCounter();
    result = cache[target] ? cache[target] : tree.sumNodes(tree.root, target);

    cache[target] = result;

    return result;
  };

  // map over teamB array to generate new array with number
  // of games where teamA performed <= teamB
  // time complexity is O(KlogN) where K is the length of teamB array
  // and logN is the time it takes to sum the nodes in the augmented BST
  const output = teamB.map(score => {
    return calculateSolution(score);
  });

  // final complexity is O(N + klogN)
  return output;
}

const teamA = [9, 8, 7, 6, 5];
const teamB = [5, 3, 7];

console.log(counts(teamA, teamB));
// const testTree = new BaseTree();

// const updateTree = val => {
//   testTree.add(val);
// };

// testing.forEach(val => updateTree(val));

const test = new AugBST();
