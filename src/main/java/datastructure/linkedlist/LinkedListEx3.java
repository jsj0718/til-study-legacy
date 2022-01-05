package datastructure.linkedlist;

/**
 * 단방향 LinkedList에서 중간에 있는 노드를 삭제 (단, 첫 번째 노드를 알지 못함)
 */
public class LinkedListEx3 {

    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        list.append(1);
        list.append(2);
        list.append(3);
        list.append(4);
        list.append(5);
        list.retreive();

        list.deleteNode(list.get(4));
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
    }
}
