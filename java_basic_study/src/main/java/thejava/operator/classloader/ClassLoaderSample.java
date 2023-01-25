package thejava.operator.classloader;

public class ClassLoaderSample {
    public static void main(String[] args) {
        ClassLoader classLoader = ClassLoaderSample.class.getClassLoader();
        System.out.println(classLoader);
        System.out.println(classLoader.getParent());
        System.out.println(classLoader.getParent().getParent());
    }
}
