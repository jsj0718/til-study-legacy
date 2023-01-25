package javastandard.thread;

public class ThreadEx21 {
    public static void main(String[] args) {
        Runnable r = new RunnableEx21();
        new Thread(r).start();
        new Thread(r).start();
    }
}

class RunnableEx21 implements Runnable {
    Account account = new Account();
    @Override
    public void run() {
        while (account.getBalance() > 0) {
            int money = (int) (Math.random() * 3 + 1) * 100;
            account.withdraw(money);
            System.out.println("balance : " + account.getBalance());
        }
    }
}

class Account {
    private int balance = 1000;

    public int getBalance() {
        return balance;
    }

    //method 또는 synchronized 블럭을 사용하면 동기화 가능

    public void withdraw(int money) {
        synchronized (this) {
            if (balance >= money) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                balance -= money;
            }
        }
    }
}