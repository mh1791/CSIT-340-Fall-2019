import Data.Char(ord)
--merge functino takes varables in a list and orders them, then merges
merge :: Ord a => [a] -> [a] -> [a]
merge [] ys         = ys
merge xs []         = xs
merge (x:xs) (y:ys) | x < y     = x:merge xs (y:ys)
                    | otherwise = y:merge (x:xs) ys
--halve splits the list int two
halve :: [a] -> ([a],[a])
halve xs = (take lhx xs, drop lhx xs)
           where lhx = length xs `div` 2
-- mergeSort function take the two functions above and uses them to take two lists, sort them, then merge.
mergeSort :: Ord a => [a] -> [a]
mergeSort [x] = [x]
mergeSort  xs = merge (mergeSort left) (mergeSort right)
            where (left,right) = halve xs
-- mHexDigit takes a hex digit and compares them to a list, then spits it out the integer number. if not -1
mHexDigit:: Char -> Int
mHexDigit n | n == 'A' = 10
            | n == 'a' = 10
            | n == 'B' = 11
            | n == 'b' = 11
            | n == 'C' = 12
            | n == 'c' = 12
            | n == 'D' = 13
            | n == 'd' = 13
            | n == 'E' = 14
            | n == 'e' = 14
            | n == 'F' = 15
            | n == 'f' = 15
            | n == '1' = 1
            | n == '2' = 2
            | n == '3' = 3
            | n == '4' = 4
            | n == '5' = 5
            | n == '6' = 6
            | n == '7' = 7
            | n == '8' = 8
            | n == '9' = 9
            | otherwise = -1

-- mHex takes a string and evaluates it's value in hex
mHex :: String -> Integer
mHex [] = 0
mHex str = 
  fromIntegral n + 16 * mHex (init str)
    where n = let i = last str 
              in if i >= 'A' && i <= 'Z' 
                    then fromEnum i - 55 
                    else if i >= 'a' && i <= 'z'
                            then fromEnum i - 87
                            else fromEnum i - 48
-- Varmap takes the function takes a string and sees if its in the list
-- takes the form of varmap "x" [("x",i),("x2",i2)...]
varmap::String ->[(String,Int)] -> Int
varmap _ [] = -1
varmap x ((a,b):xs) = if x == a then b else varmap x xs