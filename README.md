Exercícios referentes ao arquivo disponibilizado pela professora Debora Paixao- Fiap durante o curso Star Tech 7 Edição.


# EXERCÍCIOS USANDO STRINGS

**EXERCÍCIOS USANDO STRINGS**

**1. CONTANDO CARACTERES DO NOME**
Nível: Fácil
Peça ao usuário que digite o nome completo (input) e informe quantos caracteres esse nome tem, usando len(). Antes de contar, remova espaços em branco no início e no fim do texto digitado (dica: método .strip()).

**2. PADRONIZANDO NOMES**
Nível: Fácil
Muitas vezes o cliente digita o nome todo em maiúsculas, todo em minúsculas ou de forma bagunçada. Peça o nome do cliente (input) e imprima-o já formatado, com a primeira letra de cada palavra em maiúscula (dica: método .title()).

**3. VALIDANDO TELEFONE**
Nível: Fácil
Crie um programa que peça o telefone do cliente (input), apenas com números, sem espaços, parênteses ou traços. O telefone deve ter exatamente 11 dígitos (DDD + número). Verifique se o que foi digitado tem 11 caracteres e se contém apenas números, exibindo uma mensagem de sucesso ou de erro.

**4. MASCARANDO UMA SENHA**
Nível: Fácil
Por segurança, ao exibir a senha de um usuário na tela, o sistema deve mostrar apenas os 2 primeiros e os 2 últimos caracteres, substituindo o restante por asteriscos (*). Exemplo: a senha 'hashtag123' deve virar 'ha******23'. Use fatiamento (slicing) para pegar o início e o fim da senha.
Dados de partida: senha = 'hashtag123'

**5. CONTANDO LETRAS REPETIDAS**
Nível: Fácil
Dada uma palavra, use o método .count() para descobrir quantas vezes a letra 'a' aparece nela (não diferencie maiúsculas de minúsculas) e imprima o resultado.
Dados de partida: palavra = 'Abacaxi Amarelo'

**6. VALIDANDO NOME DE ARQUIVO**
Nível: Fácil
Um sistema só aceita imagens no formato '.jpg' ou '.png'. Peça ao usuário o nome do arquivo (input) e use os métodos .endswith() para verificar se ele termina com uma dessas extensões, exibindo se o arquivo é aceito ou não.

**7. NOME COMPLETO SEM ESPAÇOS EXTRAS**
Nível: Fácil
Peça ao usuário o primeiro nome e o sobrenome em dois inputs separados. Uma frase que junta as duas informações usando f-string, garantindo que não sobrem espaços extras no início ou no fim de cada parte (dica: .strip()).

**8. VERIFICANDO PALÍNDROMO**
Nível: Fácil
Um palíndromo é uma palavra que se lê da mesma forma de trás para frente, como 'arara' ou 'ovo'. Peça uma palavra ao usuário (input), inverta essa palavra usando fatiamento (slicing) e verifique se ela é um palíndromo, ignorando maiúsculas/minúsculas.

**9. VALIDANDO CNPJ COM FORMATAÇÃO**
Nível: Médio
Assim como o CPF, o CNPJ pode ser digitado com pontos, barra e traço (ex: '12.345.678/0001-90'). Peça o CNPJ ao usuário (input), remova pontos, barras e traços (dica: .replace()) e verifique se sobraram exatamente 14 números. Exiba o CNPJ já limpo ou uma mensagem de erro.

**10. VALIDANDO E-MAIL CORPORATIVO**
Nível: Médio
A empresa só aceita e-mails corporativos, que devem terminar com '@hashtag.com'. Peça o e-mail do funcionário (input) e verifique, usando .endswith(), se ele é um e-mail corporativo válido. Se não for, exiba uma mensagem informando que o e-mail deve ser do domínio da empresa.

**11. EXTRAINDO O DOMÍNIO DO E-MAIL**
Nível: Médio
Dado um e-mail válido (contendo '@'), separe a parte antes do '@' (usuário) da parte depois do '@' (domínio) usando o método .split('@'), e imprima as duas partes separadamente.
Dados de partida: email = 'lira@gmail.com'

**12. VERIFICANDO FORÇA DA SENHA**
Nível: Médio
Uma senha é considerada forte se tiver pelo menos 8 caracteres, pelo menos uma letra e pelo menos um número. Peça uma senha ao usuário (input) e use um for percorrendo cada caractere (junto com .isalpha() e .isdigit()) para verificar se há letra e número na senha, além de checar o tamanho mínimo. Informe se a senha é forte ou fraca.

**13. CONTANDO VOGAIS E CONSOANTES**
Nível: Médio
Peça uma frase ao usuário (input) e, usando um for percorrendo cada letra, conte quantas vogais e quantas consoantes existem na frase (ignore espaços e considere apenas letras). Ao final, imprima os dois totais.

**14. GERANDO NOME DE USUÁRIO**
Nível: Médio
Um sistema gera automaticamente o nome de usuário (username) de um funcionário a partir do nome completo: a primeira letra do primeiro nome, seguida do sobrenome completo, tudo em minúsculas. Exemplo: 'Ana Beatriz Souza' vira 'asouza'. Peça o nome completo (input), use .split() para separar as palavras e monte o username.

**15. VALIDANDO PLACA DE CARRO (PADRÃO ANTIGO)**
Nível: Médio
O padrão antigo de placas de carro no Brasil é composto por 3 letras seguidas de 4 números, sem separador (ex: 'ABC1234'). Peça a placa ao usuário (input) e verifique se ela segue esse padrão: os 3 primeiros caracteres devem ser letras (dica: fatiamento + .isalpha()) e os 4 últimos devem ser números (dica: fatiamento + .isnumeric()). Exiba se a placa é válida.
