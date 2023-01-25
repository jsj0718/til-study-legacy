package javastandard.thread;

public class ThreadEx16 {
    public static void main(String[] args) {
/*
        RunImplEx16 r1 = new RunImplEx16();
        RunImplEx16 r2 = new RunImplEx16();
        RunImplEx16 r3 = new RunImplEx16();

        Thread th1 = new Thread(r1, "*");
        Thread th2 = new Thread(r2, "**");
        Thread th3 = new Thread(r3, "***");

        th1.start();
        th2.start();
        th3.start();

        try {
            Thread.sleep(2000);
            r1.suspend();
            Thread.sleep(2000);
            r2.suspend();
            Thread.sleep(3000);
            r1.resume();
            Thread.sleep(3000);
            r1.stop();
            r2.stop();
            Thread.sleep(2000);
            r3.stop();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        ThreadEx16_1 th4 = new ThreadEx16_1("****");
        ThreadEx16_1 th5 = new ThreadEx16_1("*****");
        ThreadEx16_1 th6 = new ThreadEx16_1("******");
        th4.start();
        th5.start();
        th6.start();

        try {
            Thread.sleep(2000);
            th4.suspend();
            Thread.sleep(2000);
            th5.suspend();
            Thread.sleep(3000);
            th4.resume();
            Thread.sleep(3000);
            th4.stop();
            th5.stop();
            Thread.sleep(2000);
            th6.stop();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
*/

        ThreadEx16_2 th1 = new ThreadEx16_2("*");
        ThreadEx16_2 th2 = new ThreadEx16_2("**");
        ThreadEx16_2 th3 = new ThreadEx16_2("***");
        th1.start();
        th2.start();
        th3.start();

        try {
            Thread.sleep(2000);
            th1.suspend();
            Thread.sleep(2000);
            th2.suspend();
            Thread.sleep(3000);
            th1.resume();
            Thread.sleep(3000);
            th1.stop();
            th2.stop();
            Thread.sleep(2000);
            th3.stop();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }
}

class RunImplEx16 implements Runnable {
    volatile boolean suspended = false;
    volatile boolean stopped = false;

    @Override
    public void run() {
        while(!stopped) {
            if(!suspended) {
                System.out.println(Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {}
            }
        }
        System.out.println(Thread.currentThread().getName() + " - stopped");
    }

    public void suspend() {
        suspended = true;
    }

    public void resume() {
        suspended = false;
    }

    public void stop() {
        stopped = true;
    }
}

class ThreadEx16_1 implements Runnable {
    volatile boolean suspended = false;
    volatile boolean stopped = false;

    Thread th;

    public ThreadEx16_1(String name) {
        th = new Thread(this, name);
    }

    @Override
    public void run() {
        while(!stopped) {
            if(!suspended) {
                System.out.println(Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {}
            }
        }
        System.out.println(Thread.currentThread().getName() + " - stopped");
    }

    public void suspend() {
        suspended = true;
    }

    public void resume() {
        suspended = false;
    }

    public void stop() {
        stopped = true;
    }

    public void start() {
        th.start();
    }
}

class ThreadEx16_2 implements Runnable {
    volatile boolean suspended = false;
    volatile boolean stopped = false;

    Thread th;

    public ThreadEx16_2(String name) {
        th = new Thread(this, name);
    }

    @Override
    public void run() {
        while(!stopped) {
            if(!suspended) {
                System.out.println(th.getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {}
            } else {
                Thread.yield();
            }
        }
        System.out.println(th.getName() + " - stopped");
    }

    public void suspend() {
        suspended = true;
        th.interrupted();
        System.out.println(th.getName() + " - interrupt() by suspend()");
    }

    public void resume() {
        suspended = false;
    }

    public void stop() {
        stopped = true;
        th.interrupted();
        System.out.println(th.getName() + " - interrupt() by stop()");
    }

    public void start() {
        th.start();
    }
}