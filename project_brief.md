# My agent: PRD Facilitator Agent
One-liner: A conversational agent that helps product managers and development teams conduct structured elicitation sessions to build complete, business-focused PRDs, generate feature mockups, and export artifacts to Cloud Storage (with future Jira integration).

Tool coverage:
- Memory: Remembers team context, business domain, tech stack conventions, previous PRD history, and resolved decisions across sessions.
- Tools: `save_prd` (saves PRD markdown artifact to Cloud Storage / file system), `list_prds` (browses previous PRD catalog), and `validate_prd_completeness` (ensures business 'whys' and metrics are solid and open questions are resolved; prepared for future Jira MCP integration).
- Catalog/UI: Catalog of PRDs, executive summary cards, and requirements/open-questions status tables rendered via A2UI.
- Image gen: Conceptual UI mockups or user flow illustrations for the feature using `gemini-3.1-flash-lite-image`.
- Sandbox: Priority scoring (e.g., RICE calculation) and business impact estimation.

Core rails (everyone): memory, tools, eval, deploy, frontend
My stretch menu (pick later): A2UI tables/cards, Image generation (mockups), Cloud Storage export, Jira MCP integration
First eval question: "Conduza a criação do PRD para uma funcionalidade de recuperação de carrinho abandonado via notificações inteligentes no app. O PRD final deve cobrir todos os 'porquês' de negócio, definir métricas de sucesso quantitativas, resolver todas as open questions críticas e deixar os detalhes técnicos de implementação ('como') desacoplados para o time de engenharia."
