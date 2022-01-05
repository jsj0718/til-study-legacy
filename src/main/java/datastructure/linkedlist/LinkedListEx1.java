package datastructure.linkedlist;

/**
 * 정렬되지 않은 LinkedList의 중복값 제거 (단, 버퍼 X)
 */
public class LinkedListEx1 {

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.append(1);
        list.append(2);
        list.append(3);
        list.append(1);
        list.append(5);
        list.append(5);
        list.retreive();

        list.removeDups();
        list.retreive();
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
    }

}
