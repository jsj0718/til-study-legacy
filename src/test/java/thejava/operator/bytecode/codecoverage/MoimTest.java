package thejava.operator.bytecode.codecoverage;

import org.junit.Test;
import org.junit.jupiter.api.Assertions;
import thejava.operator.bytecode.codecoverage.Moim;

public class MoimTest {

    @Test
    public void isFull() {
        Moim moim = new Moim();
        moim.maxNumberOfAttendees = 100;
        moim.numberOfEnrollment = 10;

        Assertions.assertFalse(moim.isEnrollmentFull());
    }
}