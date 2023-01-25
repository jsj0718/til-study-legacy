package javastandard.annotation;

import java.util.Arrays;

public class AnnotationEx3 {
    public static void main(String[] args) {
        @SuppressWarnings("unchecked")
        MyArrayList<String> list = MyArrayList.asList("1", "2", "3");

        System.out.println(list);
    }
}

class MyArrayList<T> {
    T[] arr;

    @SafeVarargs
    @SuppressWarnings("varargs")
    MyArrayList(T... arr) {
        this.arr = arr;
    }

//    @SafeVarargs
    @SuppressWarnings("unchecked")
    public static <T> MyArrayList<T> asList(T... a) {
        return new MyArrayList<>(a);
    }

    @Override
    public String toString() {
        return Arrays.toString(arr);
    }
}