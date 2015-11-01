package inc;

public class Rectangle {

  public int x, y, width, height; // x,y are of bottom left corner.

  public Rectangle() {
    x = 0; y = 0; width = 0; height = 0;
  }

  public Rectangle(int x, int y, int w, int h) {
    this.x = x; this.y = y;
    width  = w; height = h;
  }

  public String toString() {
    return String.format("[(%d, %d) width: %d height: %d]", x, y, width, 
      height);
  }

}