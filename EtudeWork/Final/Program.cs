string [] CreateStringArray (int size)
{
    string [] newArray = new string [size];
    for (int i = 0; i < newArray.Length; i++)
    {
        Console.Write ($"Введите {i+1} значение массива: ");
        newArray[i] = Console.ReadLine();        
    }
    return newArray;
}

void ShowArray (string [] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();
}

void ThreeSimvolosArray (string [] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Length <= 3)
        Console.Write(array[i] + " ");
    }  
}

int size=3;

string [] array = CreateStringArray(size);
Console.WriteLine("Input simvols: "); 
ShowArray(array);

Console.WriteLine("Значения символов в массиве, длина которых < или = 3 :");
ThreeSimvolosArray(array);

Console.WriteLine();
