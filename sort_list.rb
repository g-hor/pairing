# 148. Sort List

# Given the head of a linked list, return the list after sorting it in ascending order.

# NAIVE SLOW APPROACH
# bubble sort on linked list:
#   set up a "sorted" boolean value
#   while not sorted, keep looping through linked list:
#       set up current variable for current iterating node
#       set up "next" variable to refer to value of next node
#       switch order of "current" and "next" based on ascending values
#           if a switch occurs, "sorted" boolean remains false

def sort_list(head)
  return nil if !head
  dummy_head = ListNode.new("dummy", head)
  sorted = false

  while !sorted do
      sorted = true
      current_node = dummy_head.next
      next_node = current_node.next
      prev_node = dummy_head

      while current_node && next_node do
          if current_node.val > next_node.val
              current_node.next = next_node.next
              next_node.next = current_node
              prev_node.next = next_node

              sorted = false
          end

          prev_node = current_node
          current_node = current_node.next
          next_node = current_node.next if current_node
      end
  end

  dummy_head.next
end

def sort_list(head)
  dummy_head = ListNode.new("dummy", head)
  curr = dummy_head.next
  nodes = []

  while curr do
      nodes << curr
      curr = curr.next
  end

  nodes.sort! { |node_1, node_2| node_1.val <=> node_2.val }

  nodes.each_with_index do |node, idx|
      node.next = nodes[idx + 1] if nodes[idx + 1]
  end

  nodes[-1].next = nil if nodes[-1]
  nodes[0]
end