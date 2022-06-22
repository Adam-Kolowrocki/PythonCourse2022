void wypisz(int, n)
{
    if(n < 0)  //(1)
    {
       print("-");
       n = -n;
    }
    if(n / 10 != 0)  //(2)
        wypisz(n / 10);

    printf("%d", (n % 10)); //(3)
}
