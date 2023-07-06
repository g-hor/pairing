// 61. Rotate List

// Given the head of a linked list, rotate the list to the right by k places.


var rotateRight = function(head, k) {
  if (!head) return null;
  if (k === 0) return head;

  let curr = head;
  let length = 0;

  while (curr) {
      length++;
      curr = curr.next;
  }

  if ((k % length) === 0) return head;

  let position = 1;
  let newTailPosition = length - (k % length);
  let newHead;
  let newTailNode;
  let rotationNode;
  curr = head;

  while (curr) {
      if (position === newTailPosition + 1) {
          newHead = curr;
      }

      if (position === newTailPosition) {
          newTailNode = curr;
      }

      if (position === length) {
          rotationNode = curr;
      }

      position++;
      curr = curr.next;
  }

  newTailNode.next = null;
  rotationNode.next = head;

  return newHead;
};