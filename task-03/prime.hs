


isPrime :: Int -> Bool
isPrime x = count == 2
  where
    count = length [i | i <- [1..x], x `mod` i == 0]

main :: IO ()
main = do
  putStrLn "Enter the limit: "
  num <- readLn :: IO Int
  let primes = [i | i <- [2..num], isPrime i]
  mapM_ print primes
