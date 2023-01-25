package datastructure.linkedlist;

/**
 * LinkedList 안에 루프가 있는지 확인하고 루프가 시작되는 노드를 찾아라.
 * 
 * 해결 방법
 * 1. 토끼(2)와 거북이(1) 투 포인터를 구현하여 만나는 지점을 계산
 * 2. 만닌 지점에서 거북이는 처음으로 돌린 후 토끼와 거북이를 1만큼 다시 반복
 * 3. 다시 만난 지점이 루프의 시작점이다.
 */
public class LinkedListEx6 {
    public static void main(String[] args) {
        Node n1 = new Node(1);
        Node n2 = n1.addNext(2);
        Node n3 = n2.addNext(3);
        Node n4 = n3.addNext(4);
        Node n5 = n4.addNext(5);
        Node n6 = n5.addNext(6);
        Node n7 = n6.addNext(7);
        Node n8 = n7.addNext(8);
        n8.addNext(n4);

        Node node = findLoop(n1);

        if (node != null) {
            System.out.println("Start of loop : " + node.data);
        } else {
            System.out.println("Loop Not Found");
        }
    }

    static Node findLoop (Node head) {
        Node fast = head;
        Node slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;

            if (fast == slow) {
                break;
            }
        }

        if (fast == null || fast.next == null) {
            return null;
        }

        slow = head;
        while (fast != slow) {
            fast = fast.next;
            slow = slow.next;
        }

        return fast;
    }

    static class Node {
        int data;
        Node next = null;

        public Node(int data) {
            this.data = data;
        }

        Node addNext(int data) {
            Node head = this;
            Node end = new Node(data);
            while(head.next != null) {
                head = head.next;
            }
            head.next = end;
            return end;
        }

        void addNext(Node node) {
            Node head = this;
            head.next = node;
        }


        Node get(int index) {
            Node n = this;
            for (int i=0; i<index; i++) {
                n = n.next;
            }
            return n;
        }
    }
}
