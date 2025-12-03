parseLine :: String -> (Char, Int)
parseLine (d:n) = (d, read n)
parseLine _     = undefined

parse :: String -> [(Char, Int)]
parse = map parseLine . lines

solve :: [(Char, Int)] -> Int
solve = sum . clicks dial where
    dial = 50

scanll :: (b -> a -> (b, c)) -> b -> [a] -> [c]
scanll f b = zipWith (flip f2) <*> scanl f1 b where
    f1 = (fst .) . f
    f2 = (snd .) . f

clicks :: Int -> [(Char, Int)] -> [Int]
clicks dial = scanll turn dial where

    turn :: Int -> (Char, Int) -> (Int, Int)
    turn dial (d, n) = (dial', m) where
        dial1 = if d == 'L' then invert dial else dial
        (m, dial3) = divMod (dial1 + n) 100
        dial' = if d == 'L' then invert dial3 else dial3

    invert :: Int -> Int
    invert = (`mod` 100) . (100 -)

main :: IO ()
main = interact (show . solve . parse)