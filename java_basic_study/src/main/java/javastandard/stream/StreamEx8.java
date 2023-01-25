package javastandard.stream;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.util.Comparator.comparingInt;
import static java.util.stream.Collectors.*;

public class StreamEx8 {
    public static void main(String[] args) {
        Student[] stuArr = {
                new Student("나자바", true, 1, 1, 300),
                new Student("김지미", false, 1, 1, 250),
                new Student("김자바", true, 1, 1, 200),
                new Student("이지미", false, 1, 2, 150),
                new Student("남자바", true, 1, 2, 100),
                new Student("안지미", false, 1, 2, 50),
                new Student("황지미", false, 1, 3, 100),
                new Student("강지미", false, 1, 3, 150),
                new Student("이자바", true, 1, 3, 200),

                new Student("나자바", true, 2, 1, 300),
                new Student("김지미", false, 2, 1, 250),
                new Student("김자바", true, 2, 1, 200),
                new Student("이지미", false, 2, 2, 150),
                new Student("남자바", true, 2, 2, 100),
                new Student("안지미", false, 2, 2, 50),
                new Student("황지미", false, 2, 3, 100),
                new Student("강지미", false, 2, 3, 150),
                new Student("이자바", true, 2, 3, 200)
        };

        System.out.printf("1. 단순그룹화 (반별로 그룹화) %n");
        Map<Integer, List<Student>> stuByBan = Stream.of(stuArr).collect(groupingBy(Student::getBan));

        for (List<Student> ban : stuByBan.values()) {
            for (Student student : ban) {
                System.out.println(student);
            }
        }

        System.out.printf("%n2. 단순그룹화 (성적별 그룹화) %n");

        Map<Student.Level, List<Student>> stuByLevel = Stream.of(stuArr).collect(groupingBy(s -> {
            if (s.getTotalScore() >= 200) return Student.Level.HIGH;
            else if (s.getTotalScore() >= 100) return Student.Level.MID;
            else return Student.Level.LOW;
        }));

        TreeSet<Student.Level> keySet = new TreeSet<>(stuByLevel.keySet());

        for (Student.Level key : keySet) {
            System.out.println("[" + key + "]");
            for (Student student : stuByLevel.get(key)) {
                System.out.println("student = " + student);
            }
            System.out.println();
        }

        System.out.printf("%n3. 단순그룹화 + 통계 (성적별 학생수) %n");
        Map<Student.Level, Long> stuCntByLevel = Stream.of(stuArr).collect(groupingBy(s -> {
            if (s.getTotalScore() >= 200) return Student.Level.HIGH;
            else if (s.getTotalScore() >= 100) return Student.Level.MID;
            else return Student.Level.LOW;
        }, counting()));

        for (Student.Level key : stuCntByLevel.keySet()) {
            System.out.printf("[%s] - %d명", key, stuCntByLevel.get(key));
            System.out.println();
        }

/*
        for (List<Student> level : stuByLevel.values()) {
            System.out.println();
            for (Student student : level) {
                System.out.println(student);
            }
        }
*/

        System.out.printf("%n4. 다중 그룹화 (학년별, 반별) %n");
        Map<Integer, Map<Integer, List<Student>>> stuByHakAndBan = Stream.of(stuArr)
                .collect(groupingBy(Student::getHak, groupingBy(Student::getBan)));

        for (Map<Integer, List<Student>> hak : stuByHakAndBan.values()) {
            for (List<Student> ban : hak.values()) {
                System.out.println();
                for (Student student : ban) {
                    System.out.println(student);
                }
            }
        }

        System.out.printf("%n5. 다중 그룹화 통계(학년별, 반별 1등) %n");
        Map<Integer, Map<Integer, Student>> topStuByHakAndBan = Stream.of(stuArr).collect(groupingBy(Student::getHak, groupingBy(Student::getBan,
                collectingAndThen(maxBy(comparingInt(Student::getTotalScore))
                        , Optional::get
                )
        )));

        for (Map<Integer, Student> ban : topStuByHakAndBan.values()) {
            for (Student student : ban.values()) {
                System.out.println(student);
            }
        }

        System.out.printf("%n6. 다중그룹화 + 통계 (학년별, 반별 성적그룹) %n");
        Map<String, Set<Student.Level>> stuByScoreGroup = Stream.of(stuArr).collect(groupingBy(s -> s.getHak() + "-" + s.getBan(),
                mapping(s -> {
                    if (s.getTotalScore() >= 200) return Student.Level.HIGH;
                    else if (s.getTotalScore() >= 100) return Student.Level.MID;
                    else return Student.Level.LOW;
                }, toSet())
        ));

        Set<String> keyset2 = stuByScoreGroup.keySet();

        for (String key : keyset2) {
            System.out.println("[" + key + "]" + stuByScoreGroup.get(key));
        }
    }
}
