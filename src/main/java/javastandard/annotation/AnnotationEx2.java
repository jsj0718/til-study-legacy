package javastandard.annotation;

import java.util.ArrayList;

public class AnnotationEx2 {
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        NewClass nc = new NewClass();

        nc.oldField = 10;
        System.out.println(nc.getOldField());

        @SuppressWarnings("unchecked")
        ArrayList<NewClass> list = new ArrayList();
        list.add(nc);
    }
}

class NewClass {
    int newField;

    public int getNewField() {
        return newField;
    }

    @Deprecated
    int oldField;

    public int getOldField() {
        return oldField;
    }
}
