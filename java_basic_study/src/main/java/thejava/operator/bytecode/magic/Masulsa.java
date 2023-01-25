package thejava.operator.bytecode.magic;

import net.bytebuddy.ByteBuddy;
import net.bytebuddy.dynamic.ClassFileLocator;
import net.bytebuddy.implementation.FixedValue;
import net.bytebuddy.matcher.ElementMatchers;
import net.bytebuddy.pool.TypePool;

import java.io.File;
import java.io.IOException;

import static net.bytebuddy.matcher.ElementMatchers.named;

public class Masulsa {
    public static void main(String[] args) {

/*
        //V1
        //먼저 실행하여 바이트 코드를 변경해야 한다. (출력과 동시에 실행하면 기존 소스코드 내용이 출력되기 때문)
        try {
            new ByteBuddy().redefine(Moja.class)
                            .method(named("pollOut")).intercept(FixedValue.value("Rabbit!"))
                            .make().saveIn(new File("C:\\devtool\\project\\intellijProject\\study\\target\\classes\\")); //saveIn은 폴더 지정 (클래스 패키지 경로 따라서 폴더가 지정되므로 classes까지 지정하면 된다.)
        } catch (IOException e) {
            e.printStackTrace();
        }
*/

        //V2
        //클래스 로딩 시점을 늦춰서 바로 변환된 바이트 코드를 사용 가능
        //그러나 로딩 시점이 의존적이므로 다른 곳에서 이미 로딩을 했다면 의미가 없어진다.
        ClassLoader classLoader = Masulsa.class.getClassLoader();
        TypePool typePool = TypePool.Default.of(classLoader);

        try {
            new ByteBuddy().redefine(typePool.describe("thejava.operator.bytecode.magic.Moja").resolve(), ClassFileLocator.ForClassLoader.of(classLoader))
                            .method(named("pollOut")).intercept(FixedValue.value("Rabbit!"))
                            .make().saveIn(new File("C:\\devtool\\project\\intellijProject\\study\\target\\classes\\"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println(new Moja().pollOut());
    }
}
