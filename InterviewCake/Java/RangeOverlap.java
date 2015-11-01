package inc;

public class RangeOverlap {

  public int start, len;

  public RangeOverlap() {
    start = 0; len = 0;
  }

  public RangeOverlap(int i, int l) {
    start = i; len = l;
  }

  public String toString() {
    return String.format("<Overlap at %d with length %d>", start, len);
  }

}