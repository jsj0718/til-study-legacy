package datastructure.linkedlist;

import com.sun.jdi.connect.spi.TransportService;

/**
 * 주어진 두 개의 단방향 LinkedList에서 교차되는 노드를 찾아라. (단, 교차점은 값이 아닌 주소로 찾아야 한다.)
 * <p>
 * 해결 방법
 * 1. 두 개의 리스트의 끝을 맞춰주면 된다.
 * 2. 같은 길이로 앞을 자른다.
 */
public class LinkedListEx5 {

    public static void main(String[] args) {
        LinkedList.Node n1 = new LinkedList.Node(5);
        LinkedList.Node n2 = n1.addNext(7);
        LinkedList.Node n3 = n2.addNext(9);
        LinkedList.Node n4 = n3.addNext(10);
        LinkedList.Node n5 = n4.addNext(7);
        LinkedList.Node n6 = n5.addNext(6);

/*
        LinkedList.Node m1 = new LinkedList.Node(6);
        LinkedList.Node m2 = m1.addNext(8);
        LinkedList.Node m3 = m2.addNext(n4);
*/
        LinkedList.Node m1 = new LinkedList.Node(6);
        LinkedList.Node m2 = m1.addNext(8);
        LinkedList.Node m3 = m2.addNext(3);
        LinkedList.Node m4 = m2.addNext(4);
        LinkedList.Node m5 = m2.addNext(1);
        LinkedList.Node m6 = m2.addNext(2);

        n1.print();
        m1.print();

        LinkedList.Node result = LinkedList.getIntersection(n1, m1);

        if (result != null) {
            System.out.println("Intersection: " + result.data);
        } else {
            System.out.println("Not Found");
        }

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

            Node get(int index) {
                Node node = this;

                for (int i = 0; i < index; i++) {
                    if (node == null) {
                        return null;
                    }
                    node = node.next;
                }

                return node;
            }

            Node addNext(int data) {
                Node end = new Node(data);
                Node node = this;
                while (node.next != null) {
                    node = node.next;
                }
                node.next = end;

                return node.next;
            }

            Node addNext(Node n) {
                Node node = this;
                while (node.next != null) {
                    node = node.next;
                }
                node.next = n;

                return node.next;
            }

            void print() {
                Node node = this;
                while (node.next != null) {
                    System.out.print(node.data + " -> ");
                    node = node.next;
                }
                System.out.println(node.data);
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

            for (int i = 0; i < index; i++) {
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

        static Node getIntersection(Node n1, Node n2) {
            int len1 = getListLength(n1);
            int len2 = getListLength(n2);

            if (len1 > len2) {
                n1 = n1.get(len1 - len2);
            } else if (len1 < len2) {
                n2 = n2.get(len2 - len1);
            }

            while (n1 != null && n2 != null) {
                if (n1 == n2) {
                    return n1;
                }
                n1 = n1.next;
                n2 = n2.next;
            }

            return null;
        }


        static int getListLength(Node node) {
            int total = 1;
            while (node.next != null) {
                total++;
                node = node.next;
            }
            return total;
        }
    }
}
