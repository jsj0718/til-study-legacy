package javastandard.lambda;

import java.util.function.Function;
import java.util.function.Predicate;

public class LambdaEx7 {
    public static void main(String[] args) {
        Function<String, Integer> f = (s) -> Integer.parseInt(s, 16);
        Function<Integer, String> g = (i) -> Integer.toBinaryString(i);

        Function<String, String> h = f.andThen(g);
        Function<Integer, Integer> h2 = f.compose(g);

        System.out.println(h.apply("FF")); //"FF" -> 255 -> "11111111"
        System.out.println(h2.apply(2)); //2 -> "10" -> 16

        Predicate<Integer> p = (i) -> i < 100;
        Predicate<Integer> q = (i) -> i < 200;
        Predicate<Integer> r = (i) -> i%2 == 0;
        Predicate<Integer> notP = p.negate();

        Predicate<Integer> all = notP.and(q.or(r));
        System.out.println(all.test(150));

        String str1 = "abc";
        String str2 = "abc";

        System.out.println(Predicate.isEqual(str1).test(str2));
    }
}
