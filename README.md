
# Mini App de Consulta Climática com Python e OpenWeatherMap

- Introdução:

Este projeto consiste em um mini aplicativo desenvolvido em Python que permite aos usuários pesquisarem cidades e visualizarem informações climáticas atualizadas, como temperatura, vento e umidade. O aplicativo utiliza a API OpenWeatherMap para recuperar os dados climáticos e bibliotecas como Pytkinner, Datatime, Requests e Beautiful Soup para processar e exibir os dados de forma amigável.


## Stack utilizada

**Back-end:** Python
- Bibliotecas: 
   - Tkinter: Interface gráfica do usuário (GUI) 
   - Datatime: Manipulação de datas e horários 
   - Requests: Requisições HTTP à API OpenWeatherMap 
   - Beautiful Soup: Extração de dados HTML da API Implementação:

- Importação das Bibliotecas:
   - As bibliotecas necessárias são importadas no início do código.
   - Função de Pesquisa: Uma função é criada para lidar com a pesquisa de cidades. A função recebe o nome da cidade como entrada e utiliza a API OpenWeatherMap para recuperar os dados climáticos.
   - Exibição de Dados: Os dados climáticos recuperados são formatados e exibidos na interface gráfica do usuário.
   - Interface Gráfica do Usuário: A interface gráfica do usuário é criada utilizando a biblioteca Pytkinner. 
   - A interface inclui um campo de entrada para o nome da cidade, um botão de pesquisa e uma área de exibição para mostrar os dados climáticos.

## Funcionalidades

- Pesquisa por Cidades: Os usuários podem digitar o nome de uma cidade e o aplicativo buscará as informações climáticas da API OpenWeatherMap.
- Exibição de Dados Climáticos: O aplicativo exibe as seguintes informações climáticas para a cidade selecionada:
   - Temperatura atual
   - Descrição do clima (por exemplo, ensolarado, nublado, chuvoso)
   - Umidade
   - Velocidade do vento
   - Interface Simples: O aplicativo possui uma interface simples e intuitiva, facilitando o uso para usuários de todos os níveis de conhecimento técnico.


- Acesso Fácil à Informação Climática: O aplicativo fornece uma maneira fácil e rápida de acessar informações climáticas atualizadas para qualquer cidade.
- Interface Simples e Intuitiva: O aplicativo possui uma interface simples e intuitiva, facilitando o uso para todos os públicos.
- Código Fácil de Entender: O código do aplicativo é bem documentado e fácil de entender, tornando-o ideal para aprendizado e personalização.


## Apêndice


- Considerações Finais:

Este mini aplicativo demonstra como utilizar Python e APIs para criar ferramentas úteis e informativas. O código pode ser facilmente adaptado para incluir funcionalidades adicionais, como previsão do tempo para os próximos dias, alertas meteorológicos e integração com mapas.

- Observações:

Este projeto é um exemplo básico e pode ser expandido com recursos adicionais.
É importante registrar-se para uma conta gratuita na OpenWeatherMap para obter uma chave de API para uso no aplicativo.
O código pode ser adaptado para funcionar em diferentes plataformas, como web ou dispositivos móveis.

## Melhorias futuras

- Adicionar Previsão do Tempo: Exibir a previsão do tempo para os próximos dias.
- Alertas Meteorológicos: Implementar alertas para eventos climáticos severos, como tempestades ou chuvas fortes.
- Integração com Mapas: Exibir a localização da cidade selecionada em um mapa.
- Personalização: Permitir que os usuários personalizem a interface e as unidades de medida.
