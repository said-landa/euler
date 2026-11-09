main :: IO ()

main = print(sum multiples)
    where 
        number, m1, m2 :: Int
        number = 1000
        m1 = 3
        m2 = 5
        multiples =
            [ i
                | i <- [1 .. number - 1]
            , i `mod` m1 == 0 || i `mod` m2 == 0
            ]