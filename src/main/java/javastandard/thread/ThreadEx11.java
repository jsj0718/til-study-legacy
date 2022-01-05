package javastandard.thread;

import java.util.Iterator;
import java.util.Map;

public class ThreadEx11 {
    public static void main(String[] args) {
        ThreadEx11_1 t1 = new ThreadEx11_1("Thread1");
        ThreadEx11_2 t2 = new ThreadEx11_2("Thread2");

        t1.start();
        t2.start();
    }
}

class ThreadEx11_1 extends Thread {
    public ThreadEx11_1(String name) {
        super(name);
    }

    @Override
    public void run() {
        try {
            sleep(1000);
        } catch (InterruptedException e) {}
    }
}

class ThreadEx11_2 extends Thread {
    public ThreadEx11_2(String name) {
        super(name);
    }

    @Override
    public void run() {
        Map map = getAllStackTraces();
        Iterator iterator = map.keySet().iterator();

        int x = 0;
        while(iterator.hasNext()) {
            Object obj = iterator.next();
            Thread t = (Thread) obj;
            StackTraceElement[] stackTraceElements = (StackTraceElement[]) map.get(obj);

            System.out.println("[" + ++x + "]" + "name : " + t.getName()
                    + ", group : " + t.getThreadGroup().getName()
                    + ", daemon : " + t.isDaemon());

            for (int i=0; i<stackTraceElements.length; i++) {
                System.out.println(stackTraceElements[i]);
            }

            System.out.println();
        }
    }
}
