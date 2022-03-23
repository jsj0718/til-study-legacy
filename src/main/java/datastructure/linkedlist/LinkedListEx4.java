package datastructure.linkedlist;

/**
 * 문제 1.
 * 어떤 숫자를 자리수 별로 한 개씩 LinkedList에 담았다.
 * 그런데 1의 자리가 헤더에 오도록 거꾸로 담았다.
 * 이런 식으로 LinkedList 두 개를 받아서 합산하고 같은 식으로 LinkedList에 담아서 반환하라.
 * 
 * 문제 2.
 * 거꾸로가 아닌 길이가 다른 두 숫자의 합 구하기 (길이 계산 후 0으로 채워야 한다.)
 */
public class LinkedListEx4 {
    public static void main(String[] args) {
        LinkedList l1 = new LinkedList();
        l1.append(9);
        l1.append(9);
        l1.append(9);
        l1.retreive();

        LinkedList l2 = new LinkedList();
        l2.append(8);
        l2.append(8);
        l2.retreive();

/*
        LinkedList.Node nodeV1 = LinkedList.sumListsV1(l1.get(1), l2.get(1), 0);
        while (nodeV1.next != null) {
            System.out.print(nodeV1.data + " -> ");
            nodeV1 = nodeV1.next;
        }
        System.out.println(nodeV1.data);
*/

        LinkedList.Node nodeV2 = LinkedList.sumListsV2(l1.get(1), l2.get(1));
        while (nodeV2.next != null) {
            System.out.print(nodeV2.data + " -> ");
            nodeV2 = nodeV2.next;
        }
        System.out.println(nodeV2.data);

    }

    static class LinkedList {
        Node header;

        static class Node {
            int data;
            Node next = null;

            public Node() {

            }

            public Node(int data) {
                this.data = data;
            }
        }

        LinkedList() {
            header = new Node();
        }

        void append(int data) {
            Node end = new Node();
            end.data = data;
            Node node = header;
            while (node.next != null) {
                node = node.next;
            }
            node.next = end;
        }

        void delete(int data) {
            Node node = header;

            while (node.next != null) {
                if (node.next.data == data) {
                    node.next = node.next.next;
                } else {
                    node = node.next;
                }
            }
        }

        void retreive() {
            Node node = header.next;
            while (node.next != null) {
                System.out.print(node.data + " -> ");
                node = node.next;
            }
            System.out.println(node.data);
        }

        Node get(int index) {
            Node node = header;

            for(int i=0; i<index; i++) {
                if (node == null) {
                    return null;
                }
                node = node.next;
            }

            return node;
        }

        boolean deleteNode(Node node) {
            if (node == null || node.next == null) {
                return false;
            }
            node.data = node.next.data;
            node.next = node.next.next;
            return true;
        }

        static Node sumListsV1(Node n1, Node n2, int carry) {
            if (n1 == null && n2 == null && carry == 0) {
                return null;
            }

            Node result = new Node();
            int value = carry;

            if (n1 != null) {
                value += n1.data;
            }
            if (n2 != null) {
                value += n2.data;
            }

            result.data = value % 10;

            if (n1 != null || n2 != null) {
                Node next = sumListsV1((n1 == null) ? null : n1.next,
                        (n2 == null) ? null : n2.next,
                        (value > 10) ? 1 : 0);

                result.next = next;
            }

            return result;
        }

        static Node sumListsV2(Node n1, Node n2) {
            int len1 = getListLength(n1);
            int len2 = getListLength(n2);

            if (len1 > len2) {
                n2 = LPadList(n2, len1 - len2);
            } else if (len1 < len2) {
                n1 = LPadList(n1, len2 - len1);
            }

            Storage storage = addLists(n1, n2);
            if (storage.carry != 0) {
                storage.result = insertBefore(storage.result, storage.carry);
            }
            return storage.result;
        }

        private static Storage addLists(Node n1, Node n2) {
            if (n1 == null && n2 == null) {
                return new Storage();
            }

            Storage storage = addLists(n1.next, n2.next);
            int value = storage.carry + n1.data + n2.data;
            int data = value % 10;
            storage.result = insertBefore(storage.result, data);
            storage.carry = value / 10;

            return storage;
        }

        static int getListLength(Node node) {
            int total = 1;
            while (node.next != null) {
                total++;
                node = node.next;
            }

            return total;
        }

        static Node insertBefore(Node node, int data) {
            Node before = new Node(data);
            if (node != null) {
                before.next = node;
            }
            return before;
        }

        static Node LPadList(Node node, int length) {
            Node head = node;
            for (int i=0; i<length; i++) {
                head = insertBefore(head, 0);
            }
            return head;
        }

        static class Storage {
            int carry = 0;
            Node result = null;
        }
    }
}
