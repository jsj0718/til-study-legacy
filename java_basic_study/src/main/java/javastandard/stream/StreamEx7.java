package javastandard.stream;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Stream;

import static java.util.Comparator.comparingInt;
import static java.util.stream.Collectors.*;

public class StreamEx7 {
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

        System.out.printf("1. 단순분할 (성별로 분할) %n");
        Map<Boolean, List<Student>> stuBySex = Stream.of(stuArr).collect(partitioningBy(Student::isMale));

        List<Student> maleStudents = stuBySex.get(true);
        List<Student> femaleStudents = stuBySex.get(false);

        for(Student maleStudent : maleStudents) {
            System.out.println("maleStudent = " + maleStudent);
        }

        for(Student femaleStudent : femaleStudents) {
            System.out.println("femaleStudent = " + femaleStudent);
        }

        System.out.printf("%n2. 단순 분할 + 통계 (성별 학생 수) %n");
        Map<Boolean, Long> stuNumBySex = Stream.of(stuArr).collect(partitioningBy(Student::isMale, counting()));

        System.out.println("남학생 수 : " + stuNumBySex.get(true));
        System.out.println("여학생 수 : " + stuNumBySex.get(false));

        System.out.printf("%n3. 단순 분할 + 통계 (성별 1등) %n");
        Map<Boolean, Student> topScoreBySex2 = Stream.of(stuArr).collect(partitioningBy(Student::isMale, collectingAndThen(
                maxBy(comparingInt(Student::getTotalScore)), Optional::get)
        ));

        System.out.println("남학생 1등 : " + topScoreBySex2.get(true));
        System.out.println("여학생 1등 : " + topScoreBySex2.get(false));

        System.out.printf("%n4. 다중 분할(성별 불합격자, 100점 이하) %n");
        Map<Boolean, Map<Boolean, List<Student>>> failedStuBySex = Stream.of(stuArr).collect(partitioningBy(Student::isMale,
                partitioningBy(s -> s.getTotalScore() <= 100))
        );

        List<Student> failedMaleStu = failedStuBySex.get(true).get(true);
        List<Student> failedFemaleStu = failedStuBySex.get(false).get(true);

        for (Student s : failedMaleStu) {
            System.out.println(s);
        }

        for (Student s : failedFemaleStu) {
            System.out.println(s);
        }
    }
}
