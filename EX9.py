num = int(input("Digite um valor natural N para calcular o valor do seu quadrado: "));
impar = 1;
if (num > 0):
    while impar != (num*num):
        impar += 1
        quadrado = impar
    print(f'O quadrado de {num} é {quadrado}');
else:
    print("Número inserido inválido!");
        