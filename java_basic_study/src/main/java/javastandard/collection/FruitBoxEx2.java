package javastandard.collection;

import java.util.ArrayList;

class FruitBoxEx2 {
    public static void main(String[] args) {
        Box<Fruit> fruitBox = new Box<>();
        Box<Apple> appleBox = new Box<>();
        Box<Grape> grapeBox = new Box<>();
//        Box<Toy> toyBox = new Box<>();

        fruitBox.add(new Fruit());
        fruitBox.add(new Apple());
        fruitBox.add(new Grape());
        appleBox.add(new Apple());
        appleBox.add(new Apple());
        grapeBox.add(new Grape());

//        toyBox.add(new Toy());

        System.out.println(fruitBox);
        System.out.println(appleBox);
        System.out.println(grapeBox);
//        System.out.println(toyBox);
    }
}

class Box<T extends Fruit & Eatable> {
    ArrayList<T> list = new ArrayList<>();
    void add(T item) {
        list.add(item);
    }
    T get(int i) {
        return list.get(i);
    }
    int size() {
        return list.size();
    }

    @Override
    public String toString() {
        return list.toString();
    }
}

class Fruit implements Eatable {
    @Override
    public String toString() {
        return "Fruit";
    }

}

class Apple extends Fruit {
    @Override
    public String toString() {
        return "Apple";
    }
}

class Grape extends Fruit {
    @Override
    public String toString() {
        return "Grape";
    }
}

class Toy {
    @Override
    public String toString() {
        return "Toy";
    }
}

interface Eatable {}