// 21. Merge Two Sorted Lists

// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.

var mergeTwoLists = function(list1, list2) {
  let curr1 = list1;
  let curr2 = list2;
  let dummyNode = new ListNode(null);
  let tail = dummyNode;

  while (curr1 && curr2) {
      if (curr2.val <= curr1.val) {
          tail.next = curr2;
          curr2 = curr2.next;
      } else {
          tail.next = curr1;
          curr1 = curr1.next;
      }

      tail = tail.next;
  }

  if (curr1) tail.next = curr1;
  if (curr2) tail.next = curr2;

  return dummyNode.next;
};