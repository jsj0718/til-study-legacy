package javastandard.thread;

import java.util.ArrayList;

public class ThreadWaitEx1 {

    public static void main(String[] args) throws InterruptedException {
        Table table = new Table();

        new Thread(new Cook(table), "COOK1").start();
        new Thread(new Customer(table, "donut"), "CUST1").start();
        new Thread(new Customer(table, "burger"), "CUST2").start();

        Thread.sleep(2000);
        System.exit(0);
    }
}

class Customer implements Runnable {
    private Table table;
    private String food;

    public Customer(Table table, String food) {
        this.table = table;
        this.food = food;
    }

    @Override
    public void run() {
        while (true) {
            try {Thread.sleep(100);} catch (InterruptedException e) {}
            String name = Thread.currentThread().getName();

            table.remove(food);
            System.out.println(name + " ate a " + food);
/*
            if (eatFood()) {
                System.out.println(name + " ate a " + food);
            } else {
                System.out.println(name + " failed to eat. :(");
            }
*/
        }
    }

/*
    boolean eatFood() {
        return table.remove(food);
    }
*/
}

class Cook implements Runnable {
    private Table table;

    public Cook(Table table) {
        this.table = table;
    }

    @Override
    public void run() {
        while(true) {
            int idx = (int) (Math.random() * table.dishNum());
            table.add(table.dishesNames[idx]);
            try {Thread.sleep(10);} catch (InterruptedException e) {}
        }
    }
}

class Table {
    String[] dishesNames = {"donut", "donut", "burger"};
    final int MAX_FOOD = 6;
    private ArrayList<String> dishes = new ArrayList<>();

    public void remove(String dishName) {
        synchronized (this) {
            String name = Thread.currentThread().getName();

            while(dishes.size() == 0) {
                System.out.println(name + " is waiting");
                try {
                    wait();
                    Thread.sleep(500);
                } catch (InterruptedException e) {}
            }

            while (true) {
                for (int i=0; i<dishes.size(); i++) {
                    if (dishName.equals(dishes.get(i))) {
                        dishes.remove(i);
                        notify();
                        return;
                    }
                }

                try {
                    System.out.println(name + " is waiting");
                    wait();
                    Thread.sleep(500);
                } catch (InterruptedException e) {}
            }
        }
    }

    public synchronized void add(String dish) {
/*
        if (dishes.size() >= MAX_FOOD) {
            return;
        }

        dishes.add(dish);
        System.out.println("Dishes : " + dishes.toString());
*/
        while (dishes.size() >= MAX_FOOD) {
            String name = Thread.currentThread().getName();
            System.out.println(name + " is waiting");

            try {
                wait();
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            dishes.add(dish);
            notify();
            System.out.println("Dishes: " + dishes.toString());
        }
    }

    public int dishNum() {
        return dishesNames.length;
    }
}