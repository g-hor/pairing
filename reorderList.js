// 143. Reorder List

// You are given the head of a singly linked-list. The list can be represented as:

// L0 → L1 → … → Ln - 1 → Ln
// Reorder the list to be on the following form:

// L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
// You may not modify the values in the list's nodes. Only nodes themselves may be changed.


var reorderList = function(head) {
  let curr = head;
  const nodesStack = [];

  while (curr) {
      nodesStack.push(curr);
      curr = curr.next;
  }

  curr = head;
  let fwdIdx = 1; 
  let backIdx = nodesStack.length - 1; 

  while (fwdIdx < backIdx) {
      curr.next = nodesStack[backIdx]; 
      curr.next.next = nodesStack[fwdIdx];

      curr = curr.next.next;
      curr.next = null;

      backIdx--; 
      fwdIdx++; 
  }
  
  if (fwdIdx === backIdx) {
      curr.next = nodesStack[fwdIdx];
      curr.next.next = null;
  }

  return head;
};