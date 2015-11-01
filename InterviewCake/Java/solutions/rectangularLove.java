import inc.Rectangle;
import inc.RangeOverlap;

class RectangularLove {

  public static RangeOverlap overlap(int pa, int la, int pb, int lb) {
    // Overlap in a single dimension.
    int highestStart = Math.max(pa, pb);
    int lowestEnd    = Math.min(pa + la, pb + lb);
    if (highestStart >= lowestEnd) return new RangeOverlap(0, 0);
    int len          = lowestEnd - highestStart;
    return new RangeOverlap(highestStart, len);
  }

  public static Rectangle intersectionOf(Rectangle a, Rectangle b) {
    // Divide problem into two halves - two 1D comparisons (x, y axes).
    RangeOverlap x    = overlap(a.x, a.width, b.x, b.width);       // x
    RangeOverlap y    = overlap(a.y, a.height, b.y, b.height);     // y
    if (x.len < 1 || y.len < 1) return new Rectangle();
    else return new Rectangle(x.start, y.start, x.len, y.len);
  }

  public static void main(String[] args) {
    Rectangle a = new Rectangle(0, 0, 10, 10);
    Rectangle b = new Rectangle(1, 2, 1, 1);
    System.out.println(intersectionOf(a,b));
  }

}