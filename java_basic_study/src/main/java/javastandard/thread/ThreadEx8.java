package javastandard.thread;

public class ThreadEx8 {
    public static void main(String[] args) {
        Thread t1 = new Thread(() -> {
            printBar(300, 10000000, "-");
        });

        Thread t2 = new Thread(() -> {
            printBar(300, 10000000, "|");
        });

        t2.setPriority(7);

        System.out.println("Priority of t1(-) : " + t1.getPriority());
        System.out.println("Priority of t2(|) : " + t2.getPriority());

        t1.start();
        t2.start();
    }

    private static void printBar(int count1, int count2, String s) {
        for (int i = 0; i < count1; i++) {
            System.out.print(s);
            for (int x = 0; x < count2; x++) ;
        }
    }
}
