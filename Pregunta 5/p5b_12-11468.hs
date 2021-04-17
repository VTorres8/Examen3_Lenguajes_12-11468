--Pregunta 5.b

--Data Arbol
data Arbol a = Hoja | Rama a (Arbol a) (Arbol a)
    deriving (Show)

--Funcion foldA propuesta
foldA  :: (a -> b -> b -> b) -> b -> Arbol a -> b
foldA f x Hoja = x
foldA f x (Rama y r d) = f y (foldA f x r)  (foldA f x d)

--Funcion TakeWhile
takeWhileA :: (a -> Bool) -> Arbol a -> Arbol a
takeWhileA p = foldA (\a i d -> if p a then Rama a i d else Hoja) Hoja

--Funcion genA
genA :: Int -> Arbol Int
genA n = Rama n (genA (n + 1)) (genA (n * 2))

--Si carga este modulo en el ghci y ejecuta la llamada:
--takeWhileA (<= 3) (genA 1)
--funciona (:'v) y retorna:
--Rama 1 (Rama 2 (Rama 3 Hoja Hoja) Hoja) (Rama 2 (Rama 3 Hoja Hoja) Hoja)
--Que es el resultado de la corrida :'v