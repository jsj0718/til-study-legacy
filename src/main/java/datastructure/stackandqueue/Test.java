package datastructure.stackandqueue;

public class Test {
    public static void main(String[] args) {
        //스택 구현
        StackV1<Integer> s = new StackV1<>();

        s.push(1);
        s.push(2);
        s.push(3);
        s.push(4);

        System.out.println(s.pop());
        System.out.println(s.pop());
        System.out.println(s.peek());
        System.out.println(s.pop());
        System.out.println(s.isEmpty());
        System.out.println(s.pop());
        System.out.println(s.isEmpty());

        //큐 구현
        QueueV1<Integer> q = new QueueV1<>();
        q.add(1);
        q.add(2);
        q.add(3);
        q.add(4);

        System.out.println(q.remove());
        System.out.println(q.remove());
        System.out.println(q.peek());
        System.out.println(q.remove());
        System.out.println(q.isEmpty());
        System.out.println(q.remove());
        System.out.println(q.isEmpty());

        //스택 2개로 큐 구현
        MyQueue<Integer> mq = new MyQueue<>();
        mq.add(1);
        mq.add(2);
        mq.add(3);

        System.out.println(mq.remove());
        System.out.println(mq.remove());
        System.out.println(mq.remove());
        System.out.println();
        
        //스택 정렬
        StackV1<Integer> s1 = new StackV1<>();
        s1.push(2);
        s1.push(5);
        s1.push(3);
        s1.push(7);
        s1.push(9);
        s1.push(1);
        sort(s1);
        while (!s1.isEmpty()) {
            System.out.println(s1.pop());
        }
    }

    private static void sort(StackV1<Integer> s1) {
        StackV1<Integer> s2 = new StackV1<>();
        while(!s1.isEmpty()) {
            int tmp = s1.pop();
            while (!s2.isEmpty() && s2.peek() > tmp) {
                s1.push(s2.pop());
            }
            s2.push(tmp);
        }

        while (!s2.isEmpty()) {
            s1.push(s2.pop());
        }
    }
}
