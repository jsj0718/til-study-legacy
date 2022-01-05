package javastandard.annotation;

import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Deprecated
@SuppressWarnings("1111")
@TestInfo(testedBy="aaa", testDate=@DateTime(yymmdd="220104", hhmmss="164330"))
public class AnnotationEx5 {
    public static void main(String[] args) {
        Class<AnnotationEx5> cls = AnnotationEx5.class;

        TestInfo annotation = (TestInfo) cls.getAnnotation(TestInfo.class);
        System.out.println("annotation.testedBy() : " + annotation.testedBy());
        System.out.println("annotation.testDate().yymmdd() : " + annotation.testDate().yymmdd());
        System.out.println("annotation.testedBy().hhmmss() : " + annotation.testDate().hhmmss());

        for (String str : annotation.testTools()) {
            System.out.println("TestTools : " + str);
        }

        System.out.println();

        for (Annotation a : cls.getAnnotations()) {
            System.out.println(a);
        }
    }
}

@Retention(RetentionPolicy.RUNTIME)
@interface TestInfo {
    int count() default 1;
    String testedBy();
    String[] testTools() default "JUnit";
    TestType testType() default TestType.FIRST;
    DateTime testDate();
}

@Retention(RetentionPolicy.RUNTIME)
@interface DateTime {
    String yymmdd();
    String hhmmss();
}


enum TestType {
    FIRST, FINAL;
}