# Recuperação de Carrinho Abandonado com Notificações Push Inteligentes

- **Status:** Rascunho
- **Data:** 24/10/2023
- **Autor / Time:** Time de Produto & Engajamento / Crescimento

## 1. Visão Geral e Problema
- **Dor do usuário/cliente:** Usuários frequentemente adicionam itens ao carrinho no aplicativo mobile, mas abandonam a jornada por distrações, indecisão sobre preço/frete ou necessidade de pesquisar mais. Sem um lembrete contextualizado e oportuno, esses usuários esquecem dos itens ou acabam comprando em concorrentes.
- **Oportunidade identificada:** Utilizar notificações push inteligentes e personalizadas (com base em tempo de inatividade, comportamento do usuário, histórico de compras e ofertas dinâmicas) para reengajar usuários que abandonaram itens no carrinho e aumentar a taxa de conversão do e-commerce mobile.

## 2. Porquês de Negócio e Dados (Why & Context)
- **Por que priorizar agora?** A taxa média de abandono de carrinho no e-commerce gira em torno de 70%. No canal mobile, essa taxa costuma ser ainda maior. Reduzir o abandono é uma das alavancas de menor custo de aquisição (CAC) para geração de receita incremental.
- **Hipótese de negócio:** Notificações push personalizadas e enviadas em janelas temporais otimizadas (ex: 1 hora e 24 horas pós-abandono) aumentarão o retorno dos usuários ao app com intenção de compra, gerando receita incremental relevante sem custo direto de mídia paga.

## 3. Métricas de Sucesso e KPIs
- **Primary KPI:** +12% na taxa de conversão de carrinhos abandonados (compradores / carrinhos abandonados).
- **Secondary KPIs:**
  - Taxa de Abertura (CTR) das notificações push de carrinho abandonado >= 8%.
  - Receita incremental gerada diretamente via canal push de carrinho.
  - Taxa de Opt-out / Desinstalação pós-notificação <= 0.5% (garantindo que o reengajamento não seja invasivo).

## 4. Escopo e Requisitos Funcionais
- **RF01 - Detecção de Abandono de Carrinho:** O sistema deve identificar quando um usuário autenticado ou identificado adiciona itens ao carrinho e não finaliza o checkout após um período de inatividade configurável (ex: 30 a 60 minutos).
- **RF02 - Motor de Disparo Personalizado:** Disparar notificação push contextual trazendo o nome do produto principal do carrinho, imagem (se suportado pela plataforma) e texto dinâmico (ex: "Seus itens estão te esperando!").
- **RF03 - Regra de Frequência e Saturação (Frequency Capping):** Limitar o envio de lembretes a no máximo 2 notificações por carrinho abandonado em uma janela de 48 horas, evitando spam.
- **RF04 - Aprofundamento no App (Deep Linking):** Ao clicar na notificação push, o usuário deve ser redirecionado diretamente para a tela do carrinho pré-preenchido com os itens salvos.
- **RF05 - Cancelamento Automático de Disparo:** Se o usuário finalizar a compra por qualquer canal antes do disparo da notificação, a fila de push pendente para aquele pedido/carrinho deve ser cancelada imediatamente.
- **RF06 - Oferta/Cupom Dinâmico (Fase 2 / Opcional):** Se o carrinho continuar abandonado após 24 horas, testar o envio de um incentivo (ex: frete grátis ou 5% de desconto válido por tempo determinado).

## 5. Questões em Aberto (Open Questions) & Riscos
- **Q1:** Como lidar com usuários que não possuem permissão de notificação push ativada (Opt-in)? Haverá canal de fallback (ex: e-mail ou SMS)?
  - *Responsável:* Produto / CRM.
- **Q2:** Qual o tempo exato e ideal de inatividade para o primeiro disparo de push (30 min vs 1 hora)?
  - *Responsável:* Data Analytics (fazer análise do tempo médio entre inclusão e checkout).
- **Q3:** Como tratar a variação de estoque do item no carrinho entre o momento do abandono e o momento do clique no push?
  - *Responsável:* Engenharia / Checkout.

## 6. Critérios de Aceite
### Cenário 1: Disparo bem-sucedido de push para carrinho abandonado
- **Dado que** um usuário logado possui itens no carrinho e não avançou para o pagamento nas últimas 60 minutos,
- **E que** o usuário tem permissão de push ativa e não comprou esses itens por outro meio,
- **Quando** o job de verificação de carrinho for executado,
- **Então** o sistema deve agendar e enviar uma notificação push com o deep link correto do carrinho e o nome de um dos itens.

### Cenário 2: Cancelamento de push após compra realizada
- **Dado que** o usuário tem uma notificação de carrinho abandonado agendada para daqui a 30 minutos,
- **Quando** o usuário realiza e confirma a compra do carrinho via aplicativo ou web,
- **Então** o sistema deve cancelar imediatamente o agendamento do push, garantindo que o usuário não receba mensagens indevidas.

### Cenário 3: Redirecionamento por Deep Link com produto esgotado
- **Dado que** o usuário clica na notificação push de carrinho abandonado,
- **E** um dos itens do carrinho ficou sem estoque durante o intervalo,
- **Quando** o aplicativo abrir na tela do carrinho,
- **Então** o sistema deve exibir um aviso claro informando qual item esgotou, mantendo os demais itens disponíveis atualizados.
