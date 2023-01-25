package javastandard.collection;

import java.util.*;

public class TreeMapEx1 {

    public static void main(String[] args) {
        String[] data = {"A", "K", "A", "K", "D", "K", "A", "K", "K", "K", "Z", "D"};

        TreeMap map = new TreeMap();

        for (int i=0; i < data.length; i++) {
            if (!map.containsKey(data[i])) {
                map.put(data[i], 1);
            } else {
                Integer value = (Integer) map.get(data[i]);
                map.put(data[i], value + 1);
            }
        }

        Iterator iterator = map.entrySet().iterator();

        System.out.println("= 기본 정렬 = ");
        while (iterator.hasNext()) {
            Map.Entry entry = (Map.Entry) iterator.next();
            int value = ((Integer) entry.getValue()).intValue();
            System.out.println(entry.getKey() + " : " + printBar('#', value) + " " + value);
        }
        System.out.println();

        Set set = map.entrySet();
        List list = new ArrayList<>(set);

        Collections.sort(list, new ValueComparator());

        iterator = list.iterator();

        System.out.println("값의 크기가 큰 순서대로 정렬");
        while (iterator.hasNext()) {
            Map.Entry entry = (Map.Entry) iterator.next();
            int value = ((Integer) entry.getValue()).intValue();
            System.out.println(entry.getKey() + " : " + printBar('#', value) + " " + value);
        }
    }

    static class ValueComparator implements Comparator {
        @Override
        public int compare(Object o1, Object o2) {
            if (o1 instanceof Map.Entry && o2 instanceof Map.Entry) {
                Map.Entry e1 = (Map.Entry) o1;
                Map.Entry e2 = (Map.Entry) o2;

                int v1 = ((Integer) e1.getValue()).intValue();
                int v2 = ((Integer) e2.getValue()).intValue();

                return v2 - v1;
            }
            return -1;
        }
    }

    private static String printBar(char ch, int value) {
        char[] bar = new char[value];

        for (int i=0; i<value; i++) {
            bar[i] = ch;
        }

        return new String(bar);
    }
}
