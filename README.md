![insta back](https://user-images.githubusercontent.com/103686624/234957832-88cada5f-1966-427d-90d3-edbd2d3e5387.jpg)
## Requerimentos
-Instale [Python](https://www.python.org/downloads/)</br>
-Instale [PostgreSQL](https://www.postgresql.org/download/)<br>
-Instale [Microsoft Visual C++](https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/), lembre de selecionar a opção "Desenvolvimento para desktop com C++"
</br>
![c++](https://user-images.githubusercontent.com/103686624/234313444-c1f7d5fc-53e4-4c63-84a1-25bf3b86f720.png)
</br>
-
-Usando **cmd.exe**, acesse a pasta da aplicação usando `cd "pasta\da\aplicação"` e use o comando `pip install venv`. Agora podemos criar o virtual enviroment usando
o comando `py -m venv venv` e ativá-lo usando `"pasta\da\aplicação"\venv\Scripts\Activate.bat`. Por fim, use `pip install -r requirements.txt` para instalar as packages e
`py manage.py runserver` para iniciar a aplicação. 
</br>
![link](https://user-images.githubusercontent.com/103686624/234323414-8999ca7a-df91-4613-91c4-2684d237c18c.jpg)
</br>
Para acessar o site, use o link conforme a image acima.
## Utilizando o site
### Login
Para acessar, você precisa criar uma conta ou entrar com uma conta existente.
<br>
![login](https://user-images.githubusercontent.com/103686624/234984644-41f4b39e-a6fa-4d84-a64a-acd08bdfa182.jpg)
<br>
### Home
Na home você consegue ver os posts feitos pelos usuários que você segue e consegue criar um post clicando no símbolo de mais e selecionando uma imagem e descrição.
<br>
![create post](https://user-images.githubusercontent.com/103686624/234971891-feddd689-38e5-4261-a31d-33e3c26366c4.jpg)
### Discover 
Você pode usar o discover clicando no símbolo de bússola. 
Lá você consegue ver uma lista aleatória de posts de usuários que você ainda não segue, caso você ache um post interessante clique nele para abrir. 
<br>
![discover](https://user-images.githubusercontent.com/103686624/234972859-13174aff-d930-4e44-8719-c5e887921fd1.jpg)
### Posts
Quando você clica em um post, você acessa a sua versão completa. É possível ver o author, a descrição, foto do post, todos comentários feitos e o número e lista de 
usuários que deram like. Além disso, aqui é póssivel adicionar seu próprio comentário ao post e também dar um like. Caso queira ver o perfil do usuário, basta clicar
em seu nome.
<br>
![post](https://user-images.githubusercontent.com/103686624/234974030-6eb7fe8e-8bcc-404c-9efa-d36be2814e29.jpg)
### Perfil
Ao acessar um perfil, você consegue ver informações que o dono do perfil adicionou, como biografia, nome, foto de perfil, os posts criados pelo usuário e também
os números de seguidores. É possível seguir e parar de seguir o perfil nessa página.
<br>
![perfil](https://user-images.githubusercontent.com/103686624/234976076-b8f32989-d2f4-4dcf-a331-dc1608e039fe.jpg)
<br>
### Notificações
Algumas ações, como seguir um perfil, podem adicionar uma mensagem na aba de notificações. Para acessar as notificações, clique no coração.
<br>
![notifi](https://user-images.githubusercontent.com/103686624/234978424-a61ff0a0-73c7-4c51-be8a-d21993e8332b.jpg)
<br>
### Seguidores
Seguir e deixar de seguir usuários afeta alguns aspectos do site, na home somente aparece posts de pessoas que você segue e no discover somente das que 
você não segue e você só consegue mandar mensagens para usuários que você segue e ele te segue de volta.
### Direct
Aqui você consegue mandar mensagens para seus mutuais, as mensagens são mandadas e recebidas em tempo real e são salvas para serem vistas mais tarde.
<br>
![chat](https://user-images.githubusercontent.com/103686624/234979154-2a5ba498-bbff-4fd0-b584-6e295c2db65b.jpg)
<br>
## Sobre
Esse projeto foi criado com a finalidade de testar meus conhecimnentos no framework Django e também em outras ferramentas como Html, Css, Javascript, Ajax,
jQuery e Channels. 
<br>
O site foi criado usando o modelo MVC com framework Django e seu ORM para realizar as operaçãoes da database. Algumas partes do site necessitaram do uso de 
requisições assíncronas em dois tipos ocasiões, uma delas era quando era necessário mostrar o resultado de alguma ação do usuário assim que ela fosse realizada,
nesse caso foi usado o AJAX para acessar um endpoint que realizava uma ação e retornava a porção da página que deveria ser atualizada, como era o caso quando era 
usado os botões de seguir, comentar e curtir, já a outra ocasião era quando era usado o direct, aqui foi usado o Django Channels, que utiliza WebSockets, para
abrir um canal de comunicação entre dois usuários. <br>
O frontend do projeto foi feito utilizando Html, Css puro e Javascript com jQuery.
<br>
O projeto originalmente foi feito para ser usado utilizando o PostgreSQL para armazenar as informações, porém o SQLite, usado como default pelo Django, acabou sendo
usado, já que este possibilita subir o projeto já com alguns dados, como perfis.





