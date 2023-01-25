package thejava.operator.bytecode.codecoverage;

public class Moim {

    int maxNumberOfAttendees; //최대 참가자

    int numberOfEnrollment; //현재 신청 수

    public boolean isEnrollmentFull() {
        //max가 존재하지 않음
        if (maxNumberOfAttendees == 0) {
            return false;
        }

        //신청 수가 max보다 적음
        if (numberOfEnrollment < maxNumberOfAttendees) {
            return false;
        }

        return true;
    }


}
