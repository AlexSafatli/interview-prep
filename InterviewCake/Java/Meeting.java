package common;

public class Meeting {

  public int startTime, endTime;

  public Meeting(int sT, int eT) {
    // Number of 30min blocks past 9am.
    startTime = sT; endTime = eT;
  }

  public String toString() {
    return String.format("(%d, %d)", startTime, endTime);
  }

}