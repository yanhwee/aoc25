parse :: String -> [String]
parse = lines

solve :: [String] -> Int
solve = count 0 . turns

count :: Eq a => a -> [a] -> Int
count x = length . filter (== x)

turns :: [String] -> [Int]
turns = scanl turn dial where
    dial = 50
    turn n = (`mod` 100) . (n +) . lineToTurn

lineToTurn :: String -> Int
lineToTurn line =
    let op = head line
        n = read $ tail line
    in  if op == 'L'
        then -n
        else n

main :: IO ()
main = interact (show . solve . parse)
