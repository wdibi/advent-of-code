import Control.Monad

main = do 
  fileLines <- liftM lines (readFile "input.in")
  print (sum . map fuel . map (read :: String -> Int) $ fileLines)

fuel :: Int -> Int
fuel x = x `div` 3 - 2 