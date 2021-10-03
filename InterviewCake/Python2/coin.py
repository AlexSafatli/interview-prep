def numberOfWaysToMakeAmountWithDenominations(amt, denominations):
  waysForCents = [0] * (amt + 1)
  waysForCents[0] = 1
  for coin in denominations:
    for higher in xrange(coin, amt+1):
      waysForCents[higher] += waysForCents[higher - coin]
  return waysForCents[amt]

if __name__ == '__main__':
  print numberOfWaysToMakeAmountWithDenominations(4, [1, 2, 3]) # => 4
  print numberOfWaysToMakeAmountWithDenominations(5, [1, 3, 5]) # => 3