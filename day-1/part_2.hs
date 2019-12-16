import Control.Monad

main = do 
  fileLines <- liftM lines (readFile "input.in")
  print (sum . map fuel . map (read :: String -> Int) $ fileLines)

fuel :: Int -> Int
fuel x
  | fuel_mass > 0 = fuel_mass + fuel fuel_mass
  | otherwise = 0
  where fuel_mass = x `div` 3 - 2