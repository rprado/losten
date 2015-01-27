Descri��o

Site/aplicativo para relato de perda de objetos,
busca e recupera��o dos mesmos. 

// same old comment

Fluxo de a��o dos usu�rios

Defini��o de Requisitos
RQ00 - cadastro/login

RQ01 - cria-se uma localidade
RQ02 - os membros interessados se cadastram

RQ03 - algu�m do grupo notifica perda
RQ04 - o sistema pergunta ao grupo quem achou

RQ05 - algu�m do grupo notifica encontro
RQ06 - o sistema pergunta ao grupo quem perdeu

RQ07 - usa foto para mostrar o que foi encontrado ou perdido
RQ08 - possui vers�o mobile para receber as notifica��es
RQ09 - possui plugin para redes sociais


Especifica��o de Requisitos
RQ00 - o acesso n�o pode ser burocr�tico, oferecer OAuth (apenas?); 
       acesso inicial (mobile) solicita usu�rio[email v�lido] e senha 
       apenas uma vez; acesso online solicita sempre.
       usu�rio deve acessar seu email para ativar conta.

RQ01 - o sistema oferece uma GUI em que o usu�rio selecione uma
       localidade (estado/cidade/bairro/institui��o) em um mapa
       no ato da cria��o/sele��o deve ser oferecida uma lista de 
       modalidade de localidades (escola, clube, condom�nio, etc);
       a digita��o do nome de uma localidade deve oferecer recurso
       de autocompletar.
       
RQ02 - procedimento id�ntico ao do RQ01 deve ser adotado para o 
       cadastro dos novos usu�rios em uma localidade; cada usu�rio
       pode, simultaneamente, acessar v�rias localidades.
       
RQ03 - a notifica��o de perda deve ser muito simples, oferecendo
       acesso a listas de objetos que as pessoas perdem com frequ�ncia
       para sele��o r�pida pelo comunicante; selecione a localidade,
       selecione o tipo de objeto e pronto.
       
RQ04 - o sistema envia notifica��es para as pessoas que se cadastraram
       como "membros de uma localidade" informando a perda e perguntando
       se algu�m achou.
       
RQ05 - idem RQ03 (usu�rio informa objeto encontrado)

RQ06 - idem RQ04 (sistema pergunta quem perdeu)
       
RQ07 - RQ03 e RQ05 devem ter acesso � c�mera (smart/tablet) 
       ou upload de imagem(laptop/desktop)
       
       
P�ginas
P0 - login
     leva a P1 se for inicial ou a P2 para usu�rio cadastrado

P1 -  cadastro e/ou sele��o de localidade
      mapa pa�s -> mapa estado -> mapa bairro -> lista localidades -> lista de sublocalidades
      
      