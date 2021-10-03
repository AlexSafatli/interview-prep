def highestProductOf3(a):
  assert (len(a) >= 3)
  highest = a[0] * a[1] * a[2]
  highestProductOf3 = a[0] * a[1] * a[2]
  highestProductOf2 = a[0] * a[1]
  lowestProductOf2 = a[0] * a[1]
  maxValue = a[0]
  minValue = a[1]
  for i in xrange(2,len(a)):
    val = a[i]
    highestProductOf3 = max([highestProductOf3,
      val*highestProductOf2,val*lowestProductOf2])
    highestProductOf2 = max([highestProductOf2,
      val*maxValue,val*minValue])
    lowestProductOf2  = min([lowestProductOf2,
      val*maxValue,val*minValue])
    maxValue = max([maxValue,val])
    minValue = min([minValue,val])
  return highestProductOf3

if __name__ == '__main__':
  print(highestProductOf3([-10,-10,3,2,1]))