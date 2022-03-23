package javastandard.lambda;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

public class LambdaEx5 {
    public static void main(String[] args) {
        Supplier<Integer> s = () -> (int) (Math.random() * 100) + 1;
        Consumer<Integer> c = i -> System.out.print(i + ", ");
        Predicate<Integer> p = i -> i%2==0;
        Function<Integer, Integer> f = i -> i/10*10;

        List<Integer> list = new ArrayList<>();
        makeRandomList(s, list);
        System.out.println(list);
        printEvenNumber(p, c, list);
        System.out.println();
        List<Integer> newList = doSomething(f, list);
        System.out.println(newList);
    }

    static <T> List<T> doSomething(Function<T, T> f, List<T> list) {
        List<T> newList = new ArrayList<>();

        for (int i=0; i<list.size(); i++) {
            newList.add(f.apply(list.get(i)));
        }

        return newList;
    }

    static <T> void printEvenNumber(Predicate<T> p, Consumer<T> c, List<T> list) {
        for (int i=0; i<list.size(); i++) {
            if (p.test(list.get(i))) {
                c.accept(list.get(i));
            }
        }
    }

    static <T> void makeRandomList(Supplier<T> s, List<T> list) {
        for (int i=0; i<10; i++) {
            list.add(s.get());
        }
    }
}
