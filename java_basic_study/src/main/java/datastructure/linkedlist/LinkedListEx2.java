package datastructure.linkedlist;

/**
 * 단방향 LinkedList의 끝에서 K번째 노드를 찾는 알고리즘 구현
 *
 * 방법 1. 총 개수 N개인 경우 N - K + 1로 구한다.
 */
public class LinkedListEx2 {

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.append(5);
        list.append(3);
        list.append(2);
        list.append(6);
        list.append(4);
        list.retreive();

        int k = 1;
        System.out.println("뒤에서 " + k + "번째 노드의 값 : " + list.kthToLastV1(list.header, k).data);

        list.kthToLastV2(list.header, k);

        System.out.println(list.kthToLastV3(list.header, k, new LinkedList.Reference()).data);

        System.out.println(list.kthToLastV4(list.header, k).data);
    }

    static class LinkedList {
        Node header;

        static class Node {
            int data;
            Node next = null;
        }

        LinkedList() {
            header = new Node();
        }

        void append(int data) {
            Node end = new Node();
            end.data = data;
            Node node = header;
            while(node.next != null) {
                node = node.next;
            }
            node.next = end;
        }

        void delete(int data) {
            Node node = header;

            while(node.next != null) {
                if (node.next.data == data) {
                    node.next = node.next.next;
                } else {
                    node = node.next;
                }
            }
        }

        void retreive() {
            Node node = header.next;
            while(node.next != null) {
                System.out.print(node.data + " -> ");
                node = node.next;
            }
            System.out.println(node.data);
        }

        void removeDups() {
            Node node = header;

            while(node != null && node.next != null) {
                Node runner = node;
                while (runner.next != null) {
                    if (node.data == runner.next.data) {
                        runner.next = runner.next.next;
                    } else {
                        runner = runner.next;
                    }
                }
                node = node.next;
            }
        }

        Node kthToLastV1(Node first, int k) {
            Node node = first;

            int total = 1;
            while(node.next != null) {
                total++;
                node = node.next;
            }

            node = first;
            for (int i=1; i<total-k+1; i++) {
                node = node.next;
            }
            return node;
        }

        int kthToLastV2(Node node, int k) {
            if (node == null) {
                return 0;
            }

            int count = kthToLastV2(node.next, k) + 1;
            if (count == k) {
                System.out.println("뒤에서 " + k + "번째 노드의 값 : " + node.data);
            }

            return count;
        }

        Node kthToLastV3(Node node, int k, Reference reference) {
            if (node == null) {
                return null;
            }

            Node find = kthToLastV3(node.next, k, reference);
            reference.count++;

            if (k == reference.count) {
                return node;
            }

            return find;
        }

        static class Reference {
            public int count;
        }

        Node kthToLastV4(Node node, int k) {
            Node p1 = node;
            Node p2 = node;

            for (int i=0; i<k; i++) {
                if (p1 == null) {
                    return null;
                }

                p1 = p1.next;
            }

            while(p1 != null) {
                p1 = p1.next;
                p2 = p2.next;
            }

            return p2;
        }
    }

}
