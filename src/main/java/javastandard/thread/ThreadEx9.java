package javastandard.thread;

public class ThreadEx9 {
    public static void main(String[] args) {
        ThreadGroup main = Thread.currentThread().getThreadGroup();
        ThreadGroup group1 = new ThreadGroup("Group1");
        ThreadGroup group2 = new ThreadGroup("Group2");

        ThreadGroup subGroup1 = new ThreadGroup(group1, "SubGroup1");

        group1.setMaxPriority(3);

        Runnable runnable = new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };

        new Thread(group1, runnable, "t1").start();
        new Thread(subGroup1, runnable, "t2").start();
        new Thread(group2, runnable, "t3").start();

        System.out.println(">>List of ThreadGroup : " + main.getName()
                + ", Active ThreadGroup : " + main.activeGroupCount()
                + ", Active Thread : " + main.activeCount());

        main.list(); //main 쓰레드 그룹 정보 출력
    }
}
