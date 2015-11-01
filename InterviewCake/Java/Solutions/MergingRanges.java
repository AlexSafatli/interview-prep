import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;

class MergingRanges {

  public static void main(String[] args) {

    MeetingTimeRanges meetings = new MeetingTimeRanges();

    // Test Case 1
    meetings.add(0,  1);
    meetings.add(3,  5);
    meetings.add(4,  8);
    meetings.add(10, 12);
    meetings.add(9,  10);
    System.out.println(meetings.condenseMeetingTimes());

    // Test Case 2
    meetings.clear();
    meetings.add(1,  2);
    meetings.add(2,  3);
    System.out.println(meetings.condenseMeetingTimes());

    // Test Case 3
    meetings.clear();
    meetings.add(1,  5);
    meetings.add(2,  3);
    System.out.println(meetings.condenseMeetingTimes());

    // Test Case 4
    meetings.clear();
    meetings.add(1, 10);
    meetings.add(2,  6);
    meetings.add(3,  5);
    meetings.add(4,  5);
    meetings.add(3,  9);
    meetings.add(7,  9);
    System.out.println(meetings.condenseMeetingTimes());

  }

}

class MeetingTimeRanges extends ArrayList<Meeting> {

  public void add(int a, int b) {
    add(new Meeting(a,b));
  }

  public MeetingTimeRanges condenseMeetingTimes() {
    if (size() == 0) {
      throw new Error("Need at least one meeting time.");
    }
    MeetingTimeRanges condensed = new MeetingTimeRanges();
    // Sort the meeting times in order of their starting time.
    Collections.sort(this, new MeetingComparator());
    // Keep track of a previous meeting time.
    Meeting previous = get(0);
    // Go through each meeting time, see if next overlaps. Add non-overlapping.
    for (Meeting meeting : this) {
      if (meeting.startTime <= previous.endTime) { // Overlap.
        previous.endTime = Math.max(meeting.endTime, previous.endTime);
      } else { // No overlap.
        condensed.add(previous);
        previous = meeting;
      }
    }
    condensed.add(previous);
    return condensed;
  }

}

class MeetingComparator implements Comparator<Meeting> {

  @Override
  public int compare(Meeting a, Meeting b) {
    return a.startTime - b.startTime;
  }

}

class Meeting {

  int startTime, endTime;

  public Meeting(int sT, int eT) {
    // Number of 30min blocks past 9am.
    startTime = sT; endTime = eT;
  }

  public String toString() {
    return String.format("(%d, %d)", startTime, endTime);
  }

}