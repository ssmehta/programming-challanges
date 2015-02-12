{-
Problem 001:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
-}

main = print $ sum [x | x <- [1..999], x `mod` 3 == 0 || x `mod` 5 == 0]
