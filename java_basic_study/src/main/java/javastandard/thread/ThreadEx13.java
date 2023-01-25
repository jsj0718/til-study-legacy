package javastandard.thread;

import javax.swing.*;

public class ThreadEx13 {
    public static void main(String[] args) {
        ThreadEx13_1 t1 = new ThreadEx13_1();
        t1.start();

        String input = JOptionPane.showInputDialog("아무 값이나 입력하세요.");
        System.out.println("입력 값 : " + input);
        t1.interrupt();
        System.out.println("isInterrupted() : " + t1.isInterrupted());
    }
}

class ThreadEx13_1 extends Thread {
    @Override
    public void run() {
        int i = 10;

        while (i != 0 && !isInterrupted()) {
            System.out.println(i--);
//            for (long x=0; x<2500000000L; x++);
            try {
                sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("카운트 종료");
    }
}
