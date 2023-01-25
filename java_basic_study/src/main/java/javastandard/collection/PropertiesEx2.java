package javastandard.collection;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class PropertiesEx2 {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("USAGE: java PropertiesEx2 INPUTFILENAME");
            System.exit(0);
        }

        Properties properties = new Properties();

        String inputFile = args[0];

        try {
            properties.load(new FileInputStream(inputFile));
        } catch (IOException e) {
            System.out.println("지정된 파일을 읽을 수 없습니다.");
            System.exit(0);
        }

        String name = properties.getProperty("name");
        String[] data = properties.getProperty("data").split(",");
        int max = 0;
        int min = 0;
        int sum = 0;

        for (int i=0; i < data.length; i++) {
            int intVal = Integer.parseInt(data[i]);

            if (i == 0) {
                max = min =intVal;
            }

            if (intVal > max) {
                max = intVal;
            } else if (intVal < min) {
                min = intVal;
            }

            sum += intVal;
        }

        System.out.println("이름 : " + name);
        System.out.println("최대값 : " + max);
        System.out.println("최소값 : " + min);
        System.out.println("합계 : " + sum);
        System.out.println("평균 : " + (sum * 100 / data.length) / 100);
    }
}
