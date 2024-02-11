1. Clonar o repositório
    git clone <URL do repositório>
2. Navegar para o diretório do projeto
    cd <diretório_do_projeto>
3. Executar a aplicação
    python main.py
4. Executar os testes unitários
    Execute os testes unitários para verificar se as classes funcionam conforme esperado:
    python testes_unitarios.py
    Sobre os testes:
Os testes unitários garantem a integridade das classes Calculador,Circle e Person. Eles verificam diferentes aspectos das classes, como operações aritmeticas para calculadora, cálculo de área e circunferência para Circle, e funcionamento correto dos métodos update_age e is_adult para Person.

5. Analisar resultados dos testes
Após a execução dos testes, verifique os resultados para garantir que todas as asserções passaram. Se algum teste falhar, analise o motivo e faça as correções necessárias no código.

 Sobre a classe Calculator:
    A classe Calculator é uma calculadora simples que possui 4 métodos principais:

    soma(a, b): Retorna a soma dos dois números passados como argumentos.
    subtrai(a, b): Retorna a diferença entre os dois números passados como argumentos.
    multiplica(a,b): Retorna o produto entre os dois números passados como argumentos.
    divide(a,b): Retorna a divisão entre os dois números passados como argumentos.
    Sobre a classe Circle:
    A classe Circle representa um círculo. Ela possui um atributo radius que armazena o raio do círculo e dois métodos:
    
    area(): Calcula e retorna a área do círculo com base no raio.
    circumference(): Calcula e retorna a circunferência do círculo com base no raio.
    
    Sobre a classe Person:
    A classe Person representa uma pessoa. Ela possui dois atributos, name e age, que armazenam o nome e a idade da pessoa, respectivamente. Além disso, possui dois métodos:
    
    update_age(new_age): Atualiza a idade da pessoa para um novo valor fornecido como argumento.
    is_adult(min_age=18): Verifica se a pessoa é considerada adulta com base em uma idade mínima fornecida como argumento. Se nenhum argumento for fornecido, a idade mínima padrão é 18 anos.
    
6. Realizar correções (se necessário)
    Se algum teste falhar, faça as correções necessárias no código e repita os passos 4 e 5 até que todos os testes passem com sucesso.
    
7. Implementar novos recursos ou correções
    Após garantir que todos os testes estão passando, você pode continuar a implementar novos recursos ou correções de bugs conforme necessário.

