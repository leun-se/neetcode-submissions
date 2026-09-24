class Node {
    int val;
    Node next;

    public Node(int val) {
        this(val, null);
    }

    public Node(int val, Node next) {
        this.val = val;
        this.next = next;
    }
}

class LinkedList {
    private Node first;
    private int length;

    public LinkedList() {
        this.first = null;
        this.length = 0;
    }

    // Get value by index
    public int get(int index) {
        if (index < 0 || index >= length) return -1;
        Node curr = first;
        for (int i = 0; i < index; i++) {
            curr = curr.next;
        }
        return curr.val;
    }

    // Insert at head
    public void insertHead(int val) {
        Node newHead = new Node(val, first);
        first = newHead;
        length++;
    }

    // Insert at tail
    public void insertTail(int val) {
        if (first == null) {
            first = new Node(val);
        } else {
            Node curr = first;
            while (curr.next != null) {
                curr = curr.next;
            }
            curr.next = new Node(val);
        }
        length++;
    }

    // Remove at index
    public boolean remove(int index) {
        if (index < 0 || index >= length) return false;
        if (index == 0) {
            first = first.next;
        } else {
            Node curr = first;
            for (int i = 0; i < index - 1; i++) {
                curr = curr.next;
            }
            curr.next = curr.next.next;
        }
        length--;
        return true;
    }

    // Method to get values of the linked list
    public ArrayList<Integer> getValues() {
        ArrayList<Integer> res = new ArrayList<>();
        Node curr = this.first;
        while (curr != null) {
            res.add(curr.val);
            curr = curr.next;
        }
        return res;
    }

    public int size() {
        return length;
    }
}
