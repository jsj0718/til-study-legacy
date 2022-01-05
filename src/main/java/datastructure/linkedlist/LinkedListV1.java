package datastructure.linkedlist;

public class LinkedListV1 {

    public static void main(String[] args) {
        Node head = new Node(5);
        head.append(3);
        head.append(2);
        head.append(1);
        head.append(6);
        head.append(8);

        head.retreive();

        head.delete(3);
        head.delete(1);
        head.delete(8);

        head.retreive();

    }

    static class Node {
        int data;
        Node next = null;

        Node(int data) {
            this.data = data;
        }

        void append(int data) {
            Node end = new Node(data);
            Node node = this;
            while(node.next != null) {
                node = node.next;
            }
            node.next = end;
        }

        void delete(int data) {
            Node node = this;

            while(node.next != null) {
                if (node.next.data == data) {
                    node.next = node.next.next;
                } else {
                    node = node.next;
                }
            }
        }

        void retreive() {
            Node node = this;

            while(node.next != null) {
                System.out.print(node.data + " -> ");
                node = node.next;
            }
            System.out.println(node.data);
        }
    }
}