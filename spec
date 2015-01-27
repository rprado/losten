Descrição

Site/aplicativo para relato de perda de objetos,
busca e recuperação dos mesmos. 

// same old comment

Fluxo de ação dos usuários

Definição de Requisitos
RQ00 - cadastro/login

RQ01 - cria-se uma localidade
RQ02 - os membros interessados se cadastram

RQ03 - alguém do grupo notifica perda
RQ04 - o sistema pergunta ao grupo quem achou

RQ05 - alguém do grupo notifica encontro
RQ06 - o sistema pergunta ao grupo quem perdeu

RQ07 - usa foto para mostrar o que foi encontrado ou perdido
RQ08 - possui versão mobile para receber as notificações
RQ09 - possui plugin para redes sociais


Especificação de Requisitos
RQ00 - o acesso não pode ser burocrático, oferecer OAuth (apenas?); 
       acesso inicial (mobile) solicita usuário[email válido] e senha 
       apenas uma vez; acesso online solicita sempre.
       usuário deve acessar seu email para ativar conta.

RQ01 - o sistema oferece uma GUI em que o usuário selecione uma
       localidade (estado/cidade/bairro/instituição) em um mapa
       no ato da criação/seleção deve ser oferecida uma lista de 
       modalidade de localidades (escola, clube, condomínio, etc);
       a digitação do nome de uma localidade deve oferecer recurso
       de autocompletar.
       
RQ02 - procedimento idêntico ao do RQ01 deve ser adotado para o 
       cadastro dos novos usuários em uma localidade; cada usuário
       pode, simultaneamente, acessar várias localidades.
       
RQ03 - a notificação de perda deve ser muito simples, oferecendo
       acesso a listas de objetos que as pessoas perdem com frequência
       para seleção rápida pelo comunicante; selecione a localidade,
       selecione o tipo de objeto e pronto.
       
RQ04 - o sistema envia notificações para as pessoas que se cadastraram
       como "membros de uma localidade" informando a perda e perguntando
       se alguém achou.
       
RQ05 - idem RQ03 (usuário informa objeto encontrado)

RQ06 - idem RQ04 (sistema pergunta quem perdeu)
       
RQ07 - RQ03 e RQ05 devem ter acesso à câmera (smart/tablet) 
       ou upload de imagem(laptop/desktop)
       
       
Páginas
P0 - login
     leva a P1 se for inicial ou a P2 para usuário cadastrado

P1 -  cadastro e/ou seleção de localidade
      mapa país -> mapa estado -> mapa bairro -> lista localidades -> lista de sublocalidades
      
      