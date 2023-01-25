package javastandard.stream;

import java.util.Comparator;
import java.util.IntSummaryStatistics;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class StreamEx3 {
    public static void main(String[] args) {
        Student[] stuArr = {
                new Student("이자바", 3, 300),
                new Student("김자바", 1, 200),
                new Student("안자바", 2, 100),
                new Student("박자바", 2, 150),
                new Student("소자바", 1, 200),
                new Student("나자바", 3, 290),
                new Student("감자바", 3, 180)
        };

        Stream<Student> studentStream = Stream.of(stuArr);

        studentStream.sorted(Comparator.comparing(Student::getBan)
                .thenComparing(Comparator.naturalOrder()))
                .forEach(System.out::println);

        studentStream = Stream.of(stuArr);
        IntStream studentScoreStream = studentStream.mapToInt(Student::getTotalScore);

        IntSummaryStatistics stat = studentScoreStream.summaryStatistics();
        System.out.println("stat.getCount() = " + stat.getCount());
        System.out.println("stat.getSum() = " + stat.getSum());
        System.out.println("stat.getAverage() = " + stat.getAverage());
        System.out.println("stat.getMax() = " + stat.getMax());
        System.out.println("stat.getMin() = " + stat.getMin());
    }
}