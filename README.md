# ALGORITMS

## Сортировка пузырьком
> Сложность алгоритма: On2


Дан массив с n элементами
`| 0 | 1 | 2 | ... | n-2 | n-1 |`
+ ![Авторство: Swfung8. Собственная работа, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=14953478](./media/Bubble-sort-example-300px.gif)
+ сравнить `0` с `1`, `1` с `2`..
+ цикл от `0` до `n-2`
### метод трёх стаканов
+ `arr[i] = tmp`
+ `arr[i+1] = arr[i]`
+ `tmp = arr[i+1]`
+ 