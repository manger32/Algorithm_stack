using System;
using System.Collections;

void printArray(int[] array)
{
    for (int i = 0; i < array.Length; ++i)
        Console.Write(array[i] + " ");
}

void heapify(int[] array, int cnt, int root)
{
    int greatest_element = root;
    int left_anscestor = 2 * greatest_element + 1; int right_anscestor = 2 * greatest_element + 2;
    if (right_anscestor < cnt && array[right_anscestor] < array[greatest_element])
        greatest_element = right_anscestor;
    if (left_anscestor < cnt && array[left_anscestor] < array[greatest_element])
        greatest_element = left_anscestor;
    if (greatest_element == root)
        return;
    int tmp = array[root];
    array[root] = array[greatest_element];
    array[greatest_element] = tmp;
    heapify(array, cnt,  greatest_element);
}

void Heap_sort(int[] array)
{
    for (int i = array.Length / 2 - 1; i >= 0; i--)
        heapify(array, array.Length, i);
    for (int i = array.Length - 1; i >= 0; i--)
    {
        int tmp = array[0];
        array[0] = array[i];
        array[i] = tmp;
        Console.WriteLine(String.Join(", ", array.Take(i).ToArray()));
        heapify(array, i, 0);
    }
}

int[] array = { 50, 1, 3, 4, 5, 7, 8, 9, 3, 10, 19, 23, 10, 18, 1 };
Heap_sort(array);
Console.Clear();
Console.WriteLine("Sorted array in descending order using heapify() procedure: ");
printArray(array);
/** OUTPUT:
Sorted array in descending order using heapify() procedure:
50 23 19 18 10 10 9 8 7 5 4 3 3 1 1
**/