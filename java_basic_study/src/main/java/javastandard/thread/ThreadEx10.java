package javastandard.thread;

public class ThreadEx10 {
    static boolean autoSave = false;

    public static void main(String[] args) {
        Thread t = new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    try {
                        Thread.sleep(3 * 1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    if (autoSave) {
                        autoSave();
                    }
                }
            }
        });

        t.setDaemon(true);
        t.start();

        for (int i=1; i<=10; i++) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println(i);

            if (i == 5) {
                autoSave = true;
            }
        }

        System.out.println("프로그램 종료");
    }

    public static void autoSave() {
        System.out.println("파일이 자동 저장되었습니다.");
    }
}
