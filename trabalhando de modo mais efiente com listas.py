#estou aprendendo como usa-se o laço for para fazer tarefas que exigem um grande numuro de repetições, tornar essa trarefa altomatizada com isso tornando meu codigo mais eficiente.
#uma coisa que reparei é que o laço for so funciona quando meu codigo estiver identado. 
latas=['boston','chicago bullslosanges lakers','new york nicks','golde state warriors']
for lata in latas:
    print(lata+'\n') 

#aqui irei alem de mostrar cada intem da minha lista usando o laço for, também vou demonstrar como escrever uma mensagem juntamente com cada item que for exibir.
#aprendi uma coisa muito interessante, quando eu escrever varios comandos abaixo do meu laço de repetição for ele irá fazer a interpretação de todos esses comandos para depois ir para a segunda etapa, que seria fazer a mesma coisa que foi feita antes.
#tambem pude ver que posso fazer o uso do print e do \n para quebrar a linha e com isso deixar meu codigo mais legivel, no entanto recomendo usar \n por que é mais simples e elagante.
 
livros=['surpreenda-se com o seu potencial', 'o poder do hábito']
for livro in livros:
    print(livro.title()+',', 'foi um livro muito marcante para mim, me encinou varias lições.')
    print('Qual e o nome do livro?','\n''O nome do livro é', livro.upper()+'\n') 
 
print('obrigado laço for por facilitar minha vida''\n')    

#fazendo testes com erros de identação.
#aqui se eu identar o print ira dar erro, porque o print nao pertecen linha de codigo anterior a ele.

msg='hello word'
print(msg+'\n')

#################################

#exercicios usando o laço de repetição for
#aqui irei criar um lista com os sabores de pizzas que eu gosto e usar o laço de repetição for para mostrar de uma forma altomatizada todos os nomes dentro da lista.
 
pizzas=['banana com canela', 'presunto e queijo', 'tradicional']

for pizza in pizzas:
    print(pizza ,'\n')

for pizza in pizzas:
    print('gosto do sabor de pizza de'+" "+pizza.upper())

print()  
print('realmente eu adoro pizza de banana com canela, presunto e queijo e tradicional.')
print()

#lista de animais que tenham uma caracteristica em comum.

animais=['leão','tigre','guepardo']
for animai in animais:
    print(animai,'\n')

print(animais[0]+" "+'é uns dos animais mais poderosos da africa.')
print('O',animais[1]+" "+'na minha opinão é o felino mais forte da terra.')
print(animais[2]+" "+'não preciso nem comentar sobre esse animal , é o felino mais rapido mundo.')
print('O motivo para mim ter escolhido esses animais é porque sao grandes caçadores, e cada um com suas habilidades unicas.','\n')

#aqui irei começar a tralhar com listas numericas, aprenderei tambem a usar as diversas ferramentas que python me disponibiliza para esse tipo de ação.
#usando o a função range() para gerar uma serie de numeros .
#uma anotação importante a se fazer é que em python ao gerar numeros atravez da função range, quaso eu queira que mostre por explo os numeros de 1 a 8 python ira mostrar apenas do 1 ao 7, isso ocorre pelo deslocamento de 1.
#uma boa solução para esse problema é sempre usar um numero acima do valor final esperado.

for numero in range(1,5):
    print(numero)

for msg in range(3,8):
    print(msg,'\n')
    
 #usando a função list para transformar os numeros gerados pela minha função range em uma lista.

f_list=list(range(1,12))
print(f_list,'\n')

#usando range para mostrar em uma lista atraves da função list os numeros pares de 1 a 20.

par=list(range(2,21,2))
print(par,'\n')

#adicionando em uma lista valores elevados ao quadrado.
#para isso primeiro irei criar uma lista vazia que possa amazenar os valores.
#depois vou usar o laço de repetição for para armazenar os numeros dentro de uma variavel.
#e por fim vou usar a fução append e a variavel elevada ao quadrado para adicionar na minha lista os resultados.

#modo mais legivel;
brr = []
for grr in range(1,11):
    ex = grr**2
    brr.append(ex)

print(brr,'\n')

#modo mais compacto; 
prr=[]
for numero in range(1,21):
    prr.append(numero**2)

print(prr,'\n')
 
#python me possibilita o uso de funções especificas para a listas de numeros.
#como por exemplo as funções sum, max e min.
#sum soma todos os valores da minha lista.
#max mostra o valor maximo da lista.
#min mostra o valor minimo.
lis=[]
for vr in range(1,13):
    lis.append(vr)
print(lis,'\n') 
print(max(lis))
print(sum(lis))
print(min(lis))

#usando abrangencia de lista para exponenciar valores que a função range ira gerar.
#a abrangencia de lista é uma boa opção pra economizar codigo, porque possibilita ao programador exponeciar valores em uma lista em apenas uma linha de codigo.

abrangencia=[vp**2 for vp in range(1,6)] 
print(abrangencia)

ab=[ var**4 for var in range(2,9)]
print(ab)
print(ab[2])
far=str(ab[3])
print(far,'transformando valores int em str', '\n')


##########################exercicios
 
#contando de 1 ate 20, mostrando em forma de lista e ordena.
pro=[]
for fit in range(1,21):
    pro.append(fit)
    print(fit)

print(pro,'\n')

#criando uma lista que vai ate um milhão.

u_milhao=[]
for um in range(101):
    print(um)
    u_milhao.append(um)

print(u_milhao,'\n')

#mostrando valores da minha lista atraves das funções min,max e sum.

print(min(u_milhao))
print(max(u_milhao))
print(sum(u_milhao),'\n')

#criando um lista de 1 a 20 para mostrar apenas os numeros impares.

impar=[]
for par in range(1,20,2):
    print(par,'\n')

#criando uma lista que me traga valores que sao multiplos de 3.
#multiplos 3 são numeros poder ser divididos por 3.
 
multp=[]
for mp in range(0,31,3):
    multp.append(mp)

print(multp,'\n')

#usando abrangencia de lista para gerar numeros multiplos de 3, mas agora usarei essa abordagem por conta de sua praticidade.

abr_list=[ simples for simples in range(0,31,3)]
print(abr_list,'\n')

#aqui vou usar um laço de repetição for para gerar valores elevados ao cubo(terceira potencia) e criar uma lista aonde eu passa armazenar esses valores.

elv_cubo=[]
for cubo in range(1,11):
    hp=cubo**3
    elv_cubo.append(hp)

print(elv_cubo,'\n')

#usando um modo mais simples.
simp=[]
for sp in range(1,11):
    simp.append(sp**3)

print(simp,'\n')

#usando abrangencia de lista para elevar numeros de 1 a 10 ao cubo.

abr_cubo=[tr**3 for tr in range(1,11)]
print(abr_cubo,'\n') 

#aqui irei testa como se faz o fatiamento de um lista em python.

jogos=['fifa 2020', 'clash of clans','the sims','star wars', 'xadrez','bem10', 'dragon boll']
print(jogos[0:2])