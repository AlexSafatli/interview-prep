package structures;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class StringBuffer {

  private List<String> strings;

  public StringBuffer() {
    strings = new ArrayList<String>();
  }

  public StringBuffer(int n) {
    strings = new ArrayList<String>(n);
  }

  public void append(String s) {
    strings.add(s);
  }

  public String toString() {
    return Arrays.toString(strings.toArray(new String[strings.size()]));
  }

}