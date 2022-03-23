package javastandard.thread;

public class ThreadEx12 {
    public static void main(String[] args) {
        ThreadEx12_1 th1 = new ThreadEx12_1();
        ThreadEx12_2 th2 = new ThreadEx12_2();

        th1.start();
        th2.start();

        try {
//            th1.sleep(2000); // sleep()은 항상 현재 실행 중인 메서드에 영향을 끼친다. (참조 변수보다는 Thread를 이용하는 것이 좋다.)
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.print("<main 종료>");
    }
}

class ThreadEx12_1 extends Thread {
    @Override
    public void run() {
        for(int i=0; i<300; i++) {
            System.out.print("-");
        }
        System.out.print("<th1 종료>");
    }
}

class ThreadEx12_2 extends Thread {
    @Override
    public void run() {
        for(int i=0; i<300; i++) {
            System.out.print("|");
        }
        System.out.println("<th2 종료>");
    }
}
